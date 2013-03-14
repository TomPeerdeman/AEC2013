import random;

def egcd(a, b):
	if b == 0:
		return (a, 1, 0);
	else:
		r = a % b;
		q = (a - r) / b;
		(d, k, l) = egcd(b, r);
		return (d, l, k - l*q);
		
def calcKeys(phi):
	while(True):
		e = random.getrandbits(16) + 1;
		(div, x, y) = egcd(e, phi);
		if div == 1 and x > 0:
			return (e, x);	
			
def strToInt(str):
	num = 0;
	for s in str:
		num |= ord(s);
		num <<= 8;
		
	# Last loop shifts 8 bits extra
	num >>= 8;
	return num;
	
def intToStr(num):
	str = "";
	while num != 0:
		str = chr(num & 0xFF) + str;
		num >>= 8;
		
	return str;
	
def encrypt(msg, e, n):
	M = strToInt(msg);
	print "Numberified: " + str(M);
	print "Back check: " + str((intToStr(M) == msg));
	
	# c = M^e mod n
	return pow(M, e, n);

def decrypt(C, d, n):
	# m = C^d mod n
	m = pow(C, d, n);
	print m;
	return intToStr(m);

random.seed(1);

p = 991;
q = 4447;

print "p: " + str(p) + " q: " + str(q);

n = p * q;
print "n: " + str(n);

phi = (p-1)*(q-1);
print "phi: " + str(phi);

(e, d) = calcKeys(phi);
print "e: " + str(e) + " d: " + str(d);

# destroy p, q and phi
p = q = phi = 0;

msg = "Hi";
print "Message: " + msg;

C = encrypt(msg, e, n);
print "Encrypted: " + str(C)

print "Decrypted: " + decrypt(C, d, n);

