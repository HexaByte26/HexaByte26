import json
import random
import os
import time

# ---------------------SCHEDULE-ORGANIZER------------------------------
def scheduleOrganizer():
    def assignDictionaryToSchedule(subjectDictionary, list):
        if subjectDictionary['Subject Day'] == list[0]:
            mondaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedMondaySchedulesList.append(subjectDictionary['Subject Start Time'])

        elif subjectDictionary['Subject Day'] == list[1]:
            tuesdaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedTuesdaySchedulesList.append(subjectDictionary['Subject Start Time'])

        elif subjectDictionary['Subject Day'] == list[2]:
            wednesdaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedWednesdaySchedulesList.append(subjectDictionary['Subject Start Time'])

        elif subjectDictionary['Subject Day'] == list[3]:
            thursdaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedThursdaySchedulesList.append(subjectDictionary['Subject Start Time'])

        elif subjectDictionary['Subject Day'] == list[4]:
            fridaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedFridaySchedulesList.append(subjectDictionary['Subject Start Time'])

        elif subjectDictionary['Subject Day'] == list[5]:
            saturdaySchedules[subjectDictionary['Subject Code']] = subjectDictionary
            # sortedSaturdaySchedulesList.append(subjectDictionary['Subject Start Time'])

    def mainMenu():
        schedORG_menu = '''
------------------------------------------
        SCHEDULE ORGANIZER
        [1] Start Input
        [2] Exit
------------------------------------------
        '''
        print(schedORG_menu)

    mondaySchedules = {}
    tuesdaySchedules = {}
    wednesdaySchedules = {}
    thursdaySchedules = {}
    fridaySchedules = {}
    saturdaySchedules = {}

    sortedMondaySchedule = {}
    sortedTuesdaySchedule = {}
    sortedWednesdaySchedule = {}
    sortedThursdaySchedule = {}
    sortedFridaySchedule = {}
    sortedSaturdaySchedule = {}

    sortedMondaySchedulesList = []
    sortedTuesdaySchedulesList = []
    sortedWednesdaySchedulesList = []
    sortedThursdaySchedulesList = []
    sortedFridaySchedulesList = []
    sortedSaturdaySchedulesList = []
                
    subjectList = ('ET1', 'CPET1L', 'ET1L', 'PATHFIT1', 'GEC1', 'CHET', 'MATHANA13', 'GEC4', 'BET1','CHETL','NSTP',)

    timeList = [700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]

    dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


