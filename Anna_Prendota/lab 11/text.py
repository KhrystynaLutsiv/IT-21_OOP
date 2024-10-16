class MovieLibrary:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieLibrary, cls).__new__(cls)
            cls._instance.movies = []  
        return cls._instance

    def add_movie(self, title, director):
        movie = Movie(title, director)
        self.movies.append(movie)
        print(f"Added movie: {movie}")

    def list_movies(self):
        if self.movies:
            print("Movies in the library:")
            for movie in self.movies:
                print(f"- {movie}")
        else:
            print("No movies in the library.")

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def __str__(self):
        return f"{self.title} directed by {self.director}"

library1 = MovieLibrary()
library2 = MovieLibrary()

library1.add_movie("Titanic", "Christopher Nolan")
library2.add_movie("Harry Potter and the Philosopher's Stone", "James Cameron")

print(library1 is library2)  

library1.list_movies()
