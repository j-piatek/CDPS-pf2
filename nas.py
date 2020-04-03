#!/usr/bin/python

############################
#--AUTORES DE LA PRACTICA--#
#--------------------------#
#----Hugo Pascual Adan-----#
#-------Jakub Piatek-------#
############################


from subprocess import call
import time

#funciones
def cmd_g(maquina,aux):
	call("sudo lxc-attach --clear-env -n "+maquina+" -- "+aux, shell=True);

#------------------------------------------
#montaje de nas y configuracion en servidores web

#emparejamiento de servidores nas
cmd_g("nas1","gluster peer probe 20.20.4.22");
cmd_g("nas1","gluster peer probe 20.20.4.23");
print("\033[1;32m"+"SERVIDORES NAS ASOCIADOS"+"\033[m");

#hacemos tiempo para que se unan los nas
time.sleep(2);
#cmd_g("nas1","gluster peer status")

#creacion del volumen
cmd_g("nas1","gluster volume create nas replica 3 20.20.4.21:/nas 20.20.4.22:/nas 20.20.4.23:/nas force");
cmd_g("nas1","gluster volume start nas");
print("\033[1;32m"+"VOLUMEN CREADO Y ARRANCADO"+"\033[m");

#recuperacion ante caidas
cmd_g("nas1","gluster volume set nas network.ping-timeout 5");
cmd_g("nas2","gluster volume set nas network.ping-timeout 5");
cmd_g("nas3","gluster volume set nas network.ping-timeout 5");
print("\033[1;32m"+"RECUPERACION ANTE CAIDAS CONFIGURADA"+"\033[m");

#montamos los nas en los servidores web en /mnt/nas
cmd_g("s1","mkdir /mnt/nas");
cmd_g("s2","mkdir /mnt/nas");
cmd_g("s3","mkdir /mnt/nas");
cmd_g("s4","mkdir /mnt/nas");
cmd_g("s1","mount -t glusterfs 20.20.4.21:/nas /mnt/nas");
cmd_g("s2","mount -t glusterfs 20.20.4.22:/nas /mnt/nas");
cmd_g("s3","mount -t glusterfs 20.20.4.23:/nas /mnt/nas");
cmd_g("s4","mount -t glusterfs 20.20.4.21:/nas /mnt/nas");

print("\033[1;32m"+"PUNTOS DE MONTAJE EN SERVIDORES WEB REALIZADOS"+"\033[m");
#------------------------------------------
print("\033[1;32m"+"SERVIDORES NAS CONFIGURADOS"+"\033[m");

