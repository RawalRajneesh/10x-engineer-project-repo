import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { APIClient } from '../api/APIClient';

const PromptEdit = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPrompt = async () => {
      try {
        const data = await APIClient.getPrompt(id);
        setTitle(data.title);
        setContent(data.content);
      } catch (error) {
        setError('Failed to load prompt for editing');
      } finally {
        setLoading(false);
      }
    };

    fetchPrompt();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await APIClient.updatePrompt(id, { title, content });
      navigate(`/prompts/${id}`);
    } catch (error) {
      setError('Failed to update prompt');
    }
  };

  if (loading) return <div className="text-center mt-8">Loading...</div>;

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Edit Prompt</h2>
      <form onSubmit={handleSubmit} className="space-y-4 bg-white p-6 shadow rounded">
        {error && <div className="text-red-500">{error}</div>}
        <div>
          <label className="block font-semibold">Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            className="w-full p-2 border rounded"
          />
        </div>
        <div>
          <label className="block font-semibold">Content:</label>
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
            className="w-full p-2 border rounded h-32"
          ></textarea>
        </div>
        <button
          type="submit"
          className="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
        >
          Save
        </button>
      </form>
    </div>
  );
};

export default PromptEdit;
