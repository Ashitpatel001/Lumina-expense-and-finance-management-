# Ensure you run: pip install chromadb sentence-transformers pypdf
import chromadb
from sentence_transformers import SentenceTransformer
import pypdf
import io

class RAGService:
    def __init__(self):
        self.client = chromadb.Client() 
        self.collection = self.client.get_or_create_collection(name="documents")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def extract_text_from_pdf(self, pdf_content: bytes) -> str:
        text = ""
        try:
            reader = pypdf.PdfReader(io.BytesIO(pdf_content))
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            print(f"Error extracting PDF text: {e}")
        return text

    def add_document(self, doc_id: str, text: str):
        if not text.strip():
            print(f"Skipping empty document {doc_id}")
            return
        embedding = self.model.encode(text).tolist()
        self.collection.add(
            embeddings=[embedding],
            documents=[text],
            metadatas=[{"doc_id": doc_id}],
            ids=[doc_id]
        )

    def semantic_search(self, query: str, top_k: int = 3):
        if self.collection.count() == 0: return []
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding], n_results=top_k
        )
        found_docs = []
        if results and results['ids'][0]:
            for i, doc_id in enumerate(results['ids'][0]):
                found_docs.append({
                    "id": doc_id,
                    "content": results['documents'][0][i],
                    "similarity": 1 - results['distances'][0][i]
                })
        return found_docs

rag_service = RAGService()