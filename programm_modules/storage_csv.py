from programm_modules import istorage
import csv

class StorageCSV(istorage.IStorage):
  def __init__(self, file_path):
    self.__file_path = file_path
    self._movies = self.get_movie_data()
    self.key_for_rating = 'rating'
    self.key_for_name = 'title'
    self.key_for_year = 'year'
    print(f"Class '{self}' wurde erstellt")

  def get_movie_data(self):
    """Gets movie data from CSV file an converts it to a dict"""
    try:
      with open(self.__file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        #returns a list of dicts
        return list(reader)
    except FileNotFoundError:
      self._write_file()
      return []

  def get_movie_list(self):
    """Returns a list of formatted movie strings"""
    return [f"{movie['name']}, {movie['year']}, {movie['rating']}" for movie in self._movies]

  def add_movie(self, api_response):
    """Adds a movie to the CSV storage from API response."""
    # Extrahieren der relevanten Daten aus dem API-Response
    new_movie = {
      "title": api_response.get("title"),
      "year": api_response.get("year"),
      "rating": api_response.get("rating"),
      "poster": api_response.get("poster")
    }

    # defines in wich order, the data is stored in the csv file
    fieldnames = ["title", "year", "rating", "poster"]

    with open(self.__file_path, mode='a', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=fieldnames)

      # if file is empty (no header), a header is written
      if file.tell() == 0:
        writer.writeheader()

      # writes new_movie to csv file
      writer.writerow(new_movie)

    print(f"Added new Movie to CSV: {new_movie['title']}")

  def delete_movie(self, title):
    """Removes a movie by title"""
    self._movies = [movie for movie in self._movies if movie['name'].lower() != title.lower()]
    self._save_movies()
    print(f"Deleted movie: {title}")

  def update_movie(self, title, rating):
    """Updates a movie's rating"""
    for movie in self._movies:
      if movie['name'].lower() == title.lower():
        movie['rating'] = rating
        break
    self._save_movies()
    print(f"Updated Movie: {title}, new rating is: {rating}")

  def _save_movies(self):
    """Writes movie data back to the CSV file"""
    with open(self.__file_path, 'w', newline='', encoding='utf-8') as csv_file:
      # defines the key names
      fieldnames = ["name", "year", "rating", "poster"]
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      # writes the headers
      writer.writeheader()
      # wiretes the rest of the lines
      writer.writerows(self._movies)

  def _write_file(self):
    """Creates an empty CSV file with headers"""
    with open(self.__file_path, 'w', newline='', encoding='utf-8') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(["name", "year", "rating", "poster"])
    print(f"New file added to Storage: {self.__file_path}")


  def get_average(self):
    """Calculates the average rating"""
    ratings = [float(movie['rating']) for movie in self._movies if movie['rating']]

    return sum(ratings) / len(ratings) if ratings else 0


  def get_median(self):
    """Calculates the median rating"""
    ratings = sorted([float(movie['rating']) for movie in self._movies if movie['rating']])

    lenght = len(ratings)
    if lenght == 0:

      return 0

    median = lenght // 2
    return (ratings[median - 1] + ratings[median]) / 2 if lenght % 2 == 0 else ratings[median]


  def sort_movies(self, key='rating'):
    """Sorts movies by a given key"""
    movies = self.get_movie_data()
    sorted_movies = sorted(movies, key=lambda dict: dict[key], reverse=True)

    return sorted_movies


  def get_movies_by_rating(self, rating_type: int):
    """sorts all movies, by their rating"""
    sorted_movie_list = self.sort_movies(self.key_for_rating)
    s_m_l = sorted_movie_list

    if rating_type == 0 or rating_type == -1:

      raiting_checker = s_m_l[rating_type][self.key_for_rating]
      sorted_list_by_rating = []

      for i, dictionary in enumerate(s_m_l):
        if dictionary[self.key_for_rating] == raiting_checker:
          sorted_list_by_rating.append(dictionary)

      return sorted_list_by_rating


  def _find_movie_index(self, title):
    """Not used, but necessary cause Parent Class IStorage"""
    pass

  def find_dict_by_name(self, title):
    """Finds a movie by its name and returns the corresponding dictionary"""
    return next((movie for movie in self._movies if movie['name'].lower() == title.lower()), None)
