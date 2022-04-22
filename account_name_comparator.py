import csv

list1 = []
list2 = []

result = []

EXCLUDED_WORDS = ["gmbh", "gmbh.","ag", "ag.","co", "co.","kg", "&" , "se", "srl", "von", "mbh", "it", "consulting", "für", "das", "e.v","e.v.", "im", "-", "mit","der", "europe", "services","international", "service","systems","+", "münchen", "deutschland","cloud","management", "a.", "germany","deutsche", "gruppe", "kgaA","und","de","holding","co.kg","Software","technologies","group","information","partner","cyber","medical","vertrieb","inc","inc.","gbr","pharma","main","des","gesellschaft","b.","v.","e.","ohg","eg","b.v." ,"as","communications","media","tech","system","solutions","engineering","am", "in","computer","verband", "energy","kgaa", "sarl", "a." , "g.", "company"]

#Open files and load them in memory
def read_input():
    with open ("input1.csv") as i1:
        for line in i1.readlines():
            list1.append(line.strip())
    with open ("input2.csv") as i2:
        for line in i2.readlines():
            list2.append(line.strip())


def clean_item(item):
    c_item = []
    words = item.split(" ")
    for word in words:
        if word.lower() not in EXCLUDED_WORDS:
            c_item.append(word.lower())
    return c_item

def process_score(item1,item2):
    score = 0
    for word1 in item1:
        for word2 in item2:
            if word1 == word2:
                score = score+1
    return score

def process_lookup():
    for item1 in list1:
        c_item1 = clean_item(item1)

        for item2 in list2:
            c_item2 = clean_item(item2)
            score = process_score(c_item1, c_item2)
            i_result = {
                "item1":item1,
                "item2":item2,
                "score":score
            }
            if(score > 0):
                result.append(item1 +","+item2+","+str(score))
                print(item1 +","+item2+","+str(score))

def generate_output():
    with open("output.csv", "a") as output:
        for line in result:
            output.write(line + "\n")


read_input()
process_lookup()
generate_output()



