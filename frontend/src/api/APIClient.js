const API_BASE_URL = 'http://localhost:8000'; // Replace with your actual API URL

async function fetchWrapper(url, options) {
  try {
    const response = await fetch(`${API_BASE_URL}${url}`, options);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('HTTP error:', error);
    throw error;
  }
}

export const APIClient = {
  getPrompts: () => fetchWrapper('/prompts', { method: 'GET' }),
  getPrompt: (id) => fetchWrapper(`/prompts/${id}`, { method: 'GET' }),
  createPrompt: (data) => fetchWrapper('/prompts', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }),
  updatePrompt: (id, data) => fetchWrapper(`/prompts/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  }),
  deletePrompt: (id) => fetchWrapper(`/prompts/${id}`, { method: 'DELETE' }),
};

// Add similar methods for collections as needed