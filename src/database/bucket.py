from typing import TYPE_CHECKING

import boto3
from src.config import S3_BUCKET, S3_ENDPOINT, S3_KEY, S3_SECRET

if TYPE_CHECKING:
    import botostubs


def get_bucket() -> "botostubs.S3.S3Resource.Bucket":
    """Boto3インスタンスを作成し、S3バケットを返します"""
    s3: "botostubs.S3.S3Resource" = boto3.resource(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=S3_KEY,
        aws_secret_access_key=S3_SECRET,
    )
    bucket = s3.Bucket(S3_BUCKET)  # type: ignore
    return bucket
