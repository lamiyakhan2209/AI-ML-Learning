secret_num = 56

while True:
    guess = int(input("Guess the secret number: "))
    if guess < secret_num:
        print("Too low!")
    elif guess > secret_num:
        print("Too high!")    
    else:
        print("correct !! u guessed the number.")
        break    