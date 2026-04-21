def main():
   string=input("ingrese el string: ")
   print(automata1(string))



def automata1(string):

    # states 9 10 11
    current_state = 9
    
    
    for character in string:

        #focusing on caching with match the refusal cases,otherwise states proceed
        match current_state:
            case 9 if not character.isalpha():
                return False
            case 10 if character.isalnum():
                current_state = current_state
            case 11:
                return False
            case _:
                current_state+=1

    if current_state == 11:
        return True
    else:
        return False
    
            












def automata2(string):
    states = range(5)
    initial_state = 0
    




main()
