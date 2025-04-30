"""
Basics done
What this will do:
1. Will have an option to make a list of characters and also sort them into teams as per the user
2. Will have an option to give characters priority like who is more important to build right now and what you need for them
3. The list made should be available as notes too which can be seen at later time from inside and outside too
Challenge:
Try to add image of characters and have a gui for the program
"""
# Defining elements to be used
import json
# Driver program
print("Welcome")
while True:
    # Code to make a txt file or choose an exsisting one
    tesel=int(input("Type 1. For making a new file.\t2. For using an old file.\t3. To view a file\n>> "))
    tname=input("Enter the name of the file: ")
    def add_char(tname): # For adding
       with open(tname, "r+") as a:
            try: 
                f=json.load(a)
            except json.JSONDecodeError:
                f={}
            charcs=input("Type the name of the character: ")
            infos=input("Type the information you want to store related to them: ")
            f[charcs]=infos
            a.seek(0)
            json.dump(f,a,indent=3)
    def findd(tname): #For viewing
        with open(tname, "r") as a:
            try:
                j=json.load(a)
                print("Character list:")
                print(json.dumps(j,indent=3))
            except json.JSONDecodeError:
                print("The file is empty or not properly formatted.")
                return
    if tesel==1:  #give option if they want to quit here or to write now and add error handling of file not found
        with open(tname, "w+") as a:
            json.dump({},a)
            print("File has been created")
    elif tesel==2: #done
        no_of_entries=int(input("Type the number of entires you want to add: "))
        for _ in range(no_of_entries):
            add_char(tname)
    elif tesel==3: 
        findd(tname)
    else:
        print("error")
    contis=input("Do you want to continue? (y/n): ").lower()
    if contis != 'y':
        print("Exiting the program.")
        break