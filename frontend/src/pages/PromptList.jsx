import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { APIClient } from '../api/APIClient';

const PromptList = () => {
  const [prompts, setPrompts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPrompts = async () => {
      try {
        const data = await APIClient.getPrompts();
        setPrompts(data);
      } catch (error) {
        setError('Failed to load prompts');
      } finally {
        setLoading(false);
      }
    };

    fetchPrompts();
  }, []);

  if (loading) return <div className="text-center mt-8">Loading...</div>;

  if (error) return <div className="text-red-500 text-center mt-8">{error}</div>;

  if (prompts.length === 0) {
    return (
      <div className="max-w-2xl mx-auto p-4 text-center">
        <h2 className="text-xl font-bold mb-4">No Prompts Available</h2>
        <p>Create a new prompt to get started!</p>
        <Link
          to="/create"
          className="inline-block mt-4 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
        >
          Create New Prompt
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Prompt List</h2>
      <ul className="space-y-4">
        {prompts.map((prompt) => (
          <li key={prompt.id} className="p-4 border border-gray-300 rounded shadow-sm bg-white">
            <h3 className="font-semibold">{prompt.title}</h3>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PromptList;