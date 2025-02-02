class MovieApp:
  def __init__(self, storage):
    self._storage = storage

  def _command_list_movies(self):
    """Gets movie list from self.storage; displays all movies"""
    movies_list = self._storage.list_movies()

    for index, value in enumerate(movies_list):
      print(index + 1, value, sep=". ") #-> 1. name:name, rating:rating,...


  def _command_movie_stats(self):
    """Gets movie data from self.storage; displays all movie-stats"""
    # movie stats von altem code einfügen
    pass


  def _generate_website(self):
    """Gets movie data form self.storage, generates movie-HTML dokument"""
    pass


  def run(self):
    """runs the app in a while loop; gets actions from User"""
    pass
    # Print menu
    # Get use command
    # Execute command