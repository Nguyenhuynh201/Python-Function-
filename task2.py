"""Create a multiplication function of two one-digit number"""
import random

def create_question():
    """Generate two random one-digit numbers, question, and answer"""
    digit_1 = random.randrange(10)
    digit_2 = random.randrange(10)

    return(f'How much is {digit_1} * {digit_2} ?', digit_1 * digit_2, digit_1, digit_2)

question, answer, digit_1, digit_2 = create_question() 
print(question)

guess = int(input('Enter your answer: '))

while guess != answer:
    guess = int(input(f"{digit_1} times {digit_2} is not {guess},please try again: " ))
   
if guess == answer:
    print("done")
    

