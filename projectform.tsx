"use client";

import { useState } from 'react'; // Make sure useState is imported

export function ProjectForm() {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [budget, setBudget] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const projectData = {
            name,
            description,
            budget: parseFloat(budget) || 0
        };
        // API call to POST /api/v1/projects
        console.log("Creating project:", projectData);
        alert("Project creation functionality to be connected to the backend.");
    };

    return (
        <form onSubmit={handleSubmit} className="p-6 mt-8 space-y-4 bg-white border rounded-lg">
            <h3 className="text-xl font-semibold">Create a New Project</h3>
            <div>
                <label htmlFor="projectName" className="block text-sm font-medium">Project Name</label>
                <input
                    type="text"
                    id="projectName" // Add ID
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full mt-1 px-3 py-2 border rounded-md"
                    required
                />
            </div>
            <div>
                <label htmlFor="projectDescription" className="block text-sm font-medium">Description</label>
                <textarea
                    id="projectDescription" // Add ID
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    className="w-full mt-1 px-3 py-2 border rounded-md"
                />
            </div>
            <div>
                <label htmlFor="projectBudget" className="block text-sm font-medium">Budget ($)</label>
                <input
                    type="number"
                    id="projectBudget" // Add ID
                    value={budget}
                    onChange={(e) => setBudget(e.target.value)}
                    className="w-full mt-1 px-3 py-2 border rounded-md"
                />
            </div>
            <button type="submit" className="px-4 py-2 text-white bg-green-600 rounded-md hover:bg-green-700">
                Create Project
            </button>
        </form>
    );
}