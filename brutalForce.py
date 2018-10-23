from random import randrange
from totiente import totiente
from primalityFermat import primalityFermat
from primalityMillerRabin import primalityMillerRabin
from genericsFunctions import MDC
from genericsFunctions import MDCEst
from genericsFunctions import testMod
from cipher import cipherMsg
import math

def brutalForce(nBits):

	cMsgTpDeciph = ""
	aInfos = cipherMsg(True,nBits)# Busca a mensagem criptografada
	nValueN = aInfos[0]
	nValueE = aInfos[1]
	aLetMsg = aInfos[2]

	# Fatorar valor de nValueN com Teste de Primalidade Até a Raiz de N
	nP = 1
	nQ = 1
	nSqrt = math.sqrt(nValueN)
	nCnt = 3
	while nCnt <= nSqrt:
		# Caso valor encontrando seja um divisor exato, encontrou o primeiro valor
		if nValueN % nCnt == 0:
			nP = ( nValueN // nCnt )
			nQ = nCnt
			break
		nCnt += 2

	#Salva os valores para calcular o Phi(N)
	nPhiP = nP - 1
	nPhiQ = nQ - 1

	#seta o valor pego na força bruta
	nValuePhi = nPhiP * nPhiQ
	nValueD = MDCEst( nValueE, nValuePhi)

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

	print( "===== Decipher: {} =====".format(cMsgTpDeciph))