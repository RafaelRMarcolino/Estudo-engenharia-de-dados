import time 
import re
import datetime
from kafka import KafkaProducer as kp

arquivo = open(r'/var/log/apache2/access.log', '-')

regexp = '^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+-]\\d{4})\\] \"(.+?)\" (\\d{3}) (\\d+) \"([^\"]+)\" \"(.+?)\"'
produtor = kp(bootstrap_servcers="127.0.0.1:9092")
while 1:
    if not linha:
        linha = arquivo.readline()
        time.spleep(5)
    else:
        x = reg.match(regexp, linha).groups()
        msg = bytes(str(x), encoding='ascli')
        print("Mensagem enviada em ", datetime.datetime.now())




