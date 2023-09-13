def calculate_comparison_budget(content):
    total_bud_marvel = 0  # Inicializa a variável para armazenar o somatório dos orçamentos da Marvel.
    total_bud_dc = 0  # Inicializa a variável para armazenar o somatório dos orçamentos da DC.

    for line in content[1:]:  # Para cada linha do conteúdo, exceto a primeira:
        columns = line.strip().split(",")  # Divide a linha em colunas usando ',' como separador.
        company = columns[2].strip('"')  # Obtém o nome da empresa da terceira coluna, removendo as aspas.

        if company == "Marvel":  # Se a empresa for "Marvel":
            bud = float(columns[7].strip('"'))  # Converte o valor do orçamento para um número de ponto flutuante.
            total_bud_marvel += bud  # Adiciona o valor do orçamento ao somatório da Marvel.
        else:  # Caso contrário (a empresa é DC):
            bud = float(columns[7].strip('"'))  # Converte o valor do orçamento para um número de ponto flutuante.
            total_bud_dc += bud  # Adiciona o valor do orçamento ao somatório da DC.

    if total_bud_marvel > total_bud_dc:  # Se o somatório dos orçamentos da Marvel for maior que o da DC:
        difference = total_bud_marvel - total_bud_dc  # Calcula a diferença entre os orçamentos.
        return(f"💰 Marvel vence no requisito de orçamento, com uma vantagem de US${difference:.2f} sobre a DC!")  # Imprime a mensagem indicando que a Marvel venceu.
    else:  # Caso contrário (a DC vence):
        difference = total_bud_dc - total_bud_marvel  # Calcula a diferença entre os orçamentos.
        return(f"💰 DC vence no requisito de orçamento, com uma vantagem de US${difference:.2f} sobre a Marvel!")  # Imprime a mensagem indicando que a DC venceu.