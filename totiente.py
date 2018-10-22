from random import randrange
from primalityFermat import primalityFermat
from primalityMillerRabin import primalityMillerRabin
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod

def totiente(nBits = 7):
	aValues = []

	#Executa o Random para buscar os números entre o limite
	nP = randrange(2**(nBits-1), 2**nBits)
	nQ = randrange(2**(nBits-1), 2**nBits)

	#Determina a primalidade do número
	while ( not primalityFermat( nP ) ):#while ( not primalityMillerRabin( nP ) ):
		# Caso seja divisor de 2 sabe-se que é par, logo busca
		# o próximo número ímpar em sequencia
		if ( nP % 2 == 0 ):
			nP += 1
		else:
			nP += 2

	#Determina a primalidade do número
	while ( not primalityFermat( nQ ) ):#while ( not primalityMillerRabin( nQ ) ):
		# Caso seja divisor de 2 sabe-se que é par, logo busca
		# o próximo número ímpar em sequencia
		if ( nQ % 2 == 0 ):
			nQ += 1
		else:
			nQ += 2
		#caso seja o mesmo número, pula para o próximo ímpar
		if nP == nQ:
			nQ += 2

	#Calcula os valore de Phi
	nPhiP = nP - 1
	nPhiQ = nQ - 1

	#Salva os valores de N e Phi(N) para retorno
	aValues.append( nP * nQ )
	aValues.append( nPhiP * nPhiQ )

	return aValues