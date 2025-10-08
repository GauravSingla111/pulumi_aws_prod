import pulumi
import pulumi_aws as aws

class EC2Instance(pulumi.ComponentResource):
    def __init__(self, name: str, network, instance_type="t3.micro", key_name=None, opts=None):
        super().__init__('custom:EC2Instance', name, None, opts)

        ami = aws.ec2.get_ami(
            most_recent=True,
            owners=["amazon"],
            filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}]
        )

        self.instance = aws.ec2.Instance(
            f"{name}-server",
            ami=ami.id,
            instance_type=instance_type,
            subnet_id=network.subnet.id,
            vpc_security_group_ids=[network.sg.id],
            key_name=key_name,
            tags={"Name": f"{name}-ec2", "Environment": "production"}
        )

        pulumi.export(f"{name}_public_ip", self.instance.public_ip)
        pulumi.export(f"{name}_dns", self.instance.public_dns)
        self.register_outputs({})
