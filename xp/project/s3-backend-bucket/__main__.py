import pulumi
from pulumi import Output, log as plog
import pulumi_aws as aws
import xpulumi
from xpulumi.runtime import StackOutputs, VpcEnv, aws_resource_options, pconfig, aws_provider

bucket_name = pconfig.require("bucket_name")
backend_subkey = pconfig.get("backend_subkey")

bucket = aws.s3.Bucket("bucket",
    bucket=bucket_name,
    opts=pulumi.ResourceOptions(
        provider=aws_provider,
      )
  )

backend_uri = f"s3://{bucket_name}"
if not backend_subkey is None:
  while backend_subkey.startswith('/'):
    backend_subkey = backend_subkey[1:]
  while backend_subkey.endswith('/'):
    backend_subkey = backend_subkey[:-1]
  if backend_subkey != '':
    backend_uri = backend_uri + '/' + backend_subkey

pulumi.export("backend_bucket", bucket.bucket)
pulumi.export("backend_uri", backend_uri)
