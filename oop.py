class Topic:

    def __init__(self):
        self.__clients = []

    def register(self, client):
        print('New subscriber: {}'.format(client))
        self.__clients.append(client)

    def notifyAll(self, *args, **kwargs):
        for client in self.__clients:
            client.notify(self, *args, **kwargs)


class Observer:

    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, '---> got ', args, 'from', topic)


topic = Topic()
obs_1 = Observer(topic)
obs_2 = Observer(topic)
topic.notifyAll('Test notification')
