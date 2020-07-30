import time, random
options_yes_or_no = 'Options:[Yes/No]'

# Room one function
def room_one():
  # Intro/narration
  narrate(f"{player_name} you will have to play Rock, Paper, Scissors and win three times to escape", 1.5)

  global wins
  global losses
  global draws
  wins = 0
  losses = 0
  draws = 0
  rock = 1
  paper = 2
  scissor = 3
  
  # While loop till you get three wins
  while wins < 3:
    # Player choice
    choice = input("Please, choose from Rock, Paper or Scissor (Case sensitive): ")
    # Computer choice
    computer = random.randint(1,3)
    # Win, Draw, Lose functions
    def win():
      print('You win')
      global wins
      # Append or update wins
      wins += 1
      print(f'Wins = {wins}, Losses = {losses}, Draws = {draws}')
      time.sleep(1.5)

    def lose():
      print('You lose')
      global losses
      # Append or update losses
      losses += 1
      print(f'Wins = {wins}, Losses = {losses}, Draws = {draws}')
      time.sleep(1.5)
  
    def draw():
      print('It\'s a draw')
      global draws
      # Append or update draws
      draws += 1
      print(f'Wins = {wins}, Losses = {losses}, Draws = {draws}')
      time.sleep(1.5)

    # If/else choices against computer 
    if choice == 'Rock' and computer == paper:
      lose()
    elif choice == 'Rock' and computer == scissor:
      win()
    elif choice == 'Rock' and computer == rock:
      draw()
    elif choice == 'Paper' and computer == paper:
      draw()
    elif choice == 'Paper' and computer == scissor:
      lose()
    elif choice == 'Paper' and computer == rock:
      win()
    elif choice == 'Scissor' and computer == paper:
      win()
    elif choice == 'Scissor' and computer == scissor:
      draw()
    elif choice == 'Scissor' and computer == rock:
      lose()
    else:
      narrate('Please, choose a valid option from Rock, Paper or Scissor (Case sensitive).', 2)

    # Break out of the loop when three wins
    if wins == 3:
      narrate("You have escaped with a bruised hand because of playing Rock, Paper, Scissor too much...", 1.5)
      break

# Room two function
def room_two():
  # Intro/narration
  narrate(f"{player_name} you will have to play Rock, Paper, Scissors and win three times to escape", 1.5)
  narrate("You enter the room Two and the door slams behind you!", 1.5)
  narrate("You try the handle of the door you just came through but it's already locked.", 1.5)
  narrate("The room in front of you appears bare aside from a table with different coloured liquids on it", 1.5)
  narrate("You walk towards the table and see a piece of paper.It reads:", 1.5)
  narrate("Of these 3 liquids, one is your end, one is the end, one has no end. Choose wisely.", 1.5)
  narrate("You look around the room for any hints as to which liquid is which.", 1.5)
  narrate("You see a CCTV camera in the corner of the room. You are being watched.", 1.5)
  narrate("You also see a rat trap on the floor, but no signs of a rat.", 1.5)
  narrate("Maybe these two objects could lead to clues. Which do you look at first? The camera or the rat trap?", 1.5)

  # rat_trap clue function
  def rat_trap():
    # Player input
    choice_rat_trap = input("Please choose from Rat Trap or CCTV ")
    # Outcomes base don player input 
    if choice_rat_trap == ("Rat Trap" or "rat trap" or "trap"):
      narrate("You still have three liquids on the table", 1.5)
      narrate("There must be more clues...", 1.5)
      narrate("You look at the table as it's the only other furniture in the room.", 1.5)
      narrate("Upon closer inspection you notice something carved into the underside of the table.", 1.5)
      narrate("1f you burn your bridges, how will you cross them?", 1.5)
      narrate("Was that a clue?", 1.5)
      narrate("There's one more liquid, surely that means there's one more clue.", 1.5)
      narrate("You look around in desperation", 1.5)
      narrate("ah! There's an air vent,hopefully there's a clue there.", 1.5)
      narrate("But it's all the way up at the top of the wall, how will you reach it?", 1.5)
    elif choice_rat_trap == ("CCTV" or "cctv" or "camera"):
      narrate("You see the camera and raise your middle finger to whoever orchestrated this sick game.", 1.5)
      narrate("Whoever is watching you is clearly not pleased with your act of defiance as gas starts to seep into the room.", 1)
      narrate("Unable to help yourself you breathe in the gas, getting dizzier and dizzier until you pass out.", 1.5)
      narrate("YOU MUST CHOOSE. NO CHOICE. NO ESCAPE.", 1.5)
      #Init back to input choice 1
      rat_trap()
    else:
      narrate("Invalid choice: Rat Trap or CCTV ?", 1.5)
      #Init back to input choice 1
      rat_trap()
  # Init rat_trap
  rat_trap()

  # table clue function
  def table():
    # Player input    
    choice_table = input("Move Table or Give Up ")
    # Outcomes base don player input  
    if choice_table == ("Move Table" or "move table" or "table"):
      narrate("Move the table to stand on", 1.5)
      narrate("While moving the table towards  the air vent, you\'re careful not to spill the liquids.", 1.5)
      narrate("Climbing up on the table you can see there are 3 slats in the air vent... does that even count as a clue?", 1.5)
    elif choice_table == ("Give Up" or "give up"):
      narrate(" ", 1.5)
      narrate("NO! YOU MUST CHOOSE. NO CHOICE. NO ESCAPE", 1.5)
      # Init back to input choice 2
      table()
    else:
      narrate("Invalid Choice: Move Table or Give Up", 1.5)
      # Init back to input choice 2
      table()
  # Init table function
  table()

  # Final clue function
  def final():
    # Player input  
    final_choice = int(input("You have all your clues now. (If you can call them clues) Which liquid will you choose? 1, 2, 3? "))
    # Outcome based on player decision
    if final_choice == 1:
      narrate("Clever you. You worked out that liquid one is an acid, if consumed it would have killed you but if you used it to dissolve the lock on the door it's your way out. Congratulations on earning your freedom.", 1.5)
    elif final_choice == 2:
      narrate("Rat Poison: All the signs were there you just didn't read them. You've swallowed the liquid down, now wait for your demise.", 1.5)
    elif final_choice == 3:
      narrate("You feel sleep creep over you. When you awake, you are left with only two liquids. You MUST choose.", 1.5)
      #Init back to final choices input
      final()
    else:
      narrate("You have three choices, what you just chose was not one of those. Try again you ill fated fool", 1.5)
      #Init back to final choices input
      final()
  # Init final function
  final()

