# Cloud Run CI/CD Demo

A simple Hello World application demonstrating CI/CD pipelines with Google Cloud Run.

## Overview

This repository contains a minimal Python Flask application that returns a JSON "Hello World" response. It's designed to demonstrate how to set up continuous integration and continuous deployment with Google Cloud Run.

## Features

- Simple Flask application
- Docker containerization
- Cloud Build integration
- Automatic deployment to Cloud Run

## Architecture

1. Code is pushed to GitHub repository
2. Cloud Build is triggered by commits to the main branch
3. Cloud Build builds a Docker container and pushes it to Container Registry
4. Cloud Run deploys the new container automatically

## Setup Instructions

### Prerequisites

- Google Cloud Platform account
- Google Cloud SDK installed locally
- Docker installed locally (for testing)
- GitHub repository

### Local Development

1. Clone this repository:
```
git clone https://github.com/yourusername/cloudrun-demo.git
cd cloudrun-demo
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run locally:
```
functions-framework --target=main --debug
```

4. Visit http://localhost:8080 in your browser

### Docker Testing

1. Build the container:
```
docker build -t cloudrun-demo .
```

2. Run locally:
```
docker run -p 8080:8080 cloudrun-demo
```

3. Visit http://localhost:8080 in your browser

### Google Cloud Setup

1. Enable required APIs:
```
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
```

2. Connect your GitHub repository to Cloud Build:
   - Go to Cloud Build > Triggers
   - Connect to your GitHub repository
   - Create a trigger for commits to the main branch

3. Manual deployment (if not using CI/CD):
```
gcloud builds submit --tag gcr.io/[PROJECT_ID]/cloudrun-demo
gcloud run deploy cloudrun-demo --image gcr.io/[PROJECT_ID]/cloudrun-demo --platform managed --region us-central1 --allow-unauthenticated
```

## CI/CD Pipeline

The CI/CD pipeline is defined in the `cloudbuild.yaml` file:

1. Build a Docker container
2. Push to Container Registry
3. Deploy to Cloud Run
4. Tag as latest
5. Push latest tag

## Environment Variables

The service uses the following environment variables:

- `PORT`: The port to listen on (default: 8080)
- `ENVIRONMENT`: The environment name (default: development)

## Testing the Deployment

After deployment, you can test your Cloud Run service at the URL provided in the deployment output.

## License

This project is licensed under the MIT License - see the LICENSE file for details.