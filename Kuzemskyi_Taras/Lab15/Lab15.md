## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №15
# "Рефакторинг програмного забезпечення"



| Виконав: студент групи ІТ-31 Куземський Тарас     |
|----------------------------------------------|
| Перевірив: Татомир А. В.     |



**Мета: познайомитися з основними принципами та найбільш
поширеними техніками рефакторингу програмного забезпечення.**

*Завдання*

1. Дати загальний опис принципів рефакторингу.
2. Ознайомитися із основними техніками рефакторингу.
3. Познайомитися із поняттям “запахів коду”

**Опис**

1. Загальний опис принципів рефакторингу

Рефакторинг — це процес покращення внутрішньої структури коду без зміни його зовнішньої поведінки. Основна мета — зробити код більш читабельним, простішим у підтримці та адаптації до майбутніх змін.

Основні принципи рефакторингу:

Мінімізація дублікатів: Дублювання коду створює складнощі при внесенні змін. Мета — винести повторювані частини в окремі методи або класи.

Прозорість коду: Код має бути зрозумілим, навіть якщо ви повернетеся до нього через кілька місяців.

Мінімізація складності: Занадто складний код важко підтримувати. Спрощення алгоритмів та структури покращує розуміння.

Підтримка тестів: Перед початком рефакторингу потрібно мати набір автоматизованих тестів, щоб переконатися, що поведінка коду не змінюється після змін.

2. Основні техніки рефакторингу

Найпоширеніші техніки:

Виділення методу (Extract Method)
Винесення частини коду в окремий метод із самодокументуючою назвою.

Інлайнування (Inline Method)
Якщо метод занадто простий, його можна вбудувати в основний код.

Виділення класу (Extract Class)
Якщо один клас виконує надто багато завдань, його варто розділити.

Замінити умови поліморфізмом (Replace Conditional with Polymorphism)
Якщо у коді є велика кількість умов, їх можна замінити поліморфізмом.

Декомпозиція великих класів або методів
Розділення великого методу на кілька дрібних, кожен із яких відповідає за одну конкретну задачу.

3. Поняття "запахи коду"

"Запахи коду" (Code Smells) — це ознаки проблем у коді, які свідчать про необхідність рефакторингу. Це не помилки, а скоріше симптоми потенційних проблем.

Основні приклади запахів коду:
Дублювання коду (Duplicated Code)
Повторення одного й того ж фрагмента в кількох місцях.

Занадто великий клас (Large Class)
Клас із багатьма методами або властивостями, що порушує принцип SRP.

Занадто довгі методи (Long Methods)
Методи, які виконують занадто багато завдань.

Довгі списки параметрів (Long Parameter List)
Методи, які приймають занадто багато аргументів, що ускладнює їх використання.

Залежність від конкретного класу (Inappropriate Intimacy)
Класи, які знають надто багато про реалізацію інших класів.

Складні умови (Complex Conditional Logic)
Велика кількість вкладених умов або перевірок, що ускладнюють розуміння коду.

## Висновки

Проблеми у коді:
Дублювання коду в методі print_invoice (розрахунок ціни кожного предмета повторюється).
Складні умови в методі calculate_total (знижки для клієнтів).
Занадто великий клас: Order виконує і логіку обчислення, і створення рахунку.

Що покращено:
Складні умови з calculate_total винесено у стратегії знижок (патерн Strategy). Це спрощує метод і дозволяє додавати нові типи знижок без зміни існуючого коду.
Розділення обов’язків:
Клас Order відповідає за логіку обчислення замовлення.
Клас InvoicePrinter відповідає за друк рахунку.
Відсутність дублювання: розрахунок вартості предмета здійснюється лише один раз.

Рефакторинг є важливою частиною розробки програмного забезпечення. Використовуючи техніки рефакторингу та виявляючи "запахи коду",  ми можемо підтримувати чистоту, модульність і читабельність свого коду. Це допомагає зменшити ризики помилок і спростити майбутні зміни.