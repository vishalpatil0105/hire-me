import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import './Auth.css';

const Auth = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLogin, setIsLogin] = useState(true);
    const [rememberMe, setRememberMe] = useState(false);
    const history = useHistory();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
        const url = isLogin ? `${API_URL}/api/auth/login` : `${API_URL}/api/auth/signup`;
        try {
            const userData = isLogin 
                ? { email, password }  // Login only needs email and password
                : { email, username, password };  // Signup needs email, username, and password
            
            console.log('Sending request to:', url);
            console.log('Request data (password hidden):', { ...userData, password: '***' });
            console.log('Full request data:', userData);
            
            const response = await axios.post(url, userData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            console.log('Login/Signup successful:', response.data);
            
            // Store user data in localStorage or sessionStorage if needed
            if (response.data) {
                localStorage.setItem('user', JSON.stringify(response.data));
            }
            
            history.push('/home');
        } catch (error) {
            console.error('Authentication error:', error);
            console.error('Error response:', error.response?.data);
            console.error('Error status:', error.response?.status);
            
            // Handle 422 validation errors specifically
            if (error.response?.status === 422) {
                const validationErrors = error.response?.data?.detail;
                if (Array.isArray(validationErrors)) {
                    const errorMessages = validationErrors.map(err => `${err.loc?.join('.')}: ${err.msg}`).join('\n');
                    alert(`Validation Error:\n${errorMessages}`);
                } else {
                    alert(`Validation Error: ${JSON.stringify(validationErrors)}`);
                }
            } else {
                const errorMessage = error.response?.data?.detail || error.response?.data?.message || error.message || 'Authentication failed. Please try again.';
                alert(errorMessage);
            }
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <div className="auth-illustration">
                    <div className="illustration-content">
                        <svg viewBox="0 0 400 400" className="person-illustration">
                            {/* Person with laptop illustration */}
                            <defs>
                                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style={{stopColor:"#E3F2FD", stopOpacity:1}} />
                                    <stop offset="100%" style={{stopColor:"#BBDEFB", stopOpacity:1}} />
                                </linearGradient>
                            </defs>
                            {/* Chair */}
                            <rect x="80" y="280" width="140" height="20" fill="#8D6E63" rx="5"/>
                            <rect x="80" y="240" width="20" height="60" fill="#6D4C41"/>
                            <rect x="200" y="240" width="20" height="60" fill="#6D4C41"/>
                            {/* Person */}
                            <ellipse cx="150" cy="180" rx="40" ry="35" fill="#FFDBAE"/>
                            <rect x="130" y="200" width="40" height="50" fill="#FFFFFF" rx="5"/>
                            <rect x="115" y="210" width="70" height="80" fill="#4A90E2" rx="5"/>
                            <rect x="115" y="250" width="70" height="60" fill="#2196F3" rx="5"/>
                            {/* Glasses */}
                            <circle cx="135" cy="180" r="12" fill="none" stroke="#333" strokeWidth="2"/>
                            <circle cx="165" cy="180" r="12" fill="none" stroke="#333" strokeWidth="2"/>
                            <line x1="147" y1="180" x2="153" y1="180" stroke="#333" strokeWidth="2"/>
                            {/* Laptop */}
                            <rect x="160" y="220" width="80" height="50" fill="#E0E0E0" rx="3"/>
                            <rect x="165" y="225" width="70" height="35" fill="#263238" rx="2"/>
                            <circle cx="220" cy="235" r="3" fill="#4CAF50"/>
                            {/* Plant stand */}
                            <rect x="280" y="200" width="8" height="100" fill="#8D6E63"/>
                            {/* Pot */}
                            <ellipse cx="284" cy="300" rx="20" ry="8" fill="#795548"/>
                            {/* Plant */}
                            <circle cx="270" cy="280" r="15" fill="#66BB6A"/>
                            <circle cx="290" cy="275" r="18" fill="#66BB6A"/>
                            <circle cx="298" cy="285" r="12" fill="#66BB6A"/>
                            {/* Flower */}
                            <circle cx="275" cy="250" r="8" fill="#E91E63"/>
                            <circle cx="285" cy="245" r="7" fill="#F06292"/>
                        </svg>
                    </div>
                </div>
                <div className="auth-form-section">
                    <h1 className="auth-title">Log In</h1>
                    <form onSubmit={handleSubmit} className="auth-form">
                        {!isLogin && (
                            <div className="input-group">
                                <span className="input-icon">👤</span>
                                <input
                                    type="text"
                                    placeholder="Your Name"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    required={!isLogin}
                                    className="auth-input"
                                />
                                <span className="input-suffix">📋</span>
                            </div>
                        )}
                        <div className="input-group">
                            <span className="input-icon">👤</span>
                            <input
                                type="email"
                                placeholder="Your Email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                                className="auth-input"
                            />
                            <span className="input-suffix">📋</span>
                        </div>
                        <div className="input-group">
                            <span className="input-icon">🔒</span>
                            <input
                                type="password"
                                placeholder="Password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                                className="auth-input"
                            />
                            <span className="input-suffix">📋</span>
                        </div>
                        {isLogin && (
                            <div className="remember-me">
                                <label className="checkbox-label">
                                    <input
                                        type="checkbox"
                                        checked={rememberMe}
                                        onChange={(e) => setRememberMe(e.target.checked)}
                                        className="checkbox-input"
                                    />
                                    <span>Remember me</span>
                                </label>
                            </div>
                        )}
                        <button type="submit" className="auth-button">
                            {isLogin ? 'Log in' : 'Create account'}
                        </button>
                    </form>
                    <div className="auth-footer">
                        {isLogin ? (
                            <p className="switch-auth">
                                Don't have an account?{' '}
                                <a href="#" onClick={(e) => { e.preventDefault(); setIsLogin(false); }} className="auth-link">
                                    Create an account
                                </a>
                            </p>
                        ) : (
                            <p className="switch-auth">
                                Already have an account?{' '}
                                <a href="#" onClick={(e) => { e.preventDefault(); setIsLogin(true); }} className="auth-link">
                                    Log in
                                </a>
                            </p>
                        )}
                        <div className="social-login">
                            <span className="social-text">Or login with</span>
                            <div className="social-icons">
                                <button className="social-icon social-facebook" aria-label="Login with Facebook">
                                    f
                                </button>
                                <button className="social-icon social-twitter" aria-label="Login with Twitter">
                                    🐦
                                </button>
                                <button className="social-icon social-google" aria-label="Login with Google">
                                    G
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Auth;
