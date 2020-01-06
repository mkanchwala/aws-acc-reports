import os

class CONFIG:
    iam_max_access_key_age = int(os.getenv('IAM_MAX_ACCESS_KEY_AGE', 60))
