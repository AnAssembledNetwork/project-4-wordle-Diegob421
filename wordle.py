from random import choice
colors = {"green": "\033[0;92m","yellow": "\033[0;93m","red": "\033[0;31m","reset": "\033[0m"}

def choose_word(filename):
  global word
  global word_list
  word_list = []
  with open(filename) as file:
    lines = file.readlines()

  for line in lines:
    word_list.append(line[:-1])
  word = choice(word_list)
  

            
def player_guess():
  count = 0
  guesses = []
  while(count < 6):
    guess = input("Please enter your 5 letter guess: ").lower()
    while guess not in word_list or len(guess) != 5:
      if guess not in word_list:
        guess = input("Error please enter a valid word: ").lower()
      elif len(guess) != 5:
        guess = input("Error please enter a 5 letter word: ").lower()
    count += 1
    print(f"Amount of Guesses: {count}")
    color_guess = process_guess(guess)
    guesses.append(color_guess)
    for g in guesses:
      print(g)
    if(guess == word) and count < 6: 
      print("Good Job!!")
      break
    elif guess != word and count >= 6:
      print(f"Game Over The Word Was {word.capitalize()}")
      break

def kbLine(line):
  line1 = ""
  for letter in line:

    if(letter != " "):
      if letter in green:
        line1 += colors["green"] + letter + colors["reset"]
      elif letter in yellow:
        line1 += colors["yellow"] + letter + colors["reset"]
      elif letter in red:
        line1 += colors["red"] + letter + colors["reset"]
      else: line1+= letter
    else:
      line1+=letter
  return line1

def kb():
  # alph = "abcdefghijklmnopqrstuvwxyz"
  kb_row1 = "q w e r t y u i o p"
  kb_row2 = " a s d f g h j k l"
  kb_row3 = "  z x c v b n m"
  line1_returning = kbLine(kb_row1)
  line2_returning = kbLine(kb_row2)
  line3_returning = kbLine(kb_row3)
  # print(red)
  # print(green)
  # print(yellow)
  print(line1_returning)
  print(line2_returning)
  print(line3_returning)
      
# if gyess[index] in word

def process_guess(guess):
  clue = ""
  global red
  global green
  global yellow
  red = ""
  green = ""
  yellow = ""
  for index in range(0, len(guess)):
    if guess[index] == word[index]:
      letter = colors["green"] + guess[index] + colors["reset"]
      clue += letter
      green+= guess[index]
    elif word.__contains__(guess[index]):
      letter = colors["yellow"] + guess[index] + colors["reset"]
      clue += letter
      yellow+=guess[index]
    elif guess[index] not in word:
      letter = colors["red"] + guess[index] + colors["reset"]
      clue += letter
      red+=guess[index]
    else: clue+=guess[index]
  kb()
  return clue

def new_game():
  play_again = input("\n\n\nDo you want to start a new game? (Y/N) ")
  play_again_ans = play_again.upper()
  if play_again_ans == "N":
    print("Thanks for playing!")
  else: 
    print()
    print()
    main()

def wordle():
  print("WELCOME TO MY WORDLE")
  choose_word("words.txt")
  # print(word.capitalize())
  player_guess()
  new_game()
  # kb()
  
##################DO NOT EDIT BELOW THIS LINE################
def main():
  wordle()
if __name__ == "__main__":
  main()