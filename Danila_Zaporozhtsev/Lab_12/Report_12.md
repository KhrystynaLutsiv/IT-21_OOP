## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій


### Звіт про виконання лабораторної роботи №12

# "Структурні шаблони проєктування"


|Виконав: студент групи ІТ-31 Запорожцев Данило|
|----------------------------------------------|
|Перевірив: Татомир Андрій Володимирович|

**Мета: ознайомитись з структурними шаблонами проєктування.**

### **Структурні шаблони**

Структурні шаблони застосовуються для створення зручної ієрархії класів.
Щоб продемонструвати їх роботу я буду використовувати компанувальний метод.

### **Компануваний метод**

Він дозволяє створювати дерева об'єктів, де кожен об'єкт може бути як простим, так і складеним з інших об'єктів. Паттерн допомагає працювати з окремими об'єктами та їх групами однаковим чином.

Далі я буду використовувати такі поняття: групи об'єктів - гілки, об'єкти - листки.

Створюю загальний клас, де буде прописана функція `play` для виведення тексту, типу програвання музики або плейлиста, яку будуть використовувати підкласи.
``` py
class Music:
    def play(self):
        pass
``` 
Від нього підкласи будуть успадковувати гілки та листки.

Перший підклас ініціює листки, пісні, які можуть програватись.
``` py
class Song(Music):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def play(self):
        print(f"Пісня: {self.name}, Виконавець: {self.artist}")
``` 
Другий підклас ініціює гілки і додає до них листки, в коді це приведено створенням плейлистів та додавання до них пісень.
``` py
class Playlist(Music):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: Music):
        self.children.append(component)

    def play(self):
        print(f"\nГрає плейлист: {self.name}")
        for child in self.children:
            child.play()
```
Далі йде користувацький код, де створюється дерево. Плейліст, який має в собі усі плейлісти, які, у свою чергу, мають пісні.
``` py
main_playlist = Playlist("Усі пісні")
playlist1 = Playlist("Улюблене")
playlist2 = Playlist("Для ігор")

main_playlist.add(playlist1)
main_playlist.add(playlist2)

song1 = Song("Room", "IVOXYGEN")
...

playlist1.add(song1)
...
```
В результаті виведення отримаємо виведення головного плейлиста, виведуться усі прив'язані плейлисти та пісні, які знаходяться в них.
У моєму випадку ще є функція пошуку пісні за його автором в любому з плейлистів. Вона знаходиться у класі плейлистів.
``` py
def show_by_artist(self, artist):
        for child in self.children:
            if isinstance(child, Song) and child.artist == artist:
                child.play()
            elif isinstance(child, Playlist):
                child.show_by_artist(artist)
``` 
Перебираючи плейлист, де `isinstance` спочатку перевіряє чи є об'єкт екземпляром класу, та чи заданий автор являється автором даної пісні, а потім виводиться ця пісня, і цикл повторюється доти, доки `isinstance` не покаже `False`

Далі нведена UML діаграми зв'язків класів:

![UML діаграма](https://raw.githubusercontent.com/KhrystynaLutsiv/IT-21_OOP/refs/heads/master/Danila_Zaporozhtsev/Lab_12/UML_12.png)

Та посилання на повний код:

[Практична робота 12](./Composite_pattern.py)

## Висновки. 

 Під час виконання лабораторної роботи дослідив, на прикладі композитного шаблону, роботу структурних шаблонів. Створивши програму, яка створює дерево класів, де виконується взаємодія з об'єктами, а саме додавання та пошук за властивісттю. Було цікаво дізнатись, що одна команда `isinstance` дає змогу суттєво скоротити код та запобігти повторенню строчок.