import os
number=input("Enter the number that you want to start from\npress h to help : ")
print("**************************************")
if number=="h":
    number=int(input("It takes a number from you. If it was a compound number, it shows you its divisor and writes 'no' and goes to the next number and does the same operation. If it was the prime number, it returns 'yes' to you, then you have to Press enter to start from the next number and find the next prime number \nEnter the number that you want to start from : "))
else:
    number=int(number)
divisor=2
mystr=''
while True:
    while divisor<number:  
        if number%divisor==0:
            mystr=mystr+' '+str(divisor)
        divisor+=1
    if mystr =='':
    	print(str(number)+" : yes")
    	if input('************************************** \npress "r" to restart the program\n**************************************')=="r":
            os.system( 'cls' )#change 'cls' to 'clear' if your OS is Mac or Linux
            number=int(input("Enter the number that you want to start from\n"))-1# it has -1 because at the continued One is added to it
            print("**************************************")

    else:
    	print(str(number)+' : 1'+mystr+' '+str(number) +' no'+'\n'+'*****')
    divisor=2
    number+=1
    mystr=''


# Created by Amirhoosein Foorjanizadeh 
#License: GNU General Public License Version 3(GPL3)