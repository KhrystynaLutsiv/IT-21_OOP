class Company:
    def __init__(self):
        self.next_worker = None

    def set_next_worker(self, next_worker):
        self.next_worker = next_worker
        return next_worker

    def request(self, request):
        print(f'Клієнт звертається до Компанії з запитом: "{request}"')
        self.process_request(request)

    def process_request(self, request):
        if self.next_worker:
            return self.next_worker.process_request(request)
        return None


class Tester(Company):
    def process_request(self, request):
        if request == 'Знайти помилки':
            print('Я тестувальник, я зможу це зробити.')
            return
        else:
            print('Я тестувальник, я вмію тільки знаходити помилки.')
        return self.next_worker.process_request(request)


class Developer(Company):
    def process_request(self, request):
        if request == 'Розробити програму':
            print('Я розробник, я зможу це зробити.')
            return
        else:
            print('Я розробник, я вмію тільки розробляти програми.')
        return self.next_worker.process_request(request)


class Designer(Company):
    def process_request(self, request):
        if request == 'Створити дизайн':
            print('Я дизайнер, я зможу це зробити.')
            return
        else:
            print('Я дизайнер, я вмію тільки створювати дизайни.')
        return self.next_worker.process_request(request)


class Analyst(Company):
    def process_request(self, request):
        if request == 'Дослідити проект':
            print('Я аналітик, я зможу це зробити.')
            return
        else:
            print('Я аналітик, я вмію тільки досліджувати проекти.')
        return self.next_worker.process_request(request)


class Manager(Company):
    def process_request(self, request):
        if request == 'Створити план проекту':
            print('Я менеджер, я зможу це зробити.')
            return
        else:
            print('Я менеджер, я вмію тільки створювати плани проектів.')
        return self.next_worker.process_request(request)


company = Company()
tester = Tester()
developer = Developer()
designer = Designer()
analyst = Analyst()
manager = Manager()

company.set_next_worker(tester).set_next_worker(developer).set_next_worker(designer).set_next_worker(analyst).set_next_worker(manager)

company.request('Створити план проекту')
print('-----------------------')
company.request('Розробити програму')