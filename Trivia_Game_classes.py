import random

class Questions:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def ask(self):
        print(f"Question: {self.prompt}")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

        try:
            user_answer = int(input("Choose an option (1-4): "))
            return self.options[user_answer - 1] == self.answer
        except (ValueError, IndexError):
            print("Invalid choice. Please select a number between 1 and 4.")
            return False

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

class TriviaGame:
    def __init__(self, player1_name, player2_name, questions):
        self.players = [Player(player1_name), Player(player2_name)]
        self.questions = questions

    def play(self):
        question_count = len(self.questions) // 2
        for i in range(2):
            print(f"\n{self.players[i].name}'s turn\n")
            for j in range(question_count):
                question = self.questions[i * question_count + j]
                if question.ask():
                    print("Correct!\n")
                    self.players[i].add_point()
                else:
                    print("Incorrect.\n")

    def show_results(self):
        print("\nGame Over!\n")
        for player in self.players:
            print(f"{player.name} scored: {player.score} points")

        if self.players[0].score > self.players[1].score:
            print(f"\n{self.players[0].name} wins!")
        elif self.players[1].score > self.players[0].score:
            print(f"\n{self.players[1].name} wins!")
        else:
            print("It's a tie!")

# List of questions
questions = [
    Questions("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"),
    Questions("Which planet is known as the Red Planet?", ["Venus", "Earth", "Mars", "Jupiter"], "Mars"),
    Questions("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
    Questions("Who wrote 'Hamlet'?", ["Shakespeare", "Hemingway", "Tolkien", "Rowling"], "Shakespeare"),
    Questions("What is the chemical symbol for water?", ["O2", "CO2", "H2O", "HO2"], "H2O"),
    Questions("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
    Questions("Which country is known as the Land of the Rising Sun?", ["China", "South Korea", "Japan", "Vietnam"], "Japan"),
    Questions("What is the currency of the United Kingdom?", ["Euro", "Dollar", "Pound", "Yen"], "Pound"),
    Questions("Which mammal is known to have the most powerful bite?", ["Lion", "Tiger", "Hippo", "Crocodile"], "Crocodile"),
    Questions("Who painted the Mona Lisa?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Van Gogh"], "Leonardo da Vinci"),
]


# Game setup
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")

# Shuffle questions to mix them up
random.shuffle(questions)

# Start the game
game = TriviaGame(player1_name, player2_name, questions)
game.play()
game.show_results()
