print("Welcome! This is a Quiz.")

def instructions():
    print("1. There will be 5 questions.\n2.+10 score for every correct answer.\n3. -3 score for every incorrect answer.\n4. You can choose not to attempt a question by pressing the M key.")
    print("Good luck!")
    print()


instructions()
questions_options=(["What is the capital of France?","A) Berlin", "B) Madrid", "C) Rome","D) Paris"],
   ["Which of the following is one of the seven wonders of the world?","A) Taj Mahal", "B) Eiffel Tower", "C) Red Fort","D) Statue of Liberty"],
   ["What is the chemical name of H2SO4?", "A) Hydrochloric Acid", "B) Sulphuric Acid", "C) Nitric Acid","D) Acetic Acid"],
   ["Who is the President of India?","A) Droupadi Murmu", "B) Narendra Modi", "C) Ram Nath Kovind","D) Jagdeep Dhankar"],
   ["When was the Constitution of India adopted?","A) August 15, 1947", "B) January 26, 1950", "C) October 2, 1948","D) November 26, 1949"],
   )

max_score = len(questions_options) * 10

choice_options = ("D", "A", "B", "A", "D")

total_score = 0

for i, question in enumerate(questions_options):
    for j in question:
        print(j)
    user_choice = input("Enter your choice or press M to leave it unattempted : ")
    user_choice = user_choice.upper().strip()
    correct_option = choice_options[i]
    if user_choice == correct_option : 
        total_score = total_score + 10
    elif user_choice == "M": 
        print("Not attempted")
    else :
        total_score = total_score - 3
    print()
total_percentage = (total_score/max_score)*100
print(f"Your total score is {total_score}")
print(f"Your percentage is {total_percentage}%")