import pika

credentials = pika.PlainCredentials('user1', 'pwd')
parameter = pika.ConnectionParameters('rabbit', 5672, 'vhost_user1', credentials)
connection = pika.BlockingConnection(parameter)
channel = connection.channel()
channel.queue_declare(queue='test01')

channel.basic_publish(exchange='',
	routing_key='test01',
	body='Hello world')

print(' [x] sent msg')
connection.close()
