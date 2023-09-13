def calculate_comparison_gross(content):
    total_gross_marvel = 0  # Inicializa a variável para armazenar o somatório do faturamento da Marvel.
    total_gross_dc = 0  # Inicializa a variável para armazenar o somatório do faturamento da DC.
    for line in content[1:]:  # Para cada linha do conteúdo, exceto a primeira:
        columns = line.strip().split(",")  # Divide a linha em colunas usando ',' como separador.
        company = columns[2].strip('"')  # Obtém o nome da empresa da terceira coluna, removendo as aspas.

        if company == "Marvel":  # Se a empresa for "Marvel":
            gross = float(columns[10].strip('"'))  # Converte o valor do faturamento para um número de ponto flutuante.
            total_gross_marvel += gross  # Adiciona o valor do faturamento ao somatório da Marvel.
        else:  # Caso contrário (a empresa é DC):
            gross = float(columns[10].strip('"'))  # Converte o valor do faturamento para um número de ponto flutuante.
            total_gross_dc += gross  # Adiciona o valor do faturamento ao somatório da DC.

    if total_gross_marvel > total_gross_dc:  # Se o somatório do faturamento da Marvel for maior que o da DC:
        difference = total_gross_marvel - total_gross_dc  # Calcula a diferença entre os faturamentos.
        return (f"💸 Marvel vence no requisito de faturamento, com uma vantagem de US${difference:.2f} sobre a DC!")  # Imprime a mensagem indicando que a Marvel venceu.
    else:  # Caso contrário (a DC vence):
        difference = total_gross_dc - total_gross_marvel  # Calcula a diferença entre os faturamentos.
        return (f"💸 DC vence no requisito de faturamento, com uma vantagem de US${difference:.2f} sobre a Marvel!")  # Imprime a mensagem indicando que a DC venceu.