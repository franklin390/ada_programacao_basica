# Importando biblioteca sys para manipular informações do sistema.

import argparse

# Importando biblioteca para manipular dados do tipo data.

from datetime import date

# Criando parser para fazer a associação dos parâmetros e argumentos.

parser = argparse.ArgumentParser(description='Gerador de relatório de funcionários.')

# Definindo o argumento --nome como obrigatório (através do required = True).

parser.add_argument(
    '--nome',
    required=True,
    help='Nome do funcionário'
)

# Definindo o argumento --ano como um valor inteiro e opcional (com o padrão sendo o ano atual).

parser.add_argument(
    '--ano',
    type=int,
    default=date.today().year,
    help='Ano base para exportação do relatório'
)

# Definindo o argumento opção --incluir-ferias como um valor booleano.

parser.add_argument(
    '--incluir-ferias',
    action='store_true',
    dest='ferias',
    help='Se devemos levar em consideração o período de férias do funcionário'
)

# Aplicando o parse sobre os argumentos passados.

args = parser.parse_args()

# Imprimindo os resultados.

print('Nome:', args.nome)
print('Ano:', args.ano)
print('Férias?', 'Sim' if args.ferias else 'Não')