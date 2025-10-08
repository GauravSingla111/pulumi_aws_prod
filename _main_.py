from components.s3_bucket import S3Bucket
from components.ec2_instance import EC2Instance
from components.eks_cluster import EKSCluster
from components.network import Network

# Build network
network = Network("prod-network")

# Create production S3 bucket
prod_bucket = S3Bucket("prod-app", enable_versioning=True, enable_encryption=True)

# Launch EC2 instance
prod_ec2 = EC2Instance("prod-server", network, instance_type="t3.micro", key_name="my-key")

# Launch EKS cluster
prod_eks = EKSCluster("prod-cluster", network, node_count=3, node_instance_type="t3.medium")
