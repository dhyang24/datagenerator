f = ''.join(open(input("input filename to emulate, only use input() and print() and do not concat using commas for io\n"),'r').readlines()).replace("input()","inputfile.readline().strip()").replace("print(","globalfile.append(")
a = int(input("Type number of cases"))
for i in range(a):
    try:
        globalfile = []
        exec("inputfile = open(str("+str(i)+"+1)+'.in','r')\nwritefile = open(str("+str(i)+"+1)+'.out','w')\n"+f+"inputfile.close();writefile.close()")
        writefile = open(str(i+1)+'.out','w')
        writefile.writelines([str(k)+'\n' for k in globalfile])
        writefile.close()
        print("output",i,"generated!")
    except:
        print("error on case",i,"please check file format")
