def rate_calculeter_movies_total(content):
    total_rate_marvel = 0  # Inicializa a variável para armazenar a soma das avaliações da Marvel.
    total_rate_dc = 0  # Inicializa a variável para armazenar a soma das avaliações da DC.
    cnm = 0  # Inicializa o contador para o número de filmes da Marvel.
    cndc = 0  # Inicializa o contador para o número de filmes da DC.

    for line in content[1:]:  # Para cada linha do conteúdo, exceto a primeira:
        columns = line.strip().split(",")  # Divide a linha em colunas usando ',' como separador.
        company = columns[2].strip('"')  # Obtém o nome da empresa da terceira coluna, removendo as aspas.

        if company == "Marvel":  # Se a empresa for "Marvel":
            rate = float(columns[3].strip('"'))  # Converte a avaliação para um número de ponto flutuante.
            total_rate_marvel += rate  # Adiciona a avaliação à soma total das avaliações da Marvel.
            cnm += 1  # Incrementa o contador de filmes da Marvel.
        else:  # Caso contrário (a empresa é DC):
            rate = float(columns[3].strip('"'))  # Converte a avaliação para um número de ponto flutuante.
            total_rate_dc += rate  # Adiciona a avaliação à soma total das avaliações da DC.
            cndc += 1  # Incrementa o contador de filmes da DC.

    rateMarvel = round(total_rate_marvel / cnm, 2)  # Calcula a média das avaliações da Marvel arredondada para 2 casas decimais.
    rateDC = round(total_rate_dc / cndc, 2)  # Calcula a média das avaliações da DC arredondada para 2 casas decimais.

    if rateMarvel > rateDC:  # Se a média da Marvel for maior que a média da DC:
        return (f"🔥 Marvel vence no requisito de avaliação!\nNota Marvel: {rateMarvel}\nNota DC: {rateDC}")  # Imprime uma mensagem indicando que a Marvel venceu.
    else:  # Caso contrário (a DC vence):
        return (f"🔥 DC vence no requisito de avaliação!\nNota Marvel: {rateMarvel}\nNota DC: {rateDC}")  # Imprime uma mensagem indicando que a DC venceu.
