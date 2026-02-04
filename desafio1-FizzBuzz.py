def fizzbuzz_check(num):
    fizz_value = 3 # Define os valores como variáveis para ser possível alterar o valor sem afetar o código
    buzz_value = 5
    fizzbuzz_value = fizz_value * buzz_value  # Um valor multiplo de 3 e 5 ao mesmo tempo pode ser obtido como 3*5=15 diminuindo a complexidade da leitura do if

    if num % fizzbuzz_value  == 0: 
        return f"{num}: FizzBuzz"
    
    if num % fizz_value == 0:
        return f"{num}: Fizz"
    
    if num % buzz_value == 0:
        return f"{num}: Buzz"

    return num   

def main():
    for num in range(1, 101): 
        print(fizzbuzz_check(num))

main()