# schedule = ScheduleOrganizer(mondaySchedules, tuesdaySchedules, wednesdaySchedules, thursdaySchedules, fridaySchedules, saturdaySchedules)


    while True:
        mainMenu()
        try:
            command = int(input("Please select the desired number: "))
        except:
            print("INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN")
            continue
        if command == 1:
            os.system('cls')
            time.sleep(0.5)
        elif command == 2:
            os.system('cls')
            time.sleep(0.5)
            main()
        else:
            os.system('cls')
            time.sleep(0.5)
            print('Invalid Response hehe.')
            continue

        while True:
            print('\nSelect Subject Code')
            for i, j in enumerate(subjectList, start=1):
                print(f'{i}. {j.upper()}')
            try:
                subjectCodeNum = int(input("\nSubject Code: "))
                os.system('cls')
                time.sleep(0.5)
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN")
                continue
            try:
                subjectCode = subjectList[subjectCodeNum-1]
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE WITHIN THE CHOICES PLEASE TRY AGAIN")
                continue
            break

        while True:
            print('\nSelect Start Time')
            ante_meridian = 7
            midday = 12
            post_meridian = 1
            for i, j in enumerate(timeList, start=1):
                if timeList.index(j) < 5:
                    print(f"{i}. {j} ({ante_meridian}:00 AM)")
                    ante_meridian += 1
                elif timeList.index(j) == 5:
                    print(f"{i}. {j} ({midday}:00 PM)")
                else:
                    print(f"{i}. {j} ({post_meridian}:00 PM)")
                    post_meridian += 1
            try:
                subjectStartTimeNum = int(input("Subject Start Time: "))
                os.system('cls')
                time.sleep(0.5)
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN")
                continue
            try:
                subjectStartTime = timeList[subjectStartTimeNum-1]
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE WITHIN THE CHOICES PLEASE TRY AGAIN")
                continue
            break

        while True:
            print('\nSelect End Time')
            ante_meridian = 7
            midday = 12
            post_meridian = 1
            for i, j in enumerate(timeList, start=1):
                if timeList.index(j) < 5:
                    print(f"{i}. {j} ({ante_meridian}:00 AM)")
                    ante_meridian += 1
                elif timeList.index(j) == 5:
                    print(f"{i}. {j} ({midday}:00 PM)")
                else:
                    print(f"{i}. {j} ({post_meridian}:00 PM)")
                    post_meridian += 1
            try:
                subjectEndTimeNum = int(input("Subject End Time: "))
                os.system('cls')
                time.sleep(0.5)
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE NUMERIC PELASE TRY AGAIN")
                continue
            try:
                subjectEndTime = timeList[subjectEndTimeNum-1]
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE WITHIN THE CHOICES PLEASE TRY AGAIN")
                continue
            break

        while True:
            print('\nSelect Subject Day')
            for i, j in enumerate(dayList, start=1):
                    print(f"{i}. {j.capitalize()}")
            try:
                subjectDayNum = int(input("Subject Subject Day "))
                os.system('cls')
                time.sleep(0.5)
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN")
                continue
            try:
                subjectDay = dayList[subjectDayNum-1]
            except:
                os.system('cls')
                time.sleep(0.5)
                print("INVALID INPUT, INPUT MUST BE WITHIN THE CHOICES PLEASE TRY AGAIN")
                continue
            break

        subjectDict = {'Subject Code':subjectCode, 
                       'Subject Start Time':subjectStartTime, 
                       'Subject End Time':subjectEndTime, 
                       'Subject Day':subjectDay}
        for key, value in subjectDict.items():
            print(f"{key}:", value)

        assignDictionaryToSchedule(subjectDictionary=subjectDict, list=dayList)

        print('\nDo you want to enter another')
        isAnother = input('Answer(Y/N):').upper()

    
        if isAnother == 'Y':
            os.system('cls')
            time.sleep(0.5)
            continue
        else:
            os.system('cls')
            time.sleep(0.5)
            mon_json = json.dumps(mondaySchedules, indent=4)
            tues_json = json.dumps(tuesdaySchedules, indent=4)
            weds_json = json.dumps(wednesdaySchedules, indent=4)
            thurs_json = json.dumps(thursdaySchedules, indent=4)
            fri_josn = json.dumps(fridaySchedules, indent=4)
            sat_json = json.dumps(saturdaySchedules, indent=4)
            with open('Schedule.json', 'w') as f:
                f.write(mon_json)
            break

    while True:
        print(mon_json)
        print(tues_json)
        print(weds_json)
        print(thurs_json)
        print(fri_josn)
        print(sat_json)
        User_SO_Exit = input('\nAre you done making your schedule? Y/N: ').upper()
        if User_SO_Exit == 'Y':
            os.system('cls')
            time.sleep(0.5)
            main()
        if User_SO_Exit == 'N':
            os.system('cls')
            time.sleep(0.5)
            scheduleOrganizer()
        else:
            os.system('cls')
            time.sleep(0.5)
            print('Invalid Response hehe')
            continue

    
# ---------------------SCHEDULE-ORGANIZER------------------------------
# ---------------------------NOTES-------------------------------------


