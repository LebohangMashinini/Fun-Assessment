def dog_years():
    pass
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    #enter your code here
    user_input = int(input("Enter your age: "))
    dog_year = 10.5 #human years
    dog_
    if user_input > 20:
        print("Enter a number 20 and below")
        return
    if user_input == 1:
        age_in_dog_years = dog_year * user_input
        print(f"Dog's age in dog's years {age_in_dog_years}")
        return
    if user_input == 2:
        age_in_dog_years = dog_year * user_input
        print(f"Dog's age in dog's years {age_in_dog_years}")
        return
    elif user_input >= 3:
        age_in_dog_years = user_input - 
dog_years()

def fizzbuzz(num):
    pass
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here

    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    split_sentence = sentence.split(" ")
    print(split_sentence)
    # sentence = {split_sentence}
    empty = {}
    for word in split_sentence:
        empty[word] = len(word)

    return empty

print(word_lengths("My favourite artist is Frank Ocean")
)
def cube_sum(number):
    pass
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here