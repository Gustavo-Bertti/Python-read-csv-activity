

from menu import Menu  # Importa a classe Menu do módulo menu.
from utils import open_path  # Importa a função open_path do módulo utils.
# Importação das funções necessárias para realizar comparações relacionadas a filmes

# Importa a função da primeira opção que calcula a taxa total de filmes
from modules.def_options_one.rate_full_movies_comparison import rate_calculeter_movies_total

# Importa a função da segunda opção que calcula a comparação de orçamentos entre filmes
from modules.def_options_two.comparison_budget import calculate_comparison_budget

# Importa a função da terceira opção que calcula a comparação de arrecadação bruta entre filmes
from modules.def_options_three.comparison_gross import calculate_comparison_gross

# Importa a função da quarta opção que filtra filmes com base nas avaliações
from modules.def_options_four.filter_movies_rate import filter_movies_rating

def main():  # Define a função principal do programa.
    # Solicita o caminho do arquivo como entrada do usuário
    file_path = input("Digite o caminho do arquivo: ")  # Solicita ao usuário que insira o caminho do arquivo.
    
    # Chama a função para abrir o arquivo no caminho especificado
    content = open_path(file_path)  # Abre o arquivo especificado pelo usuário e armazena o conteúdo.
    
    # Verifica se o conteúdo do arquivo é vazio, se sim, encerra o programa
    if not content:  # Se o conteúdo estiver vazio:
        return  # Encerra a função main e, consequentemente, o programa.

    while True:  # Inicia um loop infinito.
        try:  # Inicia um bloco de tratamento de exceção.
            # Solicita uma opção do usuário
            Menu()  # Chama a função Menu para exibir as opções.
            option = int(input("Digite uma das opções: "))  # Solicita ao usuário que digite uma opção e a converte para inteiro.

            if option == 1:  # Se a opção for 1:
                result = rate_calculeter_movies_total(content)
                print(result)

            elif option == 2:  # Se a opção for 2:
               result = calculate_comparison_budget(content)
               print(result)
            
            elif option == 3:  # Se a opção for 3:
               result = calculate_comparison_gross(content)
               print(result)

            elif option == 4:  # Se a opção for 4:
              result = filter_movies_rating(content)
              print(result)

            elif option == 0:  # Se a opção for 0 (encerrar):
                print("Fechando...")  # Imprime uma mensagem indicando que o programa está sendo fechado.
                break  # Sai do loop infinito, encerrando o programa.

            else:  # Se a opção não for nenhuma das anteriores:
                print("Digite uma das opções do menu")  # Informa ao usuário que a opção é inválida.

        except ValueError:  # Se ocorrer um erro de valor (entrada inválida):
            print("Não digitou uma opção válida, tente novamente")  # Informa ao usuário que a entrada é inválida.

# Chama a função main() para iniciar o programa
main()  # Chama a função principal para iniciar a execução do programa.
        
        
  




            
             