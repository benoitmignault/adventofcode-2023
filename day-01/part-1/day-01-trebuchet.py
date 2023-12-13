
file = open("petit-fichier")

while True:
    line = file.readline()
    if not line:        
        break
    else:
        print(line)

file.close()