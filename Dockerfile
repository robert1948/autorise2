# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set environment variables to handle Django settings properly
ENV DJANGO_SETTINGS_MODULE=autorise.settings

# Expose port 8000 to allow access to the application
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "autorise.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]