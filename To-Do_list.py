from time import sleep
print("~~~~~~~TO DO LIST APP~~~~~~~\n")

file_name=input("ENTER THE FILE NAME:")
a=open(file_name,'r')
b=a.read()
print('')

my_task = b.split()

dic={}
for i in my_task:
    dic[my_task.index(i)]=i

print('YOUR TO DO LIST:')
def print_dic():
    for i in dic:
        print("{} [{}]".format(dic[i],i))
    sleep(1)
print_dic()
print('')

print("READ THE INSTRUCTION CAREFULLY:")
print("1. ENTER A FOR ADDING IN TO DO LIST")
print("2. ENTER B FOR DELETING IN TO DO LIST")
print("3. ENTER C FOR MARKING THE COMPLETED TASK(* MEANS THAT THE TASK IS COMPLETED)")
print("4. ENTER D FOR DISPLAYING THE LIST")
print("5. ENTER E FOR EXITING THE PROGRAM")
print("\n")

while True:
    i = input("WHAT IS YOUR CHOICE?[A,B,C,D,E]").lower()

    if i == 'a':
        task = input("ENTER THE TASK YOU WANT TO ADD:")
        dic[len(dic)]=task
        print('')
        print("NEW TO DO LIST:")
        print_dic()
        
    elif i == 'b':
        my_del = int(input("\tENTER THE NUMBER ALOTTED TO THE TASK YOU WANT TO DELETE FROM THE LIST"))
        check = input("\t\tARE YOU SURE YOU WANT TO DELETE THE TASK?[y/n]").lower()
        if check == 'y':
            del dic[my_del]
            print('')
            print("NEW TO DO LIST:")
            print_dic()
        elif check == 'n':
            print_dic()

    elif i == 'c':
        my_com = input("\tENTER THE NUMBER ALOTTED TO THE TASK YOU HAVE COMPLETED:")
        flag = True
        for i in dic:
            if int(my_com) == i:
                index = dic[i]
                dic[int(my_com)] = "*" + index
                print_dic()
                flag = True
                break
            else:
                flag = False
        if not flag:
            print("NO SUCH TASK WAS FOUND")
    elif i == 'd':
        print_dic()
        
    elif i == 'e':
        break
print('UPDATED TO DO LIST IS:')
print_dic()

new_list=list(dic.values())
num=len(new_list)
string='{} '*num
new_string=string.format(*new_list)

a=open(file_name,'w')
b=a.write(new_string)
