#Nun lass uns eine Übungsaufgabe durchgehen, die das if elif, 
#und else-Konzept anwendet: Überprüfe, ob eine Zahl gerade oder ungerade ist.

#eine Gerade Zahl : 2,4,6 also durch 2 teilbar
#ungerade Zahl, ist eien zahl die beim teilen durch2, eienn rest von 1 hat. also 1,3,5

zahl = int(input('wie lautet deine zahl? mal schauen ob sie gerade oder ungerade ist.'))

if zahl % 2 == 0:
    print('Die zahl ist gerade wow.')
else:
    print('Die zahl ist ungerade lol.')