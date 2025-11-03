FROM node:18-alpine

WORKDIR /app

# Build argument for API URL
ARG REACT_APP_API_URL=http://localhost:8000
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY public /app/public
COPY src /app/src

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]

