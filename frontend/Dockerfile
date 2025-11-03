FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY public/ ./public/
COPY src/ ./src/

# Set environment variable for API URL
ENV REACT_APP_API_URL=${REACT_APP_API_URL:-http://localhost:8000}

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]

