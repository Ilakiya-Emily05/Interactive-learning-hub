import random

while True:
    print("\nOptions:")
    print("1. Fun")
    print("2. Tests")
    print("3. Close the Program")

    option = input("Enter your option (1/2/3): ")

    if option == "1":
        while True:
            print("\nFun Options:")
            print("1. Rock, Paper, Scissors")
            print("2. Guess the number") 
            print("3. Go back to the main menu")

            sub_option = input("Enter your option (1/2/3): ")

            if sub_option == "1":
            
                print("Playing Rock, Paper, Scissors...")
                choices = ["rock", "paper", "scissors"]
                player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
                if player_choice not in choices:
                    print("Invalid choice. Please choose rock, paper, or scissors.")
                else:
                    computer_choice = random.choice(choices)
                    print(f"Your choice: {player_choice}")
                    print(f"Computer's choice: {computer_choice}")
                    if player_choice == computer_choice:
                        print("It's a tie!")
                    elif (
                        (player_choice == "rock" and computer_choice == "scissors") or
                        (player_choice == "paper" and computer_choice == "rock") or
                        (player_choice == "scissors" and computer_choice == "paper")
                    ):
                        print("Congratulations! You win!")
                    else:
                        print("Sorry, you lose. Try again!")

            elif sub_option == "2":
                print("Playing Guess the number...")
                random_number = random.randint(1, 10)
                max_tries = 4
                tries = 0

                while tries < max_tries:
                    guess = int(input("Enter your guess (between 1 and 10): "))
                    tries += 1

                    if guess > random_number:
                        print("Guess too high! Try again.")
                    elif guess < random_number:
                        print("Guess too low! Try again.")
                    else:
                        print(f"Congrats, you won in {tries} tries! ʕ•́ᴥ•̀ʔっ")
                        break
                else:
                    print(f"Sorry, you've run out of tries. The correct number was {random_number}. Better luck next time! (╥﹏╥)")

            elif sub_option == "3":
                break  # Go back to the main menu

            else:
                print("Invalid option. Please enter a valid option (1/2/3/4).")

    
    elif option == "2":
        while True:
            print("\nTest Options:")
            print("1. Maths test")
            print("2. English")
            print("3. General knowledge") 
            print("4. Go back to main menu")

            sub_option = input("Enter your option (1/2/3/4): ")

            if sub_option == "1":
                print("Taking Maths test...")
                a = int(input("1.What is the value of 3a + 1 = 10? Enter the value of 'a': "))
                
                if a == 3:
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is a = 3.")
                b = int(input("2.What is the answer of 5×(7−2)+8? Enter the answer: "))
                
                if b == 33:
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is 33.")
                c = int(input("3.If x=4 and y=2 what is the value of x**2-2y+5: "))
                
                if c == 17:
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is 17.")
                d = int(input("4.What is the sum of 17+25?: "))
                
                if d == 42:
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is 42.")
                e = int(input("5.What is the result of 48−19: "))
                
                if e == 29:
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is 29.")
                               
            elif sub_option == "2":
                print("Taking English test...")
                q = str(input("1.A group of fish is called?: "))
                
                if q.upper() == 'SCHOOL':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is SCHOOL.")
                r = str(input("2.Plural of Child?: "))
                
                if r.upper() == 'CHILDREN':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is CHILDREN.")
                s = str(input("3.Superlative form of GOOD?: "))
                
                if s.upper() == 'BEST':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is BEST.")
                t = str(input("4.Comparitive degree of BAD?: "))
                
                if t.upper() == 'WORSE':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is WORSE.")
                u = str(input("5.Use the correct collective noun 'A ---- of sailors'?: "))
                
                if u.upper() ==  'CREW':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is CREW.")
                
            elif sub_option == "3":
                print("Taking General knowledge test...")
                q = str(input("1.What is the capital city of France?: "))
                
                if q.upper() == 'PARIS':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is PARIS.")
                r = str(input("2.What is the largest planet in our solar system?: "))
                
                if r.upper() == 'JUPITER':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is JUPITER.")
                s = str(input("3.Which planet is known as the Red Planet?: "))
                
                if s.upper() == 'MARS':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is MARS.")
                t = str(input("4.What is the currency used in Japan?: "))
                
                if t.upper() == 'YEN':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is YEN.")
                u = str(input("5.How many continents are there on Earth?: "))
                
                if u.upper() ==  '7' or 'SEVEN':
                    print("Correct!")
                else:
                    print("Wrong, the correct answer is SEVEN.")
            elif sub_option == "4":
                break  # Go back to the main menu
            else:
                print("Invalid option. Please enter a valid option (1/2/3/4).")

    elif option == "3":
        print("Closing the program.")
        break

    else:
        print("Invalid option. Please enter a valid option (1/2/3).")
