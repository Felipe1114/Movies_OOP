from programm_modules.ismenu import IsMenu
from programm_modules.movie_app import MovieApp
from programm_modules.omdb_api import OmdbApi

def main():
  api_key = "70e6d1f0"
  omdbapi = OmdbApi(api_key)
  applikation = MovieApp(omdbapi,"./programm_storage/movies.json", 'json', )
  menu = IsMenu(applikation)

  menu.run()


if __name__ == "__main__":
  main()