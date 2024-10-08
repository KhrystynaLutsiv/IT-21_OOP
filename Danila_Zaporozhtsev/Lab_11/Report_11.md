## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій


### Звіт про виконання лабораторної роботи №11

# "Твірні шаблони проєктування"


|Виконав: студент групи ІТ-31 Запорожцев Данило|
|----------------------------------------------|
|Перевірив: Татомир Андрій Володимирович|

**Мета: освоїти роботу з твірними шаблонами проєктування та навчитися їх використовувати.**

### **Поняття шаблонів. Твірні шаблони**

Шаблони - це спосіб вирішення певної проблеми, використовуючи вже готові рішення.
Шаблони діляться на три групи: твірні, структурні, поведінкові.
Твірні шаблони використовують для зручного та безпечного створення нових об'єктів.

### **Фабричний метод**

Щоб продемонструвати роботу твірних шаблонів, я буду використовувати фабричний метод. Він дозволяє створювати об'кти до певного класу або , у моєму випадку, підкласу за певною властивісттю.

Для реалізації цього методу створимо бібліотеку фільмів, які будуть відсортовані за жанрами, їх властивістю, по підкласам.
Створюю загальний клас Movie, де буде прописані функції `__init__` та `description`, які будуть виконувати підкласи.
``` py
class Movie:
    def __init__(self, title):
        self.title = title

    def description(self):
        pass
```
Використав наслідування для того, щоб підкласи виконували базову функцію `__init__` для створення об'єктів, та `description` для виведення опису жанру фільму. Приклад:
``` py
class ActionMovie(Movie):
    def description(self):
        return f"{self.title} - це бойовик: екшн-сцени і махачі."
```
Далі створюю клас `Factory`, де створений об'єкт через цей клас має жанр та назву, і, дивлячись на жанр, клас додає об'єкт до певного класу.
``` py
class Factory:
    def create_movie(self, genre, title):
        if genre == "action":
            return ActionMovie(title)
        elif genre == "comedy":
            return ComedyMovie(title)
        elif genre == "superhero":
            return SuperheroMovie(title)
        else:
            print("Невідомий жанр фільму")
```
Далі нведена UML діаграми зв'язків класів:

![UML діаграма](https://raw.githubusercontent.com/KhrystynaLutsiv/IT-21_OOP/refs/heads/master/Danila_Zaporozhtsev/Lab_11/UML_11.png)

Посилання на повний код:

[Лабораторна робота 11](./Creational_pattern.py)

## Висновки. 

 Під час виконання лабораторної роботи я ознайомився з твірними шаблонами, використовуючи фабричний метод, як приклад, я створив програму, яка дозволяє додавати об'єкти до підкласів безпосередньо, тобто не писати постійно SuperheroMovie додати такий об'єкт. Це дозволить спростити роботу коду.
