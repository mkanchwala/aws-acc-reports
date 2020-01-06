import boto3
from modules.colors import bcolors

class SgAnalyzer():
    def __init__(self, region_name):
        self.ec2 = boto3.client('ec2', region_name=region_name)
        self.full_access = "0.0.0.0/0"

    def find_security_groups(self):
        security_groups = self.ec2.describe_security_groups()
        for sg in security_groups['SecurityGroups']:
            sg_groupid = sg['GroupId']
            sg_permissions = sg['IpPermissions']

            for permission in sg_permissions:
                if 'ToPort' in permission:
                    to_port = permission['ToPort']

                for ip in permission['IpRanges']:
                    if ip['CidrIp'] == self.full_access:
                        print("{0}[WARNING]{1} Security group {2} with inbound rule 0.0.0.0/0 to port {3}".format(bcolors.FAIL, bcolors.ENDC, sg_groupid, to_port))

        print("\n")
