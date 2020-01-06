import boto3

from modules.colors import bcolors

class IgwAnalyzer():
    def __init__(self, region_name):
        self.ec2 = boto3.client('ec2', region_name=region_name)

    def find_igw_detached(self):
        igws = self.ec2.describe_internet_gateways()

        for igw in igws['InternetGateways']:
            igw_id = igw['InternetGatewayId']
            if not igw['Attachments']:
                print("{0}[INFO]{1} Internet Gateway {2} it is detached".format(bcolors.WARNING, bcolors.ENDC, igw_id))

        print("\n")
