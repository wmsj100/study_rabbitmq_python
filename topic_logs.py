import pika
import sys

from connect_rabbit import connect

connection, channel = connect()
channel.exchange_declare(exchange="topic_logs",
	exchange_type="topic")

print(sys.argv[1])
severity = sys.argv[1] if len(sys.argv) > 2 else 'anonymouse.info'
message = ' '.join(sys.argv[2:]) or 'Hello world'
channel.basic_publish(exchange="topic_logs",
	routing_key=severity,
	body=message)

print(f' [x] send severity {severity} smsg {message}')
connection.close()
