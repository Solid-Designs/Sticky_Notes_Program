import sys
import glob
import os
from send2trash import send2trash


class Note:
    # Main Menu --------------------------------------------------------------------------------------------------------
    def main_loop(self):
        self.menu_choice = str(input(''' 
    Welcome to the Post-it notes program
          Press "C" to create note
          Press "E" to edit note
          Press "D" to delete note
          Press "Q" to quit program 
          Please input corresponding key: ''').upper())

        # Main Loop with Error Checking for OSError: Invalid name for text file
        while True:
            if self.menu_choice == "C":
                try:
                    self.change_directory()
                    self.title_note()
                    self.create_note()
                    self.edit_note()
                    self.continue_loop()
                    break
                except OSError:
                    print('Invalid Note Name. Returning to Main Menu...')
                    self.main_loop()

            elif self.menu_choice == "E":
                try:
                    self.change_directory()
                    self.list_files()
                    self.title_note()
                    self.check_exist()
                    self.edit_note()
                    self.continue_loop()
                    break
                except OSError:
                    print('Invalid Note Name. Returning to Main Menu...')
                    self.main_loop()

            elif self.menu_choice == "D":
                self.change_directory()
                self.list_files()
                self.title_note()
                self.check_exist()
                self.delete_note()
                self.continue_loop()
            elif self.menu_choice == "Q":
                sys.exit()

            else:
                print('Invalid input.')
                self.main_loop()

    # Change Directory -------------------------------------------------------------------------------------------------
    def change_directory(self):
        self.input_location = str(input('What folder would you like to use: ')).lower()

        while True:
            if os.path.isdir(self.input_location) == True:
                os.chdir(self.input_location)
                break
            else:
                print("Location not valid. Try formatting like this: r'C:\(Users)\(Name)\(Desired-Folder)'")
                self.change_directory()

    # Continue Menu ----------------------------------------------------------------------------------------------------
    def continue_loop(self):
        self.continue_choice = str(input(''' 
Would you like to try again?
      Press "Y" to continue
      Press "N" to exit
      Please input corresponding key: ''').upper())

        # If you choose yes, call the main function | If no, break out
        while True:
            if self.continue_choice == "Y":
                self.main_loop()
                self.file_name = None

            elif self.continue_choice == "N":
                sys.exit()

            else:
                print('Invalid input. Please try again.')
                self.continue_loop()

    # Create Note and immediately edit ---------------------------------------------------------------------------------
    def create_note(self):
        # try:
        self.created_note = open(self.file_name, 'w')
        self.created_note.close()
        # except OSError:
        #     print('Nope')

    # Does The Note Exist ----------------------------------------------------------------------------------------------
    def check_exist(self):
        self.existing_files = glob.glob(self.input_location + r'\*.txt')

        if self.file_name not in self.existing_files:
            print("The file you requested does not exist. Do not include file extension.")
            self.title_note()

    # Edit Note --------------------------------------------------------------------------------------------------------
    def edit_note(self):
        # Grab information from file and print
        self.my_note = open(self.file_name, 'r')
        self.note_content = self.my_note.read()
        self.my_note.close()
        print(self.note_content)

        # Append the data
        self.my_note = open(self.file_name, 'a')
        self.my_note.write('\n' + str(input('Add Description: ')))
        self.my_note.close()

    # Delete Note ------------------------------------------------------------------------------------------------------
    def delete_note(self):
        send2trash(self.file_name)

    # List Available Files ---------------------------------------------------------------------------------------------
    def list_files(self):
        self.existing_files = glob.glob(self.input_location + r'\*.txt')
        self.files = []
        print('These are the sticky notes in this folder: ')
        for self.files in self.existing_files:
            print(self.files, end='')
            print('\n')
        if len(self.files) == 0:
            print('There are no sticky notes in this folder. Returning to Main Menu...')
            self.main_loop()

    # Create Title or Look for pre-existing note -----------------------------------------------------------------------
    def title_note(self):
        if self.menu_choice == 'C':
            self.file_name = self.input_location + r'\{}.txt'.format(str(input('Add Title: ')))
        elif self.menu_choice == 'E' or self.menu_choice == 'D':
            self.file_name = self.input_location + r'\{}.txt'.format(
                str(input('Which note would you like to edit/delete: ')))


my_note = Note()
my_note.main_loop()
