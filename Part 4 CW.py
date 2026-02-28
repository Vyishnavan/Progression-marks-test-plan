# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
#IIT ID:20221257
#WOU iD:w2001515
#Name: Sathalogithasiva Vyishnavan
#Date: 07/04/2023
#Part 4

#Initialize variables
EXIT_1="Y"
Total=0
Progress=0
Trailer=0
Retriever=0
Excluded=0
Pass=0
Defer=0
Fail=0
Pass_list=[]
Defer_list=[]
Fail_list=[]
ID_list=[]
ID_num=""
Progress_outcome=[]
dictionary_new={}

credit =[0,20,40,60,80,100,120]

#Part 4

def dictionary(name):
    dictionary_new[ID_num]=name+str(new_list).strip("][")    
    
    

def Histogram(Progress,Trailer,Retriever,Excluded):          
    print ("_"*130)
    print("Histogram") 
    print ("Progress ",Progress, ':  ',end='')          
    for c in range(Progress):                           
        print('*',end='')                                
    print('\n')                                           
    print ("Trailer ",Trailer, ':   ',end='')
    for c in range (Trailer):
        print ('*',end='')
    print('\n')
    print ("Retriver ",Retriever, ':  ',end='')
    for c in range (Retriever):
        print('*',end='')
    print('\n')
    print ("Excluded ",Excluded, ':  ',end='')
    for c in range (Excluded):
        print('*',end='')
    print('\n')

    print ('      \n')
    print (Progress + Trailer + Retriever + Excluded,"Outcomes in total. ")
    print ("_"*130)
    
while EXIT_1=="Y":
    ID_num=input("Please Enter your student ID: ")
    try:
        while True:
            try:
                  Pass = int(input("Please enter the pass Credits: "))              
            except ValueError:
                        print("Integer Required")
                        continue
            else:
                  if Pass not in credit:
                        print("Out of range")
                  elif Pass in credit:
                        break

        
        
        while True:
            try:
                  Defer =int(input("Please enter the defer credits:"))             
            except ValueError:
                  print("Integer Required")
                  continue
            else:
                  if Defer not in credit:
                        print("out of range")
                  elif Defer in credit:
                        break

        
        
        while True:
            try:
                  Fail =int(input("Please enter the fail credits:"))              
            except ValueError:
                        print("Integer Required")
                        continue
            else:
                 if Fail not in credit:
                       print("Out of range")
                 elif Fail in credit:
                       break

        
        
        while True:
            Total = Pass + Defer + Fail
            if Total != 120:
                  print("Total incorrect")
                  break
            new_list =[Pass,Defer,Fail]
        
        
            if Pass==120:
                print("Progress")
                Progress=Progress+1                                                   
                dictionary("Progress - ")
            elif Pass==100:
                print("Progress(module trailer)")
                Trailer=Trailer+1 
                dictionary("Progress(module trailer) - ")
                
            elif Pass!=120 and Pass!=100 and Fail >=0 and Fail <=60:                   
                print("Module retriever")
                Retriever=Retriever+1                                                 
                dictionary("Module retriever - ")
            else:                                                                     
                print("Exclude")
                Excluded=Excluded+1                                                   
                dictionary("Excluded - ")
            break

        print("Would you like to enter another set of data?")
        while True:
            EXIT_1 = input("Please enter 'y' to continue or else enter 'q' to quit the program : ")
            EXIT_1 = EXIT_1.upper()
            if EXIT_1=='Y':
                break

            elif EXIT_1=='Q':
                Histogram(Progress,Trailer,Retriever,Excluded)                                                    
                Total = Total+1                                                                           
                outcomes=[ 'Progress' , 'Trailer' ,' Retriever' , 'Excluded' ]
                Total_outcomes= [ Progress , Trailer , Retriever , Excluded ]
                break

            else :
                print ("Your input is wrong !")
                
            
    except ValueError:
      print("Integer Required")

print("")
print("part 4:")
for key, value in dictionary_new.items():
    print(key,":",value ,end=" ")
      
print("")
print("\n Thank You \n")
print("\nProgramme is Quited by user !\n")


            

        
                
                
    
    
