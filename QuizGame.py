questions = ("What is the name of your best friend? :", 
             "Tell me the name of adeel father? :", 
             "which laptop you use? :", 
             "Which programming language are you learning?:", 
             "which game you like the most? :")

options = (("A. Azam", "B. Adeel", "C. Sarim", "D. Faraz"), 
           ("A. Idrees", "B. Aweer", "C. Rafay ", "D. Hammad"), 
           ("A. Razer Blade", "B. Apple", "C. Rog Strix", "D. Dell"), 
           ("A. Java", "B. C++", "C. Python", "D. Ruby"), 
           ("A. LOUP2", "B. GTA 5", "C. COC", "D. RDR2"),)

answers = ("B", "C", "A", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")    
        print(f"{answers[question_num]} is the correct answer")


    question_num += 1
    

print("----------------------------")
print("          RESULTS           ")
print("----------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)*100)
print(f"Your score is:{score}%")