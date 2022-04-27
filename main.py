print('Qual seu nome?')
nome = input()

if nome.isupper():
    print(nome.title())

elif nome.islower():
    print(nome.title())

else:
    print(nome.title())

print('Em qual cidade você está residindo no momento?')
residencia = input()

print('Em qual empresa você está prestando serviço atualmente?')
empresa = input()

if empresa.islower():
    print(empresa.title())

elif empresa.isupper():
    print(empresa.upper())

else:
    print(empresa.title())

print('Em qual cidade você está trabalhando atualmente?')
cidade = input()

print('Qual seu salário?')
salario = input()
salario = int(salario)

print('Valor de Horas extras:')
extra = input()
extra = int(extra)

print('Quanto é seu gasto com despesas?')
gastos = input()
gastos = int(gastos)

print('Paga alguma mensalidade?')
reposta = input()
if 'Sim' in reposta:
    print('Quais o valores de suas mensalidades?')
    mensalidades = input()
    mensalidades = int(mensalidades)
else:
    print('Sem custo de mensalidades.')
    mensalidades = 0

print('Qual o valor da sua conta de água?')
agua = input()
agua = int(agua)

print('Qual o valor da sua conta de energia?')
energia = input()
energia = int(energia)

inss = (salario+extra)*0.1
vt = (salario+extra)*0.06
imposto = (inss+vt+agua+energia)
custoextra = (gastos+mensalidades)
liquido = (salario+extra) - (imposto+custoextra)

print('Prazer em te conhecer', nome.title())
print('Você reside no município de', residencia.title())
print('Você trabalha na empresa', empresa.title())

print('Você trabalha na cidade', cidade.title())
if residencia.title() == cidade.title():
    vt = 0
    print('Você não utiliza vale transporte, visto que reside e trabalha em', residencia.title())
else:
    vt = (salario + extra) * 0.06
    print('O vale transporte tem valor de: %.2f' % vt)

print('O valor do seu INSS é: %.2f' % inss)
print('Seu salário líquido equivale a: %.2f' % liquido)
if liquido > 1000:
    print('Não necessita de aumento!')

else:
    print('Necessita de aumento!')
