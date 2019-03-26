RSA-Algorithm
=============

Encryption and Descryption example using RSA Algorithm in Python - Asymmetric

Simulate
=============
To simulate generation, run the file `main.py`.

The variables `nBits` and `nMedia` are responsible for the creation:
* nBits - Number of Bits for Encryption
* nMedia - Number of generations of each Bit

An **infosTime.dat** file containing the average runtime of each Decryption per Bit will be generated, according to the stipulated number of generations.

They were tested with an average of 20 bits.

The **Gross Force Decryption** method was used starting from 3 to the square root of the value of N.
It was also used the **Pollard Rho heuristic** to reduce the break time of the key.

With values less than 5 key bits, the Pollard Rho heuristic in few values was **not** effective.

For the primality test two heuristics were evaluated: **MillerRabin** and **Fermat**. Fermat's heuristics proved more effective.