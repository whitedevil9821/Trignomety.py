print("Welcome to PEGASUS")
n1=input("number\n")
opreator=input("opreator")
n2=input("number\n")
def functionexponent(n1,n2):
   try:
       print(int(n1)**int(n2))
   except:
       print(float(n1)**float(n2))
while (1):
    if opreator=="+":
        try:
            print("answer\n",int(n1)+int(n2))
            break

        except:
            print("answer\n",float(n1)+float(n2))
            break
    elif opreator=="-":
        try:
            print("answer\n",int(n1)-int(n2))
            break
        except:
            print("answer\n",float(n1)-float(n2))
            break
    elif opreator=="*":
        try:
            print("answer\n",int(n1)*int(n2))
            break
        except:
            print("answer\n",float(n1)*float(n2))
            break
    elif opreator=="/":
       try:
             print("answer\n",int(n1)/int(n2))
       except:
             print("answer\n",float(n1)/float(n2))

    elif opreator=="**":
        print("answer", functionexponent(n1, n2))




        break
    else:
        print("This mathematical operation not available yet\n 🥰🤩🤩\n coming soon")

    break










