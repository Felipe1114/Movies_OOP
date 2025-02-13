from programm_modules.istorage import IStorage

class StorageCSV(IStorage):
  def __init__(self, file_path):
    try:
      # file_path = "programm_storage/test_csv.csv"
      self.__file_path = file_path
      self._movies = self.get_movie_data() # ist das richtig? oder muss ich das immer wieder aufrufen?
      self._movie_list = self.__json_to_list()
      self.key_for_rating = 'rating'
      self.key_for_name = 'name'
      self.key_for_year = 'year'
      print(f"class '{self}' wurd erstellt")

    except FileNotFoundError:
      self._write_file()





def csv_to_json():
  """gets a list of strings. converts list to json format"""
  lines = get_movie_data()
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


def get_movie_data():
  with open(file_path, 'r') as file:
    lines = file.readlines()

  return lines

print(csv_to_json())















