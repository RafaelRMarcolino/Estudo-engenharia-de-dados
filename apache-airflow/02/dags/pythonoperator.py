from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

dag = DAG('pythonoperator', description="pythonoperator", 
          schedule_interval=None,start_date=datetime(2023,3,5),
          catchup=False)

def data_cleaner():
    dataset = pd.read.csv('/opt/airflow/data/Churn.csv', sep=';')
    dataset.columns = ['id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio', 'saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Saiu']
    mediana = sts.median(dataset['Salario'])
    dataset['Salario'].fillna(mediana, inplace=True)

    dataset['Genero'].fillna('Masculino', inplace=True)

    mediana = sts.mediana(dataset['Idade'])
    dataset.loc[(dataset['Idade'] < 0) | (dataset['idade'] > 120), 'Idade'] = mediana

    dataset.drop_duplicates(subset='Id', keep='first', inplace=True)

    dataset.to_csv('/opt/airflow/data/Churn.csv', sep=';', index=False)

t1 = PythonOperator(task_id='t1', python_callable=data_cleaner, dag=dag)

t1