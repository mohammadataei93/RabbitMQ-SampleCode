import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')

message = 'this is testing fanout'
ch.basic_publish(exchange='logs', routing_key='f', body=message)

print('message sent')
connection.close()






