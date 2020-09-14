def eval_loop():
    result = 0
    while True:
        user_input = input("What would you like to evaluate? (type 'done' when finished)\n")
        if user_input == "done":
            break
        else:
            try:
                print(eval(user_input))
                result = eval(user_input)
            except NameError:
                print("Sorry, I can't evaluate that")
    return result
print(eval_loop())