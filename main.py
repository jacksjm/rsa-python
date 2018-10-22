from cipher import cipherMsg
from primalityFermat import primalityFermat
from primalityMillerRabin import primalityMillerRabin
from brutalForce import brutalForce
from pollardRho import pollardRho
from datetime import datetime
import time
arq = open('infosTime.dat','w')
nBits = 16
nTmpBit = 3
nMedia = 20

while nTmpBit < nBits:
	nTmpBit += 1
	arq.write('{} BITS'.format(nTmpBit))
	arq.write('\t')
	nTest = 0
	diffBrutal = 0
	diffPollard = 0
	while nTest < nMedia:
		#Calcula Força Bruta
		date1 = datetime.now()
		brutalForce(nTmpBit)
		date2 = datetime.now()
		if nTest == 0:
			diffBrutal = date2-date1
		else:
			diffBrutal = diffBrutal + date2-date1

		#Calcula PollardRho
		date1 = datetime.now()
		pollardRho(nTmpBit)
		date2 = datetime.now()
		if nTest == 0:
			diffPollard = date2-date1
		else:
			diffPollard = diffPollard + date2-date1
		nTest = nTest + 1

	arq.write(str(diffBrutal.total_seconds() / nMedia ))
	arq.write('\t')
	arq.write(str(diffPollard.total_seconds() / nMedia ))
	arq.write('\n')
	print("{} BITS gerado".format(nTmpBit))
arq.close()





