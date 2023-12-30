import subprocess
import optparse
import pyfiglet

def Change_Mac (interface,new_mac) :
    print("[<_>]  Changing Mac Address for " + interface + " to "+ new_mac)
    subprocess.call(["ifconfig " ,interface ," down"])
    subprocess.call(["ifconfig " ,interface ,"hw" , "ether" ,new_mac] )
    subprocess.call(["ifconfig" ,interface , "up"])

def Get_Arguments():
    parser =optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change Mac Address")
    parser.add_option("-m","--mac",dest="new_mac",help="The New Mac Address")
    (options , arguments)= parser.parse_args()
    if not options.interface :
        print("<!> Please specify interface , use --help for more informations .")
    elif not options.new_mac :
        print("<!> Please specify new mac address , use --help for more informations .")
    return options


if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("MaC'Hanger")
    print(ascii_banner)
    options = Get_Arguments()
    Change_Mac(options.interface,options.new_mac)
