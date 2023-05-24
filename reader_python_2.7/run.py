from out.numb import numb

path = raw_input("What is the path to the file?\n")

myfile = open(path, 'r')
info = myfile.read()
myfile.close()

numb += 1
resultName = "out/results/results_" + str(numb) + ".txt"
myfile = open(resultName, 'w')
myfile.write(info)
myfile.close()

myfile = open("out/numb.py", 'w')
myfile.write("numb = " + str(numb))
myfile.close()