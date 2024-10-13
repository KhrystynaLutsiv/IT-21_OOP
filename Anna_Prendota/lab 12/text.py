class MovieDatabase:
    def __init__(self):
        self.movies = []

    def add_movie(self, title: str, director: str) -> None:
        self.movies.append({"title": title, "director": director})
        print(f"Movie '{title}' by {director} added to the database.")

    def get_movies(self) -> list:
        return self.movies

class MovieSearch:
    @staticmethod
    def search_by_title(movies: list, title: str) -> list:
        results = [movie for movie in movies if title.lower() in movie["title"].lower()]
        return results

class RecommendationSystem:
    @staticmethod
    def recommend_by_director(movies: list, director: str) -> list:
        recommendations = [movie for movie in movies if director.lower() in movie["director"].lower()]
        return recommendations

class MovieLibraryFacade:
    def __init__(self):
        self._database = MovieDatabase()
        self._search = MovieSearch()
        self._recommendation = RecommendationSystem()

    def add_movie(self, title: str, director: str) -> None:
        self._database.add_movie(title, director)

    def find_movie(self, title: str) -> None:
        movies = self._database.get_movies()
        results = self._search.search_by_title(movies, title)
        if results:
            print("Search results:")
            for movie in results:
                print(f"- {movie['title']} by {movie['director']}")
        else:
            print("No movies found.")

    def recommend_movies(self, director: str) -> None:
        movies = self._database.get_movies()
        recommendations = self._recommendation.recommend_by_director(movies, director)
        if recommendations:
            print("Recommendations:")
            for movie in recommendations:
                print(f"- {movie['title']} by {movie['director']}")
        else:
            print("No recommendations available.")

library = MovieLibraryFacade()

library.add_movie("Inception", "Christopher Nolan")
library.add_movie("Interstellar", "Christopher Nolan")
library.add_movie("Titanic", "James Cameron")
library.add_movie("Avatar", "James Cameron")

library.find_movie("Inception")

library.recommend_movies("Christopher Nolan")
