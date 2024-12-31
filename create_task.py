import snowflake.connector
from snowflake.core.task import Task, StoredProcedureCall
from snowflake.core.task.dagv1 import DAG, DAGTask, DAGOperation, CreateMode
from snowflake.core import Root
from first_snowpark_project.app import procedures
from datetime import timedelta

conn = snowflake.connector.connect()

print(conn)

root = Root(conn)

task = Task(name="First_Task", definition= StoredProcedureCall(procedures.hello_procedure, stage_location='@dev_deployment'), warehouse='compute_wh', schedule=timedelta(hours=1))

schema = root.databases["demo_db"].schemas["public"]
#schema.tasks.create(task)

with DAG(name="DAG_TASK", schedule=timedelta(days=1), warehouse="compute_wh") as dag:
    dag_task_1 = DAGTask(name="Task1",definition=StoredProcedureCall(procedures.hello_procedure, stage_location="@dev_deployment"))
    dag_task_2 = DAGTask(name="Task2",definition=StoredProcedureCall(procedures.test_procedure, stage_location="@dev_deployment"))
    
    dag_task_1 >> dag_task_2
    
    schema = root.databases["demo_db"].schemas["public"]
    
    do = DAGOperation(schema)
    
    do.deploy(dag,CreateMode.or_replace)