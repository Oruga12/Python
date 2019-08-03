# !/usr/bin/python
# -*- decoding:utf8 -*-
import time
import os.path
from subprocess import Popen, PIPE

print("[+] Se esta lanzando los comandos necesario para extraer la informaion requerida....Please Wait")
################### - COMANDOS VARIOS  - ########################

date    = time.strftime("%d/%m/%y")
hora    = time.strftime("%H:%M:%S")
tiempo  =("Fecha: " + date + " siendo las " + hora)
sistem  = os.popen("uname -a")
update  = os.popen("uname -v")
datosis = sistem.readlines()
h       = os.popen("hostname")
fstab   = os.popen("cat /etc/fstab")
netstat = os.popen("netstat -antu")
tamano  = os.popen("df -h")
ifc     = os.popen("ifconfig")
home    = os.popen("mount |grep /home")
repositorio = os.popen("cat /etc/apt/apt.conf.d/10proxy")
chmotd = os.popen("ls -la /etc/motd")
chmoissue = os.popen("ls -la /etc/issue")
chmo = os.popen("ls -la /etc/issue.net")
ntp = os.popen("systemctl status ntp")


################## - HISTORY --###############################
history = os.path.isfile("~/.bash_logout")
palabrahis = ("#")
datoshis=[]
hisdatos=[]
datoshis1=[]
if history==True:
    filehistory = open("~/.bash_logout")
    for his in filehistory:
        if palabrahis in his:
            pass
        else:
            datoshis.append(his)
    for th in hisdatos:
        if len(th)<=1:
            pass
        else:
            datoshis1.append(th)
    if len(datoshis)==1:
        datoshis1=("Todo el archivo estan comentados")
else:
    datoshis1 = ("No existe el archivo ~/.bash_logout para que se configure")

################## - BLOQUEO DE USB - #############################
usb = os.path.isfile("/etc/modprobe.d/block_usb.conf")
if usb==True:
    usbvalor = (os.popen("cat /etc/modprobe.d/block_usb.conf")).read()
else:
    usbvalor = ("   No existe la direccion del archivo, segun documento de hardening ")

##########  SSH ###################
x = Popen("ssh -V", stdout=PIPE, stderr=PIPE, shell=True)
stdout = x.stdout.read()
stderr = x.stderr.read()

########### - SSH PUERTO QUE USA  - ##############################
palabrassh = "#"
datosssh =[]
datosssh1=[]

host = os.path.isfile("/etc/ssh/sshd_config")
if host==True:
    filessh = open("/etc/ssh/sshd_config")
    for ssh1 in filessh:
        if palabrassh in ssh1:
            pass
        else:
            datosssh.append(ssh1)
    for t in datosssh:
        if len(t)<=1:
            pass
        else:
            datosssh1.append(t)

    if len(datosssh)==1:
        datosssh1 =("Todo el archivo /etc/ssh/sshd_config esta comentado")
    filessh.close()
else:
    datosssh1=("[+] No existe el archivo")

###########################################################

palabrasuperuser = ("password_pbkdf2")
filessh = open("/etc/grub.d/00_header")
fileusuario = os.path.isfile(("/etc/grub.d/00_header"))

if fileusuario==True:
    for lineasuper in filessh.readlines():
        if palabrasuperuser in lineasuper:
            mensuper = (lineasuper)
            break
    mensuper=("No se encuentra la configuracion")
else:
    mensuper=("No existe el archivo")
filessh.close()

###########################- HOST DENY -####################

palabrahost = ("#")
hostdatos = []
datoshost1=[]
hostdatos1=[]
host = os.path.isfile("/etc/hosts.deny")
if host==True:
    filessh = open("/etc/hosts.deny")
    for ihost in filessh:
        if palabrahost in ihost:
            pass
        else:
            hostdatos.append(ihost)

    for thost in hostdatos:
        if len(thost)<=1:
            pass
        else:
            datoshost1.append(thost)

    if len(datoshost1)<1:
        datoshost1 =("Todo el archivo esta comentado")
    filessh.close()
else:
    datoshost1=("[+] No existe el archivo")


################### -  HOST ALLOW  - #######################
palabrahost= ("#")
hostdeny = []
datdeny = []
mendeny=[]

deny = os.path.isfile("/etc/hosts.allow")
if deny==True:
    filessh = open("/etc/hosts.allow")
    for ih in filessh:
        if palabrahost in ih:
            pass
        else:
            hostdeny.append(ih)
    if len(hostdeny)==1:
        hostdeny = ("Todo el archivo esta comentado")
    filessh.close()
else:
    hostdeny=("[+] No existe el archivo")


######################## - REDIRECT - /etc/sysctl.conf - #############
menredirect=[]
datos1=[]
dat=[]
datosred=[]
palabraredirect = ("#")
filessh = open("/etc/sysctl.conf")

redirect = os.path.isfile("/etc/sysctl.conf")
if redirect==True:
    for i in filessh:
        if palabraredirect in i:
            pass
        else:
            menredirect.append(i)
    for i1 in menredirect:
        if len(i1)<=1:
            pass
        else:
            datosred.append(i1)
    if len(datosred)==1:
        datosred = ("Todo el archivo esta comentado")
    filessh.close()
else:
    menredirect=("No existe el archivo")
filessh.close()

################## - CISC.CONF - #####################################

palabracis= ("#")
cis = []
datcis = []
mencis=[]
hostcis = []

cis = os.path.isfile("/etc/modprobe.d/CIS.conf")

if cis==True:
    filessh = open("/etc/modprobe.d/CIS.conf")
    for ih1 in filessh:
        if palabracis in ih1:
            pass
        else:
            hostcis.append(ih1)
    if len(hostcis)==1:
        hostdcis = ("Todo el archivo esta comentado")
    filessh.close()
