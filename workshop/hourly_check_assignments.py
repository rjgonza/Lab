import random

def choose_noccer(list):
	noccer_index=random.randint(0,len(list)-1)
	noccer=list[noccer_index]
	list.remove(noccer)
	return noccer,list

#all_hours=['15:45', '15:00','14:00','13:00','12:00','11:00','10:00']
all_hours=['10:00', '11:00','12:00','13:00','14:00','15:00','15:45']
all_noccers=['Ramon', 'Brendan', 'Walter', 'Jeff', 'Frank', 'Brian', 'Tim', 'Lan', 'Donald', 'Jon','Jay']
shutdown_noccers=raw_input("Who is on shutdown? (eparated by spaces)").split(' ')

for shutdown_noccer in shutdown_noccers:
	all_noccers.remove(shutdown_noccer)

chosen_noccers=[]
for hour in all_hours:
	if hour=="15:00" or hour=="15:45":
		choice,shutdown_noccers=choose_noccer(shutdown_noccers)
		print hour,choice
	elif hour=="12:00":
		choice,startup_noccers=choose_noccer(all_noccers)
		print hour,choice," - Don't forget to shutdown FREJ :)"
	else:
		choice,startup_noccers=choose_noccer(all_noccers)
		print hour,choice
