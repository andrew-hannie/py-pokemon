from pkmn_project import Pokemon
import os

# Use this file to send inputs to the pokemon project class
# and print it to a very nice text file or whatever file type you want 

def readFile(fileName):
    newFile = open(fileName, "r")
    monList = []
    for i in newFile:
        if i[-1:] == "\n":
            i = i[:-1]
        splitStr = i.split(',')
        while '' in splitStr: # redundant basically
            splitStr.remove('')
        if len(splitStr) == 4:
            newMon = Pokemon(splitStr[0], splitStr[1], splitStr[2], splitStr[3]) # 2 types /w ability
            monList.append(newMon)
        elif len(splitStr) == 3:
            newMon = Pokemon(splitStr[0], splitStr[1], splitStr[2]) # 2 types with no ability 
            monList.append(newMon)
        else:
            newMon = Pokemon(splitStr[0], splitStr[1]) # monotype mons
            monList.append(newMon)
    newFile.close()
    return monList
# Simple method for writing to files
def main():
    print("Syntax for Files:")
    print("Pokemon's Name,Type1,Type2 (if needed)")
    fileName = input("Please Input the path of your file: ")
    mons = readFile(fileName)
    output = input("Please enter a name for the file being saved: ")
    if output == "":
        output = "output.txt"
    output = open(output, "w")
    for i in mons:
        
        output.write(str(i))
        output.write("\n")
    output.close()
    print("File saved at", os.path.realpath(output.name))
    input()

   
main()