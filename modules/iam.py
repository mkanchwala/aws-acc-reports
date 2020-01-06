import boto3

from modules.config import CONFIG
from modules.colors import bcolors
from datetime import datetime, timezone

class IamAnalyzer():
    def __init__(self):
        self.iam_client = boto3.client('iam')
        self.users = list()

    def find_users(self):
        response = self.iam_client.list_users()
        for user in response['Users']:
            self.users.append(user['UserName'])

    def find_max_access_key_age(self):
        self.find_users()

        for user in self.users:
            response = self.iam_client.get_user(UserName=user)
            create_date = response['User']['CreateDate']
            current_date = datetime.now(timezone.utc).replace(microsecond=0)
            verify_date = str(current_date - create_date).split(' ')[0]

            try:
                if int(verify_date) > CONFIG.iam_max_access_key_age:
                    print("{0}[WARNING]{1} User {2} created more than {3} days ago"\
                            .format(bcolors.FAIL, bcolors.ENDC, user, verify_date))
            except:
                continue
        print("\n")
