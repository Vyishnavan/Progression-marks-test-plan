#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#IIT ID:20221257
#WOU iD:w2001515
#Name: Sathalogithasiva Vyishnavan
#Date: 07/04/2023
#Part 1


#Initialize variables
EXIT_1='Y'
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
Progress_outcome=[]

credit = [0,20,40,60,80,100,120]

print ("-----------------***PROGRESSION OUTCOME***--------------------")        

def Histogram(Progress,Trailer,Retriever,Excluded):          
    print ("_"*130)
    print("Histogram") 
    print ("Progress ",Progress, ':  ',end='')
    
    for i in range(Progress):                          
        print('*',end='')                               
    print('\n')                                         
    print ("Trailer ",Trailer, ':   ',end='')
    for i in range (Trailer):
        print ('*',end='')
    print('\n')
    print ("Retriver ",Retriever, ':  ',end='')
    for i in range (Retriever):
        print('*',end='')
    print('\n')
    print ("Excluded ",Excluded, ':  ',end='')
    for i in range (Excluded):
        print('*',end='')
    print('\n')

    print ('      \n')
    print (Progress + Trailer + Retriever + Excluded,"Outcomes in total. ")
    print ("_"*130)

while True:
    exit_1="Y"
    print("Enter 1 - Can predict student progress.")
    print("Enter 2 - A teacher can predict a student's progress.")
    print("Enter 3 - End the Program.")
    Enter=input("Enter your Enter number : ")
    if Enter!="1" and Enter!="2" and Enter!="3": 
    
        print("Invalid Enter!!!")
    if Enter=="1":
        while True:
                while True:
                    try:
                          Pass = int(input("Please enter the pass Credits: "))               
                    except ValueError:
                                print("Integer required")
                                continue
                    else:
                          if Pass not in credit:
                                print("Out of range")
                          elif Pass in credit:
                                break

                Pass_list.append(Pass)
                
                while True:
                    try:
                          Defer =int(input("Please enter the defer credits:"))
                          
                    except ValueError:
                          print("integer required")
                          continue
                    else:
                          if Defer not in credit:
                                print("out of range")
                          elif Defer in credit:
                                break

                Defer_list.append(Defer)
                
                while True:
                    try:
                          Fail =int(input("Please enter the fail credits:"))               
                    except ValueError:
                                print("Integer required")
                                continue
                    else:
                         if Fail not in credit:
                               print("Out of range")
                         elif Fail in credit:
                               break

                Fail_list.append(Fail)
                
                while True:
                    Total= Pass + Defer + Fail
                    if Total != 120:
                          print("Total incorrect")
                          break
                    else:
                        if Pass==120:
                            print("Progress")
                            break
                    
                        elif Pass==100:
                            print("Progress(Module trailer)")
                            break
                
                        elif Pass!=120 and Pass!=100 and Fail >=0 and Fail <=60:                   
                            print("Module retriever")
                            break

                        else:                                                                     
                            print("Exclude")
                            break
                break
                            
    elif Enter=="2": 
        while EXIT_1=="Y":
            try:
                while True:
                    try:
                          Pass = int(input("Please enter the pass Credits: "))               
                    except ValueError:
                                print("Integer required")
                                continue
                    else:
                          if Pass not in credit:
                                print("Out of range")
                          elif Pass in credit:
                                break

                Pass_list.append(Pass)
                
                while True:
                    try:
                          Defer =int(input("Please enter the defer credits:"))          
                    except ValueError:
                          print("Integer required")
                          continue
                    else:
                          if Defer not in credit:
                                print("Out of range")
                          elif Defer in credit:
                                break

                Defer_list.append(Defer)
                
                while True:
                    try:
                          Fail =int(input("Please enter the fail credits:"))               
                    except ValueError:
                                print("Integer required")
                                continue
                    else:
                         if Fail not in credit:
                               print("Out of range")
                         elif Fail in credit:
                               break

                Fail_list.append(Fail)
                
                while True:
                    Total = Pass + Defer + Fail
                    if Total != 120:
                          print("Total incorrect")
                          break
                    else:
                        if Pass==120:
                            print("Progress")
                            Progress=Progress+1                                                   
                            Progress_outcome.append("Progress")
                        elif Pass==100:
                            print("Progress(Module trailer)")
                            Trailer=Trailer+1                                                      
                            Progress_outcome.append("Progress(Module trailer)")
                        elif Pass!=120 and Pass!=100 and Fail >=0 and Fail <=60:                   
                            print("Module retriever")
                            Retriever=Retriever+1                                                 
                            Progress_outcome.append("Module retriever")
                        else:                                                                     
                            print("Exclude")
                            Excluded=Excluded+1                                                  
                            Progress_outcome.append("Excluded")
                        break
#C
                print("Would you like to enter another set of data?")
                while True:
                    EXIT_1 = input("Please enter 'y' to continue or else enter 'q' to quit the program : ")
                    EXIT_1 = EXIT_1.upper()
                    if EXIT_1=='Y':
                        break
#D
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
              
#part 2
        print("part 2:")
        for i in range(len(Progress_outcome)):
            print(Progress_outcome[i],'-',  Pass_list[i],',', Defer_list[i],',', Fail_list[i])
            
#part 3
        print (" ")
        print("part 3:")
        f=open('Progression_outcome.txt', 'w')                 
        f=open('Progression_outcome.txt', 'a')                 
        for i in range(len(Progress_outcome)):                    
             a= "{} - {} , {} , {}\n ".format(Progress_outcome[i],Pass_list[i], Defer_list[i], Fail_list[i])
             f.write(a)
        f.close()                                             
        f=open('Progression_outcome.txt', 'r')                 
        for i in range(len(Progress_outcome)):
             a= "{} - {} , {} , {}  ".format(Progress_outcome[i],Pass_list[i], Defer_list[i], Fail_list[i])
             print(a)                                         
        f.close()

    elif Enter=="3":
        print("")
        print("\n______Go to the next python page for Part 4______\n")
        break
        

    
                                     
        



