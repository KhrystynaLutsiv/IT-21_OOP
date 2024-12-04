## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №15
# "Рефакторинг програмного забезпечення"



| **Виконав: студент групи ІТ-31 Юрій Мавко**  |
|----------------------------------------------|
| **Перевірив: Татомир А. В.**                 |




**Мета: познайомитися з основними принципами та 
найбільш пошириними техніками рефакторингу програмного
забезпечення**


Завдання

1. Дати загальний опис принципів рефакторингу.
2. Ознайомитися із основними техніками рефакторингу.
3. Познайомитися із поняттям "запахів коду"

**Опис принципів рефакторингу**

Рефакторинг — це процес внесення змін у код програми з метою 
поліпшення його структури, читабельності та підтримуваності 
без зміни зовнішньої поведінки програми.Його основна мета 
полягає в тому, щоб зробити код більш зрозумілим для 
розробників, спростити подальший розвиток системи та 
зменшити ймовірність появи помилок.

Принципи рефакторингу спрямовані на те, щоб зробити код 
легшим для розуміння, змін і розширення. Вони включають 
кілька важливих аспектів:

Мінімізація дублювання: Видалення повторюваних фрагментів 
коду шляхом створення універсальних функцій, класів або методів. 

Розділення відповідальності: Логіка програми повинна бути 
структурована так, щоб кожен компонент або модуль відповідав 
лише за одну чітко визначену функцію. 

Чіткий поділ логіки на модулі: Код має бути організований у 
вигляді невеликих, незалежних модулів, які виконують окремі 
завдання.

Спрощення складних конструкцій: Заміна довгих і заплутаних 
фрагментів коду на більш прості й зрозумілі. 

Оптимізація роботи з даними: Удосконалення способів обробки даних, 
наприклад, через використання більш ефективних алгоритмів, правильний 
вибір структур даних або усунення зайвих операцій.

Ясна документація: Коментарі й назви змінних, функцій та класів 
повинні бути зрозумілими й описувати їх призначення. 

Дотримання стандартів програмування: Використання загальноприйнятих 
стилів і практик написання коду, які забезпечують його читабельність 
і однорідність.

**Техніки рефакторингу**

Перейменування: Зміна назв змінних, методів, класів тощо, щоб 
зробити їх зрозумілими та відповідними їхній функції.

Виділення методу: Винесення частини коду з довгого методу в 
окремий метод із чіткою назвою.

Інлайнування методу: Повернення коду з методу в місце його виклику, 
якщо метод надто простий або використовується тільки один раз.

Виділення класу: Створення нового класу для частини функціональності, 
якщо один клас виконує занадто багато завдань.

Об’єднання класів: Об’єднання двох класів, якщо їхня функціональність перетинається.

Перенесення методу: Переміщення методу до того класу, де його логічне місце.

Заміна умовного оператора поліморфізмом: Використання наслідування або 
інтерфейсів замість складних умов.

Декомпозиція умов: Розбиття складного умовного виразу на кілька простіших, 
щоб поліпшити читабельність.

Видалення дублювання коду: Знаходження однакових фрагментів коду та винесення 
їх у спільний метод чи клас.

Спрощення ланцюжків викликів: Зменшення кількості посередників у викликах, 
щоб зробити залежності більш очевидними.

Інкапсуляція змінної: Заміна прямого доступу до змінної на геттери й 
сеттери для кращого контролю.

Розбиття великого класу/методу: Поділ класів або методів на менші, 
кожен із яких виконує одну конкретну функцію.

**"Запахи коду"**

Запахи коду — це ознаки того, що код має проблеми в дизайні або структурі, 
які можуть ускладнити його розуміння, підтримку чи розвиток. Це не завжди 
помилки, але такі елементи свідчать про необхідність рефакторингу.

Основні типи запахів коду:

Дублювання коду: Однакові або схожі фрагменти коду в різних місцях.

Довгі методи: Метод містить надто багато коду, важко зрозуміти його функцію.

Великі класи: Клас відповідає за кілька завдань одночасно, порушуючи принцип єдиної відповідальності.

Довгий список параметрів: Методи або конструктори мають надто багато аргументів.

Посередники: Клас лише передає виклики іншим класам, не додаючи нічого корисного.

Нерелевантні коментарі: Коментарі пояснюють очевидне або виправдовують поганий код замість його виправлення.

Залежність від глобальних змінних: Використання глобальних змінних замість локальних або параметрів.

Магічні числа/рядки: Використання чисел чи рядків напряму в коді замість зрозумілих констант.

Непотрібна складність: Застосування надмірних патернів чи складних структур без потреби.

Непотрібні об'єкти: Створення об'єктів або класів, які не додають цінності.

**[Код у якому варто провести рефакторинг](./refactoring.py)**

**[Код у якому проведено рефакторинг](./improved_code.py)**


## Висновки. 
Під час виконання лабораторної роботи я ознайомився з основними принципами та техніками рефакторингу 
програмного забезпечення. Зокрема, я вивчив, як застосування принципів мінімізації дублювання, 
розділення відповідальності, спрощення складних конструкцій та дотримання стандартів програмування 
допомагає покращити структуру коду, його читабельність та підтримуваність.

Я також детально розглянув найпоширеніші техніки рефакторингу, такі як перейменування, виділення 
методу, інкапсуляція змінних, видалення дублювання коду та спрощення умов. Окрім цього, я навчився 
ідентифікувати "запахи коду", які вказують на проблеми у структурі програми, наприклад дублювання 
коду, довгі методи, великі класи та магічні числа.

Під час проведення рефакторингу я переніс логіку роботи з файлами у інші класи, які тільки працюють з
файлами; логіку з input/print я також виніс у новий клас, який працює тільки з введенням і виведенням;
розділив метод output_event на декілька спеціалізованих методів, задля зменшення кількості коду і легкості
його читання, та зміни.

Завдяки цим знанням я зрозумів важливість рефакторингу для підвищення якості коду, полегшення 
його розширення та зменшення ймовірності виникнення помилок у майбутньому.