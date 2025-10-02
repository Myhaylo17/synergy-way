import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Приклад для Users та Addresses (замініть на ваші моделі)
export const dataAPI = {
  // Users endpoints
  getUsers: () => api.get('/api/users/'),
  getUser: (id) => api.get(`/api/users/${id}/`),
  createUser: (data) => api.post('/api/users/', data),
  updateUser: (id, data) => api.put(`/api/users/${id}/`, data),
  deleteUser: (id) => api.delete(`/api/users/${id}/`),

  // Addresses endpoints
  getAddresses: () => api.get('/api/addresses/'),
  getAddress: (id) => api.get(`/api/addresses/${id}/`),
  createAddress: (data) => api.post('/api/addresses/', data),
  updateAddress: (id, data) => api.put(`/api/addresses/${id}/`, data),
  deleteAddress: (id) => api.delete(`/api/addresses/${id}/`),

  // Random data endpoint
  getRandomData: () => api.get('/api/random-data/'),
};

export default api;