# Room three function
def room_three():
  #arrays and variables used to put in the challenge.
  global count
  global count2
  count = 0
  count2 = 0
  room_three_roman_codes = ['MDCLXIV', 'MMDCCIV', 'MDCCCLIII'] 
  room_three_normal_codes = [1756, 2654, 1208]
  one756 = 'MDCCLVI'
  two654 = 'MMDCLIV'
  one208 = 'MCCVIII' 
  MDCLXIV = 1664
  MMDCCIV = 2704
  MDCCCLIII = 1858
  #Start of the game
  narrate('You open the door',1.5)
  narrate('See an empty room with a locked door with roman numerals displayed on top and a padlock on the left, a but "wait" there is a note in the middle of the room', 1.5)
  narrate('You go to grab the note...',1.5)
  narrate('When you hear a loud "SLAM!" you are Trapped!!!!',1.5)
  narrate('You open the note and read it',1.5)
  narrate('You have to translate from roman to normal numbers you have 3 attempst to enter the correct code into the padlock before the room starts to flood with water, if you fail you will only have time to have 2 more attempts',1.5)
  narrate('You walk towards the door and look at the Roman numeral', 1.5)
  #Ramdon numeral from the list is displayed as the challenge.
  random_number = random.randint(0,len(room_three_roman_codes) - 1 )
  #Function to loop the game when there is an incorrect answer in the first room
  def pin_one():
    print(f"the roman numeral is - {room_three_roman_codes[random_number]}")
    enter_pin_one = int(input('Please enter the code in normal numbers '))
    #if statements that checks if the answer is wright or wrong
    if MMDCCIV == enter_pin_one:
      narrate('Door opens',1.5)
      narrate('You enter another room with hungry wolves locked in cages and a door with normal numbers in displayed on top and a padlock on the left',2)
      narrate('You find a note on the floor',1.5)
      narrate('You open the note and read it',1.5)
      narrate('You have translate from normal to roman numerals you have 2 attempts to enter the correct code into the padlock before the cages open, and you will be eaten alive ;}',2)
      narrate('You walk towards the door and look at the Normal number', 1.5)
      print(f"the normal numeral is - {room_three_normal_codes[random_number]}")
      #Function to loop the game when there is an incorrect answer in the second room
      def room_three_b():
        enter_pin_two = input('Please enter the code in Roman numerals ')
        if enter_pin_two == one756:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == two654:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == one208:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        else:
          narrate('Incorrect',1.5)
          global count2
          count2 += 1
          if count2 == 2:
            narrate('You Lose, the cages open is Game over!!!',1.5)
            count2 = 0
          else:
            room_three_b()
      #Init back to room_three_b function    
      room_three_b()
    elif MDCLXIV == enter_pin_one:
      narrate('Door opens',1.5)
      narrate('You enter another room with hungry wolves locked in cages and a door with normal numbers in displayed on top and a padlock on the left',2)
      narrate('You find a note on the floor',1.5)
      narrate('You open the note and read it',1.5)
      narrate('You have translate from normal to roman numerals you have 2 attempts to enter the correct code into the padlock before the cages open, and you will be eaten alive ;}',2)
      narrate('You walk towards the door and look at the Normal number', 1.5)
      print(f"the normal numeral is - {room_three_normal_codes[random_number]}")
      def room_three_b():
        enter_pin_two = input('Please enter the code in Roman numerals ')
        if enter_pin_two == one756:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == two654:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == one208:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        else:
          narrate('Incorrect',1.5)
          global count2
          count2 += 1
          if count2 == 2:
            narrate('You Lose, the cages open is Game over!!!',1.5)
            count2 = 0
          else:
            room_three_b()
      room_three_b()
    elif MDCCCLIII == enter_pin_one:
      narrate('Door opens',1.5)
      narrate('You enter another room with hungry wolves locked in cages and a door with normal numbers in displayed on top and a padlock on the left',2)
      narrate('You find a note on the floor',1.5)
      narrate('You open the note and read it',1.5)
      narrate('You have translate from normal to roman numerals you have 2 attempts to enter the correct code into the padlock before the cages open, and you will be eaten alive ;}',2)
      narrate('You walk towards the door and look at the Normal number', 1.5)
      print(f"the normal numeral is - {room_three_normal_codes[random_number]}")
      def room_three_b():
        enter_pin_two = input('Please enter the code in Roman numerals ')
        if enter_pin_two == one756:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == two654:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        elif enter_pin_two == one208:
          narrate('Door opens',1.5)
          narrate('You won!! pass the mission you win £1,000,000 and get to leave in a brand new lamborghini Huracan Evo',1.5)
        else:
          narrate('Incorrect',1.5)
          #variable counter to count the amount of times you get the wrong asnwer
          global count2
          count2 += 1
          if count2 == 2:
            narrate('You Lose, the cages open is Game over!!!',1.5)
            count2 = 0
          else:
            room_three_b()
      room_three_b()
    else:
      narrate('Incorrect',1.5)
      global count
      count += 1
      if count == 3:
        narrate('The room starts flooding', 1.5)
        pin_one()
      elif count == 5:
        narrate('You drown, and wake up in Room 2', 1.5)
        count = 0
        room_two()
      else:
        pin_one()
  #Init back to pin_one function          
  pin_one()

