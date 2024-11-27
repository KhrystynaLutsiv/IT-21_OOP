```plantuml
@startuml
skinparam style strictuml

package "Інтерфейс додатку" {
    usecase "Реєстрація користувача" as UC_Register
    usecase "Вхід за username/password" as UC_Login
    usecase "Зміна особистої інформації\n(включно з паролем)" as UC_UpdateInfo
    usecase "Створення заявки на оренду" as UC_CreateRequest
    usecase "Додавання/оновлення інформації\nпро авто" as UC_ManageCars
    usecase "Пошук автомобілів за параметрами" as UC_SearchCars
    usecase "Перегляд списку заявок" as UC_ViewRequests
    usecase "Перегляд історії орендованих автомобілів" as UC_ViewHistory
}

actor "Користувач" as User
actor "Адміністратор" as Admin

User --> UC_Register
User --> UC_Login
User --> UC_UpdateInfo
User --> UC_CreateRequest
User --> UC_SearchCars
User --> UC_ViewRequests
User --> UC_ViewHistory

Admin --> UC_Login
Admin --> UC_ManageCars
Admin --> UC_ViewRequests
@enduml
