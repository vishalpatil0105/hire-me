import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { createJob } from '../services/api';
import './Admin.css';

const Admin = () => {
    const [formData, setFormData] = useState({
        title: '',
        description: '',
        company: '',
        location: ''
    });
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState({ type: '', text: '' });
    const history = useHistory();

    // Check if user is admin
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    if (!user.is_admin) {
        history.push('/home');
        return null;
    }

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setMessage({ type: '', text: '' });

        try {
            await createJob(formData, user.email);
            setMessage({ type: 'success', text: 'Job created successfully!' });
            setFormData({
                title: '',
                description: '',
                company: '',
                location: ''
            });
        } catch (error) {
            const errorMsg = error.detail || error.message || 'Failed to create job';
            setMessage({ type: 'error', text: errorMsg });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="admin-container">
            <div className="admin-card">
                <h1 className="admin-title">Admin Dashboard</h1>
                <p className="admin-subtitle">Add New Job Opening</p>

                {message.text && (
                    <div className={`admin-message ${message.type}`}>
                        {message.text}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="admin-form">
                    <div className="form-group">
                        <label htmlFor="title">Job Title *</label>
                        <input
                            type="text"
                            id="title"
                            name="title"
                            value={formData.title}
                            onChange={handleChange}
                            required
                            placeholder="e.g., Software Engineer"
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="company">Company *</label>
                        <input
                            type="text"
                            id="company"
                            name="company"
                            value={formData.company}
                            onChange={handleChange}
                            required
                            placeholder="e.g., Tech Company Inc."
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="location">Location</label>
                        <input
                            type="text"
                            id="location"
                            name="location"
                            value={formData.location}
                            onChange={handleChange}
                            placeholder="e.g., San Francisco, CA"
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="description">Job Description *</label>
                        <textarea
                            id="description"
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                            required
                            rows="6"
                            placeholder="Describe the job requirements, responsibilities, and benefits..."
                        />
                    </div>

                    <button 
                        type="submit" 
                        className="admin-submit-btn"
                        disabled={loading}
                    >
                        {loading ? 'Creating...' : 'Create Job'}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Admin;


