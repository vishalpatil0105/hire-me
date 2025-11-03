import React from 'react';
import { Link, useHistory, useLocation } from 'react-router-dom';
import './Header.css';

const Header = () => {
    const history = useHistory();
    const location = useLocation();

    const handleLogout = () => {
        localStorage.removeItem('user');
        history.push('/');
    };

    const isAuthPage = location.pathname === '/' || location.pathname === '/auth';
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    const isAdmin = user.is_admin === true;

    return (
        <header className="app-header">
            <div className="header-container">
                <Link to="/home" className="header-logo">
                    <span className="logo-icon">💼</span>
                    <span className="logo-text">Job Search</span>
                </Link>
                <nav className="header-nav">
                    {!isAuthPage ? (
                        <>
                            <Link to="/home" className="nav-link">
                                Jobs
                            </Link>
                            {isAdmin && (
                                <Link to="/admin" className="nav-link">
                                    Admin
                                </Link>
                            )}
                            <button onClick={handleLogout} className="nav-button">
                                Logout
                            </button>
                        </>
                    ) : (
                        <Link to="/auth" className="nav-link">
                            Sign In
                        </Link>
                    )}
                </nav>
            </div>
        </header>
    );
};

export default Header;
