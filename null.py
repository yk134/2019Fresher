list=['n','ASD','QBCBSDBSDBCSBDJBHCFBDSFHB','AAASGGGAGSG','RAghav','vej']
largest = 0
for i in range(0,len(list)):	
	if (len(str(largest))) < len(list[i]):
		largest = list[i]

print('largest :::; ',  largest,type(largest))

