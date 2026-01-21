# Traefik Ingress Controller Installation

---

## 1. Add Traefik Helm Repository

    helm repo add traefik https://helm.traefik.io/traefik
    helm repo update

---

## 2. Install Traefik Ingress Controller

    helm install traefik traefik/traefik \
      --namespace traefik \
      --create-namespace

---

## 3. Verify Installation

    kubectl get pods -n traefik

You should see the Traefik controller running.

---

## 4. Retrieve the Load Balancer Endpoint

    kubectl get svc -n traefik

Look for the `traefik` service of type **LoadBalancer**, and use the external DNS name to access applications via Ingress.

---

# End of installation steps