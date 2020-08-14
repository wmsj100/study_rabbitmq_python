import pika
import sys

credentials = pika.PlainCredentials('user1', 'pwd')
parameter = pika.ConnectionParameters('rabbit', 5672, 'vhost_user1', credentials)
connection = pika.BlockingConnection(parameter)
channel = connection.channel()
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
