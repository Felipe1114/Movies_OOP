from programm_modules.ismenu import IsMenu
from programm_modules.storage_json import StorageJson
from programm_modules.movie_app import MovieApp


def main():
  storage = StorageJson("./programm_storage/movies.json")
  applikation = MovieApp(storage)
  menu = IsMenu(applikation)

  menu.run()


if __name__ == "__main__":
  main()