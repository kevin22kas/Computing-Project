#Introduction
multiline_str= ("Hello!\n"
"Welcome to the DIGITAL COUNSELLING THERAPY\n"
"Theme: Our success is not found in doing something for the client\n"
"But rather in being someone for the client!\n ")
print(multiline_str)

#deco
# Python program to print Diamond shape
def Diamond(rows):
    n = 0
    for i in range(1, rows + 1):
        for j in range (1, (rows - i) + 1):
            print(end = " ")

        while n != (2 * i - 1):
            print("*", end = "")
            n = n + 1
        n = 0
        print()

    k = 1
    n = 1
    for i in range(1, rows):
        for j in range (1, k + 1):
            print(end = " ")
        k = k + 1
        while n <= (2 * (rows - i) - 1):
            print("*", end = "")
            n = n + 1
        n = 1
        print()

rows = 4
Diamond(rows)

#Login Credentials
input('Enter your Name: ' )
input('Enter your Age: ' )
input('Enter your Gender: ' )
input('Enter your Email Address: ' )

#printing a diamond for decoration
rows = 3
Diamond(rows)

#Defining major fuctions

def Anger_management():
    #These set of practices will help you in anger management
    print('For every minute you are angry, you lose 60 seconds of happiness.\n'
          "So please try to calm down and take a deep long breath. \n"
          " ")

    input('Please express the reason for your anger: ')
    print(" \n"
          'Here are few anger managemant practices: \n'
          "1) Think before you speak \n"
             " In the heat of the moment, it's easy to say something you'll later regret. \n "
          "2) Once you're calm, express your anger \n"
          "3) Get some exercise \n"
             " Physical activity can help reduce stress that can cause you to become angry. \n"
          "4) Don't hold a grudge.Forgiveness is a powerful tool.\n"
          "5) Practice relaxation skills \n"
          " ")
    input('Did you practice a few tips? ' )
    input('Are you feeling relaxed now? ' )
    print(" \n"
          'Always remember: One that angers you controls you. \n'
          " Don’t give anyone that power! Especially the one who does it intentionally.\n"
          " ")

def sad_to_happy():
    #These set of practices will help you avoid sadness and make you feel happy.
    print('We must understand that sadness is an ocean, and sometimes we drown\n'
           'while other days we are forced to swim.” R.M. Drake \n'
          'Action is the antidote to despair.- Joan Baez\n'
          " ")

    input('Please express the reason for your sadness: ')
    print(" \n"
          'Here are few depression managemant practices: \n'
          " 1) Find ways to handle stress and improve your self-esteem.\n"
          " 2) Take good care of yourself. Get enough sleep, eat well, and exercise regularly. \n "
          " 3) Reach out to family and friends when times get hard. \n"
          " 4) Don’t make big life decisions on a day when you’re feeling down. \n"
          " 5) Know yourself.\n"
          " ")

    input('Did you practice a few tips? ' )
    input('Are you feeling happy now? ' )
    print(" \n"
          '“Remember, no one can make you feel inferior without your consent.” —Eleanor Roosevelt \n'
          "“The greater the difficulty, the more glory in surmounting it.\n"
          "Skillful pilots gain their reputation from storms and tempests.” Epicetus \n"
          " ")

def get_motivated():
    #These set of practices will motivate you from within.
    print('Push yourself, because no one else is going to do it for you.\n'
           'Sometimes later becomes never. Do it now. \n'
          'Great things never come from comfort zones.\n'
          " ")

    input('Why do you want to get motivated? : ')
    print(" \n"
          'Is it PROCRASTINATION that is stopping you to reach your goals? : \n'
          " Here are few techniques to avoid procrastination!\n"
          " 1) First of all, Recognize That You're Procrastinating \n "
          " 2) Then Forgive yourself for procrastinating in the past. \n"
          " 3) Commit to the task. \n"
          " 4) Promise yourself a reward and Ask someone to check up on you. \n"
          "   And now....UNLEASH THE BEAST INSIDE YOU!!!!!!!\n"
          " ")

    input('How are you feeling now? ' )
    input('Are you ready to fulfill your dreams? ' )
    print(" \n"
          "“If You Are Working On Something That You Really Care About, \n"
          ' You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs \n'
          "“Great spirits have always encountered violent opposition from mediocre minds.” —Albert Einstein\n"
          "I wish you ALL THE BEST for the future!!\n "
          " ")


def entertainment():
    #These set of practices will refresh you.
    input('Are you feeling bored? ')
    print(" \n"
          'Here are some of the fun facts that will entertain you: \n'
          " 1)Humans are the only animals that blush.\n"
          " 2)Cotton candy was invented by a dentist. \n "
          " 3)I invented a new word!\n"
                                        "Plagiarism!  \n"
          " 4) Why don’t scientists trust atoms?\n"
                        "Because they make up everything. \n"
          " 5) A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”\n"
                                "The doctor replies, “Sorry, I don’t follow you …”\n"

          " ")

    input('Are you feeling refreshed now? ' )

    print(" \n"
          'Good, so now after taking a short break, you can get back to work. \n'
          " ")



def gain_confidence():
    #These set of practices will help you develop self confidence.
    print('“The most beautiful thing you can wear is confidence.”\n'
          'When you have a lot of confidence and you feel like nobody can beat you\n'
           'it’s game over for everyone else.\n'
          " ")

    input('Please express the reason for your nervousness: ')
    print(" \n"
          'Here are few ways to gain confidence: \n'
          " 1) Get Things Done!! Confidence is built on accomplishment. \n"
          " 2) Monitor Your Progress \n "
          " 3) Be Fearless \n"
          " 4) Don't Care What Others Think  \n"
          " 5) Do More Of What Makes You Happy \n"
          " ")

    input('Are you feeling confident now? ' )
    print(" \n"
          '“Remember, no one can make you feel inferior without your consent.” —Eleanor Roosevelt \n'
          "“When you have confidence, you can have a lot of fun.\n"
          "And when you have fun, you can do amazing things.”\n"
          " ")

# Asking the customer about his mood.
print ("""
    1.Angry
    2.Sad
    3.Not Motivated
    4.Bored
    5.Nervous
    """)
print('Just write a number from 1 to 5')
a=input("What is your mood? ")
if a=="1":
    Anger_management()
    rows = 3
    Diamond(rows)

elif a=="2":
    sad_to_happy()
    rows = 3
    Diamond(rows)

elif a=="3":
    get_motivated()
    rows = 3
    Diamond(rows)

elif a=="4":
    entertainment()
    rows = 3
    Diamond(rows)

elif a =="5":
    gain_confidence()
    rows = 3
    Diamond(rows)

else:
    print('Not a valid choice, please try again.')
    quit()

#Conclusion
print('I hope this DIGITAL COUNSELLING THERAPY is useful to you\n'
        "Hope to see you soon\n"
        " HAVE A NICE DAY\n"
        " ")
rows = 5
Diamond(rows)
