import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

class EKSCluster(pulumi.ComponentResource):
    def __init__(self, name: str, network, node_count=2, node_instance_type="t3.medium", opts=None):
        super().__init__('custom:EKSCluster', name, None, opts)

        self.cluster = eks.Cluster(
            f"{name}-eks",
            vpc_id=network.vpc.id,
            subnet_ids=[network.subnet.id],
            instance_type=node_instance_type,
            desired_capacity=node_count,
            min_size=1,
            max_size=node_count + 1,
            tags={"Name": f"{name}-eks", "Environment": "production"}
        )

        pulumi.export(f"{name}_kubeconfig", self.cluster.kubeconfig)
        self.register_outputs({})
