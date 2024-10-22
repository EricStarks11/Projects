#include <iostream>
#include <cstdlib>   // For srand() and rand()
#include <ctime>     // For time()

int main() {
    std::srand(static_cast<unsigned int>(std::time(0)));  // Seed the random number generator
    int randomNumber = std::rand() % 100 + 1;  // Generate random number between 1 and 100
    int guess = 0;
    int attempts = 0;

    std::cout << "Welcome to the Number Guessing Game!" << std::endl;
    std::cout << "I have selected a random number between 1 and 100." << std::endl;
    std::cout << "Can you guess it? Let's begin!" << std::endl;

    // Loop until the user guesses the correct number
    while (guess != randomNumber) {
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;

        if (guess > randomNumber) {
            std::cout << "Too high! Try again." << std::endl;
        } else if (guess < randomNumber) {
            std::cout << "Too low! Try again." << std::endl;
        } else {
            std::cout << "Congratulations! You guessed the number in " << attempts << " attempts." << std::endl;
        }
    }

    return 0;
}
