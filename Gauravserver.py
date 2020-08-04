from Question import Question


question_prompts = [
    "When did the Bubonic Plague begin?\n(a) 1346\n(b) 1129\n(c) 1800\n(d) 2005\n\n",
    "What was the reason the Bubonic plague inflated?\n(a) Cleaning themselves regularly and self isolating themselves.\n(b) Infected animals causing the virus.\n(c) Bad hygiene, and not cleaning themselves regularly.\n(d) Not doing anything.\n\n",
    "What can be helpful ways of preventing the plague from spreading?\n(a) Following what everybody else is doing, whether it is smart or not.\n(b) Going outside frequently and not being as firm as most people.\n(c) Spending time around farm animals.\n(d) Self isolating and cleaning yourself.\n\n"  
]

questions = [
    Question(question_prompts[0], "a")
    Question(question_prompts[1], "c")
    Question(question_prompts[2], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "out of " + str(len(questions)) + "correct")

run_test(questions)

app.run()
