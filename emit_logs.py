import pika
import sys

from connect_rabbit import connect

connection, channel = connect()
channel.exchange_declare(exchange="logs",
	exchange_type="fanout")

msg = ' '.join(sys.argv[1:]) or 'hello world'
channel.basic_publish(exchange="logs",
	routing_key='',
	body=msg)

print(f' [x] send msg {msg}')
connection.close()
