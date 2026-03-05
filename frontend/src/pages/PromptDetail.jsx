import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { APIClient } from '../api/APIClient';

const PromptDetail = () => {
  const { id } = useParams();
  const [prompt, setPrompt] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPrompt = async () => {
      try {
        const data = await APIClient.getPrompt(id);
        setPrompt(data);
      } catch (error) {
        setError('Failed to load prompt detail');
      } finally {
        setLoading(false);
      }
    };

    fetchPrompt();
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Prompt Detail</h2>
      {prompt && (
        <div>
          <h3>{prompt.title}</h3>
          <p>{prompt.content}</p>
          {/* Display additional prompt details as needed */}
        </div>
      )}
    </div>
  );
};

export default PromptDetail;