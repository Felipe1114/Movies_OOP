'''
storage befehle:
movie_daten erhalten: self._storage.get_movie_data()
movie_list erhalten: self._storage.get_movie_list()
workflow: 
core funktionen refactorieren

'''
import random
import copy

class MovieApp:
  def __init__(self, storage):
    self._storage = storage
    self._operations = {
    0: exit,  # ("bye")
    1: self.list_up_movies,  #,
    2: self.add_new_movie, #(title, year, rating, poster)
    3: self._storage.delete_movie, #(title)
    4: self._storage.update_movie, #(title, rating)
    5: self.get_movie_stats,
    6: self.print_random_movie,
    7: self.search_movie,
    8: self.sort_movies_by_rating,
    9: self.sort_movies_by_year,
    10: self.filter_movies
  }


  def movie_data(self):
    return self._storage.get_movie_data()


  def list_up_movies(self, sort_type: str=None) -> None:
    '''returns a sortet list of movies, depending on 'sort_type: best/worst, if existent'''
    if sort_type is None:
      movies_list = self._storage.get_movie_list()

      self._print_movies(movies_list)

    elif sort_type == 'best':
      # get best movie will ich aus storage bekommen
      best_movies = self._storage.get_movies_by_rating(0)

      for movie in best_movies:
        self._print_single_movie(movie)

    elif sort_type == 'worst':
      # get worst movie will ich aus storage bekommen

      worst_movies = self._storage.get_movies_by_raging(-1)

      for movie in worst_movies:
        self._print_single_movie(movie)


  # kann noch poster bekommen
  def add_new_movie(self, title, year, rating):
    self._storage.add_movie(title, year, rating)


  def delete_existend_movie(self, title):
    self._storage.delete_movie(title)


  def update_existend_movie(self, title, new_rating):
    self._storage.update_movie(title, new_rating)


  def print_random_movie(self) -> None:
    """Displays a random movie from movies"""
    movies = self._storage.get_movie_data()

    random_index = random.randrange(len(movies))

    print("Here is a ranodm movie out of the Database:")
    self._print_single_movie(movies[random_index])


  def _print_single_movie(self, movie: dict) -> None:
    """prints a single movie, out of a dict"""
    print(f"{movie[self._storage._storage.key_for_name]}"
          f"({movie[self._storage._storage.key_for_year]}): "
          f"{movie[self._storage.key_for_rating]}")


  def _print_movies(self, movie_list: list) -> None:
    """"""
    for index, movie in enumerate(movie_list):
      print(index + 1, end='. ')
      self._print_single_movie(movie)


  def get_movie_stats(self) -> str:
    '''Calculates and diyplays average rating, median rating, best and worst movie rating'''
    average = self._storage._get_average()
    median = self._storage._get_median()


    text_for_best_movies = self.list_up_movies('best')
    text_for_worst_movies = self.list_up_movies('worst')


    text = (f'\nThe statistics are:'
            f'Average of rating: {average:.2f}\n'
            f'The median of rating is: {median}\n'
            f'--------\nthe best movie/s is/are:\n'
            f'{text_for_best_movies}\n'
            f'he worst movie/s is/are:\n'
            f'{text_for_worst_movies}')


    return text


  def _generate_website(self):
    '''Gets movie data form self.storage, generates movie-HTML dokument'''
    pass


  def search_movie(self):
    """The user gives an input(movie name), than the funktion prints the movie,
    with its release year and ranking"""
    while True:

      try:
        searched_name = input("Wich movie are you searching for?: ")
        searched_movie = self._storage.find_dict_by_name(searched_name)

        self._print_single_movie(searched_movie)

      except ValueError as e:
        print("Error:", e)


  def sort_movies_by_rating(self) -> None:
    """prints movies, sorted by rating (high to low)"""
    sorted_movies = self._storage.sort_movies(self._storage.key_for_rating)

    self.list_up_movies(sorted_movies)


  def sort_movies_by_year(self) -> None:
    """prints movies, sorted by year (high to low)"""
    sorted_movies = self._storage.sort_movies(self._storage.key_for_rating)

    self.list_up_movies(sorted_movies)


  def filter_movies(self) -> None:
    """filters a deep copy of list(movies) by the filter values given by user"""
    movies = self._storage.get_movie_data()

    minimum_rating, start_year, end_year = self.get_filter_input()
    filtred_movies = copy.deepcopy(movies)

    if type(minimum_rating) is float:
      self.filter_rating(filtred_movies, minimum_rating)

    # if start_year and end_year got input
    if type(start_year) is int and type(end_year) is int:
      self.filter_by_start_and_end_year(filtred_movies, start_year, end_year)

    # if only start_year got input
    elif type(start_year) is int and type(end_year) is not int:
      self.filter_by_start_year(filtred_movies, start_year)

    # if only end_year got input
    elif type(start_year) is not int and type(end_year) is int:
      self.filter_by_end_year(filtred_movies, end_year)

    return self.list_up_movies(filtred_movies)


  def get_filter_input(self) -> tuple:
    """gets the filter values from user. Changes types form input to float or integer"""
    while True:
      try:
        minimum_rating = input("Enter minimum rating (leave blank for no minimum rating): ")
        start_year = input("Enter start year (leave blank for no start year): ")
        end_year = input("Enter end year (leave blank for no end year): ")

        if len(minimum_rating) > 0:
          minimum_rating = float(minimum_rating)
        if len(start_year) > 0:
          start_year = int(start_year)
        if len(end_year) > 0:
          end_year = int(end_year)

        return minimum_rating, start_year, end_year

      except ValueError as e:
        print(f"Input must be empty or an number: {e}")


  def filter_rating(self, filtred_movies, minimum_rating) -> None:
    """makes a copy of movies and deletes all elements in the list, wich ratings are under minimum_rating"""
    movies = self._storage.get_movie_data()

    for index, value in enumerate(movies):
      if movies[index][self._storage.key_for_rating] < minimum_rating:
        filtred_movies.remove(movies[index])


  def filter_by_end_year(self, filtred_movies, end_year) -> None:
    """Filters all movies, with release years higher than end_year, out of movies_copy"""
    movies = self._storage.get_movie_data()

    for index, dictionary in enumerate(movies):

      if dictionary[self._storage.key_for_year] < end_year:
        continue
      else:
        filtred_movies.remove(dictionary)


  def filter_by_start_year(self, movies_copy, start_year) -> None:
    """Filters all movies, with release years lower than start_year, out of movies_copy"""
    movies = self._storage.get_movie_data()

    for index, dictionary in enumerate(movies):

      if start_year < dictionary[self._storage.key_for_year]:
        continue
      else:
        movies_copy.remove(dictionary)


  def filter_by_start_and_end_year(self, movies_copy, start_year, end_year) -> None:
    """Filters all movies, with release years out ouf give range, out of movies_copy"""
    movies = self._storage.get_movie_data()

    for i, dictionary in enumerate(movies):

      if start_year < dictionary[self._storage.key_for_year] < end_year:
        continue
      else:
        movies_copy.remove(dictionary)


  def get_user_input(self, funktion_key):
    """Gets user_input; validades input"""
    while True:
      try:
        if funktion_key == 2:
          title = input("Type in movie name: ")
          year = int(input("Type in release year(int): "))
          rating = float(input("Type in movie rating(float): "))
          return title, year, rating

        elif funktion_key == 3:
          title = input("Type in movie name: ")
          return title
        elif funktion_key == 4:
          title = input("Type in movie name: ")
          rating = float(input("Type in movie rating(float): "))
          return title, rating

      except ValueError as e:
        print(e)
