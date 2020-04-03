#!/usr/bin/python

############################
#--AUTORES DE LA PRACTICA--#
#--------------------------#
#----Hugo Pascual Adan-----#
#-------Jakub Piatek-------#
############################


from subprocess import call

#funciones
def cmd(cmd):
	call(cmd,shell=True);

def cp(src,maquina,dst):
	cmd("sudo cp "+src+" "+"/var/lib/lxc/"+maquina+"/rootfs"+dst);

#------------------------------------------
#Destruyo el escenario
cmd("sudo vnx -f pc2/pc2.xml --destroy");
print("\033[1;32m"+"ESCENARIO DESTRUIDO"+"\033[m");
#------------------------------------------

#------------------------------------------
#Limpio todos los archivos
cmd("sudo rm -rf pc2.tgz");
cmd("sudo rm -rf pc2");
print("\033[1;32m"+"ARCHIVOS BORRADOS"+"\033[m");
#------------------------------------------

