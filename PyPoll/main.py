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
    Marsh_count = 0
    Queen_count = 0
    Bamoo_count = 0
    Trandee_count = 0
    Raffah_count = 0    
    rows = 0

    for row in csvreader:
        voterID_2 = voterID_2 + 1   
        
        if row.count('Marsh') > 0:     
            rows = rows + 1
            Marsh_count = Marsh_count + 1 
        if row.count('Queen') > 0:     
            rows = rows + 1
            Queen_count = Queen_count + 1 
        if row.count('Bamoo') > 0:     
            rows = rows + 1
            Bamoo_count = Bamoo_count + 1 
        if row.count('Trandee') > 0:     
            rows = rows + 1
            Trandee_count = Trandee_count + 1
        if row.count('Raffah') > 0:     
            rows = rows + 1
            Raffah_count = Raffah_count + 1

    totalVotes = float(Marsh_count)+float(Queen_count)+float(Bamoo_count)+float(Trandee_count)+float(Raffah_count)
    Marsh_perc = (int(Marsh_count)/totalVotes)*100
    Queen_perc = (int(Queen_count)/totalVotes)*100
    Bamoo_perc = (int(Bamoo_count)/totalVotes)*100
    Trandee_perc = (int(Trandee_count)/totalVotes)*100
    Raffah_perc = (int(Raffah_count)/totalVotes)*100   

    # candidate = []
    # candidate.append()
    # print(candidate)

    print ('\n')  
    print ("Election Results")
    print ("-------------------")
    print ('Total Votes: '+ str(voterID_2))
    print ("-------------------")    
    print ("Marsh: ", '{:.1f}%'.format(float(Marsh_perc))+ ' (' + str(Marsh_count) + ')')
    print ("Queen: ", '{:.1f}%'.format(float(Queen_perc))+ ' (' + str(Queen_count) + ')')
    print ("Bamoo: ", '{:.1f}%'.format(float(Bamoo_perc))+ ' (' + str(Bamoo_count) + ')')
    print ("Trandee: ", '{:.1f}%'.format(float(Trandee_perc))+ ' (' + str(Trandee_count) + ')')
    print ("Raffah: ", '{:.1f}%'.format(float(Raffah_perc))+ ' (' + str(Raffah_count) + ')') 
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
        write (("Marsh: ", '{:.1f}%'.format(float(Marsh_perc))+ ' (' + str(Marsh_count) + ')'), csvwriter)
        write (("Queen: ", '{:.1f}%'.format(float(Queen_perc))+ ' (' + str(Queen_count) + ')'), csvwriter)
        write (("Bamoo: ", '{:.1f}%'.format(float(Bamoo_perc))+ ' (' + str(Bamoo_count) + ')'), csvwriter)
        write (("Trandee: ", '{:.1f}%'.format(float(Trandee_perc))+ ' (' + str(Trandee_count) + ')'), csvwriter)
        write (("Raffah: ", '{:.1f}%'.format(float(Raffah_perc))+ ' (' + str(Raffah_count) + ')'), csvwriter) 
        write ("-------------------", csvwriter)

run('Resources', 'election_data_1.csv')
run('Resources', 'election_data_2.csv')        