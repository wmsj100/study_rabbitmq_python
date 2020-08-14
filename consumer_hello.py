import pika
import time

credentials = pika.PlainCredentials('user1', 'pwd')
parameter = pika.ConnectionParameters('rabbit', 5672, 'vhost_user1', credentials)
connection = pika.BlockingConnection(parameter)
channel = connection.channel()
channel.queue_declare(queue='test02', durable=True)

def callback(ch, method, properties, body):
	table_id = body
	print(f'start deal {body}')
	time.sleep(body.count(b'.'))
	print(f'table id deal done {table_id}')
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(on_message_callback=callback,
	queue='test02')

channel.basic_qos(prefetch_count=1)

channel.start_consuming()
