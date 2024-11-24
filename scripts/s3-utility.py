import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# setup variables
SRC_ACCESS_KEY = os.getenv('SRC_ACCESS_KEY')
SRC_ACCESS_SECRET = os.getenv('SRC_ACCESS_SECRET')
SRC_BUCKET_NAME = os.getenv('SRC_BUCKET_NAME')
DST_ACCESS_KEY = os.getenv('DST_ACCESS_KEY')
DST_ACCESS_SECRET = os.getenv('DST_ACCESS_SECRET')
DST_BUCKET_NAME = os.getenv('DST_BUCKET_NAME')

def initSession(key_id, key_secret):
    session = boto3.client('s3',
                      endpoint_url="https://s3.sunteco.app",
                      aws_access_key_id=key_id,
                      aws_secret_access_key=key_secret)
    return session

def listObj(session, bucket_name):
    objs = session.list_objects_v2(Bucket=bucket_name)
    return objs

def uploadObj(session, bucket_name, file_name, obj_name):
    session.upload_file(file_name, bucket_name, obj_name)

def delObj(session, bucket_name, file_name):
    session.delete_object(Bucket=bucket_name, Key=file_name)

def transferObj(session, source_bucket, destination_bucket, file_name):
    session.copy_object(Bucket=destination_bucket, CopySource=source_bucket/file_name, Key=file_name)

def main():
    # init session to source bucket
    srcSession = initSession(SRC_ACCESS_KEY, SRC_ACCESS_SECRET)

    # init session to destination bucket
    desSession = initSession(DST_ACCESS_KEY, DST_ACCESS_SECRET)

    # upload file to source bucket
    # uploadObj(desSession, DST_BUCKET_NAME, '/home/phuctruong/Downloads/ubuntu-24.04.1-desktop-amd64.iso', 'ubuntu-24.04.1-desktop-amd64.iso')

    # delete obj
    # delObj(desSession, DST_BUCKET_NAME, 'ubuntu-24.04.1-desktop-amd64.iso')

    # transfer obj
    transferObj
    
    # list objs in source bucket
    srcListObjs = listObj(srcSession, SRC_BUCKET_NAME)
    for srcObj in srcListObjs['Contents']:
        print(srcListObjs['Name'] + " ---- " + srcObj['Key'])

    # list objs in destination bucket
    desListObjs = listObj(desSession, DST_BUCKET_NAME)
    for desObj in desListObjs['Contents']:
        print(desListObjs['Name'] + " ---- " + desObj['Key'])


if __name__ == '__main__':
    main()