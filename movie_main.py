from programm_modules.ismenu import IsMenu
from programm_modules.movie_app import MovieApp
from programm_modules.omdb_api import OmdbApi
from programm_modules.createwebsite import MovieWebsiteGenerator
from programm_modules.storage_json import StorageJson

def main():
  api_key = "70e6d1f0"
  omdbapi = OmdbApi(api_key)
  web_generator = MovieWebsiteGenerator()
  applikation = MovieApp(omdbapi,"./programm_storage/movies.json", web_generator, 'json')
  menu = IsMenu(applikation)

  menu.run()


if __name__ == "__main__":
  main()