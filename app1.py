import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def translate(word):
   
    word=word.lower()

    
    
    if word in data:
        return data[word]
    elif word.title() in data:
         return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    
           
                  
      
    
    
    elif len(get_close_matches(word, data.keys())) >0 :
       yn =  input("did you mean %s instead? enter Y  IF yes or N for no : " % get_close_matches(word, data.keys()) [0])
       if yn  == "Y":
            return data[get_close_matches(word, data.keys()) [0]]
       elif yn == "N":
           return " the word doesnt exist. please double check it."
       else:
           return " we didn't understand your entry. "

        
    
    else:
        return "word doesnt exist. please double check the word."
    
    
    

    


word=input("enter a word: ")

output=(translate(word))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)



