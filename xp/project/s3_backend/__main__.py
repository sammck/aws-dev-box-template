# Copyright (c) 2022 Sam McKelvie
#
# See LICENSE file accompanying this package.
#

import pulumi
import pulumi_aws as aws
from xpulumi.runtime import pconfig, aws_provider, split_s3_uri

backend_uri = pconfig.require("backend_uri")
bucket_name, backend_subkey = split_s3_uri(backend_uri)
while backend_subkey.endswith('/'):
  backend_subkey = backend_subkey[:-1]

slash_backend_subkey = '' if backend_subkey == '' else '/' + backend_subkey

bucket = aws.s3.Bucket("bucket",
    bucket=bucket_name,
    opts=pulumi.ResourceOptions(
        provider=aws_provider,
      )
  )

pulumi.export("backend_bucket", bucket_name)
pulumi.export("backend_subkey", backend_subkey)
pulumi.export("backend_uri", backend_uri)
