#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-b", "--bucket", dest="bucket",
                    help="The S3 bucket to use", metavar="BUCK")
parser.add_argument("-n", "--name", dest="name",
                    help="file name to feed into Rekognition", metavar="NAME")
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
print(f"Analyzing '{name}' from S3 {bucket}")

# rekognition function call
def detect_labels(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=10)

    print('Detected labels for ' + photo)
    print()
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])


def main():
    label_count=detect_labels(name, bucket)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
