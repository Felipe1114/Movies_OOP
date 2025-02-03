'''
storage befehle:
movie_daten erhalten: self._storage.get_movie_data()
movie_list erhalten: self._storage.get_movie_list()
workflow: 
core funktionen refactorieren

'''
import random

class MovieApp:
  def __init__(self, storage):
    self._storage = storage
    self.__key_for_rating = 'rating'
    self.__key_for_name = 'name'
    self.__key_for_year = 'year'

    # methoden müssen noch refactorisiert werden

    # TODO alle weiteren funktionen einfügen!!!
    self._operations = {
    0: exit,  # ("bye")
    1: self.list_up_movies,  # (movies),
    2: self._storage.add_movie, #(title, year, rating, poster)
    3: self._storage.delete_movie, #(title)
    4: self._storage.update_movie, #(title, rating)
    5: self._command_movie_stats,
    6: self.print_random_movie,
    7: self.search_movie,  # (movie_name),
    8: self.sort_movies_by_rating,  # no print
    9: self.sort_movies_by_year,  # no pirnt)
    10: self.filter_movies  # (movies)
  }




  def _command_list_movies(self) -> None:
    '''Gets movie list from self.storage; displays all movies'''
    movies_list = self._storage.get_movie_data()


    for index, value in enumerate(movies_list):
      print(index + 1, value, sep='. ') #-> 1. name:name, rating:rating,...




  def print_random_movie(self):
    """Displays a random movie from movies"""
    movies = self._storage.get_movie_data()

    random_index = random.randrange(len(movies))
    random_movie = movies[random_index]

    print(f"Here is a ranodm movie out of the Database:\n"
            f"{random_movie[self.__key_for_name]}({random_movie[self.__key_for_year]}): {random_movie[self.__key_for_rating]}")





  def _command_movie_stats(self) -> str:
    '''Calculates and diyplays average rating, median rating, best and worst movie rating'''
    average = self._get_average()
    median = self._get_median()


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




  def _get_average(self) -> float:
    '''calcultes the average of all movie ratings'''
    ratings = self._sort_list_by_rating()
    average = sum(ratings) / len(ratings)


    return average




  def _get_median(self) -> float:
    '''calculates the median from all ratings(values) of movies(dict)'''
    sorted_list = self._sort_list_by_rating()


    # finds the middle vlaue of the list (for the median)
    mid_index = len(sorted_list) // 2 - 1


    # when list is even
    if len(sorted_list) % 2 == 0:
      median = (sorted_list[mid_index] + sorted_list[mid_index + 1]) / 2


    # when list is uneven
    else:
      median = sorted_list[mid_index]


    return median




  def _get_best_movies(self) -> list:
    '''gets the best movie(s) - by rating - in the list (movies)'''
    sorted_movie_list = self._sort_movies(self.__key_for_rating)

    sml = sorted_movie_list
    best_rating = sml[0][self.__key_for_rating]
    best_movies = []

    for i in range(len(sml)):
      if sml[i][self.__key_for_rating] == best_rating:
        best_movies.append(sml[i])


    return best_movies




  def _get_worst_movies(self) -> list:
    '''gets the worst movie(s) - by rating - in the list (movies)'''
    sorted_movie_list = self._sort_movies(self.__key_for_rating)


    sml = sorted_movie_list
    worst_rating = sml[-1][self.__key_for_rating]
    worst_movies = []


    for i in range(len(sml)):
      if sml[i][self.__key_for_rating] == worst_rating:
        worst_movies.append(sml[i])


    return worst_movies




  def list_up_movies(self, sort_type: str) -> str:
    '''returns a sortet list of movies, depending on 'sort_type: best/worst'''
    if sort_type == 'best':
      best_movies = self._get_best_movies()

      text = ''
      for movie in best_movies:
        text = text + f'{movie[self.__key_for_name]}({movie[self.__key_for_year]}): {movie[self.__key_for_rating]}' + '\n'

      return text


    elif sort_type == 'worst':
      worst_movies = self._get_worst_movies()

      text = ''
      for movie in worst_movies:
        text = text + f'{movie[self.__key_for_name]}({movie[self.__key_for_year]}): {movie[self.__key_for_rating]}' + '\n'

        return text




  def _sort_list_by_rating(self) -> list:
    '''sorts the list(movies) by its ratings in the dicionaries'''
    sorted_list = self._sort_movies(self.__key_for_rating)
    rating_list = []


    for dict in sorted_list:
      rating_list.append(dict[self.__key_for_rating])


    return rating_list




  def _sort_movies(self, key: str) -> list:
    '''Sorts the List(movies) by rating, key is year or name'''
    movies = self._storage.get_movie_data()
    sorted_movies = sorted(movies, key=lambda dict: dict[key], reverse=True)

    return sorted_movies




  def _generate_website(self):
    '''Gets movie data form self.storage, generates movie-HTML dokument'''
    pass




  def execute_programm_funktions(self, ):
    """Takes the funktion_key and validades wich case of funktion the key is rasing"""
    movies = self._storage.get_movie_data
    funktion_key = self.get_user_input()

    # the exit() funktion, wich is taking "bye" as argument
    a_funktions = [0]
    # all funktions, which are taking 'movies' as an argument
    b_funktions = [1, 5, 6, 7, 8, 9, 10]
    # all funktions, wich don´t take an argument
    c_funktions = [2, 3, 4]


    if funktion_key in a_funktions:
      print(self._operations[funktion_key]("bye"))

    elif funktion_key in b_funktions:
      print(self._operations[funktion_key](movies))

    elif funktion_key in c_funktions:
      print(self._operations[funktion_key]())




  def continue_with_programm(self):
    """get an empty string from user (by pressing Enter). If input is not empty, an Error is risen"""
    while True:
      try:
        continue_programm = input("press Enter to contiune")
        self.validade_programm_continuation(continue_programm)

        break


      except ValueError as e:
        print(e)




  def validade_programm_continuation(self, user_input):
    """validades if user_input is an empty string (len = 0). If not, an Error is risen"""
    if len(user_input) > 0:
      raise ValueError("Please press only Enter")




  def _menu(self) -> str:
    """Displays the Menu to the user with the input commands"""
    return """\n===Menu:===\n
           \t0. Exit\n
           \t1. List movies\n
           \t2. Add moives\n
           \t3. Delete movie\n
           \t4. Update movie\n
           \t5. stats\n
           \t6. Random movie\n
           \t7. Search movie\n
           \t8. Movies sorted by rating\n
           \t9. Movies sorted by year\n
           \t10. Filter movies"""




  def get_user_input(self):
    """gets a number between 0 and 8 from user"""
    while True:

      try:
        user_input = self.validade_user_input()
        return user_input

      except ValueError as e:
        print(e)




  def validade_user_input(self) -> int:
    """gets an input from user and changes its type to integer"""
    user_input = int(input("What do you want to do?(0-10): "))

    if 10 < user_input or user_input < 0:
      raise ValueError("Error! Input must be between 0 and 8.")

    return user_input


  def search_movie(self):
    """The user gives an input(movie name), than the funktion prints the movie,
    with its release year and ranking"""
    while True:

      try:
        searched_name = input("Wich movie are you searching for?: ")
        searched_movie = self._storage.find_dict_by_name(searched_name)
        return f'{searched_movie[self.__key_for_name]}({searched_movie[self.__key_for_year]}): {searched_movie[self.__key_for_rating]}'

      except ValueError as e:
        print("Error:", e)


  def sort_movies_by_rating(self) -> str:
    """prints movies, sorted by rating (high to low)"""
    sorted_movies = self._sort_movies(self.__key_for_rating)

    return self._storage.list_up_movies(sorted_movies)


  def sort_movies_by_year(self) -> str:
    """prints movies, sorted by year (high to low)

    :param movies: a list of dictionaries with movie informations
    """
    sorted_movies = self._sort_movies(self.__key_for_rating)

    return self._storage.list_up_movies(sorted_movies)

  def run(self):
    """gets movies form database and asks user for key(input).
    Than executes function out of dictionary(function is value of given key)
    """
    print("********** Welcome to my Movies Database **********")

    while True:
      print(self._menu())

      self.execute_programm_funktions()

      self.continue_with_programm()



    # Print menu
    # Get use command
    # Execute command