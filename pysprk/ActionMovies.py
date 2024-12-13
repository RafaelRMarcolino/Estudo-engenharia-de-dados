"""
A video store contractor hired her services to catalog her movies.
They need you to select the code and the name of the movies whose 
description of the genre is 'Action'.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructField, StructType, StringType, IntegerType
from pyspark.sql.functions import col

#Schema movie
movieSchema = StructType(fields=[
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('id_generes', IntegerType(), True)
])

#dados movie












movieData = [
    (1,'Batman', 3),
    (2, 'The Battle of the Dark River', 3),
    (3,	'White Duck', 1),
    (4,	'Breaking Barriers', 4),
    (5,	'The Two Hours', 2)
]

#DF Movie 
movies = spark.createDataFrame(movieData, movieSchema)
movies.show()

#Schema generes
genresSchema = StructType(fields = [
    StructField('id', IntegerType(), True),
    StructField('description', StringType(), True)
])

#dados generes
generesData = [
    (1,	'Animation'),
    (2,	'Horror'),
    (3,	'Action'),
    (4,	'Drama'),
    (5,	'Comedy'),
]

#df generes
generes = spark.createDataFrame(generesData, genresSchema)
generes.show(10)


#resultado
resultado = movies.alias('A').join(generes.alias('B'), col('A.id_generes') == col('B.id'), 'full_outer')\
.filter(col('B.description') == 'Action').select('A.id', 'A.name')
resultado.show(10)