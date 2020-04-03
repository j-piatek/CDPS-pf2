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
#Montaje del escenario

#descarga del escenario
cmd("wget http://idefix.dit.upm.es/cdps/pc2/pc2.tgz");
print("\033[1;32m"+"ESCENARIO DESCARGADO"+"\033[m");
cmd("sudo vnx --unpack pc2.tgz");
print("\033[1;32m"+"ESCENARIO DESCOMPRIMIDO"+"\033[m");

#sumamos el servidor4 al pc2.xml para montar el escenario
cmd("chmod +x s4.py");
cmd("./s4.py");
print("\033[1;32m"+"SERVIDOR 4 INCLUIDO EN .xml"+"\033[m");

#script proporcionado
cmd("pc2/bin/prepare-pc2-vm");
print("\033[1;32m"+"PREPARE TERMINADO"+"\033[m");

#Creo y arranco el escenario
cmd("sudo vnx -f pc2/pc2.xml --create");
print("\033[1;32m"+"ESCENARIO ARRANCADO"+"\033[m");

#------------------------------------------

#------------------------------------------
#en este momento configuramos imagen para persistencia
#------------------------------------------

'''
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
'''
print("\033[5;32m"+"ESCENARIO CONFIGURADO Y MONTADO"+"\033[m");

