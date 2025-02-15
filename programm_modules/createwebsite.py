class MovieWebsiteGenerator:
  """Generates an HTML file displaying movies with posters."""

  def __init__(self):
    self.storage = self.define_storage()

    if self.storage is None:
      print("Waitng for storage...")

    print(f"initialated {self}")

  def generate_html(self, filename="./programm_storage/index.html"):
    """Creates an HTML file with the movies from storage."""
    movies = self.storage.get_movie_data()

    html_content = """
      <html>
      <head>
          <title>My Movie App</title>
          <link rel="stylesheet" href="style.css"/>
      </head>
      <body>
          <div class="list-movies-title">
              <h1>My Movie App</h1>
          </div>
          <div>
              <ol class="movie-grid">
      """

    for movie in movies:
      html_content += f"""
              <li>
                  <div class="movie">
                      <img class="movie-poster" src="{movie['poster']}"/>
                      <div class="movie-title">{movie['title']}</div>
                      <div class="movie-year">{movie['year']}</div>
                  </div>
              </li>
          """

    html_content += """
              </ol>
          </div>
      </body>
      </html>
      """


    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)




    print(f"Website generated and saved as {filename}")


  def define_storage(self, storage=None):
    """puts storage in self.storage"""
    self.storage = storage
    print(f"defined storage as {self.storage} in {self}")
