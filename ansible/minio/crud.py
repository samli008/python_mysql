import boto3
import botocore
from botocore.exceptions import ClientError
import logging

AK='C5PR8CK8FB16NGAR125W'
SK='12345678'

s3=boto3.resource('s3',aws_access_key_id=AK,
                   aws_secret_access_key=SK,
                   endpoint_url='http://192.168.20.143:7480')

choose=input("pls input your choose[list,new,del,obj,up,down,delete]: ")

if choose == 'list':
  for bucket in s3.buckets.all():
    print('bucket name: %s' % bucket.name)
elif choose == 'new':
  new=input("pls intput new bucket name: ")
  s3.create_bucket(Bucket=new)
  for bucket in s3.buckets.all():
    print('bucket name: %s' % bucket.name)
elif choose == 'del':
  del1=input("pls input del bucket name: ")
  try:
    bucket= s3.Bucket(del1)
    bucket.delete()
    for bucket in s3.buckets.all():
      print('bucket name: %s' % bucket.name)
  except botocore.exceptions.ClientError as e:
    print('bucket is not empty')
elif choose == 'obj':
  bucket_name = input("bucket name: ")
  bucket = s3.Bucket(bucket_name)
  for obj in bucket.objects.all():
    print('obj name: %s' % obj.key)
elif choose == 'up':
  bucket_name = input("bucket name: ")
  file = input("file name: ")
  s3.Object(bucket_name,file).upload_file(file)
elif choose == 'down':
  bucket_name = input("bucket name: ")
  file = input("file name: ")
  s3.Object(bucket_name,file).download_file(file)
elif choose == 'delete':
  try:
    bucket_name = input("bucket name: ")
    bucket= s3.Bucket(bucket_name)
    bucket.objects.filter().delete()
  except botocore.exceptions.ClientError as e:
    print('bucket is not exist')
else:
  print("your choose error!")
