import serial
import telnetlib

# testato su versione python 3.2
# vlc deve aver attiva l'interfaccia telnet, accessibile attraverso: 127.0.0.1:4212 con pass: admin
# usando il client di telnet presente di default in windows o PUTTY si entra nel server telnet di vlc e lanciando il comando help si avra tutta la lista dei possibili comandi: play, pause etc.

SERIALPORT = input("Inserire la porta seriale a cui e' connesso il dispositivo: ")
# Set up serial port
try:
    ser = serial.Serial(SERIALPORT, 9600)
except serial.SerialException:
    print('No device connected - exiting...')
    time.sleep(4)
    sys.exit()


print("\n### VLC Infrared Remote Controller Module - ver 2.0 ###\n")

# Ci connettiamo in telnet al VLC locale o remoto.

host = input("Inserisci l'HOST: ") #dando la possibilita di scegliere l'host ci si puo' connettere anche a pc nella stessa LAN
password = input("Inserisci la password (default: admin): ")
porta = input("Inserisci la porta (4212 per VLC telnet server): ")

tn = telnetlib.Telnet(host, porta) #la porta di default per telnet: 23

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")


print("\nDispositivo ricevitore infrarosso collegato e connessione stabilita!\n")

pause_toggle = False
def esegui_cmd(comando):
    global pause_toggle

    comando = comando[0:-2].decode("utf-8") #ripuliamo il comando eliminando i tag \r\n finali e decodificando.
    if comando == "20FE4DBB": #play/pausa  (la variabile pause_toggle viene introdotta appositamente, per l'effetto di toggle)
          if pause_toggle:
            cmd = "play\n"
            pause_toggle = not pause_toggle
          else:
            cmd = "pause\n"
            pause_toggle = not pause_toggle
          tn.write(cmd.encode("utf-8"))
    elif comando == "A3C8EDDB": #volume +
        cmd = "volup\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "F076C13B": #volume -
        cmd = "voldown\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "D7E84B1B": #next
        cmd = "next\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "52A3D41F": #prev
        cmd = "prev\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "E5CFBD7F" : #fullscreen (a tutto schermo)
        cmd = "fullscreen\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "511DBB" : # stop
        cmd = "stop\n"
        tn.write(cmd.encode("utf-8"))
    elif comando == "FFFFFFFF": #pressione continua del tasto, viene ignorata
       pass


while True:
    comando = ser.readline()
    print(comando)
    esegui_cmd(comando)
    comando = ""

