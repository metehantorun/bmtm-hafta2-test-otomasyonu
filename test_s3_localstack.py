import boto3
import pytest

ENDPOINT = "http://localhost:4566"

@pytest.fixture
def s3_client():
    return boto3.client("s3",
        endpoint_url=ENDPOINT,
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1"
    )

def test_create_bucket(s3_client):
    s3_client.create_bucket(Bucket="my-test-bucket")
    buckets = s3_client.list_buckets()
    names = [b["Name"] for b in buckets["Buckets"]]
    assert "my-test-bucket" in names

def test_upload_and_download(s3_client):
    s3_client.create_bucket(Bucket="upload-test")
    s3_client.put_object(Bucket="upload-test", Key="hello.txt", Body=b"Merhaba Dunya!")
    response = s3_client.get_object(Bucket="upload-test", Key="hello.txt")
    content = response["Body"].read().decode()
    assert content == "Merhaba Dunya!"