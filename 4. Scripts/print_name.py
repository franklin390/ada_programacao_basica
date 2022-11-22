# Importando biblioteca sys para manipular informações do sistema.

import sys

# Definindo condição que só irá imprimir uma informação se ao menos um argumento for passado.
# Nota: sys.argv[0] = '.\print_name.py'.

if len(sys.argv) == 1:

    print("Por favor, informe o nome desejado")
    print("Exemplo: python", sys.argv[0], "nome")
    sys.exit(1)

# Imprime um Olá + string caso algum argumento seja passado.

print("Olá " + sys.argv[1])