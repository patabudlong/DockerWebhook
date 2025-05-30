module.exports = {
  apps: [{
    name: 'docker-webhook',
    script: 'dockerWebhook.py',
    interpreter: 'python3',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }]
}; 