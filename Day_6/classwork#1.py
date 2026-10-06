# use break statement to exit the loop when the value 20 is found in the list


my_list = [1, 2, 54, 32, 44, 56, 20, 65]
for number in my_list:
    print(number)

    if number == 20:
        print("20 found!")
        break


# use break statement to exit the loop if there is number greater than 30 in the list

list = [1,2,3,6,7,32,22,43]
for number in list:
    if number > 30:
        break
    else:
        print(list)


# use continue statements to skip the iteration if string can't be converted to int
# otherwise print the integer value of the string

strings = ["10", "20", "abc", "30", "xyz", "40"]
new_string = []
for string in strings:
    try:
        number = int(string)
        new_string.append(number)
    except ValueError:
        continue
print(new_string)



number = 100
count = 0
while count < 5:
    guess_number = int(input("Enter a number: "))
    if guess_number == number:
        print("Congrats! You guessed it right.")
        break
    elif guess_number > number:
        print("Dherai vayo")
    else:
        print("Alli thorai vayo")

    count += 1

if count == 5 and guess_number != number:
    print("Game over! The number was 100.")

            


