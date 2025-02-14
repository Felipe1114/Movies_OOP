from programm_modules.istorage import IStorage


class StorageCSV(IStorage):
  def __init__(self, file_path):
    try:
      self.__file_path = file_path
      self.__movie_lines = self.get_csv_lines() # gets all csv lines
      self._movies = self.get_movie_data() # ist das richtig? oder muss ich das immer wieder aufrufen?
      # self._movie_list = self.__json_to_list() # brauche ich das noch?!
      
      self.key_for_rating = 'rating'
      self.key_for_name = 'name'
      self.key_for_year = 'year'
      
      print(f"class '{self}' wurd erstellt")
      print("StorageCSV erstellt:", vars(self))

    except FileNotFoundError:

      self._write_file()


  def get_csv_lines(self):
    """returns a list of strings from the csv file"""
    with open(self.__file_path, 'r') as file:
      lines = file.readlines()

    return lines


  def get_movie_data(self):
    """gets a list of strings. converts list to a list with dictionaries"""
    lines = self.get_csv_lines()# Todo
    # creates indicies for dictionary
    name, year, rating = lines[0].strip().split(', ')

    # create empty list for json format
    movie_list = []

    for index, line in enumerate(lines):
      # dict for movies
      movie_dict = {}

      # index 0 contains the indicies
      if index > 0:
        value_name, value_year, value_rating = line.strip().split(', ')

        movie_dict[name] = value_name
        movie_dict[year] = value_year
        movie_dict[rating] = value_rating

        movie_list.append(movie_dict)

    return movie_list


  def list_to_csv(self):
    """converts movie_list to a csv compatible format"""
    new_list = []

    for index, dictionary in enumerate(self._movies):
      line = f"{dictionary[self.key_for_name]}, {dictionary[self.key_for_year]}, {dictionary[self.key_for_rating]}\n"

      new_list.append(line)


    self._save_movies(new_list)


  def add_movie(self, title, year, rating, poster=None):
    """add´s a new string to self.__movie_lines"""
    new_movie = f"{title}, {year}, {rating}\n"

    self.__movie_lines.append(new_movie)

    self._save_movies(self.__movie_lines)

  #TODO save_movies muss direckt die daten bekommen, die gespeichert werden sollen
  def _save_movies(self, new_lines=None):
    """saves self.__movie_lines to the csv file"""
    with open(self.__file_path, "w") as file:
      # lines = self.__movie_lines
      csv_data = ""

      # converts list of strings, to a long string
      for index, line in enumerate(new_lines):
        csv_data += line

      file.write(csv_data)


  def _write_file(self):
    with open (self.__file_path, "w") as file:
      file.write("name, year, rating\n"
                 "name1, year1, rating1")
    print(f"file: {self.__file_path} was created")


  def update_movie(self, title, rating):
    """updates the self.movies - list; afterwards vonverts this data to csv"""
    try:
      self._movies = self.get_movie_data()

      title_index = self._find_movie_index(title)

      self._movies[title_index]['rating'] = rating
      print(f"Updated Movie: {title}, new rating is: {rating}")

      # updated ducitionary to csv format
      self.list_to_csv()

    except TypeError as e:
      print(e)


  def delete_movie(self, title):
    """removes a moive, by given title, from the storage"""
    try:
      self._movies = self.get_movie_data()

      title_index = self._find_movie_index(title)

      del self._movies[title_index]
      print(f"Deleted movie: {title}")

      # updated ducitionary to csv format
      self.list_to_csv()

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

    for dictionary in sorted_list:
      rating_list.append(dictionary[self.key_for_rating])

    return rating_list


  def sort_movies(self, key: str) -> list:
    '''Sorts the List(movies) by rating, key is year or name'''
    movies = self.get_movie_data()
    sorted_movies = sorted(movies, key=lambda dictionary: dictionary[key], reverse=True)

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

  
  























