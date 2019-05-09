import serial# on import la bibliothèque pour communiquer avec e port série

# on crée un objet port_serie qui communique avec le port série
# attention !!! la vitesse de communication (baudrate) doit être la même entre la carte et le programme Python
# attention !!! le port doit être le même que celui choisi par la carte (à changer au cas par cas)
port_serie = serial.Serial(port = "/dev/ttyUSB0", baudrate = 9600)


# on crée un objet file : ouverture d'un fichier donnees.csv ouvert en écriture (w pour write)
file = open("donnees.csv", "w")

# on va enregistrer 10 données renvoyées par la carte
for i in range(10) : 
    ligne_recue = port_serie.readline()#on lit la ligne reçue en bytes (!!!)
    print(ligne_recue)# on affiche cette ligne en console
    ligne_recue_str = ligne_recue.decode("utf8")#on trsf la ligne reçue (en bytes) en string dans l'encodage de Python3
    print(ligne_recue_str)# on affiche en console
    #on ecrit dans le fichier donnees.csv pour svgd la ligne transformée de bytes en string
    file.write(ligne_recue_str)

# on ferme le fichier et l'objet port_serie
file.close()
port_serie.close()

