#Task 1:

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
    
print(grams_to_ounces(10))

#Task 2:

def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

print(fahrenheit_to_centigrade(64))

#Task 3:

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None

print(solve(35, 94))

#Task 4:

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#Task 5:

from itertools import permutations

def string_permutations(s):
    return [''.join(perm) for perm in permutations(s)]

print(string_permutations("abc"))

#Task 6:

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

print(reverse_sentence("We are ready"))

#Task 7:

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))

#Task 8:

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
            if not code:
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))

#Task 9:

def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * (radius ** 3)
    return volume

print(sphere_volume(5))

#Task 10:

def unique_elements(input_list):
    result = []
    for element in input_list:
        if element not in result:
            result.append(element)
    return result

print(unique_elements([1, 2, 2, 3, 4, 4]))

#Task 11:

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))

#Task 12:

def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])

#Task 13:
import random
class GuessTheNumberGame:
    def __init__(self):
        self.name = input("Hello! What is your name?\n")
        print(f"Well, {self.name}, I am thinking of a number between 1 and 20.")

    def play_game(self):
        number_to_guess = random.randrange(1, 20)
        guesses_taken = 0

        while True:
            guess = int(input("Take a guess.\n"))
            guesses_taken += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {self.name}! You guessed my number in {guesses_taken} guesses!")
                break
game = GuessTheNumberGame()
game.play_game()