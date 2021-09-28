import io
import os
import subprocess
import serial
import time
import serial.tools.list_ports
from tkinter import messagebox
ports = serial.tools.list_ports.comports()


def pop_up(error_id="Error ID",error_text="Error TEXT"):
        messagebox.showerror(title=error_id ,message=error_text)



#serial_write("COM2","text")
#return 1 on success
#return 0 on fail
def serial_write(obj, string):
        if(obj.write(string.encode('utf-8'))):
                return 1 #on success
        else:
                return 0 #on fail
        
#serial_read("COM2")
#return text on success
#return 0 on fail.
#def serial_read(chosen_port): #return 0 if no data was readed
#        recived_string = chosen_port.readline()
def serial_read_line(obj):
        wiadomosc = obj.readline()
        if(wiadomosc != "b''"):
                if(len(wiadomosc)!=0):
                        print( wiadomosc)
                        try:
                                wiadomosc = wiadomosc.decode("utf-8")
                                wiadomosc = wiadomosc.replace('\r','')
                                wiadomosc = wiadomosc.replace('\n','')
                                print('Po odkodowaniu: "'+ wiadomosc+'"')
                                return(wiadomosc)
                        except:
                                return("Oczekiwanie")

def serial_clear_read_buffer(obj):
        obj.reset_input_buffer()

def readData(object): #object type:  object = serial.Serial()
    buffer = ""
    while True:
        oneByte = object.read(1)
        if oneByte == b"\n":    #method should returns bytes #wait for EOL
            return buffer
        else:
            buffer += oneByte.decode("ascii")

# Program to find most frequent
# element in a list
def most_frequent(List):
        if(len(List)==0):
                return -1
        else:
                return max(set(List), key = List.count)
 


############################END Funkcje obsługi seriala


#return dictionary com:id
def print_what_is_connected_to_all_com_ports():
        print("Dostępne porty com: ")
        for port, desc, hwid in sorted(ports):
                print("{}: {} [{}]".format(port, desc, hwid))
        print()
        print("Dostępne porty com: ")
        for port in sorted(ports):
                print("{}".format(port))
        print()
        seq = []
        numer = 0
        slownik_port_nazwa = {}
        for port in sorted(ports):
            port = str(port)[:5]
            port = str(port).lstrip().rstrip()
            print("Odnaleziony port COM: "+str(port))
            if(str(port).find("USB")>-1 or str(port).find("COM")>-1):
                    print("Odnaleziony port COM: "+str(port))
                    ser = serial.Serial(port, 9600, timeout=1,\
                    parity=serial.PARITY_NONE,\
                    stopbits=serial.STOPBITS_ONE,\
                    bytesize=serial.EIGHTBITS)
                    time.sleep(1)
                    print("Otwieram port:")
                    #ser.open()
                    print("Nadaję wiadomość: NB\\r\\n")
                    print(("NB\r\n".encode()))
                    print("Czekam na odpowiedź")
                    serial_write(ser, "NB\r\n")
                    #ser.write(bytes(b"?\r\n")) #bytes() works
                    #ser.write("?".encode()) #works too
                    serial_write(ser, "C0\r\n")
                    #time.sleep(1)
                    lista_z_identyfikatorami = []
                    counter = 0
                    liczba_udanych_odbiorow = 0
                    polaczone_wiadomosci = ""
                    while 1:
                        #serial_clear_read_buffer(ser)
                        serial_write(ser, "NB\r\n")
                        message = serial_read_line(ser)
                        print((message))
                        if(str(message)!="None" and str(message)!="NB"):
                            counter = 0
                            polaczone_wiadomosci = polaczone_wiadomosci + str(message)+"|"
                        else: counter=counter+1
                        if str(message).find("NB A") != -1:
                            lista_z_identyfikatorami.append(str(message).replace("NB A","").replace('"','').strip())     
                            liczba_udanych_odbiorow = liczba_udanych_odbiorow+1
                        if(liczba_udanych_odbiorow == 10):
                            serial_write(ser, "C1\r\n")
                            break
                        if(counter==5):
                            break        
                    ser.close()
                    print("Najpopularniejszy element listy to: " + str(most_frequent(lista_z_identyfikatorami))+" i występuje on na porcie: "+port)
                    slownik_port_nazwa.update({str(most_frequent(lista_z_identyfikatorami)):port})
        print("widomosc")            
        print(str(message))
        print(polaczone_wiadomosci)
        for krotka in lista_z_identyfikatorami:
                print(krotka)
        print()
        print("Mamy słownik co jest podłączone na każdym porcie")
        print(slownik_port_nazwa)
        return slownik_port_nazwa


