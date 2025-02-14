import requests

class OmdbApi:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def search_movie_by_title(self, title: str):
        """Searches for a movie by title and returns the movie data."""
        params = {
            "t": title,  # Movie title to search for
            "apikey": self.api_key
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            # Wenn der Film gefunden wird
            if data.get("Response") == "True":
                return {
                    "title": data.get("Title"),
                    "year": data.get("Year"),
                    "rating": data.get("imdbRating"),
                    "genre": data.get("Genre"),
                    "director": data.get("Director"),
                    "actors": data.get("Actors"),
                    "plot": data.get("Plot")
                }
            else:
                print("Error: Movie not found.")
                return None
        else:
            print("Error: Failed to connect to the OMDb API.")
            return None