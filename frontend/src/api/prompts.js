import apiClient from './client';

export const getPrompts = () => apiClient.get('/prompts');
export const getPrompt = (id) => apiClient.get(`/prompts/${id}`);
export const createPrompt = (data) => apiClient.post('/prompts', data);
export const updatePrompt = (id, data) => apiClient.put(`/prompts/${id}`, data);
export const deletePrompt = (id) => apiClient.delete(`/prompts/${id}`);
