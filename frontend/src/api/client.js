import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5173/api', // Update this URL as needed
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.response.use(
  response => response,
  error => {
    // Handle errors consistently
    console.error('API error occurred:', error);
    return Promise.reject(error);
  }
);

export default apiClient;
