def encode(input):
	encoded = ""
	count = 1
	x = 0
	while(x < len(input)-1):
		if input[x] == input[x+1]:
			count+=1
		else:
			encoded += (input[x] + str(count))
			count = 1	
		x+=1
	if (len(input) > 0):
		encoded += (input[x] + str(count))
	if(len(input) < len(encoded)):
		return(input) 	
	return(encoded)