else:
    hostcis=("[+] No existe el archivo")

######################## - PARTICION /HOME - #######################################

ho      = home.read()
if ho!="":
    valor = ho
else:
    valor = "No existe"

###################- ANTIVIRUS INSTALADO - ############################
xanti = Popen("/etc/init.d/clamav-daemon status", stdout=PIPE, stderr=PIPE, shell=True)
stdoutanti = xanti.stdout.read()
stderranti = xanti.stderr.read()

################## - ANTIMALWARE INSTALADO -  #########################

xmal = Popen("dpkg --get-selections |grep chkrootkit", stdout=PIPE, stderr=PIPE, shell=True)
stdoutmal = xmal.stdout.read()
stderrmal = xmal.stderr.read()

##################- NOMACHINE - ######################################

nomachine = Popen("dpkg --get-selections |grep nomachine", stdout=PIPE, stderr=PIPE, shell=True)
stdoutnomachine = nomachine.stdout.read()
stderrnomachine = nomachine.stderr.read()

################## -  CORED CON PERMISOS - ############################

scored = Popen("ls -la /boot/grub/grub.cfg", stdout=PIPE, stderr=PIPE, shell=True)
stdoutscore = scored.stdout.read()
stderrscore = scored.stderr.read()

################## -  DOMINIO - ######################################

dominio = Popen("hostname -f", stdout=PIPE, stderr=PIPE, shell=True)
stdoutsdomain = dominio.stdout.read()
stderrsdomain = dominio.stderr.read()

################## - GRUB-cfg - ######################################
scored = Popen("ls -la /boot/grub/grub.cfg", stdout=PIPE, stderr=PIPE, shell=True)
stdoutscore = scored.stdout.read()
stderrscore = scored.stderr.read()


##################-  ARCHIVOS  - #####################################

file = open("hardening-Ubuntu.txt","w")  # <-- abre y/o crea el archivo

file.write("               ==================================================\n")
file.write("             | REPORTE DE HARDENING DEL SISTEMA OPERATIVO UBUNTU |\n")
file.write("               ==================================================\n\n")
file.write(" [+] Fecha: " + date + " siendo las " + hora +                                    "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El sistema Operativo es: \n" + "  --> "+ str(datosis) +                      "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El sistema Operativo esta actualizado a la fecha: \n" + "  --> "+str(update.read()) +  "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El Nombre del equipo es: \n" + "  --> "+ str(h.read()) +                     "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Las particiones FSTAB es: \n" + " --> " + str(fstab.read()))
file.write(" ==================================================================================\n")
file.write(" [+] Procesos en ejecucion: \n" + "  -->" +str(netstat.read()))
file.write(" ==================================================================================\n")
file.write(" [+] Tamaño de las particiones: \n" + "  -->" +str(tamano.read()))
file.write(" ==================================================================================\n")
file.write(" [+] La version del SSH es: \n" + "  -->" + stdout + stderr + "\n")
file.write(" ==================================================================================\n")
file.write(" [+] La configuracion del banner es: \n" + "  --> " + str(chmotd.read()) +
                                                       "  --> "+  str(chmoissue.read()) +
                                                       "  --> " + str(chmo.read()) +"\n")
file.write(" ==================================================================================\n")
file.write(" [+] El repositorio esta para que se actualice es: \n" + "  -->" + str(repositorio.read()) +   "\n")
file.write(" ==================================================================================\n")
file.write(" [+] [SSH] El puerto que hace uso el servicio SSH es: \n" + "  -->" +str(datosssh1) + "\n")
file.write(" ==================================================================================\n")
file.write(" [+] La interfaces de red y las direcciones de red son: \n\n" + "  -->" +str(ifc.read()) +  "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Historial de comandos \n" + "  -->" + str(datoshis1) +"\n")
file.write(" ==================================================================================\n")
file.write(" [+] El archivo de configuracion  /etc/modprobe.d/block_usb.conf para el bloqueo de USB es: "
           "\n " + " --> "+str(usbvalor) +  "      buscamos la linea install usb-storage /bin/true" + "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Antivirus instalado... \n" + "  -->" +  stdoutanti + stderranti +            "\n")
file.write(" ==================================================================================\n")
file.write(" [+] NoMachine instaldo: \n" + " -->" + stdoutnomachine + stderrnomachine +       "\n")
file.write(" ==================================================================================\n")

file.write(" [+] Denegacion de acceso al HOST: \n" + " --> " + str(datoshost1)  +             "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Permitir acceso al HOST: \n" + " --> " + str(hostdeny)  +              "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El SCORED muestra los siguientes permisos (root:root) \n" + " -->  " +stdoutscore + stderrscore + "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El Boot loader password: \n" + "  -->" +mensuper +                           "\n")
file.write(" ==================================================================================\n")
file.write(" [+] El servicio de NTP : \n" + " -->"+str(ntp.read()) +                              "\n")
file.write(" ==================================================================================\n")
file.write(" [+] REDIRECT sending is disable : \n" + "  -->" +str(datosred) +                 "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Los servicios CIS.conf : \n" + "  -->" +str(hostcis) +                       "\n")
file.write(" ==================================================================================\n")
file.write(" [+] Los Dominios son: \n" + "  --> " + stdoutsdomain + stderrsdomain +           "\n")
file.write(" ==================================================================================\n")


file.close()

print("[+] Finished Susessfull")
print("[+] Verificar el archivo de nombre << hardening-Ubuntu.txt >> en donde se encuentra el reporte")
"""reporte = open("hardening-Ubuntu.txt","r")
print(reporte.read())
reporte.close()"""


