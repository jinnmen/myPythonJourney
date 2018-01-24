# Create a mapping of Prefecture abbreviation
prefs = {
	'Aichi': 'AIC',
	'Ehime': 'EHI',
	'Gunma': 'GUN',
	'Hokkaido': 'HOK',
	'Hyogo': 'HYO',
	'Ibaraki': 'IBA',
	'Ishikawa': 'ISH',
	'Iwate': 'IWA',
	'Kagawa': 'KAG',
	'Kanagawa': 'KAN',
	'Mie': 'MIE',
	'Miyagi': 'MIY',
	'Osaka': 'OSA',
	'Shiga': 'SHI',
	'Tochigi': 'TOC',
	'Yamanashi': 'YAM'
}

# create a basic set of prefectures and their capital cities
cities = {
	'AIC': 'Nagoya',
	'EHI': 'Matsuyama',
	'GUN': 'Maebashi',
	'HOK': 'Sapporo',
	'HYO': 'Kobe',
	'IBA': 'Mito',
	'ISH': 'Kanazawa',
	'IWA': 'Morioka',
	'KAG': 'Takamatsu',
	'KAN': 'Yokohama',
	'MIE': 'Tsu',
	'MIY': 'Sendai',
	'OSA': 'Osaka',
	'SHI': 'Otsu',
}

# add some more cities
cities['TOC'] = 'Utsunomiya'
cities['YAM'] = 'Kofu'

# print out some cities
print '-' * 10
print "Aichi prefecture has: ", cities['AIC']
print "Ehime prefecture has: ", cities['EHI']
print "Gunma prefecture has: ", cities['GUN']
print "Hokkaido prefecture has: ", cities['HOK']

# print some prefecture
print '-' * 10
print "Aichi's abbreviation is: ", prefs["Aichi"]
print "Ehime's abbreviation is: ", prefs['Ehime']
print "Gunma's abbreviation is: ", prefs['Gunma']
print "Hokkaido's abbreviation is: ", prefs['Hokkaido']

# do it by using the prefecture then cities dict
print '-' * 10
print "Aichi has: ", cities[prefs['Aichi']]
print "Ehime has ", cities[prefs['Ehime']]

# print every prefecture's abbreviation
print '-' * 10
for pref, abbrev in prefs.items():
	print "%s is abbreviated as %s" % (pref, abbrev)
	
# print every city in the prefectures
print '-' * 10
for abbrev, pref in prefs.items():
	print "%s prefecture is abbreviated %s and has city %s" % (pref, abbrev, prefs[abbrev])
	
print '-' * 10
# safely get an abbreviation by prefecture that might not be there (Shimane=SHI, city= Matsune)
pref = prefs.get('Shimane', None)

if not pref:
	print "Sorry, no Shimane"

# get a pref with a default value
pref = prefs.get('SHI', 'Does not Exist')
print "The city for the prefecture 'SHI' is %s" % pref

# sorting within dictionary   https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
for key in sorted(prefs.iterkeys()):
	print "%s: %s" % (key, prefs[key])
	
# Differences between dictionary, list, set: https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set