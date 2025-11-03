import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const signUp = async (userData) => {
    try {
        const response = await axios.post(`${API_URL}/api/auth/signup`, userData);
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const signIn = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}/api/auth/login`, credentials);
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const fetchJobs = async () => {
    try {
        const response = await axios.get(`${API_URL}/api/jobs`);
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const createJob = async (jobData, adminEmail) => {
    try {
        const response = await axios.post(
            `${API_URL}/api/jobs`,
            jobData,
            {
                headers: {
                    'X-Admin-Email': adminEmail
                }
            }
        );
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export default api;
