import os
import csv

months1 = 0
revenue1=0

months2= 0
revenue2 = 0

csvpath1 = os.path.join('Resources','budget_data_1.csv')
csvpath2 = os.path.join('Resources','budget_data_2.csv')

with open(csvpath1, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)
    #print (csvreader)

    for row in csvreader:
        months1 = months1+1
        month_revenue1 = row[1]
        revenue1= revenue1+float(row[1])
        #revenue1 += float (row[1])

    print ("Financial analysis")
    print ("-------------------")
    print ('Total months: '+ str(months1))
    print (('Total revenue: $'), '{0:.0f}' .format(revenue1))
    print ('\n')

with open(csvpath2, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)
    #print (csvreader)

    for row in csvreader:
        months2 = months2+1
        month_revenue2 = row[1]
        revenue2= revenue2+float(row[1])
        #revenue2 += float (row[1])

    print ("Financial analysis")
    print ("-------------------")
    print ('Total months: '+ str(months2))
    print (('Total revenue: $'), '{0:.0f}' .format(revenue2))
    print ('\n') 

# Average diff

months = 0
revenue = 0    

with open(csvpath1, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)
    #print (csvreader)

    old_revenue = 0
    new_revenue = 0
    partial_revenue_diff = 0
    total_revenue = 0
    diff_revenue=0
    i=0   #iterations

    for row in csvreader:
        
        months = months + 1
        new_revenue = row[1]
        diff_revenue = float(new_revenue) - float(old_revenue) 
        partial_revenue_diff =  partial_revenue_diff + diff_revenue
        total_revenue = total_revenue + float(new_revenue)
        old_revenue=new_revenue
        i = i+1

        print('iteration: '+str(i) + '---months: '+ str(months)
        + '   new revenue: '+ str(new_revenue)
        + '   old revenue: '+str (old_revenue) 
        + '   diff revenue: ' + str(diff_revenue)
        + '   partial revenue: ' + str(partial_revenue_diff))
        average_revenue_diff = partial_revenue_diff / months
        print ('average_revenue_diff :','{0:.0f}'.format(average_revenue_diff))


# Largest and smallest increase

with open(csvpath1, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next (csvfile)
    #print (csvreader)

    old_revenue = 0
    new_revenue = 0
    partial_revenue_diff = 0
    total_revenue = 0
    diff_revenue=0
    current_max= -10000000
    current_min= 10000000
    months = 0
    date_max='TBD'
    date_min='TBD'
    i=0   #iterations
    
    for row in csvreader:
        months = months + 1
        new_revenue = row[1]
        diff_revenue = float(new_revenue) - float(old_revenue)
        if (diff_revenue > current_max):
            current_max = diff_revenue
            date_max = row [0]
        if (diff_revenue < current_min):
            current_min = diff_revenue
            date_min = row [0]
        partial_revenue_diff =  partial_revenue_diff + diff_revenue
        total_revenue = total_revenue + float(new_revenue)
        old_revenue=new_revenue
        i = i+1

        print('iteration: '+str(i) + '  current max: '+ str(current_max)
        + ' date max: ' + date_max
        + ' current min: ' + str(current_min)
        + ' date min: ' + date_min
        + ' current max: ' + str(current_max)
        + '   new revenue: '+ str(new_revenue)
        + '   old revenue: '+ str (old_revenue) 
        + '   diff revenue: ' + str(diff_revenue)
        + '   partial revenue: ' + str(partial_revenue_diff)) 

def write (line, csvwriter):
    print (line)
    csvwriter.writerow ([line])

def run(path, file):
    csvpath = os.path.join (path,file)
    #  Each row is read as a row
    old_revenue = 0
    new_revenue = 0
    partial_revenue_diff = 0
    total_revenue = 0
    revenue = 0
    diff_revenue=0
    current_max= -10000000
    current_min= 10000000
    months = 0
    date_max='TBD'
    date_min='TBD'
    i=0   #iterations 

    with open(csvpath, newline ="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter =",")
        next (csvfile)

        for row in csvreader:
            months = months + 1
            new_revenue = row[1]
            revenue += float(new_revenue)
            diff_revenue = float(new_revenue) - float(old_revenue)
            if (diff_revenue > current_max):
                current_max = diff_revenue
                date_max = row [0]
            if (diff_revenue < current_min):
                current_min = diff_revenue
                date_min = row [0]
            partial_revenue_diff =  partial_revenue_diff + diff_revenue
            total_revenue = total_revenue + float(new_revenue)
            old_revenue=new_revenue
            i = i+1  

    # Set variable for output file
    output_path = os.path.join (path, 'report-output-'+ file)

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline ="") as csvfile:

        # csv writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        # write to output files
        
        print ('\n')
        write("Financial Analysis", csvwriter)
        write("--------------------------", csvwriter)
        write('Total Months: ' + str(months), csvwriter)
        write(('Total Revenue: $ ' + '{0:.0f}' .format(revenue)), csvwriter)
        write('Average Change: $ ' + '{0:.0f}' .format(partial_revenue_diff), csvwriter)
        write('Greatest Increase in Revenue: ' + date_max + ' ($ '+ '{0:.0f}' .format(current_max) + ')', csvwriter)
        write('Greatest Decrease in Revenue: ' + date_min + ' ($ '+ '{0:.0f}' .format(current_min) + ')', csvwriter)

run('Resources', 'budget_data_1.csv')
run('Resources', 'budget_data_2.csv')