# Room four function
def room_four():
  # Intro/narration
  narrate(f"Welcome {player_name}, You have chosen room 4",1.5)
  narrate("The room is empty except for the four different colour doors, one in each corner of the room.Now that you have entered you can not go back. The only way forward is through one of these doors. You must pick a door to enter through.",3)
  narrate("Only one of these doors will lead to freedom and safety. The rest.. won't! Choose wisely, your life depends on it.",3)
  # Player input
  player_input = input(f"Are you ready to choose which color door you want to enter through? {options_yes_or_no} ")
  # Make decision based on player input
  if player_input == "Yes":
    # Outcome based on player input 
    choose_color = input("Please choose which; Red door, Brown door, Black door or Grey door? ")
    if choose_color == "Red door": 
      narrate("You have entered through the Red door and the door is locked behind you. The Oxygen in the room is being replece with carbon monoxide. You'll be dead within minutes.",2)
    elif choose_color == "Brown door":
      narrate("You have entered through the Brown door and the door is locked behind you. The electronically controlled walls on either side of you are now moving inwards and you'll be dead within minutes.",2)
    elif choose_color == "Black door":
      narrate("You have entered through the Black door and the door is locked behind you. You must enter room 5 through the door infront of you.",2)
      room_five()
    elif choose_color == "Grey door":
      narrate("You have entered through the Grey door and the door is locked behind you. You now only have to go through the door infront of you and you'll be free. You have won your live back! Treasure it",1)
  elif player_input == "No":
    # Init back to room_four
      narrate(" You made the choice to enter room 4. You can't go back and the only way forward is through one of these doors.", 1.5)
      room_four()
    
