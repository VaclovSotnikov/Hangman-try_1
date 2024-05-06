import random

class Hangman():
    def __init__(self):
        print("Welcome to 'Hangman', are you ready to die?")
        print("(1) Yes, for I am already dead.\n(2) No, get me outta here!")
        user_choice_1 = input("->")
        
        if user_choice_1 == '1':
            print("Loading nooses, murderers, rapists, thieves, lunatics...")
            self.start_game()
        elif user_choice_1 == '2':
            print("Bye bye now...")
            exit()
        else:
            print("I'm sorry, I'm hard of hearing, could you repeat that?")
            self.__init__()

    def start_game(self):
        text = ''' 
        A crowd begins to gather, they can't wait to see some real
        justice. There's just one thing, you aren't a real criminal.
        No, no. You're the wrong time, wrong place type. You may think
        you're dead, but it's not like that at all. Yes, yes. You've
        got a chance to live. All you've gotta do is guess the right
        words and you can live to see another day. But don't get so
        happy yet. If you make 6 wrong guess, YOU'RE TOAST! BAMANOS!
        '''
        print(text)
        self.core_game()

    def core_game(self):
        lives = 6 
        total_tries = 10 
        letters_used = ""
        word_list = ['noiseless', 'inform', 'toothbrush', 'mark', 'insurance', 'disappear', 'fang', 'help', 'open', 'division']
        the_word = random.choice(word_list)
        progress = ["?" for _ in range(len(the_word))]
        
        while lives > 0 and total_tries > 0: 
            guess = input("Guess a letter ->")
            total_tries -= 1 
            
            if guess in the_word and guess not in letters_used:
                print("As it turns out, your guess was RIGHT!")
                letters_used += "," + guess
                lives -= 1
                updated_progress = self.progress_updater(guess, the_word, progress)
                print("Progress: " + updated_progress)
                print("Letters used: " + letters_used)
                if "".join(updated_progress).strip() == the_word:
                    print("Congratulations! You've guessed the word correctly!")
                    self.restart_game()
                    return
            elif guess not in the_word and guess not in letters_used:
                lives -= 1
                print("Things aren't looking so good, that guess was WRONG!") 
                print("You have", lives, "lives left.")
                letters_used += "," + guess
                self.hangman_graphic(6 - lives)
                print("Progress: " + "".join(progress))
                print("Letters used: " + letters_used)
            else:
                print("That's the wrong letter, you wanna be out here all day?")
                print("Try again!")
            
        print("You've made too many wrong guesses! Game over.")
        self.restart_game()

    def hangman_graphic(self, lives):
        if lives == 0:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif lives == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif lives == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif lives == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif lives == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif lives == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("The noose tightens around your neck, and you feel the")
            print("sudden urge to urinate.")
            print("GAME OVER!")
            self.restart_game()

    def progress_updater(self, guess, the_word, progress):
        for i in range(len(the_word)):
            if guess == the_word[i]:
                progress[i] = guess
        return "".join(progress)

    def restart_game(self):
        print("Would you like to play again?")
        print("(1) Yes\n(2) No")
        user_choice = input("-> ")
        
        if user_choice == '1':
            self.start_game()
        elif user_choice == '2':
            print("Bye bye now...")
            exit()
        else:
            print("I'm sorry, I didn't get that. Let's try again.")
            self.restart_game()

game = Hangman()
        