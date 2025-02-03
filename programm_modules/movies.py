'''
storage befehle:
movie_daten erhalten: self._storage.get_movie_data()
movie_list erhalten: self._storage.get_movie_list()
workflow: 
core funktionen refactorieren

'''

class MovieApp:
  def __init__(self, storage):
    self._storage = storage
    self.key_for_rating = 'rating'
    self.key_for_name = 'name'
    self.key_for_year = 'year'




  def _command_list_movies(self):
    '''Gets movie list from self.storage; displays all movies'''
    movies_list = self._storage.get_movie_data()


    for index, value in enumerate(movies_list):
      print(index + 1, value, sep='. ') #-> 1. name:name, rating:rating,...




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
    movie_list = self._storage.get_movie_list()

    sorted_movie_list = self._sort_movies(movie_list, self.key_for_rating)


    sml = sorted_movie_list
    best_rating = sml[0][self.key_for_rating]
    best_movies = []


    for i in range(len(sml)):
      if sml[i][self.key_for_rating] == best_rating:
        best_movies.append(sml[i])


    return best_movies




  def _get_worst_movies(self, movies: list) -> list:
    '''gets the worst movie(s) - by rating - in the list (movies)'''
    sorted_movie_list = self._sort_movies(movies, self.key_for_rating)


    sml = sorted_movie_list
    worst_rating = sml[-1][self.key_for_rating]
    worst_movies = []


    for i in range(len(sml)):
      if sml[i][self.key_for_rating] == worst_rating:
        worst_movies.append(sml[i])


    return worst_movies




  def list_up_movies(self, sort_type: str) -> str:
    '''returns a sortet list of movies, depending on 'sort_type: best/worst'''
    movie_list = self._storage.get_movie_list()


    if sort_type == 'best':
      best_movies = self._get_best_movies()

      text = ''
      for movie in best_movies:
        text = text + f'{movie[self.key_for_name]}({movie[self.key_for_year]}): {movie[self.key_for_rating]}' + '\n'

      return text


    elif sort_type == 'worst':
      worst_movies = self._get_worst_movies(movie_list)

      text = ''
      for movie in worst_movies:
        text = text + f'{movie[self.key_for_name]}({movie[self.key_for_year]}): {movie[self.key_for_rating]}' + '\n'

        return text




  def _sort_list_by_rating(self) -> list:
    '''sorts the list(movies) by its ratings in the dicionaries'''
    movie_list = self._storage.get_movie_data()


    sorted_list = self._sort_movies(movie_list, self.key_for_rating)
    rating_list = []


    for dict in sorted_list:
      rating_list.append(dict[self.key_for_rating])


    return rating_list




  def _sort_movies(self, movies: list, key: str) -> list:
    '''Sorts the List(movies) by rating, year or name'''
    sorted_movies = sorted(movies, key=lambda dict: dict[key], reverse=True)


    return sorted_movies




  def _generate_website(self):
    '''Gets movie data form self.storage, generates movie-HTML dokument'''
    pass




  def run(self):
    '''runs the app in a while loop; gets actions from User'''
    pass
    # Print menu
    # Get use command
    # Execute command