import re
ans=True
while ans==True:
    print("1 - Считать имена и фамилии\n 2 - Считать все емайлы\n 3 - Считать названия файлов\n 4 - Считать цвета\n 5 - Выход")
    n=int(input())
    with open("MOCK_DATA.txt","r",encoding="utf-8") as file:
        content =file.read()
        if n==1:
            name=re.findall(r"[A-Z](?:[a-zA-Z]|-|'|)*\s",content)
            names=open("names.txt","w")
            i = 0
            while i < len(name) - 1:
                print(name[i] + name[i + 1])
                names.write(name[i] + name[i + 1]+"\n")
                i += 2
        elif n==2:
            email=re.findall(r"(?:\w)*@[^\s]*",content)
            email1=open("emails.txt","w")
            for i in email:
                email1.write(i+"\n")
                print(i)
        elif n==3:
            name_of_file=re.findall(r"[A-Z](?:[a-zA-Z])*\.[^\s]*",content)
            name_of_files=open("name_of_files.txt","w")
            for i in name_of_file:
                name_of_files.write(i + "\n")
                print(i)

        elif n==4:
            color=re.findall(r"#[^\s]*",content)
            colors = open("colors.txt", "w")
            for i in color:
                colors.write(i + "\n")
                print(i)

        elif n==5:
            break
        else:
            print("такой команды нет ")

