import os, sys


try:
	file = sys.argv[1]
	output = sys.argv[2]
except IndexError:
	print(f'[-] Usage: python {sys.argv[0]} <file> <output>')
	sys.exit()


def decrypt():
	try:
		with open(file, 'r') as f:
			data = f.read()
			f.close()
		changeData = data.replace('eval', 'echo')
		with open(output, 'w') as f:
			f.write(changeData)
			f.close()
		os.system(f'bash {output} > hack.sh')
		os.remove(output)
		os.system(f'mv -f hack.sh {output}')
		print('[+] Decrypted the script successfully.')
	except KeyboardInterrupt:
		print('[+] Good Bye!')
	except FileNotFoundError:
		print(f'[-] File not Found!')

decrypt()
# © CyberTitus 2021