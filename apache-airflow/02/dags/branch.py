from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime
import random

dag = DAG('branchtest', description="branchtest", 
          schedule_interval=None,start_date=datetime(2023,3,5),
          catchup=False)



def gera_numero_aletorio():
    return random.randint(1, 1000)

gera_numero_aletorio_task = PythonOperator(
    task_id='gera_numero_aleatorio_task',
    python_callable= gera_numero_aletorio, dag=dag
)

def avalia_numero_aleatorio(**context):
    number = context['task_instance'].xcom_pull(task_ids='gera_numero_aleatorio_task')
    if number % 2==0:
        return 'par_task'
    else:
        return 'impar_task'
    

branch_task = BranchPythonOperator(
    task_id='barcnh_task',
    python_callable=avalia_numero_aleatorio,
    provide_context=True,
    dag=dag
)

par_task = BashOperator(task_id='tsk1',bash_command='echo Numero par',dag=dag, )
impar_task = BashOperator(task_id='tsk2',bash_command='echo Numero impar',dag=dag )
