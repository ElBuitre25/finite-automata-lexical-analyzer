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

    current_state = 0

    for character in string:

        match current_state:
            case 0 if character == 't':
                current_state = 1

            case 1 if character == 'h':
                current_state = 2

            case 2 if character == 'e':
                current_state = 3

            case 3 if character == 'n':
                current_state = 4

            case 4 if character.isalnum():
                current_state = 4

            case _:
                return False

    if current_state == 4:
        return True
    else:
        return False









