import pandas as pd
<<<<<<< HEAD
#Task1: Read file
File1 = None
while File1 is None:
    try:
        filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        with open(filename+".txt", "r") as fclile1:
            File1 = pd.read_csv(filename+".txt", delimiter="\t", header=None)
        print("Successfully opened "+filename + ".txt\n*** ANALYZING ***")
    except:
        print('File cannot be found.\nPlease try again!')

#Task2: Check line validity, print out invalid line
=======
# task1: Load file
File = None
while File is None:
    try:
        filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")             
        with open(filename+".txt", "r") as File:
            File = pd.read_csv(filename+".txt", delimiter="\t", header=None)
        print("Successfully opened "+filename + ".txt\n*** ANALYZING ***")
    except:
        print('File cannot be found.\nPlease try again!')
        
#Task 2: Check line validity, print out invalid line
>>>>>>> 05357ad93a23676b1549e709ec47fc722e3430f6
delete = []
for i in range(0, len(File)):
    if File[0][i].count(",") != 25:
        print("Invalid line of data: does not contain exactly 26 values:\n" + File[0][i])
        delete.append(i)
<<<<<<< HEAD
File1.drop(delete, inplace=True)                      #Delete rows in dataframe that does not contain exactly 26 values
File1 = File1[0].str.split(",", expand=True)          #Split ID and answers to seperate columns

File1["Original"] = File1[File1.columns].astype(str).apply(lambda x: ','.join(x), axis=1)   #Insert a column of original data
File1["Invalid N#"] = File1[0].str.match("[N][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")     #Insert a column of boolean answer for invalid ID 
Invalid_N = File1.loc[File1["Invalid N#"] == False].index                                   #Find the index of the invalid rows
for j in Invalid_N:
    print("Invalid line of data: N# is invalid\n" + File1.loc[j, "Original"])
File1 = File1.drop(Invalid_N)                                                               #Delete invalid rows
File1 = File1.drop(["Original", "Invalid N#"], axis=1)
=======
File.drop(delete, inplace=True)                            #Delete rows in dataframe that does not contain exactly 26 values
File = File[0].str.split(",", expand=True)                 #Split ID and answers to seperate columns

File["Original"] = File[File.columns].astype(str).apply(lambda x: ','.join(x), axis=1)    #Insert a column of original data to show the invalid row
File["Invalid N#"] = File[0].str.match("[N][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")     #Insert a column of boolean answer for invalid ID 
Invalid_N = File.loc[File["Invalid N#"] == False].index                                   #Find the index of the invalid rows
for j in Invalid_N:
    print("Invalid line of data: N# is invalid\n" + File.loc[j, "Original"])
File = File.drop(Invalid_N)                                                               #Delete invalid rows
>>>>>>> 05357ad93a23676b1549e709ec47fc722e3430f6

#Print out report for numbers of valid and invalid lines
if len(delete) + len(Invalid_N) == 0:
    print("No errors found!\n\n***REPORTS***\nTotal valid lines of data: " + str(len(File))
            + "\nTotal invalid lines of data: " + str(0))
else:
    print("\n***REPORTS***\nTotal valid lines of data: " + str(len(File))
            + "\nTotal invalid lines of data: " + str(len(delete) + len(Invalid_N)))
<<<<<<< HEAD

#Task3: Calculate score
File1["Score"] = 0                                                                          #Insert a column of score 
=======
    
#Task3: Calculate score
File["Score"] = 0                                                                          #Insert a column of score 
>>>>>>> 05357ad93a23676b1549e709ec47fc722e3430f6
answer_key = list("0,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(","))
for i in range(0, len(File)):
    score = 0
    for j in range(1, 26):
        if File.iloc[i, j] == answer_key[j]:
            score += 4
        elif File.iloc[i, j] == "":
            score = score
        else:
            score += -1
    File.iloc[i, File.columns.get_loc("Score")] = score

<<<<<<< HEAD
#Print out staticstics of overall
print("Mean (average) score: " + str(File1["Score"].mean()) + "\nHighest score: "
        + str(File1["Score"].max()) + "\nLowest score: " + str(File1["Score"].min()) + "\nRange of scores: "
        + str(File1["Score"].max()-File1["Score"].min()) + "\nMedian score: " + str(File1["Score"].median()))

#Task4: Export final scores of the class to a txt file
File1 = File1[[0,"Score"]]
=======
    #Print out staticstics of overall
print("Mean (average) score: " + str(File["Score"].mean()) + "\nHighest score: "
        + str(File["Score"].max()) + "\nLowest score: " + str(File["Score"].min()) + "\nRange of scores: "
        + str(File["Score"].max()-File["Score"].min()) + "\nMedian score: " + str(File["Score"].median()))

#Task4: Export final scores of the class to a txt file
File1 = File[[0,"Score"]]
>>>>>>> 05357ad93a23676b1549e709ec47fc722e3430f6
File1.to_csv(filename + "_grade.txt", index=False, header=None)
