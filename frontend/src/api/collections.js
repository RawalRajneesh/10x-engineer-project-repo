import apiClient from './client';

export const getCollections = () => apiClient.get('/collections');
export const createCollection = (data) => apiClient.post('/collections', data);
export const deleteCollection = (id) => apiClient.delete(`/collections/${id}`);
