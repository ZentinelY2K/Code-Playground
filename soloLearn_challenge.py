#installed games
games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

#taking player's choice as a number input
choice = int(input("Please provide a number:\n"))
x = choice

#output the corresponding game
def user_input_to_list():
  global choice,x
  print(f"{games[x]}")
  return()
user_input_to_list()
  