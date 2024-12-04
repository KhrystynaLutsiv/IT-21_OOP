## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №13
# "Поведінкові шаблони проектування"



| Виконав: студент групи ІТ-31 Пасемко Василь    |
|----------------------------------------------|
| Перевірив: Татомир А.В   |




**Мета: познайомитися з групою поведінкових шаблонів проєктування.**


Завдання

1. Дати теоретичний опис поведінкової групи шаблонів.
2. Відповідно до индивідуального завдання:
- дати теоретичний опис даного шаблону;
- навести приклад коду який реалізовує даний шаблон;
- скласти його UML-діяграму.

1) Поведінкові шаблони проектування - це група 
шаблонів, які допомагають налагтувати взаємодію
між об'єктами в системі. Вони вирішують задачі 
комунікації між об'єктами, керування станом програми
та поведінкою об'єктів, щоб забезпечити гнучкість і 
зручність розгирення коду.

2)Поведінковий шаблон проектування Стан (state)
використовується для управління поведінкою об'єкта,
що змінюється в залежності від його поточного стану.
Основна ідея цього шаблону полягає в тому, щоб винести 
логіку поведінки об'єкта в окремі класи, які 
представляють різні стани і дозволити об'єкту змінювати
свій стан динамічно.

UML-ДІАГРАМА

```mermaid
@startuml
class Context {
    - state: State
    + setState(state: State): void
    + request(): void
}

interface State {
    + handle(context: Context): void
}

class ConcreteStateA implements State {
    + handle(context: Context): void
}

class ConcreteStateB implements State {
    + handle(context: Context): void
}

Context -> State
ConcreteStateA -> State
ConcreteStateB -> State
@enduml

```

Запитання для самоконтролю
1. Що таке поведінкові шаблони?
2. Які поведінкові шаблони Вам відомі?
3. Поясніть як реалізовано шаблон у Вашому прикладі.

Відповіді

1)Поведінкові шаблони проектування - це група шаблонів, 
які визначають, як об'єкти взаємодіють один з одним.

2)Поведінкові шаблони: strategy, observer, command,
state, mediator, memento, visitor, template method.

3)Інтерфейс AccountState визначає методи deposit і withdraw.
Стан ActiveState дозволяє депозит і зняття коштів, тоді як 
стан BlockedState забороняє будь-які операції.
Клас BankAccount використовує ці стани для обробки фінансових
операцій, змінюючи свій стан за потреби (активний чи 
заблокований). Це дозволяє динамічно змінювати поведінку 
рахунку без складного коду.

## Висновки. 

На даній лабораторній роботі я познайомився з групою поведінкових шаблонів проектування. 