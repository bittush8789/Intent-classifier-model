# Create a Kubernetes (EKS) Cluster on AWS Using eksctl  

---

## 1. Prerequisites  
You should have these installed and configured:  
- AWS CLI (`aws configure` should be completed)  
- `eksctl`  
- `kubectl`  

---

## 2. Create a Simple EKS Cluster

    eksctl create cluster \
      --name my-cluster \
      --region us-east-1 \
      --version 1.32 \
      --nodegroup-name standard-workers \
      --node-type t3.medium \
      --nodes 2 \
      --nodes-min 1 \
      --nodes-max 3 \
      --managed

This command automatically creates:  
- VPC, Subnets  
- EKS Control Plane  
- Managed Node Group  
- IAM roles & required resources  

---

## 3. Configure kubeconfig

If needed, update kubeconfig manually:

    aws eks update-kubeconfig --region us-east-1 --name my-cluster

Verify nodes:

    kubectl get nodes
    kubectl get pods -n kube-system

---

## 4. Quick Verification

List clusters:

    eksctl get cluster

Describe cluster:

    aws eks describe-cluster --name my-cluster --region us-east-1

---

## 5. Delete the Cluster (Cleanup)

    eksctl delete cluster --name my-cluster --region us-east-1

This removes the control plane and node group to avoid unwanted AWS charges.

---

If you want, I can also share  
**• a clean eksctl YAML config file**,  
**• a version for private clusters**, or  
**• a production-ready node group setup.**