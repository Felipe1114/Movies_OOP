from programm_modules import istorage
import json

class StorageJson(istorage.IStorage):
  def __init__(self, file_path):
    try:
      self.__file_path = file_path
      self._movies = self.get_movie_data() # ist das richtig? oder muss ich das immer wieder aufrufen?
      self._movie_list = self.__json_to_list()
      self.__key_for_rating = 'rating'
      self.__key_for_name = 'name'
      self.__key_for_year = 'year'
      print(f"class '{self}' wurd erstellt")

    except FileNotFoundError:
      self._write_file()


  def get_movie_data(self):
    """gets movie datas"""
    with open(self.__file_path, 'r') as json_file:
      movies = json.load(json_file)

    return movies


  def get_movie_list(self):
      """returns a list of movie f-strings"""
      self._movie_list = self.__json_to_list()

      return self._movie_list


  def __json_to_list(self):
    """extracts movie name, moive rating and movie jear and writes it to a f-String.
    retunrs a list of moive-f-strings
    """
    movie_list = []

    for index, dictionary in enumerate(self._movies):
      movie_f_string = ""

      for key, value in dictionary.items():
        movie_f_string += f"{key}: {value}"
        if key != "rating": movie_f_string += ", "

      movie_list.append(movie_f_string)

    return movie_list


  def add_movie(self, title, year, rating, poster):
    """Adds a movie to the storage"""
    # ist poster richtig hier eingefügt?
    self._movies = self.get_movie_data()

    new_movie = {"name": title, "year": year, "rating": rating, "poster": poster}
    self._movies.append(new_movie)

    self._save_movies()

    # added movie, is the last item in list
    last_item_index = -1
    print(f"Added new Movie: {self.__print_movie_data(last_item_index)}")
    # TODO exceptions einfügen


  def delete_movie(self, title):
    """removes a moive, by given title, from the storage"""
    try:
      self._movies = self.get_movie_data()

      title_index = self._find_movie_index(title)

      del self._movies[title_index]

      self._save_movies()

      print(f"Deleted movie: {title}")

    except TypeError as e:
      print(e)


  def _find_movie_index(self, title):
    """Finds the index of the movie dict, by its title"""
    self._movies = self.get_movie_data()

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
      self._movies = self.get_movie_data()

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
    with open(self.__file_path, "w") as json_file:
      json.dump([], json_file, indent=4)

    print(f"New file added to Storage: {self.__file_path}")


  def __print_movie_data(self, movie_index):
    """returns an f"string" with the datas of a specific movie"""
    self._movies = self.get_movie_data()

    movie_dict = self._movies[movie_index]
    title = movie_dict[self.__key_for_name]
    rating = movie_dict[self.__key_for_rating]
    year = movie_dict[self.__key_for_year]

    return f"title:{title}, year: {year}, rating: {rating}"


  def find_dict_by_name(self,searched_name: str) -> dict:
    """Iterates thrue all dicts in the list(movies).
    Checks, if searched name is a value from the key "name"."""
    movies = self.get_movie_data()

    for i, dictionary in enumerate(movies):
      if dictionary[self.__key_for_name].lower() == searched_name.lower():
        return movies[i]

    raise ValueError("Given name not in movie-list. Please give an existing name")


  def list_up_movies(self, movies) -> str:
    """prints a list of movies"""
    text = ""
    for movie in movies:
      text = text + f"{movie[self.__key_for_name]}({movie[self.__key_for_year]}): {movie[self.__key_for_rating]}" + "\n"  # print engine einbauen

    return text


if __name__ == "__main__":
  file_path = "../programm_storage/movies.json"
  storage = StorageJson(file_path)
  storage.list_movies()
  storage.delete_movie("dreiaffen")