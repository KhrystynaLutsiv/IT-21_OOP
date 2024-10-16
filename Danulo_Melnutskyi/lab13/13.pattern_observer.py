
class Subject:
    def __init__(self):
        self._observers = [] 

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError("Підкласи повинні реалізувати цей метод")

class NewsSubscriber(Observer):
    def __init__(self, name):
        self.name = name  # Ім'я підписника

    def update(self, message):
        print(f"{self.name} отримав нове повідомлення: {message}")

subject = Subject()

subscriber1 = NewsSubscriber("Карл")
subscriber2 = NewsSubscriber("Віктор")

subject.attach(subscriber1)
subject.attach(subscriber2)

subject.notify("Новина: Завтра по всій планеті вихідний")
