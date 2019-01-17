#Gianpaolo Pittis
import random

second_degree = []
third_degree = []
fourth_degree = []
delete_count_2 = 0
delete_count_3 = 0
delete_count_4 = 0

sentence = input("Sentence to be translate:" )
words = sentence.split()
length = len(words)

#translated word pairs
Comparison = {
        "thought":"styll",
        "right?":"ahlie",
        "get together":"link up",
        "ok":"truuuuuuu",
        "family":"fam",
        "guys":"mandem",
        "of course":"dun kno",
        "sick":"live",
        "come by":"reach",
        "get":"come through",
        "long time":"from time",
        "mississauga":"suaga city",
        "dont know":"szeen",
        "usless":"waste yute",
        "fight":"throw arms",
        "mad":"cheesed",
        "dont get on my nerves":"dont cheese me",
        "ashole":"snake",
        "idiot":"snake",
        "shady":"sus",
        "sketchy":"sus",
        "hanging out":"mossin'",
        "relaxing":"mossin'",
        "wow":"top left",
        "leave":"cut",
        "leaving":"cutting",
        "departing":"cut",
        "depart":"cut",
        "I left":"I cut",
        "I'm leaving":"I'm cutting",
        "he left":"he cut",
        "he's leaving":"he's cutting",
        "they left":"they cut",
        "they're leaving":"they're cutting",
        "she left":"she cut",
        "she's leaving":"she's cutting",
        "guy":"sweetermans",
        "good guy":"sweetermans",
        "good looks":"sweetermans",
        "cool guy":"sweetermans",
        "bitches":"cyattie",
        "ugly":"ratchet",
        "discusting":"ratchet",
        "grose":"ratchet",
        "in a long time":"in a minute",
        "$100":"bill",
        "girl":"ting",
        "my girl":"my ting",
        "his girl":"his ting",
        "really?":"say word?",
        "awsome":"say word?",
        "what?":"say word?",
        "weak":"soft",
        "easy":"soft",
        "hungry":"marved",
        "starving":"marved",
        "a lot":"bare",
        "a lot of":"bare",
        "lots":"bare",
        "tons":"bare",
        "a ton of":"bare",
        "secret":"lowkey",
        "quiet":"lowkey",
        "fight":"scrap",
        "brawl":"scrap",
        "fought":"scraped",
        "dramatic":"extra",
        "shut up":"nize it",
        "be quite":"nize it",
        "she's hot":"she's a dimepiece",
        "agree":"bout it",
        "don't agree":"not bout it",
        "awsome":"turn up",
        "fun":"lit",
        "insane":"savage",
        "going to":"finna",
        "gonna":"finna",
        "savage":"sav",
        "toronto":"the 6ix",
        "showing off":"flexing",
        "to show off":"flex",
        "get me":"scoop me",
        "pick me up":"scoop me",
        "got":"copped",
        "bought":"copped",
        "cool":"wild",
        "stupid":"bean",
        "that":"dat",
        "then":"den",
        "go to":"reach",
        "allow it":"llow it",
        "tim Hortons":"timms",
        "okay":"tru",
        "a thousand dollars":"10 bills",
        "24":"two-four",
        "get":"come thru wit",
        "the":"da",
        "you":"ya",
        "slap":"deafaz",
        "you know":"dun know",
        "fuck off":"nize it",
        "comes":"come",
        "out of nowhere":"two-twos",
        "me":"mans",
        "whats going on":"wagwan",
        "excited":"amped",
        "fight":"throw arms",
        "im high":"im blem",
        "hes high":"hes blem",
        "shes high":"shes blem",
        "theyre high":"theyre blem",
        "were high":"were blem",
        "thanks":"bless",
        "i like it":"im out it",
        "mad":"gassed",
        "stressed":"gassed",
        "damn":"gheez",
        "sexy":"dimepiece",
        "to come":"to reach",
        "girls":"tings",
        "how is":"hows",
        "want":"feeling",
        "beer":"rona",
        "big shot":"shoota",
        "my":"ma",
        "drake":"drizzy drake",
        "raptors":"raps"
       }
       
#quad word processing
if length >= 4:
    for i in range((length - 3)):
        temp = words[i] + " " + words[i + 1] + " " + words[i + 2] + " " + words[i + 3]
        fourth_degree.append(temp)

    for i in range((length - 3)):
        if fourth_degree[i] in Comparison:
            words[i - delete_count_4] = Comparison.get(fourth_degree[i])
            del words[i + 1 - delete_count_4]
            del words[i + 1 - delete_count_4]
            del words[i + 1 - delete_count_4]
            delete_count_4 += 3
            
temp_sentance = " ".join(map(str, words))
words = temp_sentance.split()
length = len(words)

#triple word processing
if length >= 3:
    for i in range((length - 2)):
        temp = words[i] + " " + words[i + 1] + " " + words[i + 2]
        third_degree.append(temp)

    for i in range((length - 2)):
        if third_degree[i] in Comparison:
            words[i - delete_count_3] = Comparison.get(third_degree[i])
            del words[i + 1 - delete_count_3]
            del words[i + 1 - delete_count_3]
            delete_count_3 += 2

temp_sentance = " ".join(map(str, words))
words = temp_sentance.split()
length = len(words)

#double word processing
if length >= 2:
    for i in range((length - 1)):
        temp = words[i] + " " + words[i + 1]
        second_degree.append(temp)
    
    for i in range((length - 1)):
        if second_degree[i] in Comparison:
            words[i - delete_count_2] = Comparison.get(second_degree[i])
            del words[i + 1 - delete_count_2]
            delete_count_2 += 1

temp_sentance = " ".join(map(str, words))
words = temp_sentance.split()
length = len(words)

#single word processing
if length >= 1:
    for i in range(length):
        if words[i] in Comparison:
            words[i] = Comparison.get(words[i])

temp_sentance = " ".join(map(str, words))
temp_sentance = temp_sentance + "."

#ambiance generator

factor = random.randint(1, 10)
if factor == 1:
    temp_sentance = temp_sentance + " Ya hear dawg."
elif factor == 2:
    temp_sentance = temp_sentance + " eh."
elif factor == 3:
    temp_sentance = temp_sentance + " ah."
elif factor == 4:
    temp_sentance = "Ahlie. " + temp_sentance
elif factor == 5:
    temp_sentance = "Dawg. "+ temp_sentance
elif factor == 6:
    temp_sentance = "Yo. " + temp_sentance
elif factor == 7:
    temp_sentance = "Yo guy. " + temp_sentance
    
#no word processing
'''
if length == 0:
    print("Nothing to Translate")
'''
if length != 0:
    print(temp_sentance)



