
class lexicon(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
	def scan(self, everything):
		return self.name.get(everything, None)
		
# https://stackoverflow.com/questions/15424895/creating-lexicon-and-scanner-in-python

lexicon ={
    ('directions', 'north'),
    ('directions', 'south'),
    ('directions', 'east'),
    ('directions', 'west'),
    ('verbs', 'go'),
    ('verbs', 'stop'),
    ('verbs', 'look'),
    ('verbs', 'give'),
    ('stops', 'the'),
    ('stops', 'in'),
    ('stops', 'of'),
    ('stops', 'from'),
    ('stops', 'at')
    }

def scan(sentence):

    words = sentence.lower().split()
    pairs = []

    for word in words:
        word_type = lexicon[word]
        tupes = (word, word_type) 
        pairs.append(tupes)

    return pairs
