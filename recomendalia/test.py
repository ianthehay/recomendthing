
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


# To implement the Concept suggestions:
 # first from the list of concepts for a user search for concepts which have a rating of greater than 4
 # from this list of highly rated concepts check for concepts which share common attributes. 
 # EG from the category of jazz or from italian restaurant or movies created by stalone.
 # Then suggest other concepts with the same attributes ranked by the most common decending to those less common.
 # To increse the size of the list the same can then be repeated for those with rating greater than 2 and less than 4
 # These can then be apended to the suggested concept list.


