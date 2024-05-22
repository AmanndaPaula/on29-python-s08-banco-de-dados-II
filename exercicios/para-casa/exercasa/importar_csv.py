import csv

colunas = ['id', 'titulo', 'autor', 'ano', 'preco']  

livros = [
    ()

]

with open('./livros.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile, delimiter= ',')
    escritor.writerow(colunas)  # Escrever o cabeçalho
    escritor.writerows(livros)  # Escrever os dados
