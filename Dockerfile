# Use the official Python image from the Docker Hub
FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app



COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/
