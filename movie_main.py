from programm_modules import movie_Menu_actions as mma
from programm_modules import movie_storage as ms

OPERATIONS = {
  0: exit,  # ("bye")
  1: mma.list_up_movies,  # (movies),
  2: ms.add_movie,
  3: ms.delete_movie,
  4: ms.update_movie,
  5: mma.get_movie_stats,  # (movies)
  6: mma.print_random_movie,  # (movies)
  7: mma.search_movie,  # (movies),
  8: mma.print_movies_sorted_by_rating,  # (movies)
  9: mma.print_movies_sorted_by_year,  # (movies)
  10: mma.filter_movies  # (movies)
}


  def main():
    """gets movies form database and asks user for key(input).
    Than executes function out of dictionary(function is value of given key)
    """
    print("********** Welcome to my Movies Database **********")

    while True:
      movies = ms.get_movies()

      print_menu()

      funktion_key = get_user_input()
      execute_programm_funktions(funktion_key, movies)

      continue_with_programm()

  def execute_programm_funktions(funktion_key, movies):
      """Takes the funktion_key and validades wich case of funktion the key is rasing.

            Args:
                funktion_key (int): the command for a specific aktion of the programm
                movies(list): a list of dictionaries, with movie informations
        """

      # the exit() funktion, wich is taking "bye" as argument
      a_funktions = [0]
      # all funktions, which are taking 'movies' as an argument
      b_funktions = [1, 5, 6, 7, 8, 9, 10]
      # all funktions, wich don´t take an argument
      c_funktions = [2, 3, 4]

      if funktion_key in a_funktions:
        print(OPERATIONS[funktion_key]("bye"))
      elif funktion_key in b_funktions:
        print(OPERATIONS[funktion_key](movies))
      elif funktion_key in c_funktions:
        print(OPERATIONS[funktion_key]())


  def continue_with_programm():
    """get an empty string from user (by pressing Enter). If input is not empty, an Error is risen"""
    while True:
      try:
        continue_programm = input("press Enter to contiune")
        validade_programm_continuation(continue_programm)
        break
      except ValueError as e:
        print(e)


  def validade_programm_continuation(user_input):
    """validades if user_input is an empty string (len = 0). If not, an Error is risen"""
    if len(user_input) > 0:
      raise ValueError("Please press only Enter")


  def print_menu():
    """Displays the Menu to the user with the input commands"""
    print("\n===Menu:===\n"
          "\t0. Exit\n"
          "\t1. List movies\n"
          "\t2. Add moives\n"
          "\t3. Delete movie\n"
          "\t4. Update movie\n"
          "\t5. stats\n"
          "\t6. Random movie\n"
          "\t7. Search movie\n"
          "\t8. Movies sorted by rating\n"
          "\t9. Movies sorted by year\n"
          "\t10. Filter movies")


  def get_user_input():
    """gets a number between 0 and 8 from user
    If input is invalid, or out of range, an error is risen

    :return: user_input(a number between 1 - 8. Will be used, to choose a programm action)
    """
    while True:

      try:
        user_input = validade_user_input()
        return user_input

      except ValueError as e:
        print(e)


  def validade_user_input():
    """gets an input from user and changes its type to integer.
    If input out of range, or not valid(string), an ValueError is risen

    :return: user_input(0-8)
    """
    user_input = int(input("What do you want to do?(0-10): "))

    if 10 < user_input or user_input < 0:
      raise ValueError("Error! Input must be between 0 and 8.")

    return user_input


if __name__ == "__main__":
  main()