# data ready

questions = [
    {
        "question": "which language is popular for all?",
        "answer": "python"
    },
    {
        "question": "which keyword defines a function?",
        "answer": "def"
    },
    {
        "question": "which data type stores True of False",
        "answer": "boolean"
    }
]

def run_quiz():
    score = 0 # user's score

    for item in questions:
        print(item["question"])
        # get the response from the user
        answer = input("Your answer: ")

        
        if answer.lower() == item["answer"]:
            score = score + 1
        else:
            print("Your answer was incorrect")

    print("Your final score: ", score, "/", len(questions))


run_quiz()
