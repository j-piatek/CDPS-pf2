PRÁCTICA DE LA ASIGNATURA CENTROS DE DATOS Y PROVISIÓN DE SERVICIOS:
DESPLIEGUE DE UNA APLICACIÓN ESCALABLE EN UNA RED VIRTUAL

Se diseñan varios scripts que permiten automatizar el despliegue y la configuración de una 
aplicación de QUIZZES en un entorno virtual desarrollado con la herramienta VNX.

-----------------------------------------------------------------------------------------------

INSTRUCCIONES PARA PERSISTENCIA

1-Destruir el escenario
sudo vnx -f pc2/pc2.xml --destroy

2-Entrar en la maquina virtual
sudo vnx --modify-rootfs pc2/filesystems/rootfs_lxc64-cdps --arch=x86_64

3-activar red
comprobar si ya esta activa, si no ejecutar:
sudo dhclient eth0

4-instalar los paquetes
apt-get update
apt-get upgrade -y
apt-get install -y npm nodejs mariadb-server haproxy

5 salir con:
halt -p

-------------------------------------------------------------------------------------------------

INSTRUCCIONES PARA DESPLIEGUE DEL ESCENARIO CON PERSISTENCIA:

1-Script pf2.py: se baja y monta el escenario una primera vez para poder modificar la imagen (necesita la imagen de disco del SO .qcow2)

2-Seguimos las instrucciones de persistencia.txt (PERSISTENCIA) para instalar los paquetes necesarios en la imagen

#A partir de aqui tenemos persistencia

3-Script conf.py: con ese script configuramos de forma adecuada cada una de las maquinas apoyandonos en los scripts de configuracion(fw, bbdd, app, nas y lb)

4-Escenario listo. Para conectase a la aplicacion: en navegador 20.20.2.2 o en el terminal ejecutar- lynx 20.20.2.2
