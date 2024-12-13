# /kafka/bin$ ./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --from-beginning

from kafka import KafkaConsumer as kc
consumidor = kc("mensagens", bootstrap_servers="127.0.0.1:9092", consumer_timeout_ms=1000,
               group_id="consumidores")

for mensagem in consumidor:
    print("Topic: ", mensagem.topic)
    print("Partição ", mensagem.partition)
    print("Chave", mensagem.key)
    print("offset ", mensagem.offset)
    print("Mensagem ", mensagem.value)
    print("-------------------------------------")

# ./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores

