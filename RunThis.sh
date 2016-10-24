#!/bin/bash
while :
do
	echo "Iniciando programa"
	python ejecuta.py
	echo "Sistema caido, diagnosticando inconveniente..."
	sleep 2
	ping -q -c5  8.8.8.8 > /dev/null
	if [ $? -eq 0 ]
	then
		echo "Problema del software"
		echo "Iniciado programa"
	else
		echo "Conexion a internet despreciable"
		sleep 1
		echo "Resolviendo"
		dhclient -v -r eth0
		dhclient -v  eth0
		echo "Nueva IP,reestableciendo software"
	fi
done
