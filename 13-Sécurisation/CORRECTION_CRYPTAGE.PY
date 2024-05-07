def cryptage(message, clef):
    longueur=len(clef)
    cryptogramme=''    
    
    for cpt in range(0, len(message)):
        
        caramessage=message[cpt] # extraction du caractère du message
        numero1=ord(caramessage) # Numérisation
       
        rang=(cpt) % longueur # Calcul du rang de la clef
        caraclef= clef[rang] # extraction du caractère de la clef.
        numero2=ord(caraclef) # Numérisation
            
        numero3 = numero1 ^ numero2 # Application du masque
        
        caracrypte=chr(numero3) # Transformation en caractère
        
        cryptogramme=cryptogramme + caracrypte # Concaténation
      
         
    return(cryptogramme)

crypto1=cryptage("Il fait super beau aujourd'hui", 'Test')

fichier = open("cryptage.txt", "w", encoding='utf8') # ouverture en mode write
fichier.write(crypto1)
fichier.close()

fichier = open("cryptage.txt", "r", encoding='utf8') # ouverture en mode read
cryptogramme=fichier.read()
fichier.close()

messageDecrypte=cryptage(cryptogramme, 'Test') # On décrypte !

fichier = open("decryptage.txt", "w", encoding='utf8')
fichier.write(messageDecrypte)
fichier.close()












    