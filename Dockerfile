# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Install Python dependencies
COPY Pipfile Pipfile.lock $APP_HOME/
RUN pip install pipenv && pipenv install --system

# Add the rest of the code
COPY . $APP_HOME/

# expose port
EXPOSE 8000
