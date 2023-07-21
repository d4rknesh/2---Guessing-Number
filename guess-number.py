import random , os , time

def check_standard(user_input , text , extend_condition_number = 1_000_000_000):
    while (not user_input.isdigit()) or int(user_input) < 1 or int(user_input) > extend_condition_number :
        os.system("cls")
        
        if int(user_input) > extend_condition_number :
            print(f'your input : {user_input} -> is greater than {extend_condition_number}\nplease enter another input')
        else :
            print(f'your input : {user_input} -> is not number or is not more than 1 !\nplease enter another input\n')

        user_input  = input(f'{text}')
    return int(user_input)

def get_number():
    os.system("cls")
    
    text = "please enter a number to define \nlength of numbers that computer picks: "
    range_of_number = input(text)
    range_of_number = check_standard(range_of_number , text )

    os.system("cls")
    
    text = "now enter how many times \nyou want to guess ?:"
    guess_times = input(text)
    guess_times = check_standard(guess_times , text)

    return (range_of_number , guess_times)  


def main_game(range_number , times_to_try) :
    # picking a rangom number :
    # goal_number = random.choice(list(range(1 , range_number+1)))
    #! random.choice(list) / random.randrage(min , max)
    goal_number = random.randrange(1 , range_number+1)
    #for loop :
    for i in range(1 ,times_to_try+1) :
        os.system("cls")
        print(f'{times_to_try-i+1} times left ! ')
        
        guess = input(f"Enter your guess (1-{range_number}): ")
        text = 'your input : {guess} -> is not number or is not more than 1 !\nplease enter another input\n'
        guess =check_standard (guess , text , extend_condition_number = range_number  )

        if guess == goal_number  :
            print('You Won !')
            return
        print("Not Correct !\ntry again !")
        time.sleep(1)
                 
    print("mabye you can guess it right for the next time !")        


if __name__ == "__main__":
    (rng , gst) = get_number()
    main_game(rng , gst)
