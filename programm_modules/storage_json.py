from programm_modules import istorage
import json

class StorageJson(istorage.IStorage):
  def __init__(self, file_path):
    try:
      self.__file_path = file_path
      self._movies = self.get_movie_data() # ist das richtig? oder muss ich das immer wieder aufrufen?
      self._movie_list = self.__json_to_list()

      self.key_for_rating = 'rating'
      self.key_for_name = 'name'
      self.key_for_year = 'year'

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

  # kann noch poster bekommen...
  def add_movie(self, title, year, rating, poster=None):
    """Adds a movie to the storage"""
    self._movies = self.get_movie_data()

    new_movie = {"name": title, "year": year, "rating": rating, "poster": poster}
    self._movies.append(new_movie)

    self._save_movies()

    # added movie, is the last item in list
    last_item_index = -1
    print(f"Added new Movie: {self.__print_movie_data(last_item_index)}")


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

      if value["name"].lower() == title.lower():
        title_index = index

    if not isinstance(title_index, int):
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
    title = movie_dict[self.key_for_name]
    rating = movie_dict[self.key_for_rating]
    year = movie_dict[self.key_for_year]

    return f"title:{title}, year: {year}, rating: {rating}"


  def find_dict_by_name(self,searched_name: str) -> dict:
    """Iterates thrue all dicts in the list(movies).
    Checks, if searched name is a value from the key "name"."""
    movies = self.get_movie_data()

    for i, dictionary in enumerate(movies):
      if dictionary[self.key_for_name].lower() == searched_name.lower():
        return movies[i]

    raise ValueError("Given name not in movie-list. Please give an existing name")


  def get_average(self) -> float:
    '''calcultes the average of all movie ratings'''
    ratings = self.sort_list_by_rating()
    average = sum(ratings) / len(ratings)


    return average


  def get_median(self) -> float:
    '''calculates the median from all ratings(values) of movies(dict)'''
    sorted_list = self.sort_list_by_rating()

    # finds the middle vlaue of the list (for the median)
    mid_index = len(sorted_list) // 2 - 1

    # when list is even
    if len(sorted_list) % 2 == 0:
      median = (sorted_list[mid_index] + sorted_list[mid_index + 1]) / 2

    # when list is uneven
    else:
      median = sorted_list[mid_index]

    return median


  def sort_list_by_rating(self) -> list:
    '''sorts the list(movies) by its ratings in the dicionaries'''
    sorted_list = self.sort_movies(self.key_for_rating)
    rating_list = []

    for dict in sorted_list:
      rating_list.append(dict[self.key_for_rating])

    return rating_list


  def sort_movies(self, key: str) -> list:
    '''Sorts the List(movies) by rating, key is year or name'''
    movies = self.get_movie_data()
    sorted_movies = sorted(movies, key=lambda dict: dict[key], reverse=True)

    return sorted_movies



  def get_movies_by_rating(self, rating_type: int) -> list:
    '''gets a sorted movie(s) - by rating_type - in the list (movies)'''
    sorted_movie_list = self.sort_movies(self.key_for_rating)
    s_m_l = sorted_movie_list

    if rating_type == 0 or rating_type == -1:


      raitig_checker = s_m_l[rating_type][self.key_for_rating]
      sorted_list_by_rating = []

      for i in range(len(s_m_l)):
        if s_m_l[i][self.key_for_rating] == raitig_checker:
          sorted_list_by_rating.append(s_m_l[i])

      return sorted_list_by_rating






