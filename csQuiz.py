wrongAnswers = []
rightAnswers = []

def question_1():
    print("0 = False AND 1 = True")
    question = input("True or False: Katy Perry has zero Grammys?  ")
    answer = ("1")
    if question == answer:
        print("Correct!")
        rightAnswers.append("Q1:Correct")
        return 1
    elif question != answer:
        print("Wrong.")
        wrongAnswers.append("Q1:Wrong")
        return 0

def question_2():
    question = input("True or False: Old Town Road by Lil Nas X is the longest #1 in billboard history?  ")
    answer = ("1")
    if question == answer:
        print("Correct")
        rightAnswers.append("Q2:Correct")
        return 1
    elif question != answer:
        print("Wrong")
        wrongAnswers.append("Q2:Wrong")
        return 0

def question_3():
    print("Choose a letter a-e")
    question = input('''         Grammys 2019 Album of the Year was:
A) Cardi B – Invasion of Privacy
B) Drake – Scorpion
C)Post Malone – Beerbongs & Bentleys
D)Janelle Monáe – Dirty Computer
E)Kacey Musgraves – Golden Hour
''')
    answer = ("e" or "E")
    if question == answer:
        print("Correct!")
        rightAnswers.append("Q3:Correct")
        return 1
    elif question != answer:
        print("That's incorrect. The correct answer is c")
        wrongAnswers.append("Q3:Wrong")
        return 0

def question_4():
    question = input("True or False: Lady Gaga has 6 Grammys.   ")
    answer = ("1")

    if question == answer:
        print("Correct")
        rightAnswers.append("Q4:Correct")
        return 1

    elif question != answer:
        print("Wrong!")
        wrongAnswers.append("Q4:Wrong")
        return 0

def question_5():
    question = input('''Beyonce has how many Grammys?
    A) 20
    B) 10
    C) 15
    D) 12   ''')
    answer = ("a" or 'A')
    if question == answer:
        print("Correct")
        wrongAnswers.append("Q5:Correct")
        return 1
    elif question != answer:
        print("Wrong! Queen Bey has 20. ")
        rightAnswers.append("Q5:Wrong")
        return 0

for i in wrongAnswers:
    print(i)
for j in rightAnswers:
    print(j)

points = question_1() + question_2() + question_3() + question_4() + question_5()
if points <= 1:
    print("Not a real music fan. You got :" + str(points) + " out of 5")

elif points == 2 or points == 3:
    print("Gotta keept trying. You got : " + str(points) + " out of 5")

else:
    print("Woohoo!! You got :" + str(points) + " out of 5")
