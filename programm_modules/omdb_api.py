from types import NoneType

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
            "year": (data.get("Year")),
            "rating": (data.get("imdbRating")),
            "poster": data.get("Poster")
          }
        else:
          print("Error: Movie not found.")

      else:
        print("Error: Failed to connect to the OMDb API.")
        print("Returning to main menu...")

        return None

  def validate_movie(self, new_movie):
    """Checks if values in movie dictionary have the correct format."""

    if new_movie is None:
      print("Error: No movie data provided.")
      return None

    required_keys = {"title": str, "year": int, "rating": float, "poster": str}

    # Prüfen, ob `new_movie` überhaupt ein Dictionary ist
    if not isinstance(new_movie, dict):
      print("Error: Provided movie is not a dictionary.")
      return None

    # Sicherstellen, dass alle Keys existieren
    for key in required_keys:
      if key not in new_movie:
        print(f"Warning: Missing key '{key}'. Setting default value.")
        if key == "year":
          new_movie[key] = 0
        elif key == "rating":
          new_movie[key] = 0.0
        elif key == "poster":
          new_movie[key] = None
        else:
          new_movie[key] = "unknown"

    # Werte validieren und ggf. konvertieren
    if not isinstance(new_movie["title"], str):
      new_movie["title"] = "unknown title"
      print("Title was not a string. Changed to 'unknown title'.")

    if not isinstance(new_movie["year"], int):
      try:
        new_movie["year"] = int(new_movie["year"])
        print("Year was not an integer. Converted.")
      except ValueError:
        new_movie["year"] = 0
        print("Invalid year format. Set to 0.")

    if not isinstance(new_movie["rating"], float):
      try:
        new_movie["rating"] = float(new_movie["rating"])
        print("Rating was not a float. Converted.")
      except ValueError:
        new_movie["rating"] = 0.0
        print("Invalid rating format. Set to 0.0.")

    if not isinstance(new_movie["poster"], str):
      new_movie["poster"] = None
      print("Poster was not a string. Changed to 'None'.")

    return new_movie