slownik_xd = print_what_is_connected_to_all_com_ports()

#ok. Skanowanie portów masz już zaliczone
#Masz już słownik zawierajacy co jest na każdym porcie.
#teraz musimy wczytać ustawienia. Co, jest z czym?

file1 = open('ustawienia.txt', 'r')
lista = file1.readlines()
# Strips the newline character
count = 0
linia_gdzie_gotowe = 0
linia_gdzie_pairs=0
linia_gdzie_serial_settings = 0
for line in lista:
    if(line.strip().find("gotowe")!=-1 and line.find("=")!=-1 ):
        linia_gdzie_gotowe = count
    if(line.strip().find("pairs")!=-1):
        linia_gdzie_pairs = count
    if(line.strip().find("serial_settings")!=-1):
        linia_gdzie_serial_settings = count
    print("Line{}: {}".format(count, line.strip()))
    count += 1


print("Linia gdzie znajduje się string gotowe= "+str(linia_gdzie_gotowe))

print("Linia gdzie znajduje się string pairs= "+str(linia_gdzie_pairs))

print("Linia gdzie znajduje się string serial_settings= "+str(linia_gdzie_serial_settings))


print()


#Waga lewa piecowa^SCALE_ID#123456&PILOT_ID#pilot_jeden|pozX=0|pozY=0
def splituj_argumenty_z_napisu(zdanie,slownik):
        nazwa_wagi = (zdanie.split("^"))[0]
        print("Nazwa gui wagi:"+nazwa_wagi)
        SCALE_ID= (((((zdanie.split("&"))[0]).split("^"))[1]).split("#"))[1]
        print("ID WAGI:"+SCALE_ID)
        try:
                SCALE_PORT = slownik[SCALE_ID]
        except:
                pop_up("Błąd wyszukiwania wagi","Nie odnaleziono wagi z id: "+SCALE_ID)
        print("PORT WAGI:" +SCALE_PORT)
        PILOT_ID= (((((zdanie.split("&"))[1]).split("|"))[0]).split("#"))[1]
        print("ID PILOTA:"+PILOT_ID)
        try:
                PILOT_PORT=slownik[PILOT_ID]
        except:
                pop_up("Błąd wyszukiwania pilota","Nie odnaleziono pilota z id: "+ PILOT_ID)
        print("PORT PILOTA:"+PILOT_PORT)
        pozX= ((zdanie.split("|"))[1].split("="))[1]
        pozY= ((zdanie.split("|"))[2].split("="))[1]
        print("POZ_X:"+pozX+" POZ_Y:"+pozY)
        print('"'+nazwa_wagi+"|"+SCALE_PORT+"|"+PILOT_PORT+"|"+pozX+"|"+pozY+'"')
        #os.system('gui0.2.py "'+nazwa_wagi+"|"+SCALE_PORT+"|"+PILOT_PORT+"|"+pozX+"|"+pozY)
        subprocess.call(
            'python gui0.2.py "'+nazwa_wagi+"|"+SCALE_PORT+"|"+PILOT_PORT+"|"+pozX+"|"+pozY+'"',
            shell=True
        )
        
print("Linie do dalszego splita")
lista_par = []
for i in range(linia_gdzie_pairs+1,linia_gdzie_serial_settings):
        print(str(i)+"||"+ lista[i].strip())
        splituj_argumenty_z_napisu(lista[i].strip(),slownik_xd)
        


        
        


