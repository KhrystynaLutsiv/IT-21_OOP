## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №13
# "Поведінкові шаблони проектування"



| Виконав: студент групи ІТ-31 Куземський Тарас |
|----------------------------------------------------|
| Перевірив: Татомир А. В.            |




**Мета: познайомитися з групою поведінкових шаблонів проєктування.**


*Завдання*

1. Дати теоретичний опис поведінкової групи шаблонів.
2. Відповідно до индивідуального завдання:
- дати теоретичний опис даного шаблону;
- навести приклад коду який реалізовує даний шаблон;
- скласти його UML-діяграму.

**Опис**
Поведінкові шаблони проектування (Behavioral Design Patterns) зосереджені на механізмах взаємодії об'єктів та
на визначенні способів управління складністю комунікацій між ними. Вони допомагають організувати, спростити та
покращити зв’язки між об'єктами в системі, що робить код більш читабельним і легким для підтримки.

**Опис поведінкового шаблону "Стратегія" (Strategy Pattern)**
Дозволяє визначити сімейство алгоритмів, інкапсулювати їх та зробити їх взаємозамінними. Це дозволяє змінювати алгоритм незалежно від клієнтів, які його використовують.

**Завдання**
Необхідно реалізувати шаблон проектування "Стратегія" для системи обробки платежів. У вас є різні способи оплати (кредитна картка, PayPal, криптовалюта), і ви хочете дозволити користувачам вибирати метод оплати під час оформлення замовлення. Кожен метод оплати має свою власну реалізацію, але ви хочете, щоб клієнтський код залишався незмінним.

**Висновок**
На цій лабораторній роботі, я навчився реалізовувати поведінковий шаблон проектування Стратегія і складати UML-
діяграму для нього.

**UML-діяграма**

```mermaid
classDiagram
    class PaymentStrategy {
        +pay(amount: float)
    }

    class CreditCardPayment {
        +pay(amount: float)
    }

    class PayPalPayment {
        +pay(amount: float)
    }

    class CryptoPayment {
        +pay(amount: float)
    }

    class ShoppingCart {
        -items: list
        -payment_strategy: PaymentStrategy
        +add_item(item: dict)
        +set_payment_strategy(payment_strategy: PaymentStrategy)
        +checkout() : str
    }

    PaymentStrategy <|-- CreditCardPayment
    PaymentStrategy <|-- PayPalPayment
    PaymentStrategy <|-- CryptoPayment
    ShoppingCart o-- PaymentStrategy
