import pika
import sys
from connect_rabbit import connect

connection, channel = connect()
channel.queue_declare(queue='test02', durable=True)

msg = ' '.join(sys.argv[1:]) or 'hello world'
channel.basic_publish(exchange='',
	routing_key='test02',
	body=msg,
	properties=pika.BasicProperties(
		delivery_mode=2,
	))

print(' [x] sent msg')
connection.close()
