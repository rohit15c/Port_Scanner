#!/usr/bin python3

import socket

print('-' * 50)
print("A Simple Port Scanner $$ Made By -MR.R0G")
print("\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter The IP- ")
port = int(input("Enter The Port- "))

def Port_Scanner(port):
    if s.connect_ex((host, port)):
        print("The Port Is Closed")
    else:
        print("The Port Is Open For Connection")

Port_Scanner(port)

print('-' * 50)
