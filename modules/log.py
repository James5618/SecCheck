from platform import system as system_name

if system_name() == "Windows":
    from modules.colorama import init
    init()

def InitializeLogger(context):
    global outfile
    outfile = context
    file = open(outfile, 'w')
    file.close()

# Background Colours.
class bcolours:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    purple = '\033[38;5;93m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

class colours:
    blue = 'blue'
    cyan = 'cyan'
    green = 'green'
    yellow = 'yellow'
    red = 'red'
    purple = 'purple'
    bold = 'bold'
    underline = 'underline'
    no_new_line = 'no_new_line'
    endc = 'endc'

def WriteToFile(data):
    colors = [bcolours.blue, bcolours.red, bcolours.yellow, bcolours.green, bcolours.cyan, bcolours.endc, bcolours.bold, bcolours.underline]
    for colorcode in colors:
        data = data.replace(colorcode, "")
    filename = outfile
    if system_name() == "Windows":
        data = data.encode("utf-8")
        file = open(filename, 'ab')
        file.write(b"\n" + bytes(data))
    else:
        file = open(filename, "a")
        file.write("\n" + data)
    file.close()

def info(msg):
    print(bcolours.blue + "[+] " + bcolours.endc + str(msg))
    WriteToFile("[+] " + msg)

def error(msg):
    print(bcolours.red + "[-] " + bcolours.endc + str(msg))
    WriteToFile("[-] " + msg)

def warning(msg):
    print(bcolours.yellow + "[*] " + bcolours.endc + str(msg))
    WriteToFile("[*] " + msg)

def success(msg):
    print(bcolours.green + "[+] " + bcolours.endc + str(msg))
    WriteToFile("[+] " + msg)

def println(msg):
    print(msg)
    WriteToFile(msg)

def banner(msg, color):
    print_coloured("\n" + "─" * 60, color)
    print_coloured(str(msg).center(60), color)
    print_coloured("─" * 60 + "\n", color)
    WriteToFile("\n" + "─" * 60)
    WriteToFile((msg).center(60))
    WriteToFile("─" * 60 + "\n")

def print_coloured(text,color):
    if color == 'blue':
        print(bcolours.blue + str(text) + bcolours.endc)
    elif color == 'cyan':
        print(bcolours.cyan + str(text) + bcolours.endc)
    elif color == 'green':
        print(bcolours.green + str(text) + bcolours.endc)
    elif color == 'yellow':
        print(bcolours.yellow + str(text) + bcolours.endc)
    elif color == 'red':
        print(bcolours.red + str(text) + bcolours.endc)
    elif color == "purple":
        print(bcolours.purple + str(text) + bcolours.endc)
    elif color == 'bold':
        print(bcolours.bold + str(text) + bcolours.endc)
    elif color == 'underline':
        print(bcolours.underline + str(text) + bcolours.endc)
    elif color == 'no_new_line':
        print(str(text), end='')