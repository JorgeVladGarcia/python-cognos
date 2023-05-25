def findSum(str1):

	temp = "0"
	Sum = 0
	for ch in str1:
		if (ch.isdigit()):
			temp += ch
		else:
			Sum += int(temp)
			temp = "0"
	return Sum + int(temp)
str1 = "Quiero indicar que 2 y 2 son 4 por 4 es 16"

print("El texto es:", str1)
print("La suma de los numeros en el texto es:", findSum(str1))
