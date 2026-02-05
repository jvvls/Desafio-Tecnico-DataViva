def bracket_checker(words):
    stack = []
    pairs = {               # define um dicionario que pareia fechar e abrir pra cada simbolo
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in words:
        if char in pairs.values():          # se o simbolo atual esta nos valores do dict, coloca ele na pilha
            stack.append(char)

        elif char in pairs:                 # tira o ultimo simbolo da pilha e compara com o indice do dict para saber se esta executando a ordem desejada
            if stack.pop() != pairs[char]:              
                print("Inválido (ordem errada)")
                return

    if stack:
        print("Inválido (faltou fechar)")
    else:
        print("Válido")


def main():
    words = '{[()]}'
    bracket_checker(words)

main()