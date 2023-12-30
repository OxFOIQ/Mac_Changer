import subprocess
import optparse
import pyfiglet

def Change_Mac(interface, new_mac):
    print("[<_>]  Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

def Get_Arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The New Mac Address")
    options, _ = parser.parse_args()
    if not options.interface or not options.new_mac:
        parser.error("Please specify both interface and new MAC address. Use --help for more information.")
    return options

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("MaC'Hanger", font="bulbhead")
    print(ascii_banner)
    
    options = Get_Arguments()
    Change_Mac(options.interface, options.new_mac)
