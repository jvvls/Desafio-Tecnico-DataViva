def invert_string(word):
    inverted_word = ""

    for char in word:
        inverted_word = char + inverted_word  # Pega o charactere atual e poe primeiro em um  novo string 

    return inverted_word

def palindromo_checker(word):
    return  word == invert_string(word)
    
def main():
    word = input("Insira palavra:")
    print(palindromo_checker(word))

main()