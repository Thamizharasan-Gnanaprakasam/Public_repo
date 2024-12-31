import os
import sys
import yaml

directory_path= sys.argv[1]

os.chdir(f"{directory_path}")

os.system(f"snow snowpark build")
os.system(f"snow snowpark deploy --replace --temporary-connection --account $SNOWFLAKE_ACCOUNT --user $SNOWFLAKE_USER --role $SNOWFLAKE_ROLE --warehouse $SNOWFLAKE_WAREHOUSE --database $SNOWFLAKE_DATABASE")  