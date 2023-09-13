def filter_movies_rating(content):
    nota = int(input("Digite a nota desejada para filtrar os filmes:"))  # Solicita ao usuário que insira uma nota para filtragem.
    lista_de_filmes = []
    for line in content[1:]:  # Para cada linha do conteúdo, exceto a primeira:
        columns = line.strip().split(",")  # Divide a linha em colunas usando ',' como separador.
        name = columns[1].strip('"')  # Obtém o nome do filme da segunda coluna, removendo as aspas.
        rate = float(columns[3].strip('"'))  # Converte a avaliação para um número de ponto flutuante.
        if rate >= nota:  # Se a avaliação for maior ou igual à nota especificada:
            movie = (f"Filme: {name}, nota: {rate}") #  o nome do filme e sua avaliação 
            lista_de_filmes.append(movie)
    if lista_de_filmes: # Se a lista de filmes correspondentes não estiver vazia:
        return "\n".join(["=" * 30] + lista_de_filmes + ["=" * 30])
    else:
        return "Nenhum filme corresponde a nota especificada."