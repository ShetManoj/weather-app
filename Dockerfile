# Use python base image

FROM python:3.9-slim

# Create working directory 

WORKDIR /app

# Copy all the files to the working directory

COPY . . 

# Install the required dependencies

RUN pip install -r requirements.txt

# Expose the port 

EXPOSE 5000

# Run the container 

CMD ["python","app.py"]
