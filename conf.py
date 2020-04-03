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
#Creo y arranco el escenario
cmd("sudo vnx -f pc2/pc2.xml --create");
print("\033[1;32m"+"ESCENARIO ARRANCADO"+"\033[m");
#------------------------------------------

#------------------------------------------
#ejecutamos los scripts de configuracion de cada componente
#damos permisos de ejecucion a cada script por si no los tiene
cmd("chmod +x app.py bbdd.py fw.py lb.py nas.py");
#ejecucion de scripts de configuracion
cmd("./fw.py");
cmd("./bbdd.py");
cmd("./nas.py");
cmd("./app.py");
cmd("./lb.py");
#------------------------------------------
