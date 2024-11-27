import os
import json
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

# Конфігурація
class Config:
    DATABASE_PATH = "data/vet_clinic_data.json"
    WORKING_HOURS = {
        "start": "09:00",
        "end": "18:00"
    }
    FILE_ENCODING = "utf-8"
    JSON_INDENT = 4

# Моделі даних
@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    id: int
    medical_history: List[str]

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "id": self.id,
            "medical_history": self.medical_history
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            species=data['species'],
            breed=data['breed'],
            age=data['age'],
            id=data['id'],
            medical_history=data.get('medical_history', [])
        )

@dataclass
class Client:
    id: int
    surname: str
    name: str
    patronymic: str
    phone: str
    pets: List[Pet]

    def get_full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def to_dict(self):
        return {
            "id": self.id,
            "surname": self.surname,
            "name": self.name,
            "patronymic": self.patronymic,
            "phone": self.phone,
            "pets": [pet.to_dict() for pet in self.pets]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            surname=data['surname'],
            name=data['name'],
            patronymic=data['patronymic'],
            phone=data['phone'],
            pets=[Pet.from_dict(p) for p in data['pets']]
        )

@dataclass
class Appointment:
    time: str
    is_available: bool
    client_id: Optional[int]
    pet_id: Optional[int]

    def to_dict(self):
        return {
            "time": self.time,
            "is_available": self.is_available,
            "client_id": self.client_id,
            "pet_id": self.pet_id
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            time=data['time'],
            is_available=data['is_available'],
            client_id=data.get('client_id'),
            pet_id=data.get('pet_id')
        )

@dataclass
class Veterinarian:
    id: int
    surname: str
    name: str
    patronymic: str
    work_hours: dict
    appointments: List[Appointment]

    def get_full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def to_dict(self):
        return {
            "id": self.id,
            "surname": self.surname,
            "name": self.name,
            "patronymic": self.patronymic,
            "work_hours": self.work_hours,
            "appointments": [apt.to_dict() for apt in self.appointments]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            surname=data['surname'],
            name=data['name'],
            patronymic=data['patronymic'],
            work_hours=data['work_hours'],
            appointments=[Appointment.from_dict(a) for a in data.get('appointments', [])]
        )

# Валідатор
class DataValidator:
    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(phone and phone.isdigit() and len(phone) == 10)

    @staticmethod
    def validate_age(age: str) -> bool:
        try:
            age_num = int(age)
            return 0 < age_num < 30
        except ValueError:
            return False

    @staticmethod
    def validate_time(time: str) -> bool:
        try:
            hours, minutes = map(int, time.split(':'))
            return 0 <= hours <= 23 and 0 <= minutes <= 59
        except ValueError:
            return False

# Менеджер файлів
class FileManager:
    def __init__(self):
        self.path = Config.DATABASE_PATH
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def save_data(self, data: dict):
        with open(self.path, 'w', encoding=Config.FILE_ENCODING) as file:
            json.dump(data, file, ensure_ascii=False, indent=Config.JSON_INDENT)

    def load_data(self) -> dict:
        if not os.path.exists(self.path):
            return {"vets": [], "clients": []}
        with open(self.path, 'r', encoding=Config.FILE_ENCODING) as file:
            return json.load(file)

# Менеджери сутностей
class ClientManager:
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager
        self.clients: List[Client] = []
        self.load_clients()

    def load_clients(self):
        data = self.file_manager.load_data()
        self.clients = [Client.from_dict(c) for c in data.get('clients', [])]

    def add_client(self, client_data: dict) -> Client:
        client = Client.from_dict(client_data)
        self.clients.append(client)
        self._save_clients()
        return client

    def _save_clients(self):
        data = self.file_manager.load_data()
        data['clients'] = [c.to_dict() for c in self.clients]
        self.file_manager.save_data(data)

class VeterinarianManager:
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager
        self.vets: List[Veterinarian] = []
        self.load_vets()

    def load_vets(self):
        data = self.file_manager.load_data()
        self.vets = [Veterinarian.from_dict(v) for v in data.get('vets', [])]

    def add_vet(self, vet_data: dict) -> Veterinarian:
        vet = Veterinarian.from_dict(vet_data)
        self.vets.append(vet)
        self._save_vets()
        return vet

    def _save_vets(self):
        data = self.file_manager.load_data()
        data['vets'] = [v.to_dict() for v in self.vets]
        self.file_manager.save_data(data)

# Головний клас системи
class VetClinicSystem:
    def __init__(self):
        self.file_manager = FileManager()
        self.client_manager = ClientManager(self.file_manager)
        self.vet_manager = VeterinarianManager(self.file_manager)
        self.validator = DataValidator()

    def add_client(self):
        print("\n=== Додавання нового клієнта ===")
        client_data = {
            "id": len(self.client_manager.clients),
            "surname": input("Введіть прізвище клієнта: "),
            "name": input("Введіть ім'я клієнта: "),
            "patronymic": input("Введіть по батькові клієнта: "),
            "phone": self._get_valid_phone(),
            "pets": [self._create_pet()]
        }
        self.client_manager.add_client(client_data)
        print("\nКлієнта успішно додано!")

    def add_veterinarian(self):
        print("\n=== Додавання нового ветеринара ===")
        vet_data = {
            "id": len(self.vet_manager.vets),
            "surname": input("Введіть прізвище ветеринара: "),
            "name": input("Введіть ім'я ветеринара: "),
            "patronymic": input("Введіть по батькові ветеринара: "),
            "work_hours": self._get_work_hours(),
            "appointments": []
        }
        self.vet_manager.add_vet(vet_data)
        print("\nВетеринара успішно додано!")

    def _get_valid_phone(self) -> str:
        while True:
            phone = input("Введіть номер телефону (10 цифр): ")
            if self.validator.validate_phone(phone):
                return phone
            print("Невірний формат номера!")

    def _create_pet(self) -> dict:
        return {
            "name": input("Введіть кличку тварини: "),
            "species": input("Введіть вид тварини: "),
            "breed": input("Введіть породу: "),
            "age": self._get_valid_age(),
            "id": 0,
            "medical_history": []
        }

    def _get_valid_age(self) -> int:
        while True:
            age = input("Введіть вік тварини: ")
            if self.validator.validate_age(age):
                return int(age)
            print("Невірний вік!")

    def _get_work_hours(self) -> dict:
        return {
            "start": input("Введіть час початку роботи (HH:MM): "),
            "end": input("Введіть час кінця роботи (HH:MM): ")
        }

    def run(self):
        while True:
            self._show_menu()
            choice = input("\nВиберіть опцію: ")
            
            if choice == "0":
                break
            elif choice == "1":
                self.add_client()
            elif choice == "2":
                self.add_veterinarian()
            # Додайте інші опції меню

    def _show_menu(self):
        print("\n=== Меню ===")
        print("1. Додати клієнта")
        print("2. Додати ветеринара")
        print("0. Вийти")

if __name__ == "__main__":
    system = VetClinicSystem()
    system.run()