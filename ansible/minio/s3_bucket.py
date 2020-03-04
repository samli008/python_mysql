# pip3 install boto3 -i https://mirrors.aliyun.com/pypi/simple
import boto3

s3=boto3.resource('s3',aws_access_key_id='C5PR8CK8FB16NGAR125W',
                      aws_secret_access_key='12345678',
                      endpoint_url='http://192.168.20.143:7480')

print("{a:15}{b:15}".format(a='bucket',b='createTime'))

for bucket in s3.buckets.all():
  print(bucket.name)
