filenames = ['dravid.txt', 'sachin.txt', 'yuvraj.txt', 'virat.txt']
devaitions = {}
import statistics as st

for filename in filenames:
	player = filename.replace(".txt", "")# here we are assigning the file name as player name by removing the .txt
	strike_rates = []
	fobj = open(filename, "r")
	
	for line in fobj: #line is a list
		fields = line.split() #assigning fields as variable to line to split
		runs = int(fields[2])
		balls = int(fields[3]) # int to convert the string
		
		strike_rate = runs/balls*100
		
		strike_rates.append(int(strike_rate))
	devaitions[player] = st.stdev(strike_rates)

    #if run in dravid: # here its checking the dict which is empty so it going to else part
     #   dravid[player] = dravid[player] + score

    #else:
     #   dravid[player] = score# all the not present things will come under this


for player in devaitions:
    print (player, end=" ")
    print (devaitions[player])
    
