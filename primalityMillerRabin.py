from random import randrange
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod

def primalityMillerRabin( nParamTest ):
	nTrial = 1
	nNumTrial = 20
	nNumTest = nParamTest

	# Casos distintos, valida as casos bases
	if nParamTest == 3:
		return True
	if nParamTest == 5:
		return True
	if nParamTest == 7:
		return True

	if nParamTest <= 10:
		return False

	# Reduz d até um número ímpar
	nReduct = nParamTest - 1
	while ( nReduct % 2 == 0):
		nReduct = nReduct // 2

	# Executa o teste a quantidade de vezes definida
	while nTrial <= nNumTrial:
		nTrial += 1
		if not millerRabinTest(nReduct,nParamTest):
			return False
	return True

def millerRabinTest(nReduct,nParamTest):

	nAleatory = randrange(2, nParamTest - 4 )# Busca um número aleatório entre 2 e o Valor - 4

	nPow = testMod(nAleatory,nReduct,nParamTest)# Executa a potência modular

	# Caso a potência modular for 1 ou o valor - 1 indica que é primo
	if (nPow == 1 or nPow == nParamTest - 1):
		return True

	# Caso não seja, reduz até encontrar o valor
	while ( nReduct != ( nParamTest - 1 ) ):
		nPow = nPow * nPow % nParamTest
		nReduct = nReduct * 2

		if (nPow == 1):
			return False

		if (nPow == ( nParamTest - 1 ) ):
			return True