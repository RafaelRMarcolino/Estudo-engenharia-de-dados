"""
The Central Bank of Financing lost many registers after a server failure that happened last October. The collection dates for the parcels where lost.

The bank requested your help to select the names and day of month in which each client must pay theirs parcel.

OBS: The day of month must be an integer.
"""

from pyspark.sql.types import StructField, StructType, StringType, IntegerType, DateType
from datetime import datetime
from faker import Faker
import random
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("YourAppName") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.pyspark.python", "python3") \
    .getOrCreate()

# Inicializando o Faker
fake = Faker()

# Definindo o esquema
schema_type = StructType([
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('value', IntegerType(), True),
    StructField('payday', DateType(), True)
])

# Gerando 30 dados fictícios
data_payday = []
for i in range(30):
    id_value = i + 1
    name_value = fake.name()
    value_value = random.randint(1000, 1000000)  # Valor aleatório entre 1000 e 1.000.000
    payday_value = fake.date_between(start_date='-3y', end_date='today')  # Data aleatória nos últimos 3 anos

    data_payday.append((id_value, name_value, value_value, payday_value))

# Criando o DataFrame
df = spark.createDataFrame(data_payday, schema=schema_type)

df.createOrReplaceTempView('payday_view')

# spark.sql("""
#           SELECT name, cast(extract(DAY FROM payday) AS INT) as day from payday_view
#           """).show()

spark.sql("""
          SELECT name, day(payday) AS day
          FROM payday_view
           """).show()

# -- SELECT name, cast(EXTRACT(DAY FROM payday) AS INT) as day
# -- FROM loan





