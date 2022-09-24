romn_numerals = {
	1000: 'M',
	900: 'CM',
	500: 'D',
	400: 'CD',
	100: 'C',
	90: 'XC',
	50: 'L',
	40: 'XL',
	10: 'X',
	9: 'IX',
	5: 'V',
	4: 'IV',
	1: 'I',
}

def translate_number(x: int):
	res = ''
	for key, value in romn_numerals.items():
		res += (x // key) * value
		x %= key
	return res

x = int(input('Введите число\n'))

print("Римская",translate_number(x))
