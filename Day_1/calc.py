first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

choices = ["add", "sub", "mul", "div"]

while True:
    print("Select a task: \n")
    for index, choice in enumerate(choices):
        print(f"{index + 1} : {choice}")

    range_value = f"1- {len(choices)}"

    try:
        selected_task = int(input(f"Enter a category number {range_value}: "))-1

        if selected_task in range(len(choices)):
            if selected_task == 0:
                print(first_num + second_num)
                break
            elif selected_task == 1:
                print(first_num - second_num)
                break
            elif selected_task == 2:
                print(first_num * second_num)
                break
            elif selected_task == 3:
                print(first_num / second_num)
                break
        else:
            print(f"Please enter a number within range {range_value}")
            break
    except ValueError:
        print("Enter a number ok..")