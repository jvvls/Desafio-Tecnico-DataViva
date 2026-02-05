import pandas as pd

def main():
    PATH = 'in.json'

    df = pd.read_json(PATH)

    result = df.groupby("categoria")["valor"].sum().to_dict() # mapeia categoria e valores da entrada somando os valores e transformando tudo em um dicionario
    print(result)

main()
