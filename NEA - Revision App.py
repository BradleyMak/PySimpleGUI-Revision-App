import PySimpleGUI as sg
# imports PySimpleGUI
sg.theme('DarkBlue')
# sets a colour theme for the program
import hashlib
# imports the module for hashing strings
import csv
# imports the module to allow us to use csv files.

StartScreen = [[sg.Text('Welcome to the revision app! Please log in, or create a new account to continue.', font=("Helvetica", 13, "bold"), size=(45, 3), justification='center')],
               # Creates a centred title for the layout which will appear at the top of the screen
               [sg.Text("                                  "), sg.Button('Log In', font=("Helvetica", 13), key='LOGIN', border_width=5, size=(16, 4))],
               [sg.Text("                                  "), sg.Button('Create an account', font=("Helvetica", 13), key='SIGNUP', border_width=5, size=(16, 4))],
               [sg.Text("                                  "), sg.Button('EXIT', font=("Helvetica", 13), key='EXIT', border_width=5, size=(16, 4), button_color=('white', 'red'))]]
#               Creates 3 centralised buttons on different 'layers' of the screen which have text on them stating their purpose. The Exit button is red to signify its purpose.

Login = [[sg.Text('Log-in details:', font=("Helvetica", 18, "bold"), justification='center', size=(45,1))],
          # Creates a block of text at the top of the screen which is centralised.
          [sg.Text("Username:", size=(9,1), font=("Helvetica", 14)), sg.InputText(key='username_entry', size=(100,4))],
          [sg.Text("Password:", size=(9,1), font=("Helvetica", 14)), sg.InputText(key='password_entry', password_char='*', size=(100,2))],
          # Creates 2 labelled input boxes for the user to enter their username and password, which can then be validated.
          [sg.Button('BACK', font=("Helvetica", 15), key='BACK2', button_color=('red', 'white')), sg.Text('', size=(12,2)), sg.Button('Log In', key='LogIn', font=("Helvetica", 15))],
          # Creates a red back button (to take the user back to the Start Screen) and a log in button for the user to validate the details they entered and enter their account.
          [sg.Text('', key='login_error', font=("Helvetica", 15, "bold"), text_color='red', justification='center', size=(38,3))]]
#          Empty red error message which can be updated to contain text if an error occurs.

Signup = [[sg.Text('Please enter the username, password and email you would like for your new account below:', font=("Helvetica", 13, "bold"), justification='center', size=(45,3))],
          # Creates a block of text at the top of the screen which is centralised and is the same size and font as the block of text on the Start Screen.
          [sg.Text("Username:", size=(12,1), font=("Helvetica", 13)), sg.InputText(key='newusername', size=(100,2))],
          [sg.Text("Password:", size=(12,1), font=("Helvetica", 13)), sg.InputText(key='newpassword', password_char='*', size=(100,2))],
          [sg.Text("Re-enter Password:", size=(12,2), font=("Helvetica", 13)), sg.InputText(key='password_re-entry', password_char='*', size=(100,2))],
          [sg.Text("Email Address:", size=(12,1), font=("Helvetica", 13)), sg.InputText(key='newemail', size=(100,2))],
          # Creates 4 labelled input boxes for the user to enter their username/password/password re-entry/email address, which can then be validated.
          [sg.Button('BACK', font=("Helvetica", 15), key='BACK1', button_color=('red', 'white')), sg.Text('', size=(12,2)), sg.Button('Submit', key='NewAccount', font=("Helvetica", 15))],
          # Creates a red back button (to take the user back to the Start Screen) and a submit button for the user to validate the details they entered and create their account.
          [sg.Text('', key='signup_error', font=("Helvetica", 15, "bold"), text_color='red', justification='center', size=(38,3))]]
#          Empty red error message which can be updated to contain text if an error occurs.

MainMenu = [[sg.Text('Welcome (username)!', key='welcomemsg', font=("Helvetica", 18, "bold"), size=(45, 2), justification='center')],
            # Creates a centred welcome message for the layout which will appear at the top of the screen.
            [sg.Text("            "), sg.Button('Create Set', font=("Helvetica", 13), key='CREATESET', border_width=5, size=(16, 4)), sg.Button('My Sets', font=("Helvetica", 13), key='MYSETS', border_width=5, size=(16, 4))],
            [sg.Text("            "), sg.Button('My Progress', font=("Helvetica", 13), key='PROGRESS', border_width=5, size=(16, 4)), sg.Button('Manage Account', font=("Helvetica", 13), key='ACCOUNT', border_width=5, size=(16, 4))],
            [sg.Text("                                  "), sg.Button('Log Out', font=("Helvetica", 13), key='LOGOUT', border_width=5, size=(16, 4), button_color=('white', 'red'))]]
