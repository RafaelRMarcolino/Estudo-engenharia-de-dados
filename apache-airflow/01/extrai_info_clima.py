# www.visualcrossing.com
# https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/
# pip install pandas
# pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.8.txt"
# instalando linux wsl --install
# export AIRFLOW_HOME=~/apache-airflow
# airflow standalone
#admin  password: 77WnG5qhckTNB3ck
#http://localhost:8080/

import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

#intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'BDBQT8K68GJHUV4ZDWV8JEXQW'

# URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
#            f'{city}/{data_inicio}/{data_fim}?key=YOUR_API_KEY ')

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL)
print(dados.head())

file_path = 'C:/projetos/treinologica/beecrowd-python-sql/apache-airflow/semena={data_inicio}'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'condicoes.csv')


