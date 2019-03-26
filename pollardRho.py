from random import randrange
from totiente import totiente
from primalityFermat import primalityFermat
from primalityMillerRabin import primalityMillerRabin
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod
from cipher import cipherMsg
import math

def pollardRho(nBits):
	cMsgTpDeciph = ""
	aInfos = cipherMsg(True,nBits)# Busca a mensagem criptografada
	nValueN = aInfos[0]
	nValueE = aInfos[1]
	aLetMsg = aInfos[2]

	# busca o valor por heuristica
	nP = PollardRho( nValueN )
	nQ = nValueN // nP

	#Salva os valores para calcular o Phi(N)
	nPhiP = nP - 1
	nPhiQ = nQ - 1
	nValuePhi = nPhiP * nPhiQ
	nValueD = MDCEst( nValueE, nValuePhi)

	#busca o valor congruente caso D seja negativo
	if nValueD < 0:
		nValueD = nValueD % nValuePhi

	# Descriptograca a Mensagem
	for nMsg in aLetMsg:
		nValueCry = testMod(nMsg,nValueD,nValueN)# Executa a Potência Modular
		cMsgTpDeciph += chr(nValueCry)# Converte de ASCII

	print( "===== Decipher: {} =====".format(cMsgTpDeciph))


def PollardRho( nValueN ):

	# Caso valore de N seja 1 somente pode ser 1
	if nValueN == 1:
		nValueD = 1

	# Caso valore de N seja 2 somente pode ser 2
	if nValueN % 2 == 0:
		nValueD = 2
	else:
		# Busca dois valores Aleatórios
		nValueX = 2 + randrange( 0, nValueN - 2 )
		nValueY = nValueX
		nValueC = 1 + randrange( 0, nValueN - 1 )
		nValueD = 1
		# Executa enquanto o MDC dos valores aleatórizados com N for 1
		while nValueD == 1:
			# Executa a potência modular em 1 salto
			nValueX = ( ( nValueX ** 2 % nValueN ) + nValueC + nValueN ) % nValueN
			# Executa a potência modular em 2 saltos
			nValueY = ( ( nValueY ** 2 % nValueN ) + nValueC + nValueN ) % nValueN
			nValueY = ( ( nValueY ** 2 % nValueN ) + nValueC + nValueN ) % nValueN

			# Verifica se o Máximo Divisor Comum é maior que 1, caso seja encontrou o valor de D
			nValueD = MDC( abs( nValueX - nValueY ) , nValueN )
			# Se o valor de D for igual a N, executa novamente
			if nValueN == nValueD:
				return PollardRho( nValueN )
	return nValueD