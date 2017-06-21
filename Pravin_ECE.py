#db
name={1:"Sriram",2:"Mukund",3:"Sebastian",4:"Aashritha",5:"Mohammad Rafi",6:"Anjili Kumar",7:"Joseph",8:"Ramachandran",9:"Abhinaya Shankar",10:"Imran Khan"}
age={1:45,2:42,3:38,4:32,5:35,6:29,7:40,8:27,9:23,10:28}
dept={1:"Management",2:"HR",3:"Finance",4:"Product Management",5:"HR",6:"HR",7:"Finance",8:"Product Development",9:"Product Development",10:"Product Testing"}
desi={1:"CEO",2:"HR Manager",3:"Finance Manager",4:"Dev Manager",5:"HR Lead",6:"HR Associate",7:"Finance Associate",8:"Tech Lead",9:"System Developer",10:"QA Lead"}
rt={1:None,2:"Sriram",3:"Sriram",4:"Sriram",5:"Mukund",6:"Mohammad Rafi",7:"Sebastian",8:"Aashritha",9:"Ramachandran",10:"Ramachandran"}


def menu():
    print("Choose any option:")
    print("""1.Show all Records
2.Search Records
3.Manager Report
4.Reporting Tree
5.Summary of Records""");
    choice=raw_input();
    return choice;

def choice1():
    for i in range(1,11):
        print i, name[i],age[i],dept[i],desi[i],rt[i];
    return 0;

def choice2():
    print """Enter a chioce to search
1.Name
2.Age
3.Department
4.Designation
5.Reporting to"""
    s=raw_input();
    s=s.split();
    i=0
    ap=[]
    for i in range(1,10):
        if s[0] is '1':
            if(name.values()[i]== s[1]):
                ap.append(i+1);
        if s[0] is '2':
            if(age.values()[i]== s[1]):
                ap.append(i+1);
        if s[0] is '3':
            if(dept.values()[i]== s[1]):
                ap.append(i+1);
        if s[0] is '4':
            if(desi.values()[i]== s[1]):
                ap.append(i+1);
        if s[0] is '5':
            if(rt.values()[i]== s[1]):
                ap.append(i+1);
    i=0
    for i in range(len(ap)):
        print ap[i], name[ap[i]],age[ap[i]],dept[ap[i]],desi[ap[i]],rt[ap[i]];



def choice3():
    print "Enter manager name:"
    n=raw_input();
    i=0;
    for i in range(1,10):
        if(str(rt.values()[i]) == str(n)):
            print name[i+1];

def findx(n1):
    i=0
    if n1 is "Sriram":
        exit;
    for i in range(1,10):
        if(str(name.values()[i]) == str(n1)):
            return i+1;

def choice4():
    print "Enter manager name:"
    n=raw_input();
    i=0;
    for i in range(1,10):
        if(str(name.values()[i]) == str(n)):
            print rt[i+1];
            ad=findx(rt[i+1]);
            print rt[ad];
            if rt[ad] is "Sriram":
                exit;
            ad=findx(rt[ad]);
            if rt[ad] is "Sriram":
                exit;
            print rt[ad];
            ad=findx(rt[ad]);
            if rt[ad] is "Sriram":
                exit;
            print rt[ad];



i=0
#main()
for i in range(100): 
    x=menu();
    if str(x) is '1':
        choice1();
    elif str(x) is '2':
        choice2();
    elif str(x) is '3':
        choice3();
    elif str(x) is '4':
        choice4();
    else:
        break;

    
