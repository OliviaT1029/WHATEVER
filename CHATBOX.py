import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "1b29dd20-af00-11e9-960f-792019754abf13d7126e-10ee-4d41-94e8-f528d1b9ccfb"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
def answer_question():
    question = input(">")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("I dont' know, please ask me another question!")
    elif answerclass == "Breakfast_Foods":
        print("The best breakfast food is pancakes with syrup.")
    elif answerclass == "Dinner":
        ("The best dinner is spaghetti and meatballs.")
    elif answerclass == "Dessert":
        ("The best dessert is cake.")
        
print("What do you want to know about food?")
while True:
    answer_question()