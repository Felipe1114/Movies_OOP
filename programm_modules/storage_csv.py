from programm_modules import istorage
import csv

class StorageCSV(istorage.IStorage):
    def __init__(self, file_path):
        self.__file_path = file_path
        self._movies = self.get_movie_data()
        self.key_for_rating = 'rating'
        self.key_for_name = 'name'
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

    def add_movie(self, title, year, rating, poster=None):
        """Adds a movie to the CSV storage"""
        self._movies.append({"name": title, "year": year, "rating": rating, "poster": poster})
        self._save_movies()
        print(f"Added new Movie: {title}")

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
        n = len(ratings)
        if n == 0:
            return 0
        mid = n // 2
        return (ratings[mid - 1] + ratings[mid]) / 2 if n % 2 == 0 else ratings[mid]

    def sort_movies(self, key='rating'):
        """Sorts movies by a given key"""
        return sorted(self._movies, key=lambda movie: float(movie[key]) if movie[key] else 0, reverse=True)

    def get_movies_by_rating(self, rating_type):
        """Returns movies with the highest or lowest rating"""
        sorted_movies = self.sort_movies()
        if rating_type in {0, -1}:
            reference_rating = float(sorted_movies[rating_type]['rating'])
            return [movie for movie in sorted_movies if movie['rating'] == reference_rating]
        return []

    def _find_movie_index(self, title):
      pass

    def find_dict_by_name(self, title):
        """Finds a movie by its name and returns the corresponding dictionary"""
        return next((movie for movie in self._movies if movie['name'].lower() == title.lower()), None)
