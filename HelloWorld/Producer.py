import pika;

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

while(True):
    name = input("Enter Something..: ")
    channel.queue_declare(queue='postBox')

    channel.basic_publish(exchange='',
                          routing_key='postBox',
                          body=name)


connection.close()
