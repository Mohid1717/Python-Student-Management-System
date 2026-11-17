import os 
import re
os.chdir(r'c:\Users\hf store\Documents\Python VS Code Programs')
students_record = []
with open('students record.txt') as F:
    reading=F.read()
    po = 0
    while(True):
        if(len(reading)==0):
            print("The file is empty.")
            break
        else:
            if("Roll number = " in reading[po : ]):
                s=reading.index("Roll number = " , po)
                e=reading.index('.' , s)
                block = reading[s : e]
                numbers = re.findall(r'\d+' , block)
                integer_numbers = [int(x) for x in numbers]
                s1 = block.index("Name") + len("Name = ")
                e1=block.index('\n' , s1)
                name = block [ s1 : e1 ]  
                students_record.append(integer_numbers[0])
                students_record.append(name)
                students_record.append(integer_numbers[1])
                po = e +1
            else:
                print()
                break 
while(True):
    print("Enter 'exit' anytime when you want to quit.")
    print()
    n=input("Enter the total number of the students = ")
    if(n.lower().strip()=="exit"):
        while(True):
            print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
            exit_confirmation_1=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
            if(len(exit_confirmation_1)==0):
                print("You entered nothing in the confirmation option for exit.")
                continue
            elif(len(exit_confirmation_1.strip())==0):
                print("You entered only spaces in the confirmation option for exit.")
                continue
            elif(exit_confirmation_1.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                continue
            elif(int(exit_confirmation_1)<0 or int(exit_confirmation_1)>1):
                print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                continue
            break
        if(int(exit_confirmation_1)==1):
            print("Quit.")
            exit()
        else:
            continue
    elif(len(n)==0):
        print("You entered nothing in the total number of the students option.")
        continue
    elif(len(n.strip())==0):
        print("You entered only spaces in the total number of the students option.")
        continue
    elif(n.strip().isalpha()==True):
        print("You entered alphabets in the total number of the students option , which is not allowed.")
        continue
    elif(n.strip().isdigit()==False):
        print("You entered symbols in the total number of the students option , which is not allowed.")
        continue
    elif(int(n)==0):
        print("The total number of the students = 0.")
        print("Entering total number of the students = 0 , results to quit.")
        exit()
    break
print("The total number of the students = ",n)


for i in range(1,int(n)+1):
    with open('students record.txt') as f:
        a=f.read()
    while(True):
        print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
        print("Enter 'exit' any time if you want to quit.")
        print()
        r=input(f"Enter the roll number of the student number {i} = ")
        if(r.strip().lower()=="exit"):
            while(True):
                exit_confirmation_2=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                if(len(exit_confirmation_2)==0):
                    print("You entered nothing in the confirmation option for exit.")
                    continue
                elif(len(exit_confirmation_2.strip())==0):
                    print("You entered only spaces in the confirmation option for exit.")
                    continue
                elif(exit_confirmation_2.strip().isnumeric()==False):
                    print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                    continue
                elif(int(exit_confirmation_2)<0 or int(exit_confirmation_2)>1):
                    print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                    continue
                break
            if(int(exit_confirmation_2)==1):
                print("Quit.")
                exit()
            else:
                continue
        elif(len(r)==0):
            print(f"You entered nothing in the roll number of the student number {i}.")
            continue
        elif(len(r.strip())==0):
            print(f"You entered only spaces in the roll number of the student number {i}.")
            continue
        elif(r.strip().isdecimal()==False):
            print(f"The entered roll number of the student number {i} must not contain alphabets or symbols.")
            continue
        elif(int(r.strip())  in students_record[0::3]):
            print(f"The entered roll number of the student number {i} is already taken by another student.")
            continue
        elif(int(r)<=0):
            print(f"The entered roll number of the student number {i} must be greater than 0.")
            continue
        elif(int(r.strip()) in students_record[0::3]):
            print(f"The entered roll number of the student number {i} is already taken by a student.")
            continue

        while(True):
            saving=input(f"Enter '1' if you want to save roll number : {r.strip()} of the student number {i} or Enter '0' if you do not want to save roll number : {r.strip()} of the student number {i} = ")
            print()
            if(saving.strip().lower()=="exit"):
                while(True):
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    exit_confirmation_3=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                    if(len(exit_confirmation_3)==0):
                        print("You entered nothing in the confirmation option for exit.")
                        continue
                    elif(len(exit_confirmation_3.strip())==0):
                        print("You entered only spaces in the confirmation option for exit.")
                        continue
                    elif(exit_confirmation_3.strip().isnumeric()==False):
                        print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                        continue
                    elif(int(exit_confirmation_3)<0 or int(exit_confirmation_3)>1):
                        print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                        continue
                    break
                if(int(exit_confirmation_3)==1):
                    print("Quit.")
                    exit()
                else:
                    continue
            elif(len(saving)==0):
                print(f"You entered nothing in saving option of the student number {i}.")
                continue
            elif(len(saving.strip())==0):
                print(f"You entered only spaces in saving option of the student number {i}.")
                continue
            elif(saving.strip().isdecimal()==False):
                print(f"The entered saving option of the student number {i} must be in numbers.")
                continue
            elif(int(saving)<0 or int(saving)>1):
                print(f"The entered saving option of the student number {i} cannot be any number other than '1' or '0'.")
                continue
            break
        if(saving.strip()=="1"):
            print(f"The roll number {r.strip()} of the student number {i} is saved.")
            print()
            print(f"The roll number of the student number {i} = ",r.strip())
            students_record.append(int(r.strip()))
        else:
            print(f"The roll number : {r.strip()} of the student number {i} is not saved.")
            print()
            continue
        break


    while(True):
        while(True):
            print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
            print("Enter 'exit' any time if you want to quit.")
            print()
            fn=input(f"Enter the first name of the student number {i} = ")
            if(fn.strip().lower()=="exit"):
                while(True):
                    exit_confirmation_4=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                    if(len(exit_confirmation_4)==0):
                        print("You entered nothing in the confirmation option for exit.")
                        continue
                    elif(len(exit_confirmation_4.strip())==0):
                        print("You entered only spaces in the confirmation option for exit.")
                        continue
                    elif(exit_confirmation_4.strip().isnumeric()==False):
                        print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                        continue
                    elif(int(exit_confirmation_4)<0 or int(exit_confirmation_4)>1):
                        print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                        continue
                    break
                if(int(exit_confirmation_4)==1):
                    print("Quit.")
                    exit()
                else:
                    continue
            elif(len(fn)==0):
                print(f"You entered nothing in the first name option of the student number {i}.")
                continue
            elif(len(fn.strip())==0):
                print(f"You entered only spaces in the first name option of the student number {i}.")
                continue
            elif(" " in fn.strip()):
                print(f"There should be no space or another name in the first name option of the student number {i}.")
                continue
            elif(fn.strip().isalpha()==False):
                print(f"You entered numbers or symbols in the first name option of the student number {i} which are not allowed.")
                continue
            print(f"The first name : {fn.strip()} of the student number {i} is accepted.")
            break

        while(True):
            asking=input(f"Enter '1' if the student number {i} has a last name or Enter '0' if the student number {i} does not have a last name = ")
            if(asking.strip().lower()=="exit"):
                while(True):
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    exit_confirmation_5=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                    if(len(exit_confirmation_5)==0):
                        print("You entered nothing in the confirmation option for exit.")
                        continue
                    elif(len(exit_confirmation_5.strip())==0):
                        print("You entered only spaces in the confirmation option for exit.")
                        continue
                    elif(exit_confirmation_5.strip().isnumeric()==False):
                        print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                        continue
                    elif(int(exit_confirmation_5)<0 or int(exit_confirmation_5)>1):
                        print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                        continue
                    break
                if(int(exit_confirmation_5)==1):
                    print("Quit.")
                    exit()
                else:
                    continue
            elif(len(asking)==0):
                print(f"You entered nothing in the option that do you have a last name or not of the student number {i} , which is not allowed.")
                print()
                continue
            elif(len(asking.strip())==0):
                print(f"You entered only spaces in the option that do you have a last name or not of the student number {i} , which is not allowed.")
                print()
                continue
            elif(asking.strip().isnumeric()==False):
                print(f"You entered alphabets or symbols in the option that do you have a last name or not of the student number {i} , which is not allowed.")
                print()
                continue
            elif(int(asking)<0 or int(asking)>1):
                print(f"You entered the number other than '1' or '0' in the option that do you have a last name or not of the student number {i} , which is not allowed.")
                print()
                continue
            break

        while(True):
            if(int(asking)==0):
                print(f"The student number {i} does not have a last name.")
                break
            else:
                ln=input(f"Enter the last name of the student number {i} = ")
                if(ln.strip().lower()=="exit"):
                    while(True):
                        print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                        exit_confirmation_6=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                        if(len(exit_confirmation_6)==0):
                            print("You entered nothing in the confirmation option for exit.")
                            continue
                        elif(len(exit_confirmation_6.strip())==0):
                            print("You entered only spaces in the confirmation option for exit.")
                            continue
                        elif(exit_confirmation_6.strip().isnumeric()==False):
                            print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                            continue
                        elif(int(exit_confirmation_6)<0 or int(exit_confirmation_6)>1):
                            print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                            continue
                        break
                    if(int(exit_confirmation_6)==1):
                        print("Quit.")
                        exit()
                    else:
                        continue
                elif(len(ln)==0):
                    print(f"You entered nothing in the last name option of the student number {i}.")
                    continue
                elif(len(ln.strip())==0):
                    print(f"You entered only spaces in the last name option of the student number {i}.")
                    continue
                elif(" " in ln.strip()):
                    print(f"There should be no space or another name in the last name option of the student number {i}.")
                    continue
                elif(ln.strip().isalpha()==False):
                    print(f"The entered last name of the student number {i} contains numbers or symbols, which are not allowed.")
                    continue
                print(f"The last name : {ln} of the student number {i} is accepted.")
                break

        while(True):
            confirmation_1=input(f"Enter '1' if you want to save the name of the student number {i} or Enter '0' if you do not want to save the name of the student number {i} = ")
            if(confirmation_1.strip().lower()=="exit"):
                while(True):
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    exit_confirmation_7=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                    if(len(exit_confirmation_7)==0):
                        print("You entered nothing in the confirmation option for exit.")
                        continue
                    elif(len(exit_confirmation_7.strip())==0):
                        print("You entered only spaces in the confirmation option for exit.")
                        continue
                    elif(exit_confirmation_7.strip().isnumeric()==False):
                        print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                        continue
                    elif(int(exit_confirmation_7)<0 or int(exit_confirmation_7)>1):
                        print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                        continue
                    break
                if(int(exit_confirmation_7)==1):
                    print("Quit.")
                    exit()
                else:
                    continue
            elif(len(confirmation_1)==0):
                print(f"You entered nothing in the confirmation option of the student number {i}.")
                continue
            elif(len(confirmation_1.strip())==0):
                print(f"You entered only spaces in the confirmation option of the student number {i}.")
                continue
            elif(confirmation_1.strip().isnumeric()==False):
                print(f"You entered alphabets or symbols in the confirmation option of the student number {i} which are not allowed.")
                continue
            elif(int(confirmation_1)<0 or int(confirmation_1)>1):
                print(f"You entered numbers other than '1' or '0' in the confirmation option of the student number {i} which are not allowed.")
                continue
            break

        if(int(confirmation_1)==1):
            if(int(asking)==1):
                print(f"The name : '{fn.strip() + " " + ln.strip()}' of the student number {i} is saved.")
                print()
                print(f"The name of the student number {i} = '{fn.strip() + " " + ln.strip()}'")
                students_record.append(fn.strip() + " " + ln.strip())

            else:
                print(f"The name : '{fn.strip()}' of the student number {i} is saved.")
                print()
                print(f"The name of the student number {i} = '{fn.strip()}'.")
                students_record.append(fn.strip())
        else:
            if(int(asking)==1):
                print(f"The name : '{fn.strip() + " " + ln.strip()}' of the student number {i} is not saved.")
            else:
                print(f"The name : '{fn.strip()}' of the student number {i} is not saved.")
            continue
        break

    while(True):
            print("Enter 'exit' anytime when you want to quit.")
            print()
            print("The maximum marks  = 100.")
            print("The minimum marks = 0.")
            marks=input(f"Enter the obtained marks of the student number {i} = ")
            if(marks.strip().lower()=="exit"):
                while(True):
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    exit_confirmation_8=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                    if(len(exit_confirmation_8)==0):
                        print("You entered nothing in the confirmation option for exit.")
                        continue
                    elif(len(exit_confirmation_8.strip())==0):
                        print("You entered only spaces in the confirmation option for exit.")
                        continue
                    elif(exit_confirmation_8.strip().isnumeric()==False):
                        print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                        continue
                    elif(int(exit_confirmation_8)<0 or int(exit_confirmation_8)>1):
                        print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                        continue
                    break
                if(int(exit_confirmation_8)==1):
                    print("Quit.")
                    exit()
                else:
                    continue
            elif(len(marks)==0):
                print(f"You entered nothing in the obtained marks of the student number {i} option.")
                continue
            elif(len(marks.strip())==0):
                print(f"You entered only spaces in the obtained marks of the student number {i} option.")
                continue
            elif(marks.strip().isnumeric()==False):
                print(f"You entered alphabets or symbols in the obtained marks of the student number {i} option , which is not allowed.")
                continue
            elif(int(marks)>100):
                print(f"The entered obtained marks of the student number {i} is greater than 100 but the maximum = 100.")
                continue
            while(True):
                print(f"The obtained marks : {marks} of the student number {i} is accepted.")
                print()
                confirmation_1=input(f"Enter '1' if you want to save the obtained marks : {marks} of the student number {i} or Enter '0' if you do not want to save the obtained marks : {marks} of the student number {i} = ")
                if(confirmation_1.strip().lower()=="exit"):
                    while(True):
                        print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                        exit_confirmation_9=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
                        if(len(exit_confirmation_9)==0):
                            print("You entered nothing in the confirmation option for exit.")
                            continue
                        elif(len(exit_confirmation_9.strip())==0):
                            print("You entered only spaces in the confirmation option for exit.")
                            continue
                        elif(exit_confirmation_9.strip().isnumeric()==False):
                            print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                            continue
                        elif(int(exit_confirmation_9)<0 or int(exit_confirmation_9)>1):
                            print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                            continue
                        break
                    if(int(exit_confirmation_9)==1):
                        print("Quit.")
                        exit()
                    else:
                        continue
                elif(len(confirmation_1)==0):
                    print(f"You entered nothing in the confirmation option of the student number {i} = ")
                    continue
                elif(len(confirmation_1.strip())==0):
                    print(f"You only entered spaces in the confirmation option of the student number {i}.")
                    continue
                elif(confirmation_1.strip().isnumeric()==False):
                    print(f"You entered alphabets or symbols in the confirmation option of the student number {i} , which is not allowed.")
                    continue
                elif(int(confirmation_1)<0 or int(confirmation_1)>1):
                    print(f"You entered numbers other than '1' or '0' in the confirmation option of the student number {i} , which is not allowed.")
                    continue
                break
            if(int(confirmation_1)==1):
                print(f"The obtained marks : {marks} of the student number {i} is saved.")
                students_record.append(int(marks.strip()))
                print()
                print(f"The obtained marks of the student number {i} = ",marks)
                break
            else:
                print(f"The obtained marks : {marks} of the student number {i} is not saved.")
                print()
                print()
                continue
    if(int(asking)==1):
        with open('students record.txt','a') as f:
            a=f.write(f'\n\nRoll number = {r} :- \n\tName = {fn.strip() + " " + ln.strip()}\n\tObtained Marks = {marks}.')
    else:
        with open('students record.txt','a') as f1:
            b=f1.write(f'\n\nRoll number = {r} :- \n\tName = {fn.strip()}\n\tObtained Marks = {marks}.')
print()
print()

while(True):
    print("Enter 'exit' anytime when you want to quit.")
    print()
    view_all=input("Enter '1' if you want to view all the entered students record or Enter '0' if you do not want to view all the entered students record = ")
    if(view_all.strip().lower()=="exit"):
        while(True):
            print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
            exit_confirmation_10=input("Enter '1' if you want to quit or Enter '0' if you do not want to quit = ")
            if(len(exit_confirmation_10)==0):
                print("You entered nothing in the confirmation option for exit.")
                continue
            elif(len(exit_confirmation_10.strip())==0):
                print("You entered only spaces in the confirmation option for exit.")
                continue
            elif(exit_confirmation_10.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                continue
            elif(int(exit_confirmation_10)<0 or int(exit_confirmation_10)>1):
                print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                continue
            break
        if(int(exit_confirmation_10)==1):
            print("Quit.")
            exit()
        else:
            continue
    elif(len(view_all)==0):
        print("You entered nothing in the viewing all entered students record option.")
        print()
        continue
    elif(len(view_all.strip())==0):
        print("You entered only spaces in the viewing all entered students record option.")
        continue
    elif(view_all.strip().isnumeric()==False):
        print("You entered alphabets or symbols in the viewing all entered students record option , which are not allowed.")
        continue
    elif(int(view_all)<0 or int(view_all)>1):
        print("You entered numbers other than '1' or '0' in the viewing all entered students record option , which are not allowed.")
        continue
    elif(int(view_all)==0):
        print("You do not want to view all the entered students record.")
        break
    else:
        for i in range(1,len(students_record)//3 + 1):
            print(f"The roll number of the student number {i} = {students_record[(i-1)*3]}.")
            print(f"The name of the student number {i} = {students_record[((i-1)*3)+1]}.")
            print(f"The obtained marks of the student number {i} = {students_record[((i-1)*3)+2]}.")
            print()
    break
while(True): #The outermost loop to controll all.
    while(True): #To handle search asking.
        print("Enter a word 'exit' ny time when you want to quit.")
        print()
        search_asking=input("Enter '1' if you want to search the students record or Enter '0' if you do not want to search the students record  = ")
        if(search_asking.strip().lower()=="exit"):
            while(True): #To handle exit confirmation.
                print("Quiting will close the system and no entered data will be saved !")
                exit_confirmation_11=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_11)==0):
                    print("You entered nothing in the exit confirmation option.")
                    continue
                elif(len(exit_confirmation_11.strip())==0):
                    print("You entered only spaces in the exit confirmation option.")
                    continue
                elif(exit_confirmation_11.strip().isdecimal()==False):
                    print("You entered alphabets or symbols in the exit confirmation option which are not allowed.")
                    continue
                elif(int(exit_confirmation_11)<0 or int(exit_confirmation_11)>1):
                    print("You entered number other than '1' or '0' in the exit confirmation option which are not allowed.")
                    continue
                break
            if(int(exit_confirmation_11)==1):
                print("Quit , no entered data is saved!")
                exit()
            else:
                continue
        elif(len(search_asking)==0):
            print("You entered only spaces in the search asking permission for the student.")
            continue
        elif(len(search_asking.strip())==0):
            print("You entered only spaces in the search asking permission for the student.")
            continue
        elif(search_asking.strip().isdecimal()==False):
            print("You entered alphabets or symbols in the search asking permission for the student which are not allowed.")
            continue
        elif(int(search_asking)<0 or int(search_asking)>1):
            print("You entered numbers other than '1' or '0' in the search asking permission for the student.")
            continue
        break
    if(int(search_asking)==0):
        print("The searching of students record is ended.")
        break
    while(True): #For searching the roll number.
        print("Enter a word 'exit' any time when you want to quit.")
        print("Enter a word 'back' if you forget roll numbe rof the stduent and want to go back to the search asking permission option for the student.")
        print()
        search=input("Enter the roll number of the student whose record you want to find = ")
        if(search.strip().lower()=="exit"):
            while(True): #for handling exit confirmation_12.
                print("Quiting will close the system and no entered data will be saved !")
                exit_confirmation_12=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_12)==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(len(exit_confirmation_12.strip())==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(exit_confirmation_12.strip().isdecimal()==False):
                    print("You entered oalphabets or symbols in the exit confirmtaion option.")
                    continue
                elif(int(exit_confirmation_12)<0 or int(exit_confirmation_12)>1):
                    print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                    continue
                break
            if(int(exit_confirmation_12)==1):
                print("Quiting and no entered data is saved!")
                exit()
            else:
                continue
        elif(len(search)==0):
            print("You entered nothing in the roll number option to search for the student.")
            continue
        elif(len(search.strip())==0):
            print("You entered nothing in the roll number option to search for the student.")
            continue
        elif(search.strip().lower()=="back"):
            break
        elif(search.strip().isdecimal()==False):
            print("You entered alphabets or symbols in the roll number option to search for the student which are not allowed.")
            continue
        elif((int(search.strip()) in students_record[0::3])==False):
            print("The entered roll number to search for the student is not in the students record !")
            continue
        break
    if(search.strip().lower()=="back"):
        print("You went back to the search asking permission option for the student.")
        continue
    position=(students_record[0::3].index(int(search.strip())))*3
    print("The roll number of the searched student = ",students_record[position])
    print("The name of the searched student = ",students_record[position+1])
    print("The obtained marks of the searched student = ",students_record[position+2])
    print()
while(True):#To handle from update asking to 
    while(True):#To handle update asking.
        print("Enter a word 'exit' anytime when you want to quit.")
        print()
        print("Note that you can only update the name and obtained marks of the student not the roll number.")
        update_asking=input("Enter '1' if you want to update the students record option or Enter '0' if you do not want to update the students record = ")
        if(update_asking.strip().lower()=="exit"):
            while(True):#To handle exit confirmation_13
                print("Quiting will close the system and no entered data will be saved !")
                exit_confirmation_13=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_13)==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(len(exit_confirmation_13.strip())==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(exit_confirmation_13.strip().isdecimal()==False):
                    print("You entered oalphabets or symbols in the exit confirmtaion option.")
                    continue
                elif(int(exit_confirmation_13)<0 or int(exit_confirmation_13)>1):
                    print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                    continue
                break
            if(int(exit_confirmation_13)==1):
                print("Quiting and no entered data is saved!")
                exit()
            else:
                continue
        elif(len(update_asking)==0):
            print("You entered only spaces in the update asking permission for the student.")
            continue
        elif(len(update_asking.strip())==0):
            print("You entered only spaces in the update asking permission for the student.")
            continue
        elif(update_asking.strip().isdecimal()==False):
            print("You entered alphabets or symbols in the update asking permission for the student which are not allowed.")
            continue
        elif(int(update_asking)<0 or int(update_asking)>1):
            print("You entered numbers other than '1' or '0' in the update asking permission for the student.")
            continue
        break
    if(int(update_asking)==0):
        print("The updating process of the students record is ended.")
        break
    while(True):#To handle roll number.
        update=input("Enter the roll number of the student whose record you want to update = ")
        if(update.strip().lower()=="exit"):
            while(True):#To handle exit confirmation_14
                print("Quiting will close the system and no entered data will be saved !")
                exit_confirmation_14=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_14)==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(len(exit_confirmation_14.strip())==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(exit_confirmation_14.strip().isdecimal()==False):
                    print("You entered oalphabets or symbols in the exit confirmtaion option.")
                    continue
                elif(int(exit_confirmation_14)<0 or int(exit_confirmation_14)>1):
                    print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                    continue
                break
            if(int(exit_confirmation_14)==1):
                print("Quiting and no entered data is saved!")
                exit()
            else:
                continue
        elif(len(update)==0):
            print("You entered nothing in the roll number option to update the student's record.")
            continue
        elif(len(update.strip())==0):
            print("You entered only spaces in the roll number option to update the student's record.")
            continue
        elif(update.strip().isdecimal()==False):
            print("The entered roll number of the student number must not contain alphabets or symbols fo updating the student's record.")
            continue
        elif(int(update)<=0):
            print("The entered roll number to update the student's record must be greater than 0.")
            continue
        elif((int(update.strip()) in students_record[0::3])==False):
            print("The entered roll number to update the student's record is not in the students record.")
            continue
        break
    position_1=(students_record[0::3].index(int(update)))*3
    print("The roll number of the student = ",students_record[position_1],".")
    print("The current name of the student = ",students_record[(position_1)+1],".")
    print("The current obtained marks of the student = ",students_record[(position_1)+2],".")
    print()
    while(True):#To handle the update thing option.
        print("Enter a word 'exit' anytime when you want to quit.")
        print()
        what_update=input("Enter '1' if you want to update the 'current name' of the student or Enter '2' if you want to update the 'current obtained marks' of the student = ")
        if(what_update.strip().lower()=="exit"):
            while(True):#to handle the exit confirmation_15
                print("Quiting will close the system and no entered data will be saved !")
                exit_confirmation_15=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_15)==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(len(exit_confirmation_15.strip())==0):
                    print("You entered only spaces in the exit confirmtaion option.")
                    continue
                elif(exit_confirmation_15.strip().isdecimal()==False):
                    print("You entered oalphabets or symbols in the exit confirmtaion option.")
                    continue
                elif(int(exit_confirmation_15)<0 or int(exit_confirmation_15)>1):
                    print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                    continue
                break
            if(int(exit_confirmation_15)==1):
                print("Quiting and no entered data is saved!")
                exit()
            else:
                continue
        elif(len(what_update)==0):
            print("You entered only spaces in the what to update option for the student.")
            continue
        elif(len(what_update.strip())==0):
            print("You entered only spaces in the what to update opyion for the student.")
            continue
        elif(what_update.strip().isdecimal()==False):
            print("You entered alphabets or symbols in the what to update option for the student which are not allowed.")
            continue
        elif(int(what_update)<1 or int(what_update)>2):
            print("You entered numbers other than '1' or '2' in the what to update aoption for the student which are not allowed.")
            continue
        break
    if(int(what_update)==1):
        while(True):#To handle the first name having.
            print("Enter a word 'exit' anytime when you want to quit.")
            print()
            n_fn_name=input("Enter the new first name of the student = ")
            if(n_fn_name.strip().lower()=="exit"):
                while(True):#to handle the exit confirmation _ 16
                    print("Quiting will close the system and no entered data will be saved!")
                    print()
                    exit_confirmation_16=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_16)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_16.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_16.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_16)<0 or int(exit_confirmation_16)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_16)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                    continue
            elif(len(n_fn_name)==0):
                print("You entered nothing in the first name option of the student to update its record.")
                continue
            elif(len(n_fn_name.strip())==0):
                print("You entered only spaces in the first name option of the student to update its record.")
                continue
            elif(" " in n_fn_name.strip()):
                print("There should be no space or another name in the first name option of the student number to update its record.")
                continue
            elif(n_fn_name.strip().isalpha()==False):
                print("You entered numbers or symbols in the first name option of the student to update its record which are not allowed.")
                continue
            break
        while(True):#To handle asking the last name have or not.
            asking_ln=input("Enter '1' if the new name has a last name or Enter '0' if the new name does not have a last name = ")
            print("Enter a word 'exit' anytime when you want to quit.")
            print()
            if(asking_ln.strip().lower()=="exit"):
                while(True):#To handle the exit confirmation_17.
                    print("Quiting will close the system and no entered data will be saved !")
                    exit_confirmation_17=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_17)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_17.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_17.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_17)<0 or int(exit_confirmation_17)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_17)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                    continue
            elif(len(asking_ln)==0):
                print("You entered nothing in the option that do you have a last name or not to update the student's record.")
                continue
            elif(len(asking_ln.strip())==0):
                print("You entered only spaces in the option that do you have a last name or not to update the student's record.")
                continue
            elif(asking_ln.strip().isdecimal()==False):
                print("The entered option that do you have a last name or not must not contain alphabets or symbols for updating the student's record.")
                continue
            elif(int(asking_ln)<0 or int(asking_ln)>1):
                print("The entered option that do you have a last name or not to update the student's record must not be numbers other than '1' or '0'.")
                continue
            break
        if(int(asking_ln)==1):
            while(True):
                n_ln_name=input("Enter the new last name of the student = ")
                if(n_ln_name.strip().lower()=="exit"):
                    while(True):#To handle the exit confirmation _ 18.
                        exit_confirmation_18=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                        if(len(exit_confirmation_18)==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(len(exit_confirmation_18.strip())==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(exit_confirmation_18.strip().isdecimal()==False):
                            print("You entered oalphabets or symbols in the exit confirmtaion option.")
                            continue
                        elif(int(exit_confirmation_18)<0 or int(exit_confirmation_18)>1):
                            print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                            continue
                        break
                    if(int(exit_confirmation_18)==1):
                        print("Quiting and no entered data is saved!")
                        exit()
                    else:
                        continue
                elif(len(n_ln_name)==0):
                    print("You entered nothing in the last name option of the student to update its record.")
                    continue
                elif(len(n_ln_name.strip())==0):
                    print("You entered only spaces in the last name option of the student to update its record.")
                    continue
                elif(" " in n_ln_name.strip()):
                    print("There should be no space or another name in the last name option of the student number to update its record.")
                    continue
                elif(n_ln_name.strip().isalpha()==False):
                    print("You entered numbers or symbols in the last name option of the student to update its record which are not allowed.")
                    continue
                break
            print("The old stored name of the student = ",students_record[(position_1)+1],".")
            print("The new name of the student = ",n_fn_name.strip() + " " + n_ln_name.strip(),".")
            while(True):#To handle the update confirmation.
                update_confirmation=input(f"Enter '1' if you are confirm to update the name of the roll number {students_record[position_1]} from {students_record[(position_1)+1]} to {n_fn_name.strip() + " " + n_ln_name.strip()} or Enter '0' if you are not confirm = ")
                if(update_confirmation.strip().lower()=="exit"):
                    while(True):#Tp handle the exit confirmation _ 19.
                        exit_confirmation_19=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                        if(len(exit_confirmation_19)==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(len(exit_confirmation_19.strip())==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(exit_confirmation_19.strip().isdecimal()==False):
                            print("You entered oalphabets or symbols in the exit confirmtaion option.")
                            continue
                        elif(int(exit_confirmation_19)<0 or int(exit_confirmation_19)>1):
                            print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                            continue
                        break
                    if(int(exit_confirmation_19)==1):
                        print("Quiting and no entered data is saved!")
                        exit()
                    else:
                        continue   
                elif(len(update_confirmation)==0):
                    print("You entered nothing in the update confirmation option to change the name of the student.")
                    continue
                elif(len(update_confirmation.strip())==0):
                    print("You entered only spaces in the update confirmation option to change the name of the student.")
                    continue
                elif(update_confirmation.strip().isdecimal()==False):
                    print("The entered update confirmation option must not contain alphabets or symbols to change the name of the student.")
                    continue
                elif(int(update_confirmation)<0 or int(update_confirmation)>1):
                    print("The entered update confirmation option must not be numbers other than '1' or '0'.")
                    continue
                break
            if(int(update_confirmation)==1):
                old_name = students_record[(position_1)+1]
                students_record[(position_1)+1]=n_fn_name.strip() + " " + n_ln_name.strip()
                with open('students record.txt') as f2:
                    c=f2.read()
                    start=c.index(f"Roll number = {update} :-")
                    end=c.index('.' , start)
                    old_block=c[start : end + 1]
                    new_name = n_fn_name.strip() + " " + n_ln_name.strip()
                    new_block = old_block.replace(f"Name = {old_name}", f"Name = {new_name}")
                with open('students record.txt' , 'w') as f3:
                    updated = c.replace(old_block , new_block)
                    f3.write(updated)
                print(f"The new name of the roll number : {students_record[position_1]} is {n_fn_name.strip() + " " + n_ln_name.strip()} saved and updated.")
                continue
            else:
                print(f"The new name of the roll number student : {students_record[position_1]} is not {n_fn_name.strip() + " " + n_ln_name.strip()} saved.")
                print("The name of the student in the students record = ",students_record[(position_1)+1])
                continue
        else:
            while(True):#To handle the update confirmation for not having a last name.
                update_confirmation=input(f"Enter '1' if you are confirm to update the name of the roll number {students_record[position_1]} from {students_record[(position_1)+1]} to {n_fn_name.strip()} or Enter '0' if you are not confirm = ")
                if(update_confirmation.strip().lower()=="exit"):
                    while(True):#Tp handle the exit confirmation _ 20.
                        exit_confirmation_20=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                        if(len(exit_confirmation_20)==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(len(exit_confirmation_20.strip())==0):
                            print("You entered only spaces in the exit confirmtaion option.")
                            continue
                        elif(exit_confirmation_20.strip().isdecimal()==False):
                            print("You entered oalphabets or symbols in the exit confirmtaion option.")
                            continue
                        elif(int(exit_confirmation_20)<0 or int(exit_confirmation_20)>1):
                            print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                            continue
                        break
                    if(int(exit_confirmation_20)==1):
                        print("Quiting and no entered data is saved!")
                        exit()
                    else:
                        continue   
                elif(len(update_confirmation)==0):
                    print("You entered nothing in the update confirmation option to change the name of the student.")
                    continue
                elif(len(update_confirmation.strip())==0):
                    print("You entered only spaces in the update confirmation option to change the name of the student.")
                    continue
                elif(update_confirmation.strip().isdecimal()==False):
                    print("The entered update confirmation option must not contain alphabets or symbols to change the name of the student.")
                    continue
                elif(int(update_confirmation)<0 or int(update_confirmation)>1):
                    print("The entered update confirmation option must not be numbers other than '1' or '0'.")
                    continue
                break
            if(int(update_confirmation)==1):
                old_first_name = students_record[(position_1)+1]
                students_record[(position_1)+1]=n_fn_name.strip()
                with open('students record.txt') as f4:
                    d=f4.read()
                    start=d.index(f"Roll number = {update} :-")
                    end=d.index('.' , start)
                    old_block_1=d[start : end +1]
                    new_block_1 = old_block_1.replace(f"Name = {old_first_name}", f"Name = {n_fn_name.strip()}")
                with open('students record.txt' , 'w') as f5:
                    updated_1=d.replace(old_block_1 , new_block_1)
                    f5.write(updated_1)
                print(f"The new name of the roll number : {students_record[position_1]} is {n_fn_name.strip()} saved.")
                continue
            else:
                print(f"The new name of the roll number : {students_record[position_1]} is {n_fn_name.strip()} not saved.")
                continue
    else:
        while(True):#To handle the obtained marks
            print("The maximum obtained marks for the student = 100.")
            print("The minimum obtained marks for the student = 0.")
            print()
            n_marks=input(f"Enter the new obtained marks of the roll number : {students_record[position_1]} = ")
            if(n_marks.strip().lower()=="exit"):
                while(True):#To handle the exit confirmation _21.      
                    exit_confirmation_21=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_21)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_21.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_21.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_21)<0 or int(exit_confirmation_21)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_21)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                    continue
            elif(len(n_marks)==0):
                print("You entered nothing in the new obtained marks of the student option.")
                continue
            elif(len(n_marks.strip())==0):
                print("You entered only spaces in the new obtained marks of the student option.")
                continue
            elif(n_marks.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the new obtained marks of the student option , which is not allowed.")
                continue
            elif(int(n_marks)>100):
                print("The new entered obtained marks of the student is greater than 100 but the maximum = 100.")
                continue
            break
        while(True):#to handle the update marks confirmation.
            print(f"The current obtained marks of the roll number : {students_record[(position_1)]} = ",students_record[(position_1)+2])
            n_marks_confirmation=input(f"Enter '1' if you are confirm to update the roll number : {students_record[(position_1)]} mark's from {students_record[(position_1)+2]} to {int(n_marks.strip())} = ")
            if(n_marks_confirmation.strip().lower()=="exit"):
                while(True):#To handle the exit confirmation _ 22.
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    print()
                    exit_confirmation_22=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_22)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_22.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_22.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_22)<0 or int(exit_confirmation_22)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_22)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                     continue
            elif(len(n_marks_confirmation)==0):
                print("You entered nothing in the new obtained marks confirmation option.")
                continue
            elif(len(n_marks_confirmation.strip())==0):
                print("You entered only spaces in the new obtained marks confirmation option.")
                continue
            elif(n_marks_confirmation.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the new obtained marks confirmation option , which is not allowed.")
                continue
            elif(int(n_marks_confirmation)<0 or int(n_marks_confirmation)>1):
                print("The new entered obtained marks confirmation option cannot be '1' or '0' number.")
                continue
            break
        if(int(n_marks_confirmation)==1):
            old_marks=students_record[(position_1)+2]
            students_record[(position_1)+2]=int(n_marks.strip())
            with open('students record.txt') as f6:
                e=f6.read()
                start=e.index(f"Roll number = {update} :-")
                end=e.index('.' , start)
                old_block_2 = e[start : end + 1]
                new_block_2 = old_block_2.replace(f"Obtained Marks = {old_marks}.",f"Obtained Marks = {n_marks.strip()}.")
            with open('students record.txt' , 'w') as f7:
                updated_2=e.replace(old_block_2 , new_block_2)
                f7.write(updated_2)
            print(f"The new obtained marks of the roll number : {students_record[position_1]} which is {int(n_marks.strip())} is saved and updated in the students record.")
            continue
        else:
            print(f"The new obtained marks of the roll number : {students_record[position_1]} which is {int(n_marks.strip())} is not saved in the students record.")
            continue
while(True):#Outermost.
    while(True):#Delete asking.
        delete_asking=input("Enter '1' if you want to delete all the records of a student or Enter '0' if you do not want to delete all the records of a student = ")
        if(delete_asking.strip().lower()=="exit"):
            while(True):#exit confirmation 23.
                print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                print()
                exit_confirmation_23=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                if(len(exit_confirmation_23)==0):
                    print("You entered nothing in the confirmation option for exit.")
                    continue
                elif(len(exit_confirmation_23.strip())==0):
                    print("You entered only spaces in the confirmation option for exit.")
                    continue
                elif(exit_confirmation_23.strip().isnumeric()==False):
                    print("You entered alphabets or symbols in the confirmation option for exit which are not allowed.")
                    continue
                elif(int(exit_confirmation_23)<0 or int(exit_confirmation_23)>1):
                    print("You entered numbers other than '1' or '0' in the confirmation option for exit which are not allowed.")
                    continue
                break
            if(int(exit_confirmation_23)==1):
                print("Quit.")
                exit()
            else:
                continue
        elif(len(delete_asking)==0):
            print("You entered nothing in the new obtained marks confirmation option.")
            continue
        elif(len(delete_asking.strip())==0):
            print("You entered only spaces in the new obtained marks confirmation option.")
            continue
        elif(delete_asking.strip().isnumeric()==False):
            print("You entered alphabets or symbols in the new obtained marks confirmation option , which is not allowed.")
            continue
        elif(int(delete_asking)<0 or int(delete_asking)>1):
            print("The new entered obtained marks confirmation option cannot be '1' or '0' number.")
            continue
        break
    if(int(delete_asking)==1):
        if(len(students_record)==0):
            print("There is no record of any student in the file to be deleted.")
            break
        while(True):#Asking roll number to delete.
            delete_r=input("Enter the roll number of the student whose all record you want to delte from the students record = ")
            if(delete_r.strip().lower()=="exit"):
                while(True):#To handle the exit confirmation _ 24
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    print()
                    exit_confirmation_24=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_24)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_24.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_24.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_24)<0 or int(exit_confirmation_24)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_24)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                    continue
            elif(len(delete_r)==0):
                print("You entered nothing in the roll number option to delete the students record.")
                continue
            elif(len(delete_r.strip())==0):
                print("You entered only spaces in the roll number option option to delte the students record.")
                continue
            elif(delete_r.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the roll number option to delete the students record , which is not allowed.")
                continue
            elif((int(delete_r) in students_record[0::3])==False):
                print("The entered roll number to delete the students record is not in the current students record.")
                continue
            break
        while(True):#For deleting confirmation.
            delete_confirmation=input(f"Enter '1' if you are confirm to delete all the information of roll number : {delete_r} or Enter '0' if you are not confirm to delete all the information of roll number : {delete_r} = ")
            if(delete_confirmation.strip().lower()=="exit"):
                while(True):#To handle the exit confirmation _ 25.
                    print("Quit will exit the whole system. Previously saved records will be preserved, but incomplete records will not be saved.")
                    print()
                    exit_confirmation_25=input("Enter '1' if you are confirm to quit or Enter '0' if you are not confirm to quit = ")
                    if(len(exit_confirmation_25)==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(len(exit_confirmation_25.strip())==0):
                        print("You entered only spaces in the exit confirmtaion option.")
                        continue
                    elif(exit_confirmation_25.strip().isdecimal()==False):
                        print("You entered oalphabets or symbols in the exit confirmtaion option.")
                        continue
                    elif(int(exit_confirmation_25)<0 or int(exit_confirmation_25)>1):
                        print("You entered numbers other than '1' or '0' in the exit confirmtaion option.")
                        continue
                    break
                if(int(exit_confirmation_25)==1):
                    print("Quiting and no entered data is saved!")
                    exit()
                else:
                    continue
            elif(len(delete_confirmation)==0):
                print("You entered nothing in the deleting student record option.")
                continue
            elif(len(delete_confirmation.strip())==0):
                print("You entered only spaces in the deleting student record option.")
                continue
            elif(delete_confirmation.strip().isnumeric()==False):
                print("You entered alphabets or symbols in the deleting student record option , which is not allowed.")
                continue
            elif(int(delete_confirmation)<0 or int(delete_confirmation)>1):
                print("You entered numbers other thn '1' or '0' in the deleting student record option , which is not allowed.")
                continue
            break
        if(int(delete_confirmation)==1):
            position=(students_record[0::3].index(int(delete_r)))*3
            del students_record[position]
            del students_record[position]
            del students_record[position]
            with open('students record.txt') as f8:
                f=f8.read()
                start=f.index(f"Roll number = {delete_r} :-")
                end=f.index('.' , start)
                old_data=f[start : end +1]
                new_data=f.replace(old_data , "")
            with open('students record.txt' , 'w') as f9:
                f9.write(new_data)
            print(f"All the records of the roll number : {delete_r} is deleted.")
            continue
        else:
            print(f"All the records of the roll number : {delete_r} is not deleted.")
            continue
    else:
        print("The deleting process of a student is ended.")
        break