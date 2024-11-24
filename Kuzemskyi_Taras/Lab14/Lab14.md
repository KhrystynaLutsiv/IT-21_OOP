## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №14
# "Принципи проєктування програмного забезпечення"



| Виконав: студент групи ІТ-31 Куземський Тарас     |
|----------------------------------------------|
| Перевірив: Татомир А. В.     |



**Мета: познайомитися з найбільш поширеними сучасними
принципами проєктування програмного забезпечення.**

*Завдання*

1. Дати загальний опис принципів проєктування.
2. Дати детальний опис одного із принципів SOLID з наведення прикладу
коду.

**Опис**

Принцип Open/Closed Principle (OCP) є одним із п’яти принципів SOLID, що визначають якісне програмування в об'єктно-орієнтованих мовах.

Опис принципу OCP:
Принцип Open/Closed Principle (OCP) стверджує, що програмні модулі повинні бути відкритими для розширення, але закритими для модифікації. Це означає, що ви повинні мати можливість додавати нову функціональність до існуючих класів, не змінюючи їхнього коду. Це дозволяє зберігати стабільність системи, мінімізуючи кількість помилок при додаванні нових функціональних можливостей.

Щоб дотримуватись OCP, часто використовують абстракції, такі як інтерфейси або абстрактні класи, щоб змінювати поведінку системи через розширення існуючих класів.

Клас AreaCalculator не потребує змін, коли додаються нові типи фігур, оскільки кожен новий тип фігури реалізує метод calculate_area згідно з інтерфейсом Shape. Таким чином, ми можемо додавати нові класи фігур без модифікації вже існуючих класів і не порушуємо принцип OCP.


 *UML-Діаграма*

 ```mermaid
 from graphviz import Digraph

# Create a UML class diagram using Graphviz
uml = Digraph("UML_Diagram", format="png")
uml.attr(rankdir="BT")

# Define styles for clarity
uml.attr('node', shape='record', fontname='Helvetica')

# Classes
uml.node("Shape", '''{Shape|+ calculate_area() : float}''', style="dashed")
uml.node("Circle", '''{Circle|+ radius : float\\l+ calculate_area() : float}''')
uml.node("Square", '''{Square|+ side : float\\l+ calculate_area() : float}''')
uml.node("AreaCalculator", '''{AreaCalculator|+ calculate_area(shape: Shape) : float}''')

# Relationships
uml.edge("Shape", "Circle", arrowhead="onormal", label="inherits")
uml.edge("Shape", "Square", arrowhead="onormal", label="inherits")
uml.edge("AreaCalculator", "Shape", arrowhead="open", label="uses")

# Render and display the diagram
uml_filepath = "/mnt/data/UML_Diagram"
uml.render(uml_filepath, cleanup=True)
uml_filepath + ".png"


   ```

## Висновки
Я навчився використовувати принципи SOLID, а саме принцип OCP.
Принцип OCP допомагає створювати більш гнучкі та масштабовані програми, де додавання нової функціональності не призводить до змін у вже існуючому коді. Це знижує ризик помилок і спрощує підтримку коду. 