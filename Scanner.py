import socket
from datetime import datetime


def scan():
    tStart = datetime.now()
    target = input("Enter the IP of the target to scan: ")
    portStart = input("Enter the port you want the scan to begin at: ")
    portEnd = input("Enter the port you want to end the scan at: ")
    print("Initiating scan of target: " + target)
    log = open(target+'-ScanReport.txt', "w+")
    logRegister = list()
    portDict = {
        "1": "tcpmux",
        "5": "rje",
        "7": "echo",
        "9": "discard",
        "11": "systat",
        "13": "daytime",
        "17": "qotd",
        "18": "msp",
        "19": "chargen",
        "20": "ftp-data",
        "21": "ftp",
        "22": "ssh",
        "23": "telnet",
        "25": "smtp",
        "37": "time",
        "39": "rlp",
        "42": "nameserver",
        "43": "nicname",
        "49": "tacacs",
        "50": "re-mail-ck",
        "53": "domain",
        "63": "whois++",
        "67": "bootps",
        "68": "bootpc",
        "69": "tftp",
        "70": "gopher",
        "71": "netrjs-1",
        "72": "netrjs-2",
        "73": "netrjs-3",
        "73": "netrjs-4",
        "79": "finger",
        "80": "http",
        "88": "kerberos",
        "95": "supdup",
        "101": "hostname",
        "102": "iso-tsap",
        "105": "csnet-ns",
        "107": "rtelnet",
        "109": "pop2",
        "110": "pop3",
        "111": "sunrpc",
        "113": "auth",
        "115": "sftp",
        "117": "uucp-path",
        "119": "nntp",
        "123": "ntp",
        "137": "netbios-ns",
        "138": "netbios-dgm",
        "139": "netbios-ssn",
        "143": "imap",
        "161": "snmp",
        "162": "snmptrap",
        "163": "cmip-man",
        "164": "cmip-agent",
        "174": "mailq",
        "177": "xdmcp",
        "178": "nextstep",
        "179": "bgp",
        "191": "prospero",
        "194": "irc",
        "199": "smux",
        "201": "at-rtmp",
        "202": "at-nbp",
        "204": "at-echo",
        "206": "at-zis",
        "209": "qmtp",
        "210": "z39.50",
        "213": "ipx",
        "220": "imap3",
        "245": "link",
        "347": "fatserv",
        "363": "rsvp_tunnel",
        "369": "rpc2portmap",
        "370": "codaauth2",
        "372": "ulistproc",
        "389": "ldap",
        "427": "svrloc",
        "434": "mobileip-agent",
        "435": "mobilip-mn",
        "443": "https",
        "444": "snpp",
        "445": "microsoft-ds",
        "464": "kpasswd",
        "468": "photuris",
        "487": "saft",
        "488": "gss-http",
        "496": "pim-rp-disc",
        "500": "isakmp",
        "535": "iiop",
        "538": "gdomap",
        "546": "dhcpv6-client",
        "547": "dhcpv6-server",
        "554": "rtsp",
        "563": "nntps",
        "565": "whoami",
        "587": "submission",
        "610": "npmp-local",
        "611": "npmp-gui",
        "612": "hmmp-ind",
        "631": "ipp",
        "636": "ldaps",
        "674": "acap",
        "694": "ha-cluster",
        "749": "kerberos-adm",
        "750": "kerberos-iv",
        "765": "webster",
        "767": "phonebook",
        "873": "rsync",
        "992": "telnets",
        "993": "imaps",
        "994": "ircs",
        "995": "pop3s"

    }
    try:
        for port in range(int(portStart), int(portEnd)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    value = portDict[str(port)]
                    entry = "Port " + str(port) + ", " + value + ", is open."
                except:
                    entry = "Port " + str(port) + " is open."

                logRegister.append(entry)




    except KeyboardInterrupt:
        print("Control + C terminated the scan early.")

    except socket.error:
        print('Could not connect to target host.')

    tEnd = datetime.now()
    entryStart = "Scan begun at: " + str(tStart)
    entryEnd = "Scan ended at: " + str(tEnd)
    tLength = "Scan lasted: " + str(tEnd - tStart)
    log.writelines(entryStart)
    log.writelines("\n")
    log.writelines(entryEnd)
    log.writelines("\n")
    log.writelines(tLength)
    log.writelines("\n")
    for entry in logRegister:
        log.writelines(entry)
        log.writelines("\n")
    log.close()



if __name__ == "__main__":
    scan()