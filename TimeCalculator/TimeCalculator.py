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

    #Variables declaration
    part=start[-2:]
    start=start[0:5]
    start=(stringToHour(start))
    duration=(stringToHour(duration))

    #Define hour
    hora=(start[0]+duration[0])
    if part=="PM" and start[0]!=12:
        hora+=12
    #Define minutes
    minutos=(start[1]+duration[1])

    #Format    
    sumaHoras=(minutos//60)
    hora+=sumaHoras
    minutos-=(60*sumaHoras)

    #Days
    dias=(hora//24)    
    if dias==0:
        mssg=""
    elif dias==1:
        mssg=" (next day)"
    else:
        mssg=f" ({dias} days later)"    
    
    hora-=(24*dias)  

   # 24hs To 12hs.        
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

    #Show results.         
    return new_time