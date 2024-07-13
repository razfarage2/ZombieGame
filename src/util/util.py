# generic input

def generic_question(question,yes_answer='',no_answer=''):
    print(question)
    decision = input()
    if decision == 'y':
        print(yes_answer)
        return True
    elif decision == 'n':
        print(no_answer)
        return False
    else:
        print("please choose a valid input, y/n")
        generic_question(question)
