import os
import pandas as pd
from pyathena import connect

from config.aws_config import(
    AWS_ACESS_KEY,
    AWS_SECRET_KEY,
    AWS_REGION,
    S3_STAGING_DIR
)

def select_query(query_paths, number: int):
    list_archives = os.listdir(query_paths)
    list_archives = [archives for archives in list_archives if archives.endswith('.sql')][number]
    return list_archives

def execute_query(query: str):
    query_note = select_query(query_paths= query, number = 0)
    
    with open(f"data/queries/{query_note}", 'r') as file:
        query_note = file.read()
        conn = connect(aws_access_key_id=AWS_ACESS_KEY,
                    aws_secret_access_key=AWS_SECRET_KEY,
                    region_name=AWS_REGION,
                    s3_staging_dir=S3_STAGING_DIR)
        
        cursor = conn.cursor()
        cursor.execute(query_note)
        
        col_names = [col[0] for col in cursor.description]
        results = cursor.fetchall()
        
        return col_names, results


def create_dataframe_from_query(query: str):
    #importando os resultados 
    try:
        col_names, result = execute_query(query)
        df = pd.DataFrame(result, columns=col_names)
        return df
    except Exception as e:
        print(e)
        return None