def notes_menu():
    while True:
        print(notes_menu_display)
        try:
            user_menuInput = int(input('Please enter the desired number: '))
        except:
            os.system('cls')
            time.sleep(0.5)
            print("INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRYAGAIN")
            continue
        if user_menuInput == 1:
            os.system('cls')
            time.sleep(0.5)
            try:
                with open("Subjects.json", "r") as file:
                    data = json.load(file)
                    print(json.dumps(data, indent=4))
                    user_note_respones = input("\nPress any key to exit... ").upper()
                    if user_note_respones == '':
                        os.system('cls')
                        time.sleep(0.5)
                        continue
            except:
                with open("Subjects.json", "w") as file:
                    data = json.dumps(Subjects, indent=4)
                    file.write(data)
            break
        elif user_menuInput == 2:
            os.system('cls')
            time.sleep(0.5)
            break
        elif user_menuInput == 3:
            os.system('cls')
            time.sleep(0.5)
            askuser = input("Do you want to clear your notes? Y/N: ").upper()
            if askuser == "Y":
                os.system('cls')
                time.sleep(0.5)
                with open('Subjects.json', 'w') as f:
                    new_json = json.dumps(Subjects, indent=4)
                    f.write(new_json)
            else:
                os.system('cls')
                time.sleep(0.5)
                continue
        elif user_menuInput == 4:
            os.system('cls')
            time.sleep(0.5)
            main()
        else:
            os.system('cls')
            time.sleep(0.5)
            print('Invalid Response hehes')
            continue

def input_data():
    print(subject_list)
    user_subject_choice = input('Subject: ').upper()
    while True: 

        user_inputUNIT = input('TOPIC: ').upper()
        user_inputTERM = input('TERMINOLOGY: ').upper()
        user_inputDESC = input('DEFINITION: ').upper()
        try:
            x[user_subject_choice][user_inputUNIT][user_inputTERM] = user_inputDESC
        except:
            x[user_subject_choice][user_inputUNIT] = {user_inputTERM: user_inputDESC}

        user_exit = input('Are you done putting datas? (Y/N): ').upper()
        with open('Subjects.json', 'w') as f:
            xjason = json.dumps(x, indent=4)
            f.write(xjason) 
        if user_exit == 'Y':
            os.system('cls')
            time.sleep(0.5)
            notes_menu()

notes_menu_display = '''
------------------------------------------
    NOTES
    [1] List of Notes
    [2] Add Notes
    [3] Clear Notes
    [4] Exit
------------------------------------------
'''
subject_list = '''
(NOTICE: Make sure to type the correct data. Thank you!)
List of Subjects:
ET1
CPETL
ET1L
PATHFIT1
GEC1
CHET
MATHA13
GEC4
BET1
CHETL
NSTP
'''
Subjects = {
"ET1": {},
"CPETL": {},
"ET1L": {},
"PATHFIT1": {},
"GEC1": {},
"CHET": {},
"MATHA13": {},
"GEC4": {},
"BET1": {},
"CHETL": {},
"NSTP": {}
}

# ---------------------------NOTES-------------------------------------

# ---------------------------FLASHCARD-------------------------------------

#for inputs
def create_flashcard():
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    return question, answer

#showing the inputs
def flashcard_mode(question, answer):
    print("\nFlashcard Mode")
    print("----------------")
    input("Press Enter to see question...")
    os.system('cls')
    time.sleep(0.5)
    print(f"Question: {question}")
    answers = input("Please put your answer here: ")
    if answers == answer:
        print(f"\nYou are correct! \nThe correct answer is: {answer}")
    else:
        print(f"\nYou are wrong! \nThe correct answer is: {answer}")
