## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №14
# "Структурні шаблони проектування"



 Виконав: Роман Тупісь
|----------------------------------------------------|
 |**Перевірив: Татомир А. В.**      




**Мета: познайомитися з найбільш поширеними сучасними принципами проєктування програмного забезпечення.**


**Завдання:**

1. Дати загальний опис принципів проєктування.
2. Дати детальний опис одного із принципів SOLID з наведенням прикладу коду.


## Принципи SOLID

**SOLID –** це набір із п'яти ключових принципів об'єктно-орієнтованого програмування, які допомагають створювати гнучкий, масштабований і простий у підтримці код.

**S - Single Responsibility Principle (Принцип єдиної відповідальності):** Клас має виконувати лише одну задачу і мати лише одну причину для змін.


**O - Open/Closed Principle (Принцип відкритості/закритості):** Класи, модулі чи функції повинні бути відкритими для розширення, але закритими для змін.


**L - Liskov Substitution Principle (Принцип підстановки Лісков):** Об’єкти підкласу повинні без проблем замінювати об’єкти батьківського класу, не порушуючи логіку програми.


**I - Interface Segregation Principle (Принцип розділення інтерфейсу):**  Краще мати декілька вузьких інтерфейсів, ніж один універсальний, щоб уникнути зайвої залежності класів від невикористовуваних методів.


**D - Dependency Inversion Principle (Принцип інверсії залежностей):** Система повинна залежати від абстракцій, а не від конкретних реалізацій.


<hr>

## SRP (Single Responsibility Principle)


**Суть принципу:**
Кожен клас або модуль у програмі повинен виконувати лише одну конкретну задачу і мати лише одну причину для змін.


**Навіщо це потрібно:**

1. Зменшується складність і полегшується підтримка коду.
2. Зміни в одній частині програми не впливають на інші.
3. Клас стає легким для тестування та повторного використання.

Приклад коду наведено за [посиланням](./code.py).

### **Переваги:**

1. Кожен клас відповідає лише за свою частину роботи.
2. Легко тестувати кожен клас окремо.
3. Зміни в одному класі не впливають на інші.
4. Цей підхід сприяє створенню структурованого й зрозумілого коду.

<hr>

### Висновок:

На цьому уроці я познайомився з основними сучасними принципами проєктування програмного забезпечення, такими як KISS, DRY, YAGNI та TDA, а також глибше вивчив набір принципів SOLID, які є основою для створення якісного та масштабованого коду.

Особливо корисним було ознайомлення з Принципом єдиної відповідальності (SRP). Я зрозумів, що дотримання цього принципу допомагає розробляти модульний, легкий у підтримці та тестуванні код.

Я навчився:

Розрізняти загальні принципи проєктування та їхні переваги для написання зрозумілого коду.
Виявляти порушення SRP у коді й правильно рефакторити класи.
Будувати системи, де кожен компонент виконує лише одну задачу, що робить їх більш надійними та масштабованими.
Ці знання допоможуть мені створювати більш професійний та ефективний код у майбутніх проєктах.