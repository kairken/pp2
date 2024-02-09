#ex.1
def convert(grams):
  print(28.3495231 * grams)
convert()

#ex.2
def temperature(F):
  print((5 / 9) * (F - 32))
temperature()

#ex.3
def solve(numheads,numlegs):
    for chickens in range (numheads+1):
      rabbits=numheads-chickens
      legs = 2 * chickens + 4 * rabbits
      if alllegs==numlegs:
        print(chickens,rabbits)
solve(35,94)

#ex.4
def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):  
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    print(prime_numbers)
filter_prime()

#ex.5
from itertools import permutations

def print_permutations(input_string):
    perm1 = permutations(input_string)
    for perm2 in perm1:
        print(''.join(perm2))

input_string = "123" 
print_permutations(input_string)

#ex.6
def r_words(sentence):
    words = sentence.split()
    r_sentence = ' '.join(reversed(words)) 
    return r_sentence

user_input = input("your sentence:")
result = r_words(user_input)
print("reversed:", result)


#ex.7
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
user_input = input("enter numbers separated by space")
nums_list = list(map(int, user_input.split()))
print(has_33(nums_list))

#ex.8
def spy(nums):
    for num in nums:
        if num == 0:
            for next_num in nums[nums.index(num)+1:]:
                if next_num == 0:
                    for last_num in nums[nums.index(next_num)+1:]:
                        if last_num == 7:
                            return True
    return False
user_input = input("enter numbers separated by space")
user_list = [int(x) for x in user_input.split()]
result = spy(user_list)
print(result)

#ex.9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    print(volume)
sphere_volume()

#ex.10
def unique_elements(input_list):
    unique_list=[]
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
    
user_input = input("enter numbers separated by space ")
user_list = [int(x) for x in user_input.split()]
result = unique_elements(user_list)
print("your list", user_list)
print("list with unique elements:", result)

#ex.11
def palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]
user_input = input("your word or phrase")
result = palindrome(user_input)
print(result)

#ex.12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])

#ex.13
import random 
def guess_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess")
        guess = int(input())
        guesses_taken +=1
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break        
guess_number() 
