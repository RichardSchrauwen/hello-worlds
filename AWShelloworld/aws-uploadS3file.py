import logging
import boto3
import sys
from botocore.exceptions import ClientError
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-b", "--bucket", dest="bucket",
                    help="The S3 bucket to use", metavar="BUCK")
parser.add_argument("-n", "--name", dest="name",
                    help="file name to upload", metavar="NAME")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the bucket from command line (default is pictures-to-analyze)
bucket = "pictures-to-analyze"
if args.bucket != None:
    bucket = args.bucket

# get the file name from command line
if args.name == None:
    print("Oops, no file name was entered. Please use '-n <name>' arg.")
    sys.exit()
name = args.name
print(f"Uploading '{name}' to S3 {bucket}")

# S3 function call
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#file_name = "test1.jpg"
#bucket = "pictures-to-analyze"
print(f"Upload file {name} to bucket {bucket}")
if (upload_file(name, bucket)):
    print("success")
else:
    print("failed")
