from random import randint

numeroSecreto = randint(1, 100)
tentativas = 3

print(' ***************************\n Bem-Vindo ao Jogo do Acerto\n ***************************\n\n')

for rodada in range(1, tentativas+1):

	print('Tentativa %i de %i'%(rodada, tentativas))
	chute = int(input('Digite o seu número de chute: '))

	if (numeroSecreto == chute):
		print ('Voce acertou, miseraviii!!!')
		break
	else:
		if(chute > numeroSecreto):
			print('Você errou, o seu chute foi MAIOR que o número secreto!\n')
		elif(chute < numeroSecreto):
			print('Você errou, o seu chute foi MENOR que o número secreto!\n')
print('O número correto era %i'%(numeroSecreto))
print('*** FIM DO JOGO ***')