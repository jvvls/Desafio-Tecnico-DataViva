def duplicate_check(numbers):
    seen = set()    
    duplicates = set()

    for number in numbers:  
        if number in seen:                  # Itera cada valor e ve se ja foi visto antes, se sim salva na lista de duplicados se não marca como visto
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates) 

    

        
def main():
    numbers = [1,2,3,4,2,5]
    print(f"{duplicate_check(numbers)}")


main()