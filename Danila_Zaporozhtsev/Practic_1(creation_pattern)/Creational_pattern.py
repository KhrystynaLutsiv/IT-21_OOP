class Movie:
    def __init__(self, title):
        self.title = title

    def description(self):
        pass


class ActionMovie(Movie):
    def description(self):
        return f"{self.title} - це бойовик: екшн-сцени і махачі."


class ComedyMovie(Movie):
    def description(self):
        return f"{self.title} - це комедія: гумор та смішні ситуації."


class SuperheroMovie(Movie):
    def description(self):
        return f"{self.title} - це супергеройський фільм: люди з суперсилами."


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


factory = Factory()

movie_1 = factory.create_movie("superhero", "Залізна людина")
movie_2 = factory.create_movie("action", "Джон Уік")
movie_3 = factory.create_movie("superhero", "Людина павук 2")
movie_4 = factory.create_movie("comedy", "Маска")
movie_5 = factory.create_movie("comedy", "Один вдома")
movie_6 = factory.create_movie("superhero", "Тор 3: Рагнарк")

print(movie_1.description())
print(movie_2.description())
print(movie_3.description())
print(movie_4.description())
print(movie_5.description())
print(movie_6.description())
