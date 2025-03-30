import pika 

def send(queue_name, request_data):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=request_data,
                          properties=pika.BasicProperties(delivery_mode=2))

    connection.close()
    return print(f"{request_data}")
