Starvation = {1: 50, 2: 45, 3: 0, 4: 20}

file1 = open("starvation.txt","w")
S = [str(Starvation[1]), str(Starvation[2]), str(Starvation[3]), str(Starvation[4])]
file1.writelines([str(Starvation[1]), '\n'])
file1.writelines([str(Starvation[2]), '\n'])
file1.writelines([str(Starvation[3]), '\n'])
file1.writelines([str(Starvation[4]), '\n'])
file1.close()

file2 = open("starvation.txt","r+")
old_den = file2.readlines()
print(old_den[0][0:2])
