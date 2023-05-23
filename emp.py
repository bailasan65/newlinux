inputfile = open ("e.txt", "r")


line=inputfile.readline()
while(line!=""):
     name,job,income=line.split(',')
     first,last=name.split(" ")
     line=inputfile.readline()

print(name,job,income)

inputfile.close()
