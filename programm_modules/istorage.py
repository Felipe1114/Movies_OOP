from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def _get_movie(self):
        """gets movie datas"""
        pass

    @abstractmethod
    def list_movies(self):
        """returns a list with movie-f-strings

        :return: movie_list
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Adds a movie to the storage"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """removes a moive from the storage"""
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """pudates the datas of a movie"""
        pass


    @abstractmethod
    def _save_movies(self):
      """Saves the movie data to storage"""

      pass


    @abstractmethod
    def _find_movie_index(self, title):
        pass













# ===========================================================================================
#
# import json as js
# from . import movie_Menu_actions as mma
#
# DATAPATH = "./programm_files/movie_storage.json"
#
# KEY_FOR_YEAR = "year"
# KFY = KEY_FOR_YEAR
# KEY_FOR_RATING = "rating"
# KFR = KEY_FOR_RATING
# KEY_FOR_NAME = "name"
# KFN = KEY_FOR_NAME
#
#
# def get_movies() -> list:
#   """
#   Returns a list of dictionaries that
#   contains the movies information in the database.
#
#   The function loads the information from the JSON
#   file and returns the data.
#   """
#   with open(DATAPATH, "r") as json_data:
#     movies = js.load(json_data)
#   return movies
#
#
# def save_movies(movies):
#   """
#   Gets all your movies as an argument and saves them to the JSON file.
#   """
#   with open(DATAPATH, "w") as json_data:
#     js.dump(movies, json_data, indent=4)
#
#
# def add_movie():
#   """
#   Adds a movie to the movies database.
#   Loads the information from the JSON file, add the movie,
#   and saves it. The function doesn't need to validate the input.
#   """
#   movies = get_movies()
#   new_movie = {}
#
#   mma.get_movie_informations(new_movie)
#
#   movies.append(new_movie)
#
#   save_movies(movies)
#
#   return (f"A new Movie({movies[-1][KFN]}({movies[-1][KFY]})"
#           f"with rating {movies[-1][KFR]} was added to movie list")
#
#
# def delete_movie():
#   """
#   Deletes a movie from the movies database.
#   Loads the information from the JSON file, deletes the movie,
#   and saves it. The function doesn't need to validate the input.
#
#   movie_dict: the dictionary the user want to delete
#   index: the index of the dictionary in movie list
#   """
#   movies = get_movies()
#
#   while True:
#
#     try:
#       searched_movie_title = mma.get_movie_name(movies)
#
#       movie_dict, index = find_dict_by_name(movies, searched_movie_title)
#       delete_notification = (f"Movie({movie_dict[KFN]}({movie_dict[KFY]})"
#                              f"with rating {movie_dict[KFR]} was deleted")
#
#       del movies[index]
#       save_movies(movies)
#
#       return delete_notification
#     except ValueError as e:
#       print(e)
#
#
# def update_movie():
#   """
#   Updates a movie from the movies database.
#   Loads the information from the JSON file, updates the movie,
#   and saves it. The function doesn't need to validate the input.
#   """
#   movies = get_movies()
#
#   movie_name = mma.get_movie_name(movies)
#   movie_rating = mma.get_movie_rating()
#
#   searched_dict, index = find_dict_by_name(movies, movie_name)
#   movies[index][KFR] = movie_rating
#   save_movies(movies)
#
#   return (f"The rating of the movie({movies[index][KFN]}({movies[index][KFY]})"
#           f"is now: {movies[index][KFR]}")
#
#
# def find_dict_by_name(movies: list, searched_name: str) -> tuple:
#   """Iterates thrue all dicts in the list(movies).
#   Checks, if searched name is a value from the key "name".
#   searching is case insensitive
#   If so, it returns the whole dict, with the key-value "movie_name"
#
#   Args:
#     movies(list): a list, of dictionaries, with movie informations
#     searched_name: the value of the key "name" of a movie-dictionary
#
#   Returns:
#     dict: a single dictionary, with informations about one film
#     i: the index of the searched dict in the movie-list
#   """
#   for i in range(len(movies)):
#     if movies[i][KFN].lower() == searched_name.lower():
#       return movies[i], i
#   raise ValueError("Given name not in movie-list. Please give an existing name")
#
#