#           Defines the Main Menu layout which consists of 5 symmetrically placed buttons on the screen with large text at the top welcoming the user.

CreateSet = [[sg.Text('Create your revision set:', font=("Helvetica", 18, "bold"), size=(45, 2), justification='center')],
            # Creates a centred message for the layout which will appear at the top of the screen.
            [sg.Text("Set Name:", size=(12,1), font=("Helvetica", 13)), sg.InputText(key='newsetname', size=(100,2))],
            [sg.Button('Back', font=("Helvetica", 13), key='BACK3', border_width=5, size=(6, 1), button_color=('white', 'red')), sg.Text("                        "),
             sg.Button('Confirm', font=("Helvetica", 13), key='confirmset', border_width=5, size=(6, 1))],
             [sg.Text('', key='newset_error', font=("Helvetica", 15, "bold"), text_color='red', justification='center', size=(38,3))]]
#           Defines the CreateSet layout which consists of an entry box for the set name, a confirm button and a back button.

MySets = [[sg.Text('My Sets', font=("Helvetica", 13, "bold"), size=(45, 1), justification='center')],
        # Creates a centred title for the layout which will appear at the top of the screen
            [sg.Button('Set 1', font=("Helvetica", 13), key='SET1', border_width=5, size=(50, 2))],
            [sg.Button('Set 2', font=("Helvetica", 13), key='SET2', border_width=5, size=(50, 2))],
            [sg.Button('Set 3', font=("Helvetica", 13), key='SET3', border_width=5, size=(50, 2))],
            [sg.Button('Set 4', font=("Helvetica", 13), key='SET4', border_width=5, size=(50, 2))],
            [sg.Button('Set 5', font=("Helvetica", 13), key='SET5', border_width=5, size=(50, 2))],
            [sg.Button('Back', font=("Helvetica", 13), key='BACK4', border_width=5, size=(5, 1), button_color=('white', 'red'))]]
#           Creates 5 centralised buttons on different 'layers' of the screen which have text on them stating their purpose. The back button is red to signify its purpose.

Set = [[sg.Text('Please choose an option for this set:', font=("Helvetica", 18, "bold"), justification='center', size=(45,1))],
#       Creates a block of text at the top of the screen which is centralised.
        [sg.Text("                                  "), sg.Button('Add flashcards', font=("Helvetica", 13), key='ADDFLASHCARDS', border_width=5, size=(16, 3))],
        [sg.Text("                                  "), sg.Button('Revise flashcards', font=("Helvetica", 13), key='REVISE', border_width=5, size=(16, 3))],
        [sg.Text("                                  "), sg.Button('Quiz', font=("Helvetica", 13), key='QUIZ', border_width=5, size=(16, 3))],
        [sg.Button('Back', font=("Helvetica", 13), key='BACK5', border_width=5, size=(5, 1), button_color=('white', 'red'))]]
#       3 centralised buttons each of which serving their own purpose.

AddFlashcard = [[sg.Text('New Flashcard:', font=("Helvetica", 18, "bold"), justification='center', size=(45,1))],
          # Creates a block of text at the top of the screen which is centralised.
          [sg.Text("Term:", size=(9,1), font=("Helvetica", 14)), sg.InputText(key='term_entry', size=(100,2))],
          [sg.Text("Definition:", size=(9,1), font=("Helvetica", 14)), sg.Multiline(key='definition_entry', size=(100,1))],
          # Creates 2 labelled input boxes for the user to enter the term and definition.
          [sg.Button('BACK', font=("Helvetica", 15), key='BACK6', button_color=('red', 'white')), sg.Text('', size=(15,2)), sg.Button('Add', key='ADD', font=("Helvetica", 15))],
          # Creates a red back button and an 'add' button for the user to confirm the term and definition and write them to their CSV file.
          [sg.Text('', key='addflashcard_error', font=("Helvetica", 15, "bold"), text_color='red', justification='center', size=(38,3))]]
#          Empty red error message which can be updated to contain text if an error occurs.

