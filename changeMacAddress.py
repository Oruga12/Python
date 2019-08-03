#!/usr/bin/env pyhton

import subprocess
from subprocess import Popen, PIPE
import optparse
import os.path
import re

def argumentos():
	parse = optparse.OptionParser()
	parse.add_option("-i","--interface",dest="interface",help="Ingrese la interfaz de red")
	parse.add_option("-m","--mac",dest="mac",help="registre la nueva MAC")
	(options, arguments) = parse.parse_args()
	if not options.interface:
		parse.error("Por favor registre la interfaz")
	if not options.mac:
		parse.error("Por favor registre la nueva MAC address")
	else:
		return options

def cambio_mac(interface,mac):
	x11 = subprocess.check_output(["ifconfig",options.interface]).decode('utf-8')
	macaddress = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',x11)
	print("==" * 33)
	print("[+] Se cambiara la mac de " + interface + ": " + str(macaddress.group(0)))
	print("[+] Por la nueva mac " + mac)

def ejecutar(mac):
	comando=("ifconfig eth0 hw ether "+ mac)
	scored = Popen(comando, stdout=PIPE, stderr=PIPE, shell=True)
	stdoutscore = scored.stdout.read()
	stderrscore = scored.stderr.read()

if __name__=="__main__":

	options = argumentos()
	cambio_mac(options.interface,options.mac)
	ejecutar(options.mac)
	
	print("\n[*]--> Cambio realizado exitosamente...")
