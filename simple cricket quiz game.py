#simple cricket quiz game
def quiz_game(questions,options,answers,guesses,score):
    question_num=0
    for question in questions:
        print("----------------------------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        
        guess=input("Enter option(A,B,C,D): ").upper()
        if guess in ['A','B','C','D']:
            guesses.append(guess)
            if guess == answers[question_num]:
                score+=1
                print("***CORRECT!***")
            else:
                print("****WRONG!****")
                print(f"Correct answer is *{answers[question_num]}*")
        else:
            print("'Invalid Option'")
            return
        question_num+=1

    print("----------------------------------------")
    print("\t\t*RESULTS*\t\t")
    print("----------------------------------------")
    print(" QUESTIONS \t| ANSWERS \t| GUESS \t| RESULTS ")
    i=0
    for answer in answers:
        for guess in guesses[i]:
            if answer == guess:
                print(f"\t{i+1}\t|\t{answer}\t|\t{guess}\t|\t✔️")
            else:
                print(f"\t{i+1}\t|\t{answer}\t|\t{guess}\t|\t❌")
        i+=1
    print(f"YOUR SCORES:*{score}/5*")


questions=("1.Who is known as the 'God of Cricket' in India? ",
           "2.Which Indian bowler took a hat-trick in the 2019 World Cup?",
           "3.Which Indian player is known as 'Captain Cool'?",
           "4.In which year was the IPL (Indian Premier League) founded?",
           "5.In which year did India win the inaugural T20 World Cup?")

options=(("A. rohit sharma ","B. Sachin Tendulkar","C. MS Dhoni","D. Virat kohli"),
         ("A. Bhuvneshwar Kumar","B. Jasprit Bumrah","C. Ravichandran Ashwin","D. Mohammed Shami"),
         ("A. MS Dhoni","B. rohit sharma","C. Virat kohli","D. Virender Sehwag"),
         ("A. 2006","B. 2007","C. 2008","D. 2009"),
         ("A. 2007","B. 2006","C. 2008","D. 2010"))


answers=('B','D','A','C','A')
guesses=[]
score=0

quiz_game(questions,options,answers,guesses,score)