ReviseFlashcard = [[sg.Text('', font=("Helvetica", 18, "bold"), text_color='blue', justification='center', key='flashcard_text', border_width=5, size=(37,10), background_color='white')],
                   [sg.Text('                           '), sg.Button('', key='PREVIOUS', font=("Helvetica", 12), size=(7,1), image_data=b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAAAAACpleexAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQflAhsUOgagYNOPAAAA9klEQVQ4y83UsWrCUBQG4B+DoJ0U7Sya+ArWPkOwaEFfQ0EcfQRp0adwqEifoYPJoC8gdUjcqlMSOxiOV7skg+bf7D9/cDnnnnMgZPCPoOd6FLQaFXOZDMN5FUAzSIKH8aNyqLoJcNfPnh105zb8bmtg4KIOEDD80MHA4K0ABv50M2DgupWKOJTsrROP61/gVw2xpEuGHo/RtCDHaRnJeUIwyhMOGoYPjFPJkY6H9NN0MWR76mzD7b8vfNWi8OoXqqHocUOhxuy9yEEJZwYH1UY/k1A2HW65RPYDbl1FfifcAVAlfXInRcV+qZgrIaD45Nm7mjvCE31NCTMC2AOGAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTAyLTI3VDIwOjU4OjA2KzAwOjAwpvtxUAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0wMi0yN1QyMDo1ODowNiswMDowMNemyewAAAAASUVORK5CYII='),
                    sg.Button('', key='NEXT', font=("Helvetica", 12), size=(7,1), image_data=b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAQAAAAm93DmAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQflAhsUOCk5h4xUAAABQUlEQVRIx+2WTU7CUBSFv2IToczE6KDIgAU4cADuQqMDF2EkgchE1yAJxl0QJ01cgtHoEvgxjo0xTuhA4DKofxhf8fnukNNJm958zX3v9NwHC7lqyaI2zxoT3rQ+vcUVAyKqOriACEEQeuyScQduMHgHCk/UyLoCSzx+AoUhLVY0gcKYS8qaQEG4ZVsXKPTZtzLeXKDwTIOcJlCIOWf1q9AHAgpkkBScEBpby3JIiSbd5NGjygmbc6wq+Kzjp1TcU+c6ub0ztGJ7PXCQdDFSAgovHBN4qWtnq5iWLhBeFXJjVrrAmAvtTcmp28ajwqmmsT3+9usV6RAa3k6IaNKzW+60cGhTsN8/c3zVNeOrz95/jfcb8MZlRv8EjuhoDqkhZ65jtDgz6I9YdsN9P4p02dFJgI/DUkUDlihPSKCHW8ikKcz8S10jKgWSAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTAyLTI3VDIwOjU2OjQxKzAwOjAw+d9xlwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0wMi0yN1QyMDo1Njo0MSswMDowMIiCySsAAAAASUVORK5CYII='),
                    sg.Button('', key='FLIP', font=("Helvetica", 12), size=(7,1), image_data=b'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'),
                    sg.Button('', key='DELETE', font=("Helvetica", 12), size=(7,1), image_data=b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAAAAACpleexAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAHdElNRQflAhsVAgEoWZDgAAACL0lEQVQ4y2P4jwC/YxlgQO7KfzTAgMT+asdq4WAPBA7SXAfwKfxiI3f7+zcg+J7Jjlfhzwn17yGsNYW38SnECyAK38wqLMACGi+gKfyayMSAFWicR1V4SpABB6hDVbiHA5fCDFSFu3EqTEdVeLe5Hjuo3Uxm8PybEZuQkBA7/R+EEZ//7P+5ZDDjOZqJqWAHRf79Gw1mSFz/v4EVnDbuoyksA8tH/f0HUSh5A6pQ8wWawgYcCg3eoSnsx6HQ+jOawrk4FHr+QFO4nAlTIYt2YtPGv2gKt7BhKNSaCvTIP/RkdogbXeHNS/+udkYF5G/8hKLwND+6wv/fJ8iAmOzBt5AVXhVDV/ivl4Obk4GBiZ/R6QmSwnty6ArPSfGtXCjBGHfKk6EGSeFTFXSF9Qy8G/+vyHvzxpVB5zlSntFHU/jXn4FBccff36+iGBn4TiAUfrZGU/jbA0iV/P1/XIqBgXMfQuF3Z3SrExkY496+uvB3pRiD+BWEwt+B6AoXM4teeBsJtD2eweMLQuG/OHSFb5yZQj2YGOQz5Xk3IGeFDIwAP2sEyV68nb+RFZajK/z2+3aWPCeboOOaXyiZqw1d4Z7Wt38f7Nt2FhbVMIUTMVIPp/X0Kx/Qc+H///MZMRMus2D6LwyFa1nQFG4EpfCIvxgKt7FBsmsULLuuB+lMwrT6MA9Q3PjObWOwQs4lnytAdAGmwvNCQHEmDXVoOSlqDE7yDZgKH+tgKcrYFyMpBADsP6WKN8Dm9AAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMS0wMi0yN1QyMTowMjowMSswMDowMNi/qtAAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjEtMDItMjdUMjE6MDI6MDErMDA6MDCp4hJsAAAAAElFTkSuQmCC')],
                   [sg.Text('', key='revise_error', font=("Helvetica", 15, "bold"), text_color='red', justification='center', size=(38,2))],
                   [sg.Button('BACK', font=("Helvetica", 15), key='BACK7', button_color=('red', 'white'))]]
#                   Layout for revising flashcards, consisting of a white text box and 4 buttons underneath, as well as an error message and back button.

NoFlashcards = [[sg.Text('There are no flashcards in this set to revise!', font=("Helvetica", 18, "bold"), text_color='red', justification='center', size=(30,3))],
                [sg.Button('BACK', font=("Helvetica", 15), key='BACK8', button_color=('red', 'white'))]]
                # simple layout to display to the user there are no flashcards in a set to revise.

ProgressTracker = [[sg.Text('Progress Tracker')]]
ManageAccount = [[sg.Text('Manage Account')]]

layout = [[sg.Column(StartScreen, key='-COL1-', visible=True), sg.Column(Login, visible=False, key='-COL2-'), sg.Column(Signup, visible=False, key='-COL3-'),
           sg.Column(MainMenu, visible=False, key='-COL4-'), sg.Column(CreateSet, key='-COL5-', visible=False), sg.Column(MySets, key='-COL6-', visible=False),
           sg.Column(ProgressTracker, key='-COL7-', visible=False), sg.Column(ManageAccount, key='-COL8-', visible=False),
           sg.Column(Set, key='-COL9-', visible=False), sg.Column(AddFlashcard, key='-COL10-', visible=False), sg.Column(ReviseFlashcard, key='-COL11-', visible=False),
           sg.Column(NoFlashcards, key='-COL12-', visible=False)]]
# Defines the 'column' layouts which can be made visible/invisible to the user as required to give the impression of the program switching layouts.

window = sg.Window('Revision App', layout, size=(500,400))
# Creates a window with a given name for the layout to be displayed on whilst the program is running.

def validate_username(username):
    with open('userinfo.txt', 'r') as file:
        # opens the file userinfo.txt to read.
        for line in file.readlines():
            # for each line in userinfo.txt...
            if line == (username + "\n"):
                # "\n" is present because the line extracted from the file has a line break,
                # so to check whether the characters are the same I have added a line break to the username too before being compared.
                global valid_details
                # makes valid_details global.
                valid_details = False
                # If a line in the file is the same as the username, valid_details is set to False.

def validate_password(password, password_validation):
    if password != password_validation:
        global valid_details
        # makes valid_details global.
        valid_details = False
        # If the 2 passwords the user entered do not match (possible typo), valid_details is set to False.

def validate_email(email):
    global valid_details
    # makes valid_details global.
    if len(email)>10 and email[(len(email)-10): (len(email))] == '@gmail.com':
        valid_details = True
    else:
        valid_details = False
        # if the email the user entered is a valid gmail address, then valid_details remains true,
        # otherwise it is set to false.

def set_names(username):
    file = open(f'{username}.csv', mode='r')
    rows = list(csv.reader(file))
#   the rows are extracted from the users file in a 2D array
    names = rows[0]
#   the first row is saved as the names variable
    file.close()
    for i in range (0,5):
        window.FindElement(f'SET{i+1}').update(f'Set {i+1} - {names[i]}')
#   goes through each of the users 5 saved set names and
#   updates each of the buttons in turn on the MySets layout to display the set name.

while True:  # event loop to allow the program to run
    event, values = window.read()
    print(event, values)
#   Read and print the event that happened and the values dictionary. This allows me to see if the buttons have been defined correctly.
    if event in (None, 'EXIT'):
        break
#   If the window is closed or the exit button is pressed, the event loop breaks and the program stops running.
    if event == 'LOGIN':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)
#   If the user presses the log in button, the 'StartScreen' layout is made invisible and the 'Login' layout is made visible.
    if event == 'SIGNUP':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL3-'].update(visible=True)
#   If the user presses the sign up button, the 'StartScreen' layout is made invisible and the 'Signup' layout is made visible.
    if event == 'BACK1':
        window[f'-COL3-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
#   If the user presses the back button on the sign up screen, the 'Signup' layout is made invisible and the 'StartScreen' layout is made visible.
        window.FindElement('newusername').update('')
        window.FindElement('newpassword').update('')
        window.FindElement('password_re-entry').update('')
        window.FindElement('newemail').update('')
        window.FindElement('signup_error').update('')
#       All of the entry fields on the signup page, as well as the error message, are cleared too.
    if event == 'BACK2':
        window[f'-COL2-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
#       If the user presses the back button on the log in screen, the 'Login' layout is made invisible and the 'StartScreen' layout is made visible.
        window.FindElement('username_entry').update('')
        window.FindElement('password_entry').update('')
        window.FindElement('login_error').update('')
#       The input fields, as well as the error message, on the log in screen are cleared for security reasons upon pressing the back button.
    if event == 'NewAccount':
#       If the 'Submit' button is pressed...
        username = values['newusername']
        password = hashlib.sha256(str(values['newpassword']).encode('utf-8')).hexdigest()
        password_validation = hashlib.sha256(str(values['password_re-entry']).encode('utf-8')).hexdigest()
        # hashes the passwords the user entered using the SHA-256 hashing algorithm and converts them into hexadecimal to shorten it.
        email = str(values['newemail'])
#       Reads the username, password entries (and hashes them) and email the user entered from the display and saves them as variables.
        valid_details = True
#       This variable is initially set to True but will be used to tell the program whether the username the user enters is true or false.
        if username == '' or password == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' or password_validation == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' or email == '':
#       If any of the entry fields are left empty...
            valid_details = False
            window.FindElement('signup_error').update('Error: Please fill all fields!')
            # ...set valid_details to False so the user does not advance and alert them to the error.
        else:
            validate_username(username)
#           Calls the function validate_username with the username as a parameter.
            if valid_details == False:
                window.FindElement('signup_error').update('Error: Username already taken!')
#           Updates the error message to tell the user the username they entered is already taken.
            else:
                validate_password(password, password_validation)
#                If valid_details is true (i.e. the username is valid), the password can then be validated.
                if valid_details == False:
                    window.FindElement('signup_error').update('Error: Passwords do not match!')
#               Updates the error message to alert the user to a possible typo as the passwords they entered do not match.
                else:
                    validate_email(email)
#                    If valid_details is true at this stage (i.e. both the username and passwords were valid),
#                    the email next needs to be verified, so the relevant subroutine is called.
                    if valid_details == False:
                        window.FindElement('signup_error').update('Error: Invalid email address! Must be a gmail address!')
#                       Updates the error message to alert the user to the fact that the email they entered is invalid.
        if valid_details == True:
            file = open('userinfo.txt', 'a+')
#           Opens the file 'userinfo.txt' so that the users details can be appended to it, which means information can be written to the file without overwriting it.
            file.write(username + "\n")
            file.write(password + "\n")
            file.write(email + "\n")
#           Writes the contents of the 3 variables declared earlier to the file. The "\n" ensures all info is written on seperate lines.
            file.close()
#           Closes the file.
            file = open(f"{username}.csv", "x")
            file.close()
#           creates a CSV file specific to that user.
            with open(f"{username}.csv", mode="w", newline='') as userfile:
                userfile = csv.writer(userfile, delimiter=',')
                userfile.writerow(['','','','',''])
#               Opens the users CSV file and writes the first row to the file, consisting of the number of sets the user uas
#               (initially 0), as well as 5 empty slots for set names to be inserted upon creation.
            window.FindElement('newusername').update('')
            window.FindElement('newpassword').update('')
            window.FindElement('password_re-entry').update('')
            window.FindElement('newemail').update('')
#           Clears each of the input fields by updating their contents to nothing, ready for the next user to log in.
            window.FindElement('signup_error').update('')
#           Clears the error message from the sign up screen when the details entered are valid.
            window[f'-COL3-'].update(visible=False)
            window[f'-COL4-'].update(visible=True)
#           Updates the layout to the main menu after a successful Sign Up by making the sign up column invisible and the main menu column visible.
            window.FindElement('welcomemsg').update(f'Welcome {username}!')
#           When the user successfully signs up and is taken to the main menu, the welcome message is updated to include their username.
    if event == 'LogIn':
#       If the Log in button on the LOGIN layout is pressed...
        username = values['username_entry']
        password = hashlib.sha256(str(values['password_entry']).encode('utf-8')).hexdigest()
#       The username and password the user entered are saved as variables (and the password is hashed before being saved).
        file = open('userinfo.txt', 'r')
#       opens the file userinfo.txt to read.
        line = file.readline()
#       reads the first line from the file and saves it as 'line'
        while line != (username + "\n") and line != '':
            line = file.readline()
#           while the line read from the file isn't the username, read the next line from the file and save it as the variable 'line'
        if file.readline() == (password + "\n"):
            window[f'-COL2-'].update(visible=False)
            window[f'-COL4-'].update(visible=True)
            window.FindElement('username_entry').update('')
            window.FindElement('password_entry').update('')
            window.FindElement('login_error').update('')
#           once the line extracted equals the username (+ "\n" as the line extracted has a line break so the username needs to have one too),
#           it will exit the while loop, and if the next line is equal to the hash of the password the user enters, their log in details are correct,
#           and they are taken to the main menu. the information entered and error messages are cleared.
            email = file.readline().rstrip('\n')
#           defines the email variable to the users email which they inputted when signing up,
#           and removes the line break from the line which has been read from the file before saving it.
            window.FindElement('welcomemsg').update(f'Welcome {username}!')
#           When the user successfully logs in, the welcome message is updated to include their username.
        elif file.readline() == '':
            window.FindElement('login_error').update('Error: Invalid username/password!')
#           If all of the information in the file has been searched through (and thus there is nothing left to search so the next line is nothing), print that.
        else:
            window.FindElement('login_error').update('Error: Invalid username/password!')
#           If the username has been found but the password on the next line does not match with what the user entered.

    if event == 'CREATESET':
        window[f'-COL4-'].update(visible=False)
        window[f'-COL5-'].update(visible=True)
#   If the 'Create Set' button is pressed, the Main Menu layout is made invisible and the 'CREATESET' layout is made visible.
    if event == 'MYSETS':
        window[f'-COL4-'].update(visible=False)
        window[f'-COL6-'].update(visible=True)
#   If the 'My Sets' button is pressed, the Main Menu layout is made invisible and the 'MYSETS' layout is made visible.
        set_names(username)
#   set_names subroutine is called to update the set names on the buttons on the MySets layout.
    if event == 'PROGRESS':
        window[f'-COL4-'].update(visible=False)
        window[f'-COL7-'].update(visible=True)
#   If the 'Progress Tracker' button is pressed, the Main Menu layout is made invisible and the 'PROGRESS' layout is made visible.
    if event == 'ACCOUNT':
        window[f'-COL4-'].update(visible=False)
        window[f'-COL8-'].update(visible=True)
#   If the 'Manage Account' button is pressed, the Main Menu layout is made invisible and the 'ACCOUNT' layout is made visible.
    if event == 'LOGOUT':
        window[f'-COL4-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)
#   if the log out button is pressed, the layout is updated to display the Start Screen
        username = ''
        password = ''
        password_validation = ''
        email = ''
#   also all variables are set to empty strings for security reasons

    if event == 'BACK3':
        window[f'-COL5-'].update(visible=False)
        window[f'-COL4-'].update(visible=True)
        window.FindElement('newset_error').update('')
        window.FindElement('newsetname').update('')
#       Updates the layout from the CreateSet display to the MainMenu and clears the entry field and error message.
    if event == 'BACK4':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL4-'].update(visible=True)
#       Updates the layout from the MySets display to the MainMenu.
    if event == 'confirmset':
#       if the button to confirm the users desired set name is pressed...
        setname = values['newsetname']
#       ...the value they entered in the entry field is saved as setname.
        inserted = False
#       this is the inserted variable used later on to tell the program whether the set name has been written to the file,
#       and thus showing whether the user has reached their 5 set limit or not.
        if setname == '':
            window.FindElement('newset_error').update('Please enter a set name.')
#           if the user did not enter a name before pressing confirm, the error message is updated to alert the user of this.
        else:
            csv_file = open(f"{username}.csv", mode="r")
            rows = list(csv.reader(csv_file))
#           the rows are extracted from the users file in a 2D array
            names = rows[0]
#           the first row is saved as the names variable
            csv_file.close()
            csv_file = open(f"{username}.csv", mode="w", newline='')
#           everything previously in the file is overwritten
            for i in range (0,5):
#           the program iterates through each of the 5 name slots (i.e. the 5 items) in the array.
                if names[i] == '' and inserted == False:
                    names[i] = setname
#                   the names array now includes the desired set name
                    rows[0] = names
#                   this array is then updated in the 2D array
                    csv_file = (csv.writer(csv_file)).writerows(rows)
#                   and the 2D array is fully written back to the file
                    inserted = True
#                   once the name has been inserted, it does not need to be inserted again. the inserted variable is used to ensure this.
                    set = i + 1
#                   declares the set number so that flashcards are successfully written to the users CSV file
#                   when they are taken to the add flashcard screen.
                else:
                    i += 1
            if inserted == False:
                window.FindElement('newset_error').update('You have reached your limit of 5 sets.')
                csv_file = (csv.writer(csv_file)).writerows(rows)
#           if the name could not be inserted it indicates all slots were full and so the user has reached their 5 set limit.
#           this is displayed on the error message and then the original contents of the file are written back into it.
            else:
                window[f'-COL5-'].update(visible=False)
                window[f'-COL10-'].update(visible=True)
                window.FindElement('newset_error').update('')
                window.FindElement('newsetname').update('')
#           if a set is successfully created, the entry field/error message is cleared and the layout is updated to the main menu.

    if event == 'SET1':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL9-'].update(visible=True)
        set = 1
    if event == 'SET2':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL9-'].update(visible=True)
        set = 2
    if event == 'SET3':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL9-'].update(visible=True)
        set = 3
    if event == 'SET4':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL9-'].update(visible=True)
        set = 4
    if event == 'SET5':
        window[f'-COL6-'].update(visible=False)
        window[f'-COL9-'].update(visible=True)
        set = 5
#   All of these take the user to the same layout byt update the set variable to the respective set being chosen.
    if event == 'BACK5':
        window[f'-COL6-'].update(visible=True)
        window[f'-COL9-'].update(visible=False)
#   Takes the user from the Set layout to the MySets layout.
    if event == 'BACK6':
        window[f'-COL9-'].update(visible=True)
        window[f'-COL10-'].update(visible=False)
        window.FindElement('term_entry').update('')
        window.FindElement('definition_entry').update('')
        window.FindElement('addflashcard_error').update('')
#   Takes the user from the AddFlashcard layout to the Set layout, and clears the input fields and error message.
    if event == 'BACK7':
        window[f'-COL9-'].update(visible=True)
        window[f'-COL11-'].update(visible=False)
        window.FindElement('revise_error').update('')
#   Takes the user from the revise screen to the set menu and clears the error message.
    if event == 'ADDFLASHCARDS':
        window[f'-COL10-'].update(visible=True)
        window[f'-COL9-'].update(visible=False)
#   If the user wishes to add flashcards to a set and they press the button to do so, the layout will be updated to the relevant layout.
    if event == 'ADD':
        term = values['term_entry']
        definition = ((values['definition_entry']).strip('\n'))
        # saves both of the values entered by the user as variables
        if term != '' and definition !='':
            file = open(f'{username}.csv', mode = 'a', newline='')
            # opens the users CSV file to write to append to.
            file = (csv.writer(file)).writerow([set, term, definition])
            # writes the flashcard data to the file
            window.FindElement('term_entry').update('')
            window.FindElement('definition_entry').update('')
            # clears the input fields
            window.FindElement('addflashcard_error').update('')
            # clears the error message
        else:
            window.FindElement('addflashcard_error').update('Please fill in both fields.')
            # displays an error message
    if event == 'REVISE':
        file = csv.reader(open(f'{username}.csv', mode='r', newline=''))
        # opens the CSV file and creates a CSV reader.
        rows = list(file)
        # extracts the contents of the file into a 2D array.
        terms = []
        definitions = []
        # these 2 lists will store all of the terms/definitions for a particular set so they can be iterated through.
        for i in range (1, len(rows)):
            # iterates through the file (ignoring the first row as this does not contain flashcards)
            if int(rows[i][0]) == set:
                terms.append(rows[i][1])
                definitions.append(rows[i][2])
                # appends all terms/definitions associated with the relevant set name to the correct list.
        if len(terms) == 0 or len(definitions) == 0:
            # if there are no flashcards in the set...
            window[f'-COL12-'].update(visible=True)
            window[f'-COL9-'].update(visible=False)
            # takes the user to the display telling them that this set has no flashcards.
        else:
            window[f'-COL11-'].update(visible=True)
            window[f'-COL9-'].update(visible=False)
            # updates the layout to the revise flashcard layout
            flashcard_status = 'term'
            # this variable is to determine whether the flashcard is currently displaying its term or definition.
            current_flashcard_index = 0
            # this variable will be used for when the user wants to go to the next/previous flashcard
            # - to store the index position of the term/definition of flashcard currently being viewed.
            window.FindElement('flashcard_text').update(terms[0])
            # displays the first term on the screen so that the user can begin revising.
    if event == 'NEXT':
        if current_flashcard_index == (len(terms)-1):
            window.FindElement('revise_error').update('You have reached the end of the set.')
        # if the user reaches the end of the set (i.e. the end of the list), they are notified that there are no further flashcards.
        else:
            current_flashcard_index += 1
            # increments the variable to point to the index position of the next flashcard.
            window.FindElement('flashcard_text').update(terms[current_flashcard_index])
            # displays the next term on screen
            window.FindElement('revise_error').update('')
            # clears the error message (so it does not stay there forever)
            flashcard_status = 'term'
            # ensures the next flashcard shows its term first
    if event == 'PREVIOUS':
        if current_flashcard_index == 0:
            window.FindElement('revise_error').update('You have reached the start of the set.')
        # if the user reaches the start of the set (i.e. the end of the list), they are notified that there are no previous flashcards.
        else:
            current_flashcard_index -= 1
            # decrements the variable to point to the index position of the previous flashcard.
            window.FindElement('flashcard_text').update(terms[current_flashcard_index])
            # displays the previous term on screen
            window.FindElement('revise_error').update('')
            # clears the error message (so it does not stay there forever)
            flashcard_status = 'term'
            # ensures the previous flashcard shows its term first
    if event == 'FLIP':
        if str(flashcard_status) == 'term':
            window.FindElement('flashcard_text').update(definitions[current_flashcard_index])
            flashcard_status = 'definition'
        # if it is the term currently being displayed, it is changed to show the definition.
        elif str(flashcard_status) == 'definition':
            window.FindElement('flashcard_text').update(terms[current_flashcard_index])
            flashcard_status = 'term'
        # if it is the definition currently being displayed, it is changed to show the term.
        window.FindElement('revise_error').update('')
        # clears the error message (so it does not stay there forever)
    if event == 'DELETE':
        file = csv.reader(open(f'{username}.csv', mode='r', newline=''))
        # opens the CSV file and creates a CSV reader.
        rows = list(file)
        # extracts the contents of the file into a 2D array.
        for i in range(1,(len(rows))):
        # iterates through the 2D array...
            try:
                if rows[i][0] == str(set) and rows[i][1] == terms[current_flashcard_index] and rows[i][2] == definitions[current_flashcard_index]:
                # if the flashcard currently being viewed is the same as the flashcard in a particular index position in the 2D array...
                    del rows[i]
                    # ... it is deleted from the 2D array.
                    print(rows)
            except:
                i += 1
                # avoids an error due to the value of i being out of range when an item is removed from rows (and so its length decreases).
        file = csv.writer(open(f'{username}.csv', mode='w+', newline=''))
        file = file.writerows(rows)
        # rewrites the new 2D array to the CSV file, overwriting what was there previously.
        if len(terms) == 1 or len(definitions) == 1:
        # if there is only one term left in the set which is about to be deleted...
            terms.remove(terms[current_flashcard_index])
            definitions.remove(definitions[current_flashcard_index])
            # removes the term and definition being deleted from the terms and definition lists.
            # this is so that they no longer appear when pressing next/previous.
            window[f'-COL12-'].update(visible=True)
            window[f'-COL11-'].update(visible=False)
            # takes the user from the revise flashcards display to the no flashcards display to indicate there are no flashcards left in the set.
        else:
            if terms[len(terms)-1] == terms[current_flashcard_index]:
            # if it is the last term in the list being deleted...
                terms.remove(terms[current_flashcard_index])
                definitions.remove(definitions[current_flashcard_index])
                # removes the term and definition being deleted from the terms and definition lists.
                # this is so that they no longer appear when pressing next/previous.
                current_flashcard_index -= 1
                # decrements the current flashcard index by 1 (due to the end item being removed)
                window.FindElement('flashcard_text').update(terms[current_flashcard_index])
                # updates the flashcard text to show the new flashcard in that index position.
                window.FindElement('revise_error').update('')
                # clears the error message (so it does not stay there forever)
            else:
            # otherwise...
                terms.remove(terms[current_flashcard_index])
                definitions.remove(definitions[current_flashcard_index])
                # removes the term and definition being deleted from the terms and definition lists.
                # this is so that they no longer appear when pressing next/previous.
                window.FindElement('flashcard_text').update(terms[current_flashcard_index])
                # updates the flashcard text to show the new flashcard in that index position.
                window.FindElement('revise_error').update('')
                # clears the error message (so it does not stay there forever)
    if event == 'BACK8':
        window[f'-COL9-'].update(visible=True)
        window[f'-COL12-'].update(visible=False)
        # takes the user from the no flashcards display to the set menu.
