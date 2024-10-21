def add (num1, num2, operation):
    returne=0
    if operation== "+": #  Tu operacia udris + daprintavs jams
        returne(num1+num2)
    elif operation=="-":# tu operacia unda  minuss - mashin gamoitans sxvaobas
        returne(num1-num2)
    elif operation=="*":  # tu opracia udris * mashin dabewdas namravls
         returne(num1*num2) 
    elif operation=="/": # tu opracia udris "/"mashin dabewdas ganayofs
        returne(num1/num2)
    else:# sxva shemtxvvevashi dabewdos errori
        returne("Error") 
    
    print(add(3,4,"+"))
    print(add(5,6, "-"))
    print(add(10,7,"*"))
    print(add(2,5,"/"))
