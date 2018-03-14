import os
import csv

voterID_1 = 0
voterID_2= 0

csvpath1 = os.path.join('Resources','election_data_1.csv')
csvpath2 = os.path.join('Resources','election_data_2.csv')

with open(csvpath1, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)

    totalVotes = 0
    Vestal_count = 0
    Torres_count = 0
    Seth_count = 0
    Cordin_count = 0
    rows = 0

    for row in csvreader:
        voterID_1 = voterID_1 + 1   
        
        if row.count('Vestal') > 0:     
            rows = rows + 1
            Vestal_count = Vestal_count + 1 
        if row.count('Torres') > 0:     
            rows = rows + 1
            Torres_count = Torres_count + 1 
        if row.count('Seth') > 0:     
            rows = rows + 1
            Seth_count = Seth_count + 1 
        if row.count('Cordin') > 0:     
            rows = rows + 1
            Cordin_count = Cordin_count + 1

    totalVotes = float(Vestal_count)+float(Torres_count)+float(Seth_count)+float(Cordin_count)
    Vestal_perc = (int(Vestal_count)/totalVotes)*100
    Torres_perc = (int(Torres_count)/totalVotes)*100
    Seth_perc = (int(Seth_count)/totalVotes)*100
    Cordin_perc = (int(Cordin_count)/totalVotes)*100

    print ('\n')  
    print ("Election Results")
    print ("-------------------")
    print ('Total Votes: '+ str(voterID_1))
    print ("-------------------")    
    print ("Vestal: " + str(Vestal_perc) + "%" + ' (' + str(Vestal_count) + ')')
    print ("Torres: " + str(Torres_perc) + "%" + ' (' + str(Torres_count) + ')')
    print ("Seth: " + str(Seth_perc) + "%" + ' (' + str(Seth_count) + ')')
    print ("Cordin: " + str(Cordin_perc) + "%" + ' (' + str(Cordin_count) + ')')
    print ("-------------------")
    # print ("Winner: " + str()

    print("Winner: ", max(Vestal_perc, Torres_perc, Seth_perc, Cordin_perc))



with open(csvpath2, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)

    totalVotes = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0   
    rows = 0

    for row in csvreader:
        voterID_2 = voterID_2 + 1   
        
        if row.count('Khan') > 0:     
            rows = rows + 1
            Khan_count = Khan_count + 1 
        if row.count('Correy') > 0:     
            rows = rows + 1
            Correy_count = Correy_count + 1 
        if row.count('Li') > 0:     
            rows = rows + 1
            Li_count = Li_count + 1 
        if row.count('O Tooley') > 0:     
            rows = rows + 1
            OTooley_count = OTooley_count + 1

    totalVotes = float(Khan_count)+float(Correy_count)+float(Li_count)+float(OTooley_count)
    Khan_perc = (int(Khan_count)/totalVotes)*100
    Correy_perc = (int(Correy_count)/totalVotes)*100
    Li_perc = (int(Li_count)/totalVotes)*100
    OTooley_perc = (int(OTooley_count)/totalVotes)*100
 

    # candidate = []
    # candidate.append()
    # print(candidate)

    print ('\n')  
    print ("Election Results")
    print ("-------------------")
    print ('Total Votes: '+ str(voterID_2))
    print ("-------------------")    
    print ("Khan: ", '{:.1f}%'.format(float(Khan_perc))+ ' (' + str(Khan_count) + ')')
    print ("Correy: ", '{:.1f}%'.format(float(Correy_perc))+ ' (' + str(Correy_count) + ')')
    print ("Li: ", '{:.1f}%'.format(float(Li_perc))+ ' (' + str(Li_count) + ')')
    print ("O Tooley: ", '{:.1f}%'.format(float(OTooley_perc))+ ' (' + str(OTooley_count) + ')')
    print ("-------------------")
    # print ("Winner: " + str()

    # print("Winner: ", max(Marsh_perc, Queen_perc, Bamoo_perc, Trandee_perc,Raffah_perc))


def write (line, csvwriter):
    print (line)
    csvwriter.writerow ([line])

def run(path, file):
    csvpath = os.path.join (path,file)
    #  Each row is read as a row    

    # Set variable for output file
    output_path = os.path.join (path, 'report-output-'+ file)
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline ="") as csvfile:

        # csv writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        # write to output files
        print ('\n')  
        write ("Election Results", csvwriter)
        write ("-------------------", csvwriter)
        write ('Total Votes: '+ str(voterID_2), csvwriter)
        write ("-------------------", csvwriter)    
        write (("Khan: ", '{:.1f}%'.format(float(Khan_perc))+ ' (' + str(Khan_count) + ')'), csvwriter)
        write (("Correy: ", '{:.1f}%'.format(float(Correy_perc))+ ' (' + str(Correy_count) + ')'), csvwriter)
        write (("Li: ", '{:.1f}%'.format(float(Li_perc))+ ' (' + str(Li_count) + ')'), csvwriter)
        write (("O Tooley: ", '{:.1f}%'.format(float(OTooley_perc))+ ' (' + str(OTooley_count) + ')'), csvwriter)
        write ("-------------------", csvwriter)

run('Resources', 'election_data_1.csv')
run('Resources', 'election_data_2.csv')        