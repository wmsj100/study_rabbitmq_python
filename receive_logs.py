import time
from connect_rabbit import connect

connection, channel = connect()
channel.exchange_declare(exchange='logs',
	exchange_type='fanout')

result = channel.queue_declare(exclusive=True, queue='')
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
	queue=queue_name)

print(' [*] waiting for logs')

def callback(ch, method, properties, body):
	print(f' [x] ${body}')

channel.basic_consume(on_message_callback=callback,
	queue=queue_name,
	)

channel.start_consuming()
