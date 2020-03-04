# pip3 install boto3 -i https://mirrors.aliyun.com/pypi/simple
import boto3

s3client=boto3.client('s3',aws_access_key_id='C5PR8CK8FB16NGAR125W',
                      aws_secret_access_key='12345678',
                      endpoint_url='http://192.168.20.143:7480')

print("{a:15}{b:15}".format(a='bucket',b='createTime'))

buckets = s3client.list_buckets()

for bucket in buckets['Buckets']:
  date=str(bucket['CreationDate'])
  print(f"{bucket['Name']:15}{date:15}")
