from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.models import Variable

dag = DAG('variaveis', description="variaveis", 
          schedule_interval=None,start_date=datetime(2023,3,5),
          catchup=False)

def python_variaveis(**context):
    minha_var = Variable.get('minhavar')
    print(f'O valor da variavel é {minha_var}')

task1 = PythonOperator(task_id='tsk1',python_callable=python_variaveis,dag=dag)


task1
