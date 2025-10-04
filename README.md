# Lumina-expense-and-finance-management-
An intelligent financial and project management suite featuring AI-powered semantic search to instantly find information within your documents.
# Axiom Finance Suite


 About The Project

This project is a comprehensive financial and project management suite developed for the **Odoo x Amalthea Hackathon '25**. In modern business workflows, critical information is often siloed between financial spreadsheets, project management tools, and folders of documents. This application provides a single source of truth, enabling teams to manage project budgets, track payments, and intelligently search through all related documentation in one place.

Key Features

* **Centralized Project Management:** Create, view, and manage all your projects and their associated budgets in a clean, intuitive dashboard.
* **Secure Document Hub:** Upload and store critical documents like invoices, contracts, and technical specifications securely for each project.
* **AI-Powered Semantic Search:** The core innovation of this project. Instead of basic keyword search, our system uses a Retrieval-Augmented Generation (RAG) pipeline. You can ask complex, natural-language questions (e.g., "*what are the payment terms in the main contract?*") and get instant, accurate answers extracted from the content of your uploaded documents.
* **Robust & Scalable Architecture:** Built with a modern tech stack and fully containerized with Docker to ensure reliability and ease of deployment.

---

 Tech Stack
Backend: FastAPI (Python), SQLAlchemy
Frontend: Next.js (React & TypeScript), Tailwind CSS
Database: PostgreSQL
AI:`sentence-transformers` & ChromaDB for vector embeddings and search.
DevOps: Docker & Docker Compose



1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd your-repo-name
    ```
3.  **Install frontend dependencies:**
    This step is crucial for the local development environment and Docker to work correctly.
    ```bash
    cd frontend
    npm install
    cd ..
    ```
4.  **Launch the application with Docker Compose:**
    This command will build and start the frontend, backend, and database containers.
    ```bash
    docker compose up --build
    ```
5.  **Access the application:**
    * **Frontend Web App:** `http://localhost:3000`
    * **Backend API Docs:** `http://localhost:8000/docs`

---

## Project Structure
