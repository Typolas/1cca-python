#operadores de atribuição
from sqlalchemy.sql.operators import truediv

num = 15
print(num)

num = num +2
print(num)

num += 2
print(num)


#operadores relacionais
print()
print(6 != 2)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)


#operador lógico
#lógica e (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("po.. foi hackeado")


