import pulumi
import pulumi_aws as aws

class S3Bucket(pulumi.ComponentResource):
    def __init__(self, name: str, enable_versioning=True, enable_encryption=True, opts=None):
        super().__init__('custom:S3Bucket', name, None, opts)

        self.bucket = aws.s3.Bucket(
            f"{name}-bucket",
            bucket_prefix=f"{name}-",
            acl="private",
            versioning=aws.s3.BucketVersioningArgs(enabled=enable_versioning),
            server_side_encryption_configuration=aws.s3.BucketServerSideEncryptionConfigurationArgs(
                rule=aws.s3.BucketServerSideEncryptionConfigurationRuleArgs(
                    apply_server_side_encryption_by_default=aws.s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                        sse_algorithm="AES256"
                    )
                )
            ) if enable_encryption else None
        )

        pulumi.export(f"{name}_bucket_name", self.bucket.bucket)
        self.register_outputs({})
