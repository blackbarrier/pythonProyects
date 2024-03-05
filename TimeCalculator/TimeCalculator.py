DAYS={"MONDAY":"TUESDAY",
      "TUESDAY":"WEDNESDAY",
      "WEDNESDAY":"THURSDAY",
      "THURSDAY":"FRIDAY",
      "FRIDAY":"SATURDAY",
      "SATURDAY":"SUNDAY",
      "SUNDAY":"MONDAY"}

def stringToHour(hour):
    hour=hour.split(":")
    hora=int(hour[0])
    minutos=int(hour[1])
    return hora, minutos

def determineDay(today,dias):
    today=today.upper()    
    i=0
    while i!=dias:
        today=(DAYS[today])
        i+=1
    today=today.capitalize()
    return today

def add_time(start, duration, today=""):

    #Declaracion de variables
    part=start[-2:]
    start=start[0:5]
    start=(stringToHour(start))
    duration=(stringToHour(duration))

    #Defino la hora resultante
    hora=(start[0]+duration[0])
    if part=="PM" and start[0]!=12:
        hora+=12
    #Defino los minutos resultantes
    minutos=(start[1]+duration[1])

    #Cantidad de horas sumadas por 60min
    sumaHoras=(minutos//60)
    #Sumo las horas calculadas
    hora+=sumaHoras
    #Resto los minutos ya sumados en horas
    minutos-=(60*sumaHoras)

    #Cantidad de dias sumadas por 24hs.
    dias=(hora//24)
    

    #Sumo los dias calculadas
    if dias==0:
        mssg=""
    elif dias==1:
        mssg=" (next day)"
    else:
        mssg=f" ({dias} days later)"
    
    
    #Resto las horas ya sumadas en dias.
    hora-=(24*dias)
    
   

   #Formato de 24hs a 12hs.
    
    if hora<=11 and minutos<=59:
        part="AM"
        if hora==00:
            hora+=12 
    else:
        part="PM"
        if hora!=12:
            hora-=12
    
    if 0 <= minutos <= 9:
        minutos="0"+str(minutos)


    if today!="":
        diaCaulculado=determineDay(today,dias)
        new_time=f"{hora}:{minutos} {part}, {diaCaulculado}{mssg}"
    else:
        new_time=f"{hora}:{minutos} {part}{mssg}"

    #Muestra de resultados.    
    print("."+new_time+".")


add_time("3:30 PM", "2:12", "Monday")