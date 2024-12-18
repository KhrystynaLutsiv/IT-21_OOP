## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №12
# "Структурні шаблони проєктування"



| Виконала: студентка групи ІТ-31 Прендота Анна |
|----------------------------------------------|
| **Перевірив: Татомир А.В.**               |




**Мета: познайомитися з групою структурних шаблонів проектування.**


Хід роботи

1. Дати теоретичний опис структурної групи шаблонів.
2. Відповідно до индивідуального завдання:
- дати теоретичний опис даного шаблону;
- навести приклад коду який реалізовує даний шаблон;
- скласти його UML-діяграму.

**Опис шаблону** 

Шаблон "Фасад" (Facade) є структурним шаблоном проектування, який забезпечує спрощений інтерфейс для складної системи, приховуючи її внутрішню реалізацію. Це дозволяє користувачам або клієнтам взаємодіяти з системою через єдиний, зручний інтерфейс, що значно полегшує використання.

Основні характеристики шаблону "Фасад":
Спростити взаємодію: Фасад забезпечує простий інтерфейс для складних підсистем. Це дозволяє користувачам зосередитися на основних функціях, не вникаючи в деталі реалізації.

Зменшити залежності: Завдяки фасаду, клієнти мають справу лише з ним, а не з численними класами та інтерфейсами підсистеми. Це зменшує зв'язність між компонентами, що полегшує підтримку та зміни в системі.

Захист від змін: Зміни в підсистемі не впливають на код клієнтів, якщо інтерфейс фасаду залишається незмінним. Це підвищує стійкість системи до змін.

Організація коду: Фасад може допомогти структурувати код, об'єднуючи пов'язані функції під одним інтерфейсом. Це полегшує читання і розуміння коду.

Використовувати цей шаблон потрібно тоді, коли потрібно спростити взаємодію з складною системою, що складається з багатьох компонентів.
Коли потрібно зменшити залежності між системами або модулями.
Коли система може змінюватись, і ви хочете захистити клієнтський код від цих змін.

**Опис коду**

Цей код реалізує систему управління бібліотекою фільмів, використовуючи шаблон "Фасад". Він складається з кількох класів, які обробляють різні аспекти управління фільмами, такі як зберігання, пошук та рекомендації. Далі наведено детальний опис кожної частини коду.

1. Клас MovieDatabase

Конструктор __init__:
Ініціалізує порожній список movies, в якому зберігатимуться фільми.

Метод add_movie:
Приймає заголовок фільму (title) та ім'я режисера (director).
Додає фільм до списку movies у вигляді словника з ключами "title" і "director".
Виводить повідомлення про додавання фільму.

Метод get_movies:
Повертає список усіх фільмів у базі даних.

2. Клас MovieSearch

Статичний метод search_by_title:
Приймає список фільмів та заголовок для пошуку.
Повертає список фільмів, у заголовках яких міститься заданий рядок (не залежить від регістру).

3. Клас RecommendationSystem

Статичний метод recommend_by_director:
Приймає список фільмів та ім'я режисера.
Повертає список фільмів, знятих цим режисером.

4. Клас MovieLibraryFacade
Конструктор __init__:
Ініціалізує три внутрішні компоненти: MovieDatabase, MovieSearch та RecommendationSystem, що відповідають за зберігання, пошук та рекомендації.

Метод add_movie:
Викликає метод add_movie у класі MovieDatabase, щоб додати фільм до бази даних.

Метод find_movie:
Отримує список фільмів із MovieDatabase, викликає search_by_title з класу MovieSearch для пошуку фільму за заголовком.
Виводить результати пошуку або повідомлення про відсутність фільмів.

Метод recommend_movies:
Отримує список фільмів із MovieDatabase, викликає recommend_by_director з класу RecommendationSystem для отримання рекомендацій.
Виводить знайдені рекомендації або повідомлення про їх відсутність.


[Практична робота №12](https://github.com/KhrystynaLutsiv/IT-21_OOP/blob/master/Anna_Prendota/lab%2012/text.py)

![UML-діаграма](lab12.png) 

UML-діаграма



## Висновки. 

На даній лабораторній роботі я ознайомилася зі структурними шаблонами проєктування та навчилася використовувати їх на практиці. Це дозволило зрозуміти, як організовувати взаємодію між класами та об'єктами, забезпечуючи більш ефективну структуру коду,  і спрощену підтримку в програмних проєктах. 
