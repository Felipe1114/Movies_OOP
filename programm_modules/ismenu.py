class IsMenu:
  def __init__(self, applikation):
    self.applikation = applikation


  def execute_programm_funktions(self):
    """Takes the funktion_key and validades wich case of funktion the key is rasing"""
    movies = self.applikation.movie_data()
    funktion_key = self.get_user_input()

    if funktion_key == 0:
      exit('bye')

    elif funktion_key == 1:
      self.applikation.list_up_movies()

    elif funktion_key == 2:
      # title, year und rating bekommen
      title, year, rating = self.applikation.get_user_input(funktion_key)
      self.applikation.add_new_movie(title, year, rating)

    elif funktion_key == 3:
      # title bekommen
      title = self.applikation.get_user_input(funktion_key)
      self.applikation.delete_existend_movie(title)

    elif funktion_key == 4:
      # title und new_rating bekommen
      title, new_rating = self.applikation.get_user_input(funktion_key)
      self.applikation.update_existend_movie(title, new_rating)

    elif funktion_key == 5:
      self.applikation.get_movie_stats()

    elif funktion_key == 6:
      self.applikation.print_random_movie()

    elif funktion_key == 7:
      self.applikation.search_movie()

    elif funktion_key == 8:
      self.applikation.sort_movies_by_rating()

    elif funktion_key == 9:
      self.applikation.sort_movies_by_year()
      #
    elif funktion_key == 10:
      self.applikation.filter_movies()


  def menu_funktions(self) -> str:
    """Displays the Menu to the user with the input commands"""
    return """\n===Menu:===\n
           \t0. Exit\n
           \t1. List movies\n
           \t2. Add moives\n
           \t3. Delete movie\n
           \t4. Update movie\n
           \t5. stats\n
           \t6. Random movie\n
           \t7. Search movie\n
           \t8. Movies sorted by rating\n
           \t9. Movies sorted by year\n
           \t10. Filter movies"""


  def get_user_input(self):
    """gets a number between 0 and 8 from user"""
    while True:

      try:
        user_input = self.validade_user_input()
        return user_input

      except ValueError as e:
        print(e)


  def validade_user_input(self) -> int:
    """gets an input from user and changes its type to integer"""
    user_input = int(input("What do you want to do?(0-10): "))

    if 10 < user_input or user_input < 0:
      raise ValueError("Error! Input must be between 0 and 10.")

    return user_input


  def continue_with_programm(self):
    """get an empty string from user (by pressing Enter). If input is not empty, an Error is risen"""
    execution_number = 0
    while True:
      try:
        if execution_number == 0:
          continue_programm = input("press Enter to contiune")

        else:
          continue_programm = input("")

        if continue_programm != "":
          raise ValueError("Please just press enter to contiunue!")

        break

      except ValueError as e:
        print(e)


  def run(self) -> None:
    """gets movies form database and asks user for key(input)"""
    print("********** Welcome to my Movies Database **********")

    while True:
      print(self.menu_funktions()) # Done

      self.execute_programm_funktions()

      self.continue_with_programm()


    # Print menu
    # Get use command
    # Execute command