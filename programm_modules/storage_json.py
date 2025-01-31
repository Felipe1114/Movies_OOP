from istorage import IStorage
import json
class StorageJson(IStorage):
  def __init__(self, file_path):
    self.__file_path = file_path
    self.data = self.__get_movie()
    self.movie_list = self.__json_to_list()
    print(f"class '{self}' wurd erstellt")


  def _get_movie(self):
    """gets movie datas"""
    with open(self.__file_path, 'r') as json_file:
      data = json.load(json_file)


    return data


  def __json_to_list(self):
    """extracts movie name, moive rating and movie jear and writes it to a f-String.
    retunrs a list of moive-f-strings

    :param data: json-file with movie datas
    :param movie_list: list with movie-f-strings
    :return: None
    """
    movie_list = []

    for index, dictionary in enumerate(self.data):
      movie_f_string = ""

      for key, value in dictionary.items():
        movie_f_string += f"{key}: {value}"
        if key != "rating": movie_f_string += ", "

      movie_list.append(movie_f_string)

      return movie_list

  def list_movies():
      for index, value in enumerate(self.movie_list):
        print(value, end=None)




  def add_movie(self, title, year, rating, poster):
    """Adds a movie to the storage"""
    pass

  def delete_movie(self, title):
    """removes a moive from the storage"""
    pass

  def update_movie(self, title, rating):
    """pudates the datas of a movie"""
    pass


if __name__ == "__main__":
  file_path = "../programm_storage/movies.json"
  storage = StorageJson(file_path)
  storage.list_movies()