# randomQuizGenerator.py
# Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz_num in range(35): # Generate 35 quiz files.
    # Create the quiz and answer key files.
    quiz_file = open('capitalsquiz%s.txt' % (quiz_num + 1), 'w')
    answer_key_file = open('capitalsquiz_answers%s.txt' % (quiz_num + 1), 'w')

    # Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz_num + 1))
    quiz_file.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys()) # get all states in a list
    random.shuffle(states) # randomize the order of the states

    # Loop through all 50 states, making a question for each.
    for question_num in range(50):

        # Get right and wrong answers.
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values()) # get a complete list of answers
        del wrong_answers[wrong_answers.index(correct_answer)] # remove the right answer
        wrong_answers = random.sample(wrong_answers, 3) # pick 3 random ones

        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options) # randomize the order of the answers

        # Write out the question and answer options.
        quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
        for i in range(4):
            quiz_file.write('    %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # Write out the answer key to a file.
        answer_key_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))
    quiz_file.close()
    answer_key_file.close()