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


def ret_faceoff_text(animal):

    faceoff_text_dict = {
        'panda': "A hush falls over the bamboo forest, you stare into the cold dead eyes of panda",
        'duck':  "Unflinching, your opponent duck readies its wing for a decisive move",
        'fox':   "This is what it has come to, you face your nemesis fox one final time"
    }

    return faceoff_text_dict[animal]


def ret_outcome_text(animal, outcome):

    animal_outcome = animal + "_" + outcome

    outcome_dict = {
        'panda_win':  "You've bested panda, you pop champagne to celebrate",
        'panda_lose': "Panda does not react much to his victory, you however, are devastated",
        'duck_win':   "You stand up to cheer your victory, leaving duck humiliated in your shadow",
        'duck_lose':  "Duck is happy for his victory. Duck wears a little hat to celebrate",
        'fox_win':    "You've bested your arch nemesis. You eat cake in fox's face to celebrate",
        'fox_lose':   "Fox looks gleeful after beating you, shoving cake into her fat little face"
    }

    return outcome_dict[animal_outcome]