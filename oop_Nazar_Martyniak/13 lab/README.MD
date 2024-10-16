## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №13
# "Поведінкові шаблони проєктування"

| Виконав: студент групи ІТ-31 Мартиняк Назар     |
|----------------------------------------------|
| Перевірив: Андрій Володимирович Татомир               |

## Мета: познайомитися з групою поведінкових шаблонів проєктування.

## Хід роботи
1. Дати теоретичний опис поведінкової групи шаблонів
Поведінкові шаблони проектування — це група шаблонів, що спрямовані на ефективну організацію взаємодії між об'єктами, а також на управління їх поведінкою. Основна мета цих шаблонів — полегшити комунікацію між об'єктами і зробити систему більш гнучкою та масштабованою, коли справа стосується алгоритмів і контролю потоку даних.
Основні характеристики поведінкових шаблонів:
Організація взаємодії — поведінкові шаблони забезпечують ефективний спосіб взаємодії між об'єктами. Вони дозволяють уникати жорсткої прив'язки між класами та забезпечують можливість додавання нових об'єктів або функцій без зміни існуючої логіки.
2. Відповідно до индивідуального завдання:
- дати теоретичний опис даного шаблону;
Шаблон Visitor — це патерн проектування, який дозволяє додавати нову поведінку до об'єктів без зміни їхньої структури. Це досягається шляхом введення додаткового об'єкта — відвідувача (Visitor), який "відвідує" елементи об'єктної структури і виконує над ними операції.
- навести приклад коду який реалізовує даний шаблон;
Приклад коду знаходиться за цим [посиланням](1.2.py)
- скласти його UML-діяграму.
```mermaid
from graphviz import Digraph

dot = Digraph('UML Diagram', filename='visitor_pattern', format='png')

# Visitor interface
dot.node('Visitor', '''<<interface>> Visitor
+ visit_concrete_component_a(element: ConcreteComponentA) -> None
+ visit_concrete_component_b(element: ConcreteComponentB) -> None''')

# Component interface
dot.node('Component', '''<<interface>> Component
+ accept(visitor: Visitor) -> None''')

# ConcreteVisitor1
dot.node('ConcreteVisitor1', '''ConcreteVisitor1
+ visit_concrete_component_a(element: ConcreteComponentA) -> None
+ visit_concrete_component_b(element: ConcreteComponentB) -> None''')

# ConcreteVisitor2
dot.node('ConcreteVisitor2', '''ConcreteVisitor2
+ visit_concrete_component_a(element: ConcreteComponentA) -> None
+ visit_concrete_component_b(element: ConcreteComponentB) -> None''')

# ConcreteComponentA
dot.node('ConcreteComponentA', '''ConcreteComponentA
+ accept(visitor: Visitor) -> None
+ exclusive_method_of_concrete_component_a() -> str''')

# ConcreteComponentB
dot.node('ConcreteComponentB', '''ConcreteComponentB
+ accept(visitor: Visitor) -> None
+ special_method_of_concrete_component_b() -> str''')

# Edges
dot.edge('Visitor', 'ConcreteVisitor1', arrowhead='empty', label='<<implements>>')
dot.edge('Visitor', 'ConcreteVisitor2', arrowhead='empty', label='<<implements>>')
dot.edge('Component', 'ConcreteComponentA', arrowhead='empty', label='<<implements>>')
dot.edge('Component', 'ConcreteComponentB', arrowhead='empty', label='<<implements>>')
dot.edge('ConcreteComponentA', 'Visitor', label='accept()')
dot.edge('ConcreteComponentB', 'Visitor', label='accept()')

# Render the UML diagram and open it
dot.render(view=True)
```


## Висновок:
На цій лабораторній роботі я засвоїв застосування принципу групою твірних шаблонів в
об’єктно-орієнтованому програмуванні.