from random import randrange
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod

def primalityFermat( nParamTest ):
	nTrial = 1
	nNumTrial = 20 # Seta a quantidade de tentativas em 20
	nNumTest = nParamTest

	if nNumTest != 1:
		while nTrial <= nNumTrial:
			nTrial += 1
			# Gera um número aleatório de  1 até nNumTest - 1
			nNumRand = randrange(1, nNumTest )

			# Avalia se o numero possui outro máximo denominador comum
			# que não 1, caso tenha não é primo
			if (MDC(nNumRand,nNumTest) != 1):
				return False

			# Avalia pelo Teste de Fermat se o número é composto
			nTest = testMod(nNumRand,(nNumTest - 1),nNumTest)
			if ( nTest != 1):
				return False
	return True
