#All Question are taken in the tuple 
questions=('1.Which one of the following rier flows between Vindhyan and Satpura ranges?',
           '2.The country that has the highest in Barley Production',
           '3.The hottest planet in the Solar system',
           '4.Which of the following ports is the oldest port in India',
           '5.At which one of the following places do the rivers Alakananda and Bhagirathi merge to form Ganga?',
           '6.What is the capital of Australia?',
           '7.What is the largest ocean in the world?',
           '8.Which planet is known as the "Red Planet"?',
           '9.Who wrote the play "Romeo and Juliet"?',
           "10.What is currency of INDIA?"
           )
# All the Options for each questions storing in the tuple
options=(('A. Narmada','B. Mahanadi','C. Son','D. Netravati'),
         ('A. China','B. India','C. Russia','D. France'),
         ('A. Mercury','B. Venus','C.Mars','D. Jupiter'),
         ('A. Mumbai Port','B. Chennai Port','C. Kolkata Port','D. Vishakhapatnam Port'),
         ('A. Devprayag','B. Rudra Prayag','C. Karnaprayag','D. Vishnuprayag'),
         ('A. Sydney','B. Melbourne','C.Canberra','D. Perth'),
         ('A. Atlantic Ocean','B. Indian Ocean','C. Arctic Ocean','D. Pacific Ocean'),
         ('A. Venus','B. Mars','C. Jupiter','D. Saturn'),
         ('A. William Shakespeare','B. Jane Austen','C. Charles Dickens','D. F.Scott Fitzgerald'),
         ('A. Yen','B. Euro','C. Dollar','D. Rupee'))
 
# Answers for the above questions are taken into the list and storing them into the variable answers
answers=['A','C','B','B','A','C','D','B','A','D']
guesses=[]
score=0
question_number=0
# for loop is used for printing all the questions in tuple
for qtn in questions:
     print("*********************************************************************")
     print(qtn)
    #  This for loop is used to printing the options 
     for optn in options[question_number]:
          print(optn)
     guess=input("Enter Your Option(A,B,C,D):").upper()
    #  All the user guessing options are stored into the list guesses
     guesses.append(guess)
    #  comparing the guess answer with the correct answer using the if condition
     if guess==answers[question_number]:
    #    Since if the option is correct then score will increments
       score+=1
       print("Congratualations YOUR ANSWER IS CORRECT!") 
    #    Since the if condition is false then print else statement
     else:
         print(f"Wrong Answer!!! {answers[question_number]} is the correct answer")
     question_number+=1 
    #  Finnaly prints the RESULTs
print("*********************************************")
print("--------------------RESULT-------------------")
print("*********************************************")

print("GUESSINGS :",end=" ")
for i in guesses:
    print(i,end=" ")
print()
print("ANSWERS :",end=" ")
for i in answers:
    print(i,end=" ")
print()
score=int(score/len(questions)*100)
print(f"Your score is {score}%")


