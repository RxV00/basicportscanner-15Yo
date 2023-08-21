import socket
import sys

topscannedports =[21,22,23,25,53,80,110,111,135,139,143,443,445,993,1723,3306,3389,5900,8080]



def scan(target,defaulttimer):
    ports = int(input("How Many Ports Should be Scanned : "))
    for port in range(1,ports):
        port_scanner(target,port,defaulttimer)


def port_scanner(ipaddres,port,defaulttimer):
    try:
        sock = socket.socket()
        sock.connect((ipaddres,port))
        sock.settimeout(defaulttimer)
        sock.close()
        print("[+] OPEN PORT FOUND : " + str(port))
    except:
        print("[-] PORT IS CLOSED : " + str(port))

       
       

def top20_ports(target,defaulttimer):
    for port in topscannedports:
        port_scanner(target,port,defaulttimer)
        



def main():
    target = input("Please write the ip of the target : ")
    defaulttimer = int(input("Please write the default timeout : "))
   
    while True:
     scantype = input("choose if you want to scan top20 ports or normalscan : ")
     if scantype == "top20":
         top20_ports(target,defaulttimer)
         break
     if scantype == "normalscan":
         scan(target,defaulttimer)
         break
     else:
         print("please write top20 or normalscan : ")
main()



    
