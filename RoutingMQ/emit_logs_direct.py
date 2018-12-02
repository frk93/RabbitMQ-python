import pika
import sys
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

n = int(input("Enter number of queues you want to create : "))

StockQueues = []

for x in range(n):
    StockQueues.append(input("Enter Stock Queues.... : "))


print(StockQueues)

while True:
    for x in StockQueues:
        message = str(random.randint(1, 101))
        channel.basic_publish(exchange='direct_logs',
                              routing_key=x,
                              body=message)
        print("Send -> %r" % message)

    time.sleep(3)



connection.close()