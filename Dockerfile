# Use Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy your app code into the container
COPY app/ /app

# Install Flask inside the container
RUN pip install flask redis

# Run the Flask app
CMD ["python", "app.py"]
