import re

ques = [

'(hi)|(hello)',
'how are you',
'((^|\W)fine($|\W))|(i am fine)',
'(your age)|(old are you)',
'(your name)|(who are you)',
'(python for you)|(python)'

]

ans = [
    
'hello :)',
'i am fine how are you?',
'Good, Nice to here',
'i am not human i am a bot, and bot does not have age',
'I am a chatbot my name is Super Chatbot, I was made with python',
'Python is just a programming language.'


]


userInput = ''
notKnown = "I did not understand my developers are working to improve me"


# Function to run loop and check ans
def checkAns():
    for index, items in enumerate(ques):
        if re.search(items, userInput):
            print('\n' + ans[index] + '\n')
            break
        elif len(ques) - 1 == index:
            print('\n' + notKnown + '\n')
        
    inputFunc()

# Function to take input and save
def inputFunc():
    global userInput
    userInput = input("Say something : ").lower()
    checkAns()

inputFunc()

