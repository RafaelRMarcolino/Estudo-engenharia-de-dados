from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.subdag import SubDagOperator
from airflow.operators.python import PythonOperator


dag = DAG('exemplo_xcom', description="xcom", 
          schedule_interval=None,start_date=datetime(2023,3,5),
          catchup=False)


def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valorxcom1', value=10200)
task1 = PythonOperator(task_id='tsk1', python_callable=task_write, dag=dag)

def task_read(**kwargs):
    valor = kwargs['ti'].xcom_pull(key='valorxcom1')
    print(f'Valor recuperado: {valor}')

task2 = PythonOperator(task_id='tsk2',python_callable=task_read, dag=dag)


task1 >> task2
