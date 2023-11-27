# Use an official Python runtime as a parent image
FROM python:3.9

# Create the directory /home/app
RUN mkdir -p /home/app

# Set the working directory to /home/app
WORKDIR /home/app

# Copy the local directory contents into the container at /home/app
COPY . /home/app

# Install dependencies specified in requirement.txt
RUN pip install --no-cache-dir -r requirements.txt


# Define the command to run your application
CMD ["python", "main.py"]
