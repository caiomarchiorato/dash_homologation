import os

S3_STAGING_DIR = 's3://underberg-datalake-queries-prd/caio.gouveia' 
AWS_ACESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')