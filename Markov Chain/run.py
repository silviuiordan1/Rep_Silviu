from markov_python.cc_markov import MarkovChain
from fetch_data import fetch_data

mc = MarkovChain()
mc.add_string(fetch_data('http://phyton.org'))
phrase1 = ""
phrase2 = ""
phrase3 = ""
phrase4 = ""
text1 = mc.generate_text()
for word in text1:
    phrase1 += " " + word 
print "Phrase num 1:", phrase1
text2 = mc.generate_text()
for word in text2:
    phrase2 += " " + word 
print "Phrase num 2:",phrase2
text3 = mc.generate_text()
for word in text3:
    phrase3 += " " + word
print "Phrase num 3:",phrase3
text4 = mc.generate_text()
for word in text4:
    phrase4 += " " + word
print "Phrase num 4:",phrase4
