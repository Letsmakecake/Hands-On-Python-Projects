try:
    questions = [
        ["Who is Shahrukh Khan", "Actor", "Plumber", "Teacher", "Driver", 1],
        ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
        ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
        ["What is the boiling point of water?", "90°C", "100°C", "80°C", "120°C", 2],
        ["Which animal is known as the king of the jungle?", "Tiger", "Elephant", "Lion", "Bear", 3],
        ["Which language is primarily used for Android app development?", "Python", "Kotlin", "Swift", "Ruby", 2],
        ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
        ["Who invented the light bulb?", "Newton", "Einstein", "Edison", "Tesla", 3],
        ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Rhino", 2],
        ["Which is the smallest continent?", "Asia", "Europe", "Australia", "Africa", 3],
        ["What is H2O?", "Salt", "Oxygen", "Hydrogen", "Water", 4],
        ["Who wrote the Ramayana?", "Tulsidas", "Valmiki", "Ved Vyas", "Kalidas", 2],
        ["How many colors are there in a rainbow?", "5", "6", "7", "8", 3],
        ["Which instrument is used to measure temperature?", "Thermometer", "Barometer", "Speedometer", "Altimeter", 1],
        ["What is the national bird of India?", "Peacock", "Sparrow", "Crow", "Parrot", 1]
    ]
    prizes = [5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,9000000,9500000,10000000]
    i=0
    for question in questions:
        print(f"{question[0]}")
        print(f"1: {question[1]}")
        print(f"2: {question[2]}")
        print(f"3: {question[3]}")
        print(f"4: {question[4]}")
        a=int(input("Enter the Choice 1,2,3,4\n"))
        if (a == question[5]):
            print(f"Correct Answer {question[5]}")
        else:
            print("Better Luck Next Time!")
            print(f"Correct Answer was {question[5]}")
            print(f"Yov have won {prizes[i]}")
            break
        i+-1
except Exception as e:
    print("Enter Valid Value")
        