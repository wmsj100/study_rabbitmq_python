import pika

def connect():
	credentials = pika.PlainCredentials('user1', 'pwd')
	parameter = pika.ConnectionParameters('rabbit', 5672, 'vhost_user1', credentials)
	connection = pika.BlockingConnection(parameter)
	channel = connection.channel()
	return connection, channel
