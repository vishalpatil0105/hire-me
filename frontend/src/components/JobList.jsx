import React from 'react';
import './JobList.css';

const JobList = ({ jobs = [] }) => {
    if (jobs.length === 0) {
        return (
            <div className="job-list-empty">
                <div className="empty-icon">📋</div>
                <h3>No jobs available</h3>
                <p>Check back later for new opportunities</p>
            </div>
        );
    }

    return (
        <div className="job-list-container">
            <div className="job-grid">
                {jobs.map(job => (
                    <div key={job.id} className="job-card">
                        <div className="job-card-header">
                            <div className="job-icon">💼</div>
                            <div className="job-badge">Open</div>
                        </div>
                        <h3 className="job-title">{job.title || 'Job Title'}</h3>
                        <p className="job-description">
                            {job.description || 'No description available'}
                        </p>
                        {job.company && (
                            <div className="job-company">
                                <span className="company-icon">🏢</span>
                                <span>{job.company}</span>
                            </div>
                        )}
                        {job.location && (
                            <div className="job-location">
                                <span className="location-icon">📍</span>
                                <span>{job.location}</span>
                            </div>
                        )}
                        <div className="job-card-footer">
                            <button className="job-apply-button">Apply Now</button>
                            <button className="job-details-button">View Details</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default JobList;
