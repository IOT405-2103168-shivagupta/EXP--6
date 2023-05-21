import csv
import socket
f=open('C:\\Users\\user\\OneDrive\\Desktop\\4 sem\\405\\ip scan data\\data.csv','w')
writer=csv.writer(f)
name="Shivagupta2103168"
for i in range(10):
        output = 'shiva gupta'
        print(output)
        writer.writerow([output])
# writer.writerow(name)
f.close()
