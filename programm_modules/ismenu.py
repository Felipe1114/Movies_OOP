class IsMenu:
  def __init__(self, applikation):
    self.applikation = applikation


  def _execute_programm_funktions(self) -> None:
    """Takes the funktion_key and validades wich case of funktion the key is rasing"""
    movies = self.applikation.movie_data()
    funktion_key = self._get_user_input()

    if funktion_key == 0:
      exit('bye')

    elif funktion_key == 1:
      self.applikation.list_up_movies()

    elif funktion_key == 2:
      self.applikation.add_new_movie() # film comes from the API

    elif funktion_key == 3:
      title = self.applikation._get_extra_data(funktion_key)
      self.applikation.delete_existend_movie(title)

    # update movie wird nicht mehr gebraucht
    elif funktion_key == 4:
      # title, new_rating = self.applikation._get_extra_data(funktion_key)
      # self.applikation.update_existend_movie(title, new_rating)
      print("This feature is offline")

    elif funktion_key == 5:
      self.applikation.get_movie_stats()

    elif funktion_key == 6:
      self.applikation.print_random_movie()

    elif funktion_key == 7:
      self.applikation.search_movie()

    elif funktion_key == 8:
      self.applikation.sort_movies_by_rating() # falsche methode

    elif funktion_key == 9:
      self.applikation.sort_movies_by_year()

    elif funktion_key == 10:
      self.applikation.filter_movies()

    elif funktion_key == 11:
      self.applikation.generate_website()


  def _menu_funktions(self) -> str:
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
           \t10. Filter movies\n
           \t11. Create website"""


  def _get_user_input(self) -> int:
    """gets a number between 0 and 8 from user"""
    while True:

      try:
        user_input = self._validade_user_input()

        return user_input

      except ValueError as e:
        print(e)


  def _validade_user_input(self) -> int:
    """gets an input from user and changes its type to integer"""
    user_input = int(input("What do you want to do?(0-11): "))

    if 11 < user_input or user_input < 0:
      raise ValueError("Error! Input must be between 0 and 11.")

    return user_input


  def _continue_with_programm(self) -> None:
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
      print(self._menu_funktions()) # Done

      self._execute_programm_funktions()

      self._continue_with_programm()


    # Print menu
    # Get use command
    # Execute command