ALPHABET_SIZE=26
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(shift, text): #allows negatives numbers for left shifts. Dosen't need a decryp, just use this function with oposite value in the shift
	result=""
	for l in text.lower():
		try:
			i = (alphabet.index(l)+shift) % ALPHABET_SIZE
			result+=alphabet[i]
		except ValueError:
			result += l

	return result.lower()