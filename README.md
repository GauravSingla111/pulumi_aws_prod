
# Pulumi AWS Production-Ready Infrastructure (Python)

This project demonstrates a **production-grade, reusable AWS infrastructure setup** using **Pulumi with Python**.  
It provides **modular, object-oriented components** for deploying **VPCs, S3 buckets, EC2 instances, and EKS clusters**, suitable for enterprise workloads.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Architecture Diagram](#architecture-diagram)  
3. [Project Structure](#project-structure)  
4. [Components](#components)  
5. [Setup & Deployment](#setup--deployment)  
6. [Usage Example](#usage-example)  
7. [Best Practices](#best-practices)  

---

## Project Overview
- **Reusable & modular:** Classes can be reused across multiple environments (staging, production)  
- **Production-ready:** Includes encryption, versioning, tags, and secure networking  
- **Scalable:** Supports multiple EC2 instances and EKS clusters  
- **Team-friendly:** Clear separation of components for collaboration  

---

## Architecture Diagram

Here’s a high-level architecture of the infrastructure:

![Pulumi AWS Architecture](https://example.com/architecture-diagram.png)

```

+------------------------+
|        S3 Bucket       |
| (Encrypted, Versioned) |
+------------------------+
|
+------------------------+
|       EC2 Instance     |
|  (SSH/HTTP Access)     |
+------------------------+
|
+------------------------+
|       EKS Cluster      |
|  (Managed Kubernetes)  |
+------------------------+
|
VPC / Networking
(Subnets + Security Groups)

```

> Replace the above image link with your actual architecture diagram image hosted on GitHub or an image hosting service.

---

## Project Structure
```

pulumi_aws_prod/
├── **main**.py              # Main stack orchestrator
├── components/
│   ├── **init**.py
│   ├── s3_bucket.py         # Reusable S3 component
│   ├── ec2_instance.py      # Reusable EC2 component
│   ├── eks_cluster.py       # Reusable EKS component
│   └── network.py           # Reusable VPC/network component
└── Pulumi.yaml              # Pulumi project configuration

````

---

## Components

### 1. Network Component
- Creates **VPC, Subnets, and Security Groups**  
- Security group allows SSH (22) and HTTP (80)  
- Designed to be **reused across EC2 and EKS deployments**

### 2. S3 Bucket Component
- Private, encrypted S3 bucket  
- Supports versioning for production workloads  
- Parameterized to enable/disable encryption or versioning  
- Exports bucket name for downstream use

### 3. EC2 Instance Component
- Configurable instance type and key pair  
- Security group attached from network component  
- Exports **public IP** and **DNS** for monitoring  
- Tagged for **Environment = production**

### 4. EKS Cluster Component
- Managed EKS cluster  
- Parameterized for **node count** and **instance type**  
- Uses network component's VPC/subnets  
- Exports **kubeconfig** for kubectl access  

---

## Setup & Deployment

### 1. Prerequisites
- Python 3.9+  
- Pulumi CLI installed  
- AWS CLI configured with proper credentials  
- Required Python packages:
```bash
pip install pulumi pulumi-aws pulumi-eks
````

### 2. Configure Pulumi

```bash
pulumi login
pulumi stack init dev
pulumi config set aws:region us-east-1
```

### 3. Deploy Infrastructure

```bash
pulumi up
```

* Preview changes
* Deploy VPC, S3, EC2, and EKS
* Outputs include **bucket name, EC2 public IP, kubeconfig**

### 4. Destroy Infrastructure

```bash
pulumi destroy
```

* Safely deletes all resources managed by the stack

---

## Usage Example

```python
from components.s3_bucket import S3Bucket
from components.ec2_instance import EC2Instance
from components.eks_cluster import EKSCluster
from components.network import Network

# Build network
network = Network("prod-network")

# Deploy S3 bucket
prod_bucket = S3Bucket("prod-app", enable_versioning=True, enable_encryption=True)

# Deploy EC2 instance
prod_ec2 = EC2Instance("prod-server", network, instance_type="t3.micro", key_name="my-key")

# Deploy EKS cluster
prod_eks = EKSCluster("prod-cluster", network, node_count=3, node_instance_type="t3.medium")
```

---

## Best Practices

* Always enable **versioning and encryption** for S3 buckets
* Tag all resources for **environment tracking** and **cost management**
* Separate **network layer** to avoid duplication across stacks
* Use **parameterized classes** to easily replicate resources across staging and production
* Prefer **managed EKS** for Kubernetes workloads
* Use **Pulumi CI/CD integration** for automated deployments

---

### Optional: Add your architecture diagram images

* Example: `/images/architecture.png` in your repo
* Replace the placeholder link in the diagram section with actual image path:

```markdown
![Pulumi AWS Architecture](./images/architecture.png)
```

---

## 🧑‍💻 Author

**Gaurav Singla**
DevOps & Cloud Automation Specialist
💡 Building conscious systems with intelligent automation.

---

