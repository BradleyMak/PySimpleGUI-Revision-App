This is a partially completed revision app created with Python using the PySimpleGUI library. Most of the applications features should be self explanatory to use. 
There is a user login system, where new users can sign up with their chosen username, password and email. Only @gmail.com addresses are accepted when creating your account. There is a validation system to ensure this and also to make sure the user does not accidentally mistype their password. Passwords are hashed before they are stored for security reasons.
Once logged in, users can createw new revision sets, manage their sets, add new flashcards to those sets and then revise the content on those flashcards.
The features that were not fully implemented were the progress tracker and the account management.#

The following libraries were used:
- PySimpleGUI
- hashlib
- csv

The word document in this repository describes the full design methodology, as well as the development progress and a description of which parts were not fully implemented and why.
