import React, { useState } from 'react';
import { APIClient } from '../api/APIClient';
import { useNavigate } from 'react-router-dom';

const PromptCreate = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await APIClient.createPrompt({ title, content });
      navigate('/');
    } catch (error) {
      setError('Failed to create prompt');
    }
  };

  return (
    <div>
      <h2>Create a New Prompt</h2>
      <form onSubmit={handleSubmit}>
        {error && <div>{error}</div>}
        <label>
          Title:
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </label>
        <label>
          Content:
          <textarea value={content} onChange={(e) => setContent(e.target.value)} required></textarea>
        </label>
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default PromptCreate;