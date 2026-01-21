# Model Deployment & Serving on Kubernetes — High-Level Steps (Flask + Gunicorn)

### Prepare the application code

- Add Flask inference API
- Add Gunicorn entrypoint
- Package model + requirements

### Create a production-ready Dockerfile

- Use Python base image
- Copy app + model
- Install dependencies
- Use Gunicorn as CMD

### Build and push Docker image to a registry

- Build the image locally
- Tag the image
- Push to ECR/GCR/Docker Hub

### Create Kubernetes Deployment manifest

- Define pod spec with your model image
- Expose container port (e.g., 8000 for Gunicorn)

### Set replicas

- Configure resource requests/limits

### Add ConfigMap/Secrets (optional)

- For environment variables such as model path, API tokens, etc.

### Create a Kubernetes Service

- ClusterIP or NodePort to expose the Deployment
- Map to container port used by Gunicorn

### Deploy to the Kubernetes cluster

- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`

### Model Serving

- Add Ingress controller
- Add Ingress

### Test the inference endpoint

Use external IP + path to test the Flask model API