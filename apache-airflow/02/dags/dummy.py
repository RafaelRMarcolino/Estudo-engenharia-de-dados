from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator





dag = DAG('dummy', description="dummy", 
          schedule_interval=None, start_date=datetime(2024,5,17),
          catchup=False, default_view='graph', tags=['processo', 'tag', 'pipeline'])

task1 = BashOperator(task_id='tsk1',bash_command="sleep 5",dag=dag)
task2 = BashOperator(task_id='tsk2',bash_command="sleep 5",dag=dag)
task3 = BashOperator(task_id='tsk3',bash_command="sleep 5",dag=dag)
task4 = BashOperator(task_id='tsk4',bash_command="sleep 5",dag=dag)
task5 = BashOperator(task_id='tsk5',bash_command="sleep 5",dag=dag)
# taskdummy = DummyOperator(task_id='taskdummy', dag=dag)

# [task1, task2, task3] >> taskdummy >> [task3 , task4]
