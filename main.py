#madlibs game!

print("Welcome to the mad libs game! Samurai, you better cyberpump yourself up for this game, its taken 7 years of hard work and glitchproccessing to make, wake the heck up samurai! ")

play = input("Are you ready to play? ")
#if they answer with some type of yes, then we will play, otherwise we won't
#set the entire string to lower case
play = play.lower()

# Check to see if: play is defined and the first letter is 'y'
while play and play[0] == 'y': 
  exclamation = input("Give me an exclamation: ")
  # If the exclamation is not defined or expclamation is not at all alphabet letters 
  if not exclamation or not exclamation.isalpha(): 
    continue
  adverb = input("Give me an adverb: ") 
  if not adverb or not adverb.isalpha(): 
    continue
  noun = input("Give me a noun: ")
  adjective = input("Give me an adjective: ")

  story = f"{exclamation}! he said {adverb} as he jumped into his super mega {noun} and flew into space getting ready to fight the final boss that plauged the world with it's {adjective} smell"

  print(story)   

  play = input("Would you like to play again? ")
  play = play.lower()


print("Thanks for p-p-p-p-playing! ")

