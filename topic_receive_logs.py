from connect_rabbit import connect
import sys

connection, channel = connect()
channel.exchange_declare(exchange='topic_logs',
	exchange_type='topic')

result = channel.queue_declare(exclusive=True, queue='')
queue_name = result.method.queue

servities = sys.argv[1:]

for servity in servities:
	channel.queue_bind(exchange='topic_logs',
		queue=queue_name,
		routing_key=servity)

print(f' [*] waiting for logs')

def callback(ch, method, properties, body):
	print(f' [x] routing_key is {method.routing_key} body id ${body}')

channel.basic_consume(on_message_callback=callback,
	queue=queue_name,
	)

channel.start_consuming()
