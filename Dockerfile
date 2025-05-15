# Use Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Copy your app code into the container
COPY app/ /app

# Install Flask inside the container
RUN pip install flask redis

# Run the Flask app
CMD ["python", "app.py"]
