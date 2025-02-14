import requests

class OmdbApi:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def get_movie_from_api(self):
        """Searches for a movie by title and returns the movie data."""
        while True:
            title = input("Enter movie title (or press Enter to return to main menu): ").strip()

            if title == "":
                print("Returning to main menu...")
                return None

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
                        "year": int(data.get("Year")),
                        "rating": float(data.get("imdbRating")),
                        "poster": data.get("Poster")
                    }
                else:
                    print("Error: Movie not found.")

            else:
                print("Error: Failed to connect to the OMDb API.")
                print("Returning to main menu...")

                return None