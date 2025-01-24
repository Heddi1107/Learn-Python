from os import system
from time import sleep


# Variáveis

roxo = '\033[0;49;35m'
amarelo = '\033[0;49;33m'
azul = '\033[0;49;34m'
ciano = '\033[0;49;36m'
verde = '\033[0;49;32m'


# Código

system('cls')

print(f'Bem vindo ao {roxo}Learn {amarelo}Py{azul}thon\033[m!')

sleep(0.6)

print(f'''
{verde}Comandos Disponíveis:\033[m

{amarelo}print()\033[m - Mostra a informação desejada na tela;
{ciano}caixa_de_entrada\033[m = {amarelo}input()\033[m - Uma caixa de entrada de texto na tela;
{amarelo}exit()\033[m: Fecha a tela do programa;
{roxo}if\033[m: - Usado para determinar algo com base na informaçãos de variáveis, funciona como condição;
{roxo}else\033[m: - Usado para determinar o que acontecerá se a condição do '{roxo}if\033[m' não for seguida;
{roxo}elif\033[m: - Cria uma condição adicional;
{roxo}while\033[m: - Determina o que acontecerá enquanto uma condição for seguida, funcionando continuamente, não só de uma vez;
{amarelo}Variáveis\033[m - Itens que podem armazenar valores ou informações desejadas;
{azul}def\033[m ({azul}Funções\033[m) - Usado normalmente para facilitar a repetição dos mesmos comandos, permitindo que somente uma palavra 
seja entendida como os comandos desejados, assim, economizando tempo e linhas;
{verde}Criação de {amarelo}variáveis{verde}:\033[m {ciano}nome_da_variável\033[m = {amarelo}valor da variável\033[m;
{verde}Criação de {azul}Funções{verde}:\033[m {azul}def {amarelo}nome_da_função()\033[m:;
{verde}Tipos de {amarelo}variáveis{verde}:\033[m {verde}string\033[m({verde}str\033[m) - De palavras (''), {verde}inteiro\033[m({verde}int\033[m) - De números inteiros, {verde}float\033[m({verde}float\033[m) - De números negativos, flutuantes, etc... ,
{verde}booleana\033[m({verde}bool\033[m) - De {azul}True\033[m({azul}Verdadeiro\033[m) e {azul}False\033[m({azul}Falso\033[m);
''')