import click

from modules.s3 import S3Analyzer
from modules.iam import IamAnalyzer
from modules.securitygroups import SgAnalyzer
from modules.elasticip import ElasticIpAnalyzer
from modules.volumes import VolumesAnalyzer
from modules.ami import AmiAnalyzer
from modules.igw import IgwAnalyzer
from modules.banner import Banner

@click.command()
@click.option("--s3", is_flag=True, help="Search buckets public in s3")
@click.option("--iam", is_flag=True, help="Search iam users based on creation date")
@click.option('--sg', is_flag=True, help="Search security groups with inbound rule 0.0.0.0")
@click.option('--elasticip', is_flag=True, help="Search elastic IP not associated")
@click.option('--volumes', is_flag=True, help="Search volumes available")
@click.option('--ami', is_flag=True, help="Search AMIs with permission public")
@click.option('--owner', multiple=True, default='', help="Defines the owner of the resources to be found")
@click.option('--igw', is_flag=True, help="Search internet gateways detached")
@click.option('--region', default="us-east-1", help="Defines the region of resources")

def main(s3, iam, sg, elasticip, volumes, ami, owner, igw, region):

    if s3:
        s3 = S3Analyzer()
        s3.bucket_analyzer()

    if iam:
        iam = IamAnalyzer()
        iam.find_max_access_key_age()

    if sg:
        sg = SgAnalyzer(region)
        sg.find_security_groups()

    if elasticip:
        ip = ElasticIpAnalyzer(region)
        ip.find_elastic_dissociated()

    if volumes:
        vol = VolumesAnalyzer(region)
        vol.find_volumes_available()

    if ami:
        owners = list()

        for own in owner:
            owners.append(own)

        ami = AmiAnalyzer(owners, region)
        ami.find_public_ami()

    if igw:
        igw = IgwAnalyzer(region)
        igw.find_igw_detached()

if __name__=='__main__':
    print(Banner.banner)
    main()
