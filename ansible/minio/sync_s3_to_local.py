# sync bucket to local
def sync_s3_to_local(bucket, local):
  import boto3
  import os

  mkdir(local)

  files = set(os.listdir(local))

  s3 = boto3.resource('s3')
  bucket = s3.Bucket(bucket)
  for obj in bucket.objects.all():
    file = obj.key
      if file not in files:
        bucket.download_file(file, os.path.join(local, file))
