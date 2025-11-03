import React, { useEffect, useState } from 'react';
import JobList from '../components/JobList';
import { fetchJobs } from '../services/api';
import './Home.css';

const Home = () => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getJobs = async () => {
            try {
                const jobData = await fetchJobs();
                setJobs(jobData);
            } catch (err) {
                setError(err.message || 'Failed to fetch jobs');
            } finally {
                setLoading(false);
            }
        };

        getJobs();
    }, []);

    if (loading) {
        return (
            <div className="home-container">
                <div className="loading-container">
                    <div className="loading-spinner"></div>
                    <p>Loading jobs...</p>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="home-container">
                <div className="error-container">
                    <div className="error-icon">⚠️</div>
                    <h2>Error loading jobs</h2>
                    <p>{error}</p>
                    <button onClick={() => window.location.reload()} className="retry-button">
                        Try Again
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="home-container">
            <div className="home-header">
                <h1 className="home-title">Open Jobs</h1>
                <p className="home-subtitle">Find your next opportunity</p>
            </div>
            <JobList jobs={jobs} />
        </div>
    );
};

export default Home;