#The main menu
def main_flashcard():
    flashcards = []
    flashcard_menu = '''
------------------------------------------
        FLASHCARDS
        [1] Create Flashcard
        [2] Flashcard Mode
        [3] Exit
------------------------------------------
    '''
    while True:
        print(flashcard_menu)
        try:
            choice = int(input("Please select the desired number: "))
        except:
            print('INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN')
            continue
        #Basically the options/choice
        if choice == 1:
            os.system('cls')
            time.sleep(0.5)
            while True:
                question, answer = create_flashcard()  
                flashcards.append((question, answer))
                print("Flashcard created!")
                user_flashcardINPUT = input('Are you done creating flashcards? Y/N: ').upper()
                if user_flashcardINPUT == 'Y':
                    os.system('cls')
                    time.sleep(0.5)
                    break
                else:
                    os.system('cls')
                    continue
        elif choice == 2:
            os.system('cls')
            time.sleep(0.5)
            if flashcards:
                os.system('cls')
                time.sleep(0.5)
                while True:
                    random_flashcard = random.choice(flashcards)
                    flashcard_mode(*random_flashcard)
                    while True:
                        user_flashcardANSWER = input('\nAre you done answering flashcards? Y/N: ').upper()
                        if user_flashcardANSWER == 'Y':
                            os.system('cls')
                            time.sleep(0.5)
                            main_flashcard()
                        elif user_flashcardANSWER == 'N':
                            os.system('cls')
                            time.sleep(0.5)
                            break
                        else:
                            os.system('cls')
                            time.sleep(0.5)
                            print('Invalid Response hehe')
                            continue
                    continue
            else:
                os.system('cls')
                time.sleep(0.5)
                print("No flashcards created yet!")
        elif choice == 3:
            os.system('cls')
            time.sleep(0.5)
            main()
        else:
            os.system('cls')
            time.sleep(0.5)
            print('Invalid Response hehe')
            continue
# ---------------------------FLASHCARD-------------------------------------

# ---------------------------HANGMAN-------------------------------------

keywords = ['CPETL', 'BET1', 'ET1', 'MATHANA', 'GEC4', 'GEC1', 'CHEMISTRY']
correct_word = random.choice(keywords)
tries = 1
max_attempt = 7
hangman_display = 0
hangman_menu = '''
------------------------------------------
    HANGMAN
    [1] Start
    [2] Tutorial
    [3] Exit
------------------------------------------
'''
hangman_howtoplay = '''
                    HOW TO PLAY

1. You will be given a question that you need to answer.
2. You have a total of 6 attempts before the man will be hang.
3. If you fail to answer the question after 6 attempts. YOU LOSE!
4. But if you answered it correctly before 6 attempts. YOU WIN!
'''
losehangman_display = '''
You've reached your max attempt :<
  \033[31mYOU LOSE!\033[0m'''

hangman_playagain = '''
NOTE: Type "E" to EXIT and return HOME
            
[1] Yes
[2] No'''
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']


# ---------------------------HANGMAN-------------------------------------

noteplay_mainmenu = '''
------------------------------------------

        Welcome to NOTEPLAY!

        [1] Schedule Organizer
        [2] Notes
        [3] Flashcard
        [4] Hangman
        [5] Quit

------------------------------------------
'''

