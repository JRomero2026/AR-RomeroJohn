#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importa el módulo socket, que permite trabajar con conexiones de red
import socket


# Define una función llamada test_socket_modes
def test_socket_modes():

    # Crea un socket TCP/IP usando IPv4
    # AF_INET  -> protocolo IPv4
    # SOCK_STREAM -> protocolo TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configura el socket en modo bloqueante
    # 1 significa True (bloqueante)
    # En este modo, las operaciones esperan hasta completarse
    s.setblocking(True)

    # Establece un tiempo máximo de espera de 0.5 segundos
    # para operaciones del socket
    s.settimeout(0.5)

    # Asocia el socket a la dirección local 127.0.0.1
    # y al puerto 0.
    # El puerto 0 indica que el sistema operativo elegirá
    # automáticamente un puerto disponible
    s.bind(("127.0.0.1", 0))

    # Obtiene la dirección y puerto asignados al socket
    socket_address = s.getsockname()

    # Muestra en pantalla la dirección del servidor creado
    # En Python 3 se usa print() como función
    print("Servidor trivial iniciado en el socket: {}".format(socket_address))

    # Bucle infinito para mantener el servidor activo
    while True:

        # Pone el socket en modo escucha
        # El parámetro 1 indica el número máximo de conexiones
        # pendientes en cola
        s.listen(1)


# Punto de entrada principal del programa
# __name__ == '__main__' indica que el archivo
# se está ejecutando directamente y no importado como módulo
if __name__ == '__main__':

    # Llama a la función principal
    test_socket_modes()