import nltk 


class UniTagger:
	"""
	This class is used to instantiate an object that identifies the tags of certain words
	"""
	
	def __init__(self, tagged_words):
		self.CndFreqDist = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_words) #a conditional frequency distribution that holds all required information
	
	def __get_conditions(self):
	# Return all the tags within the frequency distribution
		return self.CndFreqDist.conditions()	


	def __get_pertinent_tags(self, word):
	# Return only a list of tags within which the target word appears
		return [condition for condition in self.__get_conditions() if word in self.__get_keys(condition)]
	
	
	def __get_keys(self, condition):
	# Obtain the dictionary associated with a certain function and return the keys of that dictionary
		return self.CndFreqDist[condition].keys()
	
	def __get_val(self, key, condition):
	#  Return the value associated with a certain key within a particular dictionary
		return self.CndFreqDist[condition][key]

	def tag(self, word):
	# Assuming a word exists within the frequency distribution, return the most likely tag associated with the word
		conditions = self.__get_pertinent_tags(word)
		if len(conditions) == 0: # if there are no tags associated with a certian word
			return "None"
		tag = "" # stores the tag with the current highest value as we iterate through the loop, intitlally set to an empty string 
		max_val = 0 # stores the highest value of all tags associated with a certain word
		for condition in conditions:
			temp = self.__get_val(word, condition) # the number of times a certain word has appeared with a certain tag 
			if max_val < temp:
				max_val = temp 
				tag = condition # The tag with the highest value uptill that point
		return tag


				
					
			 
			 
				
				
		
