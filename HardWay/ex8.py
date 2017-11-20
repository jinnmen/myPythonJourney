#repr = evaluatable string representation of an object. / raw programmers version of variable
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing. ", #double quotes won't show when executed because no ' inside string.
	"That you could type up right. ",
	"But it didn't sing. ", #double quotes will be shown because of ' inside double quotes.
	"So I said goodnight."
)