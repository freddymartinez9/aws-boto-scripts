# This script will result all the AWS IAM Users whose access keys are 90 days old

import datetime
import boto3

from dateutil import parser

iam = boto3.client('iam')
paginator = iam.get_paginator('list_users')

timeLimit = datetime.datetime.now() - datetime.timedelta(days=90)

print("-------------------------------------------------------------------")
print(" Username" + "\t\t" + "Access Keys ID " + "\t\t" + "Day/Month/Year ")
print("-------------------------------------------------------------------")

for p in paginator.paginate():
    for user in p.get('Users', []):
        if 'UserName' in user:
            username = user['UserName']
            for key in iam.list_access_keys(UserName=username).get('AccessKeyMetadata', []):
                cd = key['CreateDate'].date()
                if cd <= timeLimit.date():
                    print(username, key['AccessKeyId'], cd.strftime('%m/%d/%Y'))






