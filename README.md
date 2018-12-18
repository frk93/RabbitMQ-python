# RabbitMQ-python

Implementation of RabbitMQ tutorials in **Python**.

*On Master Branch*, 

*Hello World*
We have a simple Hello world Program which doesn't expect some exchange between a producer and consumer but a **QUEUE**. 

*Pubsub*
PubSub have a exchange with dynamic queues, so if we subcribe to specific exchange ( channeling / Channel ) , All the consumer will get what the producer is sending to the specific channel. The channel is basically a kind of **FANOUT**, you can say a **BROACAST**.

*RoutingMQ*
RoutingMQ is a little bit different both of the above, what its do is creating a DIRECT exchange and an option to describe a TOPIC, so if someone need to listen from special TOPIC you need to subscribe that.
