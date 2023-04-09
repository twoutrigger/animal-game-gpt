import random

def rock_paper_scissors(choice):

    # input choice is one of these three text options
    rps_options = ['rock', 'paper', 'scissors']

    # generate opponent's choice
    comp_choice_num = random.randrange(0, 3, 1)
    comp_choice = rps_options[comp_choice_num]
    
    # in a case of a tie, re-randomize opponent's choice for V1
    while comp_choice == choice:
        comp_choice_num = random.randrange(0, 3, 1)
        comp_choice = rps_options[comp_choice_num]

    # rock paper scissors logic
    if (choice=='rock' and comp_choice=='paper'):
        outcome = {'status': 'lose', 'choice': choice, 'comp_choice': comp_choice}
    elif (choice=='rock' and comp_choice=='scissors'):
        outcome = {'status': 'win', 'choice': choice, 'comp_choice': comp_choice}
    elif (choice=='paper' and comp_choice=='scissors'):
        outcome = {'status': 'lose', 'choice': choice, 'comp_choice': comp_choice}
    elif (choice=='paper' and comp_choice=='rock'):
        outcome = {'status': 'win', 'choice': choice, 'comp_choice': comp_choice}
    elif (choice=='scissors' and comp_choice=='rock'):
        outcome = {'status': 'lose', 'choice': choice, 'comp_choice': comp_choice}
    elif (choice=='scissors' and comp_choice=='paper'):
        outcome = {'status': 'win', 'choice': choice, 'comp_choice': comp_choice}

    return outcome

# print(rock_paper_scissors('scissors'))