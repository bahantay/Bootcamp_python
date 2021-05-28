def count_letter(param_1):
	param_1 = param_1.lower()
	param_1 = ''.join(x for x in param_1 if x.isalpha())
	d = {}
	for i in param_1:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	clean = str(d).replace("'","").replace(": ", "").replace("{", "").replace("}", "")
	letter = ''.join(x for x in clean if x.isalpha())
	num = ''.join(x for x in clean if x.isdigit())
	out = ', '.join(map(''.join, zip(num, letter)))
	return out
