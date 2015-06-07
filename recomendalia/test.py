
import recomendalia
import recomendalia.sampledata
recomendalia.sampledata
data= recomendalia.sampledata.generate_sample_data()
users=data[0]
usertest=users[0]
usertest.suggest_friends()



network =[]


for friend in self.friends:
	for userfriend in friend.friends:
		network.append(userfriend)

# for person in network:
# 	matches = [x for x in network if x = person]
# 	friendsuggestion.rank = len(matches)
	
# remove already friends and self from network 
nonfriendnetwork=[x for x in self.network if x in self.friends]
# determine the occurances of each non friend in the network
counter = collections.Counter(self.nonfriendnetwork)	
# get a lsit of the most commonly occuring 4 people
common = nonfriendnetwork.most_common(4)

suggestionlist=[]

for suggestion in common:
	userobject = suggestion[0]
	rank=suggestion[1]
	# suggestedperson = new friendsuggestion(userobject ,rank)
	# suggestionlist.append(suggestedperson)
	suggestionlist.append(friendsuggestion(userobject,rank))

# if match : 
# 	friendsuggestion.rank +=1

# matches = [x for x in network if x = person]