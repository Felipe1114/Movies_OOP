from jinja2.lexer import TOKEN_DOT

from istorage import IStorage
import json


class StorageJson(IStorage):
  def __init__(self, file_path):
    try:
      self.__file_path = file_path
      self._movies = self._get_movie() # ist das richtig? oder muss ich das immer wieder aufrufen?
      self._movie_list = self.__json_to_list()
      print(f"class '{self}' wurd erstellt")


    except FileNotFoundError:
      self._write_file()





  def _get_movie(self):
    """gets movie datas"""
    with open(self.__file_path, 'r') as json_file:
      movies = json.load(json_file)

    return movies


  def __json_to_list(self):
    """extracts movie name, moive rating and movie jear and writes it to a f-String.
    retunrs a list of moive-f-strings

    :param data: json-file with movie datas
    :param movie_list: list with movie-f-strings
    :return: None
    """
    movie_list = []

    for index, dictionary in enumerate(self._movies):
      movie_f_string = ""

      for key, value in dictionary.items():
        movie_f_string += f"{key}: {value}"
        if key != "rating": movie_f_string += ", "

      movie_list.append(movie_f_string)

    return movie_list


  def list_movies(self):
      for index, value in enumerate(self._movie_list):
        print(value, end=None)


  def add_movie(self, title, year, rating, poster):
    """Adds a movie to the storage"""
    # ist poster richtig hier eingefügt?
    new_movie = {"name": title, "year": year, "rating": rating, "poster": poster}
    self._movies.append(new_movie)

    self._save_movies()

    # added movie, is the last item in list
    last_item_index = -1
    print(f"Added new Movie: {self.__print_movie_data(last_item_index)})
    # TODO exceptions einfügen


  def delete_movie(self, title):
    """removes a moive, by given title, from the storage"""
    try:

      title_index = self._find_movie_index(title)

      del self._movies[title_index]

      self._save_movies()

      print(f"Deleted movie: {title}")

    except TypeError as e:
      print(e)


  def _find_movie_index(self, title):
    """Finds the index of the movie dict, by its title"""
    title_index = None

    for index, value in enumerate(self._movies):

      if value["name"] == title:
        title_index = index

    if isinstance(title_index, type(None)):
      raise TypeError("list indices must be integers or slices, not NoneType")

    return title_index


  def update_movie(self, title, rating):
    """pudates the datas of a movie"""
    try:

      title_index = self._find_movie_index(title)

      self._movies[title_index]['rating'] = rating

      self._save_movies()

      print(f"Updated Movie: {title}, new rating is: {rating}")

    except TypeError as e:
      print(e)


  def _save_movies(self):
    with open(self.__file_path, "w") as json_file:
      json.dump(self._movies, json_file, indent=4)


  def _write_file(self):
    """Writes an empty Json file"""
    with open(file_path, "w") as json_file:
      json.dump([], json_file, indent=4)


  def __print_movie_data(self, movie_index):
    """returns an f"string" with the datas of a specific movie"""
    movie_dict = self._movies[movie_index]
    title = movie_dict["title"]
    rating = movie_dict['rating']
    year = movie_dict['year']

    return f"title:{title}, year: {year}, rating: {rating}"



if __name__ == "__main__":
  file_path = "../programm_storage/movies.json"
  storage = StorageJson(file_path)
  storage.list_movies()
  storage.delete_movie("dreiaffen")