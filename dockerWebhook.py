from flask import Flask, request
import docker
from docker.errors import DockerException, NotFound
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Script requirements :
# Python
# Flask
# Pip
# python-dotenv
# PM2 (when running in background)

# @app.post('/webhook/<tag>/<container_name>')
@app.post('/webhook')
# def run_hook(tag,container_name):
def run_hook():
  tag = request.args.get('tag')
  print(tag)
  container_name = request.args.get('container_name')
  print(container_name)

  # Get repository from environment variable
  repository = os.getenv('DOCKER_REPOSITORY', 'juntabudlong/vyde-portal-dev')
  
  # Get port configuration from environment variables
  container_port = os.getenv('CONTAINER_PORT', '3000')
  host_port = int(os.getenv('HOST_PORT', '3001'))

  # Initialize docker 
  client = docker.from_env()

  # Get the running container named portal-dev-container
  # Stop and Remove
  try:
    container = client.containers.get(container_name)
    container.stop()
    container.remove()
  except NotFound:
    print(f"Error: Container {container_name} not found.")
  except DockerException as e:
    print(f"Error stopping container {container_name}: {e}")

  try:
    client.containers.run(
      f'{repository}:{tag}', # Image 
      ports={f'{container_port}/tcp': host_port},  # Use environment variables for ports
      detach=True,
      name=container_name # Retain the name: portal-dev-container
    )
  except DockerException as e:
    print(f"Error running {container_name}: {e}")

  return f"Docker pull and run {repository}:{tag} successful"

if __name__ == "__main__":
  # Get Flask configuration from environment variables
  flask_host = os.getenv('FLASK_HOST', '0.0.0.0')
  flask_port = int(os.getenv('FLASK_PORT', '5001'))
  
  app.run(host=flask_host, port=flask_port)