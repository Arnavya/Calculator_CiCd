# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements and install only production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "app.routes"]
