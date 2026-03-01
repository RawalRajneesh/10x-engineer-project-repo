# Use the official Python 3.11 slim image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the default port FastAPI application runs on (e.g., 8000)
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]
