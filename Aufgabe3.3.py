
liste = [3,9,8,5,10,12,2,9,7]

def Zahlfinden (listenplatz):
    for listenplatz, wert in enumerate (liste):
        merker = listenplatz+1
        if wert == 4:
            print (merker)
            return True
            break
        else:
            merker = listenplatz+2
           
#if Zahlfinden(liste) == True:
 #   print ("Ja")
#else:
 #   print ("Nein")

Nachnamen = ["Bauer","Klaas","Grieb","Grieb","Franz","Weber","Schiller"]

def Namenfinden (listenplatz):
    for listenplatz, wert in enumerate (Nachnamen):
        merker = listenplatz+1
        if wert == ("Müller"):
            print ("Der Name befindet sich auf Platz")
            print (merker)
            return True
            break
        else:
            merker = listenplatz+2

#if Namenfinden(Nachnamen) != True:
 #   print ("Der Name befindet sich nicht in der Liste")

def Namenfolge (listenplatz):
    for listenplatz,wert in enumerate (Nachnamen):
        if listenplatz == 0:
            merker = wert
        else:
            if wert == merker:
                print ("Es gibt eine Dopplung")
        merker = wert

#Namenfolge(Nachnamen)

def Namendopplung (listenplatz):
    for listenplatz,wert in enumerate(Nachnamen):
        for i in (Nachnamen):
            if wert == i:
                print ("Es gibt eine Dopplung")
            else:
                continue

#Namendopplung(Nachnamen)

#i = 1
#merker = folge[0]
#counter = 1

#for i < n:
 #   if folge[i]<merker:
  #      merker = folge[i]
   #     counter = 1
    #else:
     #   if folge[i] == merker:
      #      counter = counter+1
    #i = i+1
#
#if counter>=2:
 #   print ("Ja")

Zahlen = [3,7,6,2,1,0,8,9]

def Zahlendopplung (listenplatzAußen):
    for listenplatzAußen,SchleifeAußen in enumerate(Zahlen):
        merker = SchleifeAußen
        for listenplatzInnen,SchleifeInnen in enumerate(Zahlen):
            if listenplatzInnen != listenplatzAußen:
                if merker == SchleifeInnen:
                    print ("ja")
                    return True

if Zahlendopplung(Zahlen) != True:
    print ("nein")




