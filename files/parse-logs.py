import re 
import sys 
import os 
import io 
 
input = 'zero-client.log'
output = 'parsed.txt'

match_list = []

keyword_list = [
"MGMT_SYS:Firmware Version",
"MGMT_USB:mgmt_usb_dds",
"unauthorized",
"web login",
"web logout",
"DISCONNECT_CAUSE",
"scancode",
"MGMT_PEM:PEM_MANAGED.CONNECT_TO_EM",
"WEBSOCKET:tera_socket_client_connect",
"MGMT_FW_PROV:Download complete",
"Previous Firmware Build",
"MGMT_EMT:PemCommandTransaction Commit",
"NTP time",
"MGMT_SYS:SESSION ACTIVE",
"NOT_AUTHORIZED",
"MGMT_SYS:(net_cback):",
"Network is down",
"MGMT_PCOIP_DATA:RTT",
"SESSION ACTIVE",
"rtt last",
"MGMT_IMG :log",
"MGMT_PEM:Certificate store",
"certificate",
"issued by",
"Cert not valid",
"fingerprint match result",
"Certificate fingerprint was used to verify and trust",
"MGMT_PEM:EM passed SSL verification",
"Trusted result: ",
"EM did not meet the full certificate verification requirement",
"Leaf certificate",
"MGMT_PEM:Certificate verification overall result:",
"MGMT_PEM:SHA256 fingerprint match result:",
"MGMT_PCB:Certificate verification overall result:",
"MGMT_PCB:Hostname result:",
"MGMT_PCB:Trusted setting",
"MGMT_PCB:Self-signed setting",
"MGMT_PCB:SHA256 fingerprint match setting",
"MGMT_PCB:Hostname setting",
"MGMT_PCB:Expected hostname",
"MGMT_SSL:verify_validity_time",
"MGMT_PEM:Trusted result",
"MGMT_PEM:Validity result",
"MGMT_PEM:SHA256 fingerprint match result",
"MGMT_PCB:Revocation result",
"MGMT_PEM:Server certificate"
]
 
try:
    with io.open(input, mode = 'r') as f:
#     with io.open(input, mode = 'r', encoding='utf-16', errors = 'replace') as f: (if running on WSL)
        lines = f.readlines()
        for line in lines:
            for item in keyword_list:
                if line.lower().find(item.lower()) > 0:
    #                 print(line)
                    match_list.append(line)
except IOError:
    print("the file you are trying to open doesn't exist.")

with open(output, "w+") as file:
    file.write("Parsed Logs:\n")
    match_list_clean = list(match_list)
    for item in xrange(0, len(match_list_clean)):
        print match_list_clean[item]
        file.write(match_list_clean[item] + "\n")
file.close()