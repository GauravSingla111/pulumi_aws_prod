import pulumi
import pulumi_aws as aws

class Network(pulumi.ComponentResource):
    def __init__(self, name: str, opts=None):
        super().__init__('custom:Network', name, None, opts)

        # VPC
        self.vpc = aws.ec2.Vpc(
            f"{name}-vpc",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True
        )

        # Subnet
        self.subnet = aws.ec2.Subnet(
            f"{name}-subnet",
            vpc_id=self.vpc.id,
            cidr_block="10.0.1.0/24",
            map_public_ip_on_launch=True
        )

        # Security group
        self.sg = aws.ec2.SecurityGroup(
            f"{name}-sg",
            vpc_id=self.vpc.id,
            description="Allow SSH and HTTP",
            ingress=[
                {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
                {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]}
            ],
            egress=[{"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}]
        )

        self.register_outputs({})
