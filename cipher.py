from random import randrange
from totiente import totiente
from primalityFermat import primalityFermat
from primalityMillerRabin import primalityMillerRabin
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod

def cipherMsg(lPrivate = False,nBits = 2):
	# Valor para a chave pública E
	nValueE = 0
	# Valor para a chave privada D
	nValueD = 0
	lLoc = False
	# Mensagem a ser criptografada
	cMsgToCipher = "Ola Mundo"
	cMsgTpDeciph = ""
	cLogMsg = ""
	aValues = totiente(nBits)
	aLetMsg = []
	# Valor para a chave pública N
	nValueN = aValues[0]
	# Valor para o Phi(N)
	nValuePhi = aValues[1]
	# Variável para retorno da Criptografia
	aRet = []

	# Adiciona valor de N para retorno
	aRet.append(nValueN)

	# Calcula um valor aleatório para E
	nValueE = randrange(3, nValuePhi )
	# Executa até localizar um número válido
	while ( not lLoc ):
		# Determina a primalidade do número
		while ( not primalityFermat( nValueE ) ):#while ( not primalityMillerRabin( nValueE ) ):
				# Caso seja divisor de 2 sabe-se que é par, logo busca
				# o próximo número ímpar em sequencia
				if( nValueE % 2 == 0):
					nValueE += 1
				else:
					nValueE += 2
		# Determina se Phi(N) e o número possem o máximo denominador comum de 1
		if (MDC( nValuePhi, nValueE) == 1):
			lLoc = True
		else:
			# Caso o Máximo denominador comum não seja 1, pula para o próximo número
			nValueE += 1

	# Busca o valor de D pelo Inverso Modular
	nValueD = MDCEst( nValueE, nValuePhi)

	# Adiciona valor de E para retorno
	aRet.append(nValueE)

	# Criptografa a Mensagem
	for cMsg in list(cMsgToCipher):
		nASCII = ord(cMsg) # Pega o valor de ASCII
		nValueCry = testMod(nASCII,nValueE,nValueN) # Executa a Potência Modular
		aLetMsg.append( nValueCry ) # Salva o valor criptografado
		# Adiciona para mostrar mensagem no console
		cSepar = ','
		if(cLogMsg==''):
			cSepar = ''

		cLogMsg += cSepar + str(nValueCry)

	# Adiciona valor da Mensagem para Retorno
	aRet.append(aLetMsg)

	# Caso seja para enviar a chave Privada
	if not lPrivate:
		#busca o valor congruente caso D seja negativo
		if nValueD < 0:
			nTemp = 1
			while nTemp % nValuePhi != nValueD % nValuePhi:
				nTemp += 1
			nValueD = nTemp
		# Descriptografa a mensagem
		for nMsg in aLetMsg:
			nValueCry = testMod(nMsg,nValueD,nValueN)# Executa a Potência Modular
			cMsgTpDeciph += chr(nValueCry)# Converte de ASCII

		#print( "===== Decipher: {} =====".format(cMsgTpDeciph))

	return aRet