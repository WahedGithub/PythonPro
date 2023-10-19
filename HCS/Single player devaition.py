import statistics as st
filename = ['dravid.txt'] 
deviations = {}#empty dict

for filename in filename:
	player = filename.replace(".txt", "")
	fobj = open(filename, "r")
	strike_rates = []

for line in fobj: 
	fields = line.split()
	runs = int(fields[2])
	balls = int(fields[3])
	strike_rate = runs/balls*100
	strike_rates.append(int(strike_rate))
	
	deviations[player] = st.stdev(strike_rates)
	

for player in deviations:
    print (player, end=" ")
    print (deviations[player])
    