def main():
    while True:
        print(noteplay_mainmenu)
        try:
            select = int(input('Please select the desired number: '))
        except:
            print('INVALID INPUT, INPUT MUST BE NUMERIC PLEASE TRY AGAIN')
            continue

        # SCHEDULE ORGANIZER
        if select == 1:
            os.system('cls')
            time.sleep(0.5)
            scheduleOrganizer()

        # NOTES
        elif select == 2:
            os.system('cls')
            time.sleep(0.5)
            while True:
                notes_menu()

                try:
                    with open('Subjects.json', 'x') as f:
                        json_string = json.dumps(Subjects, indent=4)
                        f.write(json_string)
                    with open('Subjects.json', 'w') as f:
                        f.write(json_string)
                    while True:
                        print(subject_list)
                        user_subject_choice = input('Subject: ').upper()
                        #user_subject_choice == 'ET1':     
                        user_inputUNIT = (input('FORMAT TOPIC: ')).upper()
                        user_inputTERM = input('FORMAT (TERM): ').upper()
                        user_inputDESC = input('FORMAT (DESCRIPTION): ').upper()
                        Subjects[user_subject_choice] = ({user_inputUNIT: {user_inputTERM: user_inputDESC}})
                        break
                    json_string = json.dumps(Subjects, indent=4)
                    with open('Subjects.json', 'w') as f:
                        f.write(json_string)
                except:
                    pass

                with open('Subjects.json', 'r') as f:
                    jason = f.read()
                global x
                x = json.loads(jason)
                input_data()

                askUser = input('Are you finished?((Y/N)): ').upper()
                if askUser == 'Y':
                    os.system('cls')
                    time.sleep(0.5)
                    main()

        #Flashcard
        elif select == 3:
            os.system('cls')
            time.sleep(0.5)
            main_flashcard()

        # HANGMAN
        elif select == 4:
            os.system('cls')
            time.sleep(0.5)
            while True:
                print(hangman_menu)
                user_input = input('Please enter the desired number: ')
                if user_input == '1':
                    os.system('cls')
                    time.sleep(0.5)
                    print('\nHave Fun!')
                    print(HANGMANPICS[0])   
                elif user_input == '2':
                    os.system('cls')
                    time.sleep(0.5)
                    print(hangman_howtoplay)
                    exit_button = input('Press any key to exit...')
                    if exit_button == '':
                        os.system('cls')
                        time.sleep(0.5)
                        continue
                elif user_input == '3':
                    os.system('cls')
                    time.sleep(0.5)
                    main()
                else:
                    os.system('cls')
                    time.sleep(0.5)
                    print('Invalid Response hehe')
                    continue

                while True:
                    global tries
                    if tries == max_attempt:
                        print(losehangman_display)
                        play_agains = input('\nDo you want to play again?(Y/N): ').upper()
                        if play_agains == 'Y':
                            os.system('cls')
                            time.sleep(0.5)
                            tries = 1
                            print(HANGMANPICS[0])
                            continue
                        elif play_agains == 'N':
                            os.system('cls')
                            time.sleep(0.5)
                            tries = 1
                            break
                    if tries == 1:
                        random_number = random.randint(0, 6)
                        correct_word = keywords[random_number]
                    if correct_word == keywords[0]:
                        print('\nThis subject teaches about programming.')
                    elif correct_word == keywords[2]:
                        print('\nThis subject teaches about electrical.')
                    elif correct_word == keywords[3]:
                        print('\nThis subject talks about mathematics of change.')
                    elif correct_word == keywords[4]:
                        print('\nThis subject teaches about application of mathematics.')
                    elif correct_word == keywords[5]:
                        print('\nThis subject talks about identity.')
                    elif correct_word == keywords[6]:
                        print('\nThis subject talks about chemicals.')
                    else:
                        print('\nThis subject teaches about the course.')
                    user_answer = input('What is your answer? ').upper()
                    if user_answer == correct_word:
                        print('\n\033[32mCongratulations!\033[0m Your answer is correct.') 
                    elif user_answer != correct_word:
                        os.system('cls')
                        time.sleep(0.5)
                        print(f'Your answer "{user_answer}" is incorrect. Try again.')
                        tries += 1
                        print('Tries', tries)
                        print(HANGMANPICS[tries-1])
                        continue
                        
                    play_agains = input('\nDo you wish to play again?(Y/N): ').upper()
                    tries = 1
                    if play_agains == 'Y':
                        os.system('cls')
                        time.sleep(0.5)
                        print(HANGMANPICS[0])
                        continue
                    else:
                        os.system('cls')
                        time.sleep(0.5)
                        tries = 1
                        break
        #Quit
        elif select == 5:
            os.system('cls')
            time.sleep(0.5)
            print('Thank you for playing!!!')
            quit()

        else:
            os.system('cls')
            time.sleep(0.5)
            print('Invalid Response hehe')
            continue
main()         