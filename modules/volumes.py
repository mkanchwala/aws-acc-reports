import boto3

from modules.colors import bcolors

class VolumesAnalyzer():
    def __init__(self, region_name):
        self.ec2 = boto3.client('ec2', region_name=region_name)

    def find_volumes_available(self):
        volumes = self.ec2.describe_volumes()
        for volume in volumes['Volumes']:
            volume_id = volume['VolumeId']
            if not volume['Attachments']:
                print("{0}[INFO]{1} EBS Volume {2} available".format(bcolors.WARNING, bcolors.ENDC, volume_id))

        print("\n")
