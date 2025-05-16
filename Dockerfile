# Use Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (cached unless requirements change)
COPY app/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy in your application code
COPY app/ /app

# Expose the port your Flask app runs on
EXPOSE 80

# Run the Flask application
CMD ["python", "app.py"]

