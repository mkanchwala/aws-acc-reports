import boto3

from modules.colors import bcolors

class ElasticIpAnalyzer():
    def __init__(self, region_name):
        self.ec2 = boto3.client('ec2', region_name=region_name)

    def find_elastic_dissociated(self):
        elasticips = self.ec2.describe_addresses()
        for ip in elasticips['Addresses']:
            allocation_id = ip['AllocationId']
            public_ip = ip['PublicIp']

            if 'InstanceId' not in ip:
                print("{0}[INFO]{1} Elastic IP {2} with public IP {3} is not associated".format(bcolors.WARNING, bcolors.ENDC, allocation_id, public_ip))

        print("\n")
