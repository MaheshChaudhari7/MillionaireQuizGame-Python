questions = [

    ["Who is the Prime Minister of India?", "Rahul Gandhi", "Narendra Modi", "Amit Shah", "Manmohan Singh", 2],

    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],

    ["What is the capital of India?", "Mumbai", "New Delhi", "Delhi", "Chennai", 2],

    ["Who invented the light bulb?", "Nikola Tesla", "Albert Einstein", "Thomas Edison", "Isaac Newton", 3],

    ["Which is the largest ocean in the world?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", 3],

    ["Who wrote the Ramayana?", "Tulsidas", "Valmiki", "Ved Vyasa", "Kalidasa", 2],

    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],

    ["Which is the fastest land animal?", "Tiger", "Cheetah", "Lion", "Horse", 2],

    ["What is the national animal of India?", "Elephant", "Tiger", "Lion", "Peacock", 2]

]

prizes = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

i = 0 #Loop variable

for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    #check whether the answer is correct or not
    answer = int(input("enter your answer(1,2,3,4):"))
    if (question[5]==answer):
        print("correct Answer")
    else:
        print(f"Incorrect , the correct answer is {question[5]}")
        print("Better Luck Next Time")
        break

    print(f"you won{prizes[i]}")#print the prizes
    i+=1 #increment the loop variable