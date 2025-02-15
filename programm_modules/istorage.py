from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_movie_data(self):
        """gets movie datas"""
        pass


    @abstractmethod
    def add_movie(self, new_movie):
        """Adds a movie to the storage"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """removes a moive from the storage"""
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """pudates the datas of a movie"""
        pass


    @abstractmethod
    def _save_movies(self):
      """Saves the movie data to storage"""

      pass


    @abstractmethod
    def _find_movie_index(self, title):
        pass


    @abstractmethod
    def _write_file(self):
        pass









