import subprocess
import optparse
import pyfiglet


text = pyfiglet.figlet_format("mac Changer" )
print(text)

def arguments():
    parser = optparse.OptionParser(epilog="Example - python3 mac_changer.py -i eth0 -m 00:1a:22:45:33:33")
    parser.add_option("-i", "--interface ", dest="interface", metavar =" " ,help="Interface to change its MAC address")
    parser.add_option("-m" , "--mac ", dest="macaddress", metavar =" ", help="macaddress for changing mac address")
    (options, arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[+] please specify the interface, use --help for more info")
    elif not options.macaddress:
        parser.error("[+] please specify macaddress-value, use --help for more info")
    return options
    


def mac_changer(interface,macaddress):
    print("[+] Changing MAC address for " + interface + " to " + macaddress)

    subprocess.call(["ifconfig" , interface, "down"])
    subprocess.call(["ifconfig" , interface, "hw", "ether", macaddress])
    subprocess.call(["ifconfig" , interface, "up"])

options = arguments()
mac_changer(options.interface,options.macaddress)