# Room five function
def room_five():
  narrate(f'Well, well, well {player_name}, it seems you have made it to Room 5!', 3.5)
  narrate('You enter room 5: A dark room with white bright star-like dots.  The star-like dots then align and print the words.', 2)
  narrate('HERE YOU MUST DECIDE YOUR FATE  WILL YOU REMAIN TRAPPED FOR ETERNITY OR ESCAPE?', 3.5)
  narrate('The star-like dots starts to move again this time they seem to write a question', 3.5)
  narrate('Your late friend Michael Jackson released his Thriller album in what year?', 3.5)
  choose_number = input(f'Please choose from  1980, 1985, 1982, 1987 ')
  if choose_number == '1982': # If the player chooses the correct answer they procceed to the next question.
    narrate('Great! You’re closer to deciding your fate.', 1)
    narrate('You answered correctly, the dot start to spin around the room', 2.5)
    narrate('They disappear. All that is around you is darkness.', 2.5)
    narrate('Then a bright beam of light appears in the top right corner of the room', 2.5)
    narrate('Bright white dots start to jump out of the bright light', 2.5)
    narrate('This time they spell out', 1.5)
    answer = input(f'Was  your good friend Mr. John Proctor a faithful man? {options_yes_or_no} ')
    if answer == 'No':
     narrate('RUN FORREST RUN!! YOUR ESCAPE IS CLOSE!', 2.5)
     narrate('The dots spin around the room once more this time', 2.5)
     narrate('They spell out', 1.5)
     narrate('FINAL CHALLENGE', 1.5)
     meaning_life = input('What is the meaning of Life? ')
     print(f'Meaning of life is {meaning_life}!')# Here I added a simple reply showing whatever answer the player would give was correct, allowing them to escape the room.
    else:
     narrate('You must like it here, please restart room', 1.5)
     room_five()# This is the reply they would get if they got the SECOND question wrong.
  else:
    narrate('WRONG! The dots start to move again and repeat', 3.5)
    narrate('HERE YOU MUST DECIDE YOUR FATE  WILL YOU REMAIN TRAPPED FOR ETERNITY OR ESCAPE?', 1.5)
    room_five() # This is the reply the player would get if they got the FIRST question wrong.

# Naration function
def narrate(text,sec):
  print(text)
  return time.sleep(sec)

# Define the main game function
def init_game():
  # Intro to game
  narrate('Hello', 1.5)
  narrate('Hello', 1.5)
  accept_job_post = input(f'Are you ringing about the job posting at the mansion? {options_yes_or_no} ')
  if accept_job_post == 'Yes':
    time.sleep(1.5)
    global player_name
    player_name = input('Can I ask you your name? ')
    time.sleep(1.5)
    start_immediately = input(f'Brilliant, {player_name} can you start immediately? {options_yes_or_no} ')
    if start_immediately == 'Yes':
      narrate('Excellent, i\'ll see you soon.', 1.5)
      narrate('Well that was easy...', 1.5)
      narrate('You arrive at the mansion and knock on the door.', 1.5)
      narrate('Knock, Knock, Knock...', 1.5)
      narrate('You wait for a reply before knocking again.', 1.5)
      narrate('Knock, Knock, Knock...', 1.5)
      narrate('You hear footsteps approaching from behind the door and wait for the door to open.', 1.5)
      narrate(f'Hello, I\'m {player_name}, here for the caretaker position.', 1.5)
      narrate('You hear a *thunk* and suddenly the floor disappears underneath you and you fall through the air until you hit the ground and fall unconscious.', 3)
      # Player needs to choose room
      def choose_room():
        choose_room = input('When you awake you find your self in an empty room with five doors ahead of you, which one do you go through? [room_one, room_two, room_three, room_four, room_five] ')
        if choose_room == 'room_one':
          room_one()
        elif choose_room == 'room_two':
          room_two()
        elif choose_room == 'room_three':
          room_three()
        elif choose_room == 'room_four':
          room_four()
        elif choose_room == 'room_five':
          room_five()
        else:
          narrate('You need to select a valid room from [room_one, room_two, room_three, room_four, room_five] ', 2)
          # Needs to choose room so will be prompted again
          choose_room()
      choose_room()
    elif start_immediately == 'No':
      narrate('Too bad... You\'re going to have to start again anyway', 1.5)
      init_game()
    else:
      print(f'Please, enter from {options_yes_or_no}')

  elif accept_job_post == 'No':
    narrate('Not up to the challenge ey? Tough! You\'re just going to have to start again...', 1.5)
    init_game()
  else:
    print(f'The game will restart. Please, enter from {options_yes_or_no}')
    time.sleep(1)
    init_game()

# Init game
init_game()