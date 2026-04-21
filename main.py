def main():
   #Palabras reservadas 


    string=input("ingrese el string: ")

    if automata1(string):
        if automata2(string):
           print("Es una palabra clave")
        else:
            print(f"Es una variable: {string[:-1]}")
    else: 
        print("La cadena no es valida")



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
    #print("implement here automata2")
    return False
    




main()
