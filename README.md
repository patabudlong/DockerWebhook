# Docker Webhook Service

A Flask-based webhook service that automatically pulls and runs Docker containers when triggered. This service is designed to facilitate continuous deployment by listening for webhook calls and managing Docker container lifecycle.

## Features

- **Webhook Endpoint**: Receives POST requests to trigger container updates
- **Container Management**: Automatically stops, removes, and recreates Docker containers
- **Environment Configuration**: Configurable through environment variables
- **PM2 Support**: Can be run as a background service using PM2

## Prerequisites

- Python 3.x
- Docker
- pip (Python package manager)
- PM2 (optional, for background service)

## Installation

1. **Clone the repository** (or download the files)

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install PM2** (optional, for background service):
   ```bash
   npm install -g pm2
   ```

## Configuration

Create a `.env` file in the project root directory with the following variables: 




## About the Developer

This project was created by **Jun TaBudlong Jr**, a Full Stack Developer specializing in Software Development and Architecture.

### Get in Touch
- 📧 **Email**: [peregrino.tabudlong@gmail.com](peregrino.tabudlong@gmail.com)
- 🐙 **GitHub**: [github.com/patabudlong](https://github.com/patabudlong)
- 💼 **LinkedIn**: [linkedin.com/in/patabudlong](https://www.linkedin.com/in/patabudlong/)
- 🌐 **Portfolio**: [patabudlong.github.io](https://patabudlong.github.io)

### Support This Project
If you find this project helpful, consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 🔧 Contributing improvements
- ☕ [Buy me a Ko-fi](https://ko-fi.com/patabudlong)