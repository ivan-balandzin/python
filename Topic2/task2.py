a = "А роза упала на лапу Азора"
print (a)
# меняем все символы на строчные и удаляем пробелы
b = a.lower().replace(' ', '', len(a))
# то же самое, но еще и слово в обратном порядке
c = a.lower().replace(' ', '', len(a))[::-1]
if b == c:
	print ("The word is palindrome")
else:
	print ("The word is not palindrome")
