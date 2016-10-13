def search(array, fElement, sElement):
	for a in array:
		if a == fElement * sElement:
			return True
	return False 
