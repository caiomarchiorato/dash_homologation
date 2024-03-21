import os
import pandas as pd
from pyathena import connect

from config.aws_config import(
    AWS_ACESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
    S3_STAGING_DIR
)

def execute_query(sql_query: str):
    try:
        conn = connect(aws_access_key_id=AWS_ACESS_KEY,
                    aws_secret_access_key=AWS_SECRET_KEY,
                    region_name=AWS_REGION,
                    s3_staging_dir=S3_STAGING_DIR)
        
        cursor = conn.cursor()
        cursor.execute(sql_query)
        
        col_names = [col[0] for col in cursor.description]
        results = cursor.fetchall()
        
        return col_names, results
    except Exception as e:
        print(e)
        return None, None


def create_dataframe_from_query(sql_query: str) -> pd.DataFrame:
    #importando os resultados 
    try:
        col_names, result = execute_query(sql_query)
        if col_names and result:
            df = pd.DataFrame(result, columns=col_names)
            return df
    except Exception as e:
        print(e)
        return None