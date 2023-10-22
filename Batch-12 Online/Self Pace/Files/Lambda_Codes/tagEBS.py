#!/usr/bin/env python

import os   
import boto3
            
ec2 = boto3.resource('ec2',
        region_name="us-west-1",
        aws_access_key_id="AKIATG2NJ2OECRN7BBE3",
        aws_secret_access_key="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"
    )
    
def lambda_handler(event, context):
            
    base = ec2.instances.all()
                
    for instance in base:
            
        print("\n[DEBUG] EC2\n\t\tID: " + str(instance))
        print("\tEBS")

        for vol in instance.volumes.all():
    
            vol_id = str(vol)
            print("\t\tID: " + vol_id)
        
if __name__ == "__main__":
    lambda_handler(0, 0)