## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №13
# "Принципи проєктування програмного забезпечення"



| Виконала: студентка групи ІТ-31 Прендота Анна |
|----------------------------------------------|
| **Перевірив: Татомир А.В.**               |




**Мета: познайомитися з найбільш поширеними сучасними принципами проєктування програмного забезпечення**


Хід роботи

1. Дати теоретичний опис принципам проєктування програмного забезпечення.
2. Відповідно до індивідуального завдання:
- дати теоретичний опис даного шаблону;
- навести приклад коду який реалізовує даний шаблон;
- скласти його UML-діяграму.

**Опис шаблону**

Принципи проєктування програмного забезпечення спрямовані на створення зрозумілого, гнучкого та підтримуваного коду. Дотримання цих принципів дозволяє уникнути поширених проблем під час розробки, таких як дублювання коду, складність модифікації та низька тестованість. Нижче наведені основні принципи, що застосовуються в проєктуванні програмного забезпечення.

SOLID: Набір із п’яти ключових принципів об'єктно-орієнтованого програмування, які допомагають зробити структуру програми більш гнучкою та зручною для модифікацій.

S: Single Responsibility Principle (SRP) – Принцип єдиного обов’язку.
O: Open/Closed Principle (OCP) – Принцип відкритості/закритості.
L: Liskov Substitution Principle (LSP) – Принцип підстановки Лісков.
I: Interface Segregation Principle (ISP) – Принцип розділення інтерфейсів.
D: Dependency Inversion Principle (DIP) – Принцип інверсії залежностей.
KISS (Keep It Simple, Stupid): Закликає до написання простого коду. Занадто складні рішення часто стають джерелом помилок і важкі в підтримці.

DRY (Don't Repeat Yourself): Принцип забороняє дублювання коду. Якщо певний функціонал повторюється, його слід винести в окремий метод або клас.
YAGNI (You Aren't Gonna Need It): Не слід додавати функціонал, який не потрібен прямо зараз. Це запобігає зайвій складності.
Separation of Concerns (SoC): Розподіл функціональності програми на окремі компоненти або модулі, кожен з яких виконує лише одну задачу, знижуючи взаємозалежності.

Дотримання цих принципів дозволяє створювати гнучку, зрозумілу та підтримувану архітектуру програмного забезпечення.

**Опис коду**

Цей код демонструє використання принципів SOLID для проєктування системи, яка дозволяє обробляти замовлення з різними способами оплати. Ось детальний опис кожного компоненту та його ролі відповідно до принципів SOLID:

Огляд класів та SOLID принципів
Single Responsibility Principle (SRP)

Клас Order відповідає тільки за зберігання інформації про замовлення, як-от order_id та amount. Він не включає в себе логіку обробки платежів чи інших операцій, що забезпечує виконання SRP — кожен клас має лише одну відповідальність.
Open/Closed Principle (OCP)

Абстрактний клас PaymentProcessor реалізований як базовий клас для всіх платіжних процесорів, які можуть додаватися в майбутньому. Це дозволяє розширювати систему новими типами платежів (наприклад, Google Pay, банківський переказ тощо) без модифікації існуючого коду, оскільки всі нові процесори будуть успадковувати PaymentProcessor і реалізовувати метод process_payment. Завдяки цьому реалізується принцип OCP — класи відкриті для розширення, але закриті для модифікації.
Liskov Substitution Principle (LSP)

Класи CreditCardPaymentProcessor та PayPalPaymentProcessor є підкласами PaymentProcessor і реалізують метод process_payment, який використовується для обробки платежів для певного замовлення. Це гарантує, що будь-який об'єкт, який реалізує PaymentProcessor, можна використовувати в системі без зміни її логіки, відповідно до принципу LSP — підкласи можуть замінювати батьківський клас без порушення поведінки.
Interface Segregation Principle (ISP)

Клас PaymentProcessor містить лише один метод process_payment, необхідний для обробки платежів. Завдяки цьому різні платіжні процесори не змушені реалізовувати зайві методи, які вони не використовують, і кожен клас реалізує лише потрібний функціонал. Це відповідає принципу ISP — уникаємо нав’язування зайвих методів.
Dependency Inversion Principle (DIP)

Клас OrderProcessor залежить від абстракції PaymentProcessor, а не від конкретних реалізацій, як-от CreditCardPaymentProcessor або PayPalPaymentProcessor. Це означає, що ми можемо легко передати будь-який платіжний процесор, який реалізує PaymentProcessor, як залежність у OrderProcessor, роблячи систему більш гнучкою і легкою до розширення. Так забезпечується дотримання DIP — залежність від абстракцій, а не від конкретних реалізацій.
Використання коду
Створення замовлення

Об’єкт order класу Order з ID 1 та сумою 100 представляє замовлення, яке потрібно обробити.
Створення платіжних процесорів

Об’єкти credit_card_processor і paypal_processor є екземплярами класів CreditCardPaymentProcessor та PayPalPaymentProcessor, відповідно, і реалізують метод обробки платежів для кожного конкретного способу.
Обробка замовлення

OrderProcessor отримує певний платіжний процесор (через конструктор), і метод process_order обробляє замовлення з використанням заданого платіжного процесора.
У прикладі замовлення обробляється як через кредитну картку (order_processor_credit.process_order(order)), так і через PayPal (order_processor_paypal.process_order(order)).
Переваги цього підходу
Цей підхід дозволяє:

Легко додавати нові способи оплати без змін у наявних класах.
Забезпечити заміну платіжних процесорів без зміни основної логіки.
Дотримуватися принципів модульності, гнучкості та тестованості.
Така структура робить систему стійкою до змін, модульною та легко підтримуваною, що є основними цілями принципів SOLID.

[Практична робота №14](https://github.com/KhrystynaLutsiv/IT-21_OOP/blob/master/Anna_Prendota/lab%2014/text.py)

![UML-діаграма](https://github.com/KhrystynaLutsiv/IT-21_OOP/blob/master/Anna_Prendota/lab%2014/lab%2014.png) 

UML-діаграма

## Висновки. 

На цій лабораторній роботі я ознайомилася з принципами SOLID є основою для створення якісного, гнучкого та масштабованого програмного забезпечення. Дотримання цих принципів допомагає розробникам створювати код, який легко розширювати, тестувати та підтримувати. Кожен принцип має свою роль: SRP запобігає надмірній відповідальності класів, OCP дозволяє розширювати функціональність без зміни існуючого коду, LSP забезпечує коректність підкласів, ISP усуває зайві залежності, а DIP знижує залежність від конкретних реалізацій. Разом ці принципи формують фундамент для ефективного та надійного програмування.