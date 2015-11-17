import time
import sys

filename = 'Word Storage.txt'

# start menu text
print_this1 = 'Hello, my name is Felcitiy. A pseudo-AI, here to help you.'
print_this2 = '\nThis is a lexicon program...'
print_this3 = '\nWould you like to: '
print_this4 = '\n\n\t[1] Add Word'
print_this5 = '\n\t[2] Search Word'
print_this6 = '\n\t[3] Edit Word'
print_this7 = '\n\t[4] Leave a Comment'
print_this8 = '\n\t[5] Quit\n\n'

def text_effect(string):
	for i in string:
		print i,
		sys.stdout.softspace=0
		time.sleep(0.01)
	time.sleep(0.1)

def add_word():
	text_effect('\nWord: ')
	add_word1 = raw_input()
	text_effect('Meaning: ')
	add_meaning = raw_input()
	add_word1st = add_word1.capitalize()
	add_meaning1st = add_meaning.capitalize()
	text_effect("\n\t[%s]:\n\t\t%s\n" % (add_word1st, add_meaning1st))
	text_effect('\nConfirm?')
	user_confirm = raw_input('\n>>> ')
	if 'N' in user_confirm or 'n' in user_confirm:
		menu_return()
	else:
		add_word2st = add_word1st[0] + ":"
		with open(filename, 'r') as txtr:
			buf = txtr.readlines()
		with open(filename, 'w') as txtw:
			for line in buf:
				if add_word2st in line:
					line = line + "\n\t[%s]:\n\t\t%s\n" % (add_word1st, add_meaning1st)
				txtw.write(line)
		text_effect('\n%s has been added to the lexicon.' % (add_word1st))
	text_effect('\n\nWould you like to keep adding words?')
	user_answer = raw_input('\n\n>>> ')
	if 'N' in user_answer or 'n' in user_answer:
		menu_return()
	else:
		add_word()
	
	

def add_word2(this_word):
	this_word1st = this_word.capitalize()
	text_effect("Word: %s" % this_word1st)
	text_effect('\nMeaning: ')
	add_meaning = raw_input()
	text_effect("\n\t[%s]:\n\t\t%s\n" % (this_word1st, add_meaning))
	text_effect("\nConfirm?")
	user_confirm = raw_input('\n>>> ')
	if 'N' in user_confirm or 'n' in user_confirm:
		menu_return()
	else:
		add_word2st = this_word1st[0] + ":"
		with open(filename, 'r') as txtr:
			buf = txtr.readlines()
		with open(filename, 'w') as txtw:
			for line in buf:
				if add_word2st in line:
					line = line + "\n\t[%s]:\n\t\t%s\n" % (this_word1st, add_meaning)
				txtw.write(line)
	menu_return()


def search_word():
	text_effect('Enter the word you want to search: ')
	this_word = raw_input()
	print "\n"
	this_word1st = this_word.capitalize()
	this_word2 = '[' + this_word1st
	if this_word2 in open(filename).read():
		with open(filename, 'r') as txtr:
			for line in txtr:
				if this_word2 in line:
					text_effect(line)
					for line in txtr:
						if line != "\n":
							text_effect(line)
							print "\n"
						else:
							break
		raw_input()
		menu_return()
	else:
		text_effect("%s not found. Would you like to add" % (this_word1st))
		text_effect(" this word into the lexicon")
		user_answer = raw_input("\n>>> ")
		if 'Y' in user_answer or 'y' in user_answer:
			add_word2(this_word1st)
	

def comment_(comment):
	time.sleep(1)
	text_effect('\n\nAre you really sure you want to submit that?')
	time.sleep(.25)
	text_effect("\nThis can't be undone...")
	time.sleep(.5)
	text_effect("\nWell, technically you can... ")
	time.sleep(1)
	text_effect("You can edit them manually you know...")
	user_answer = raw_input('\n\n>>> ')
	if 'N' in user_answer or 'n' in user_answer:
		menu_return()
	else:
		with open(filename, 'r') as txtr:
			buf = txtr.readlines()
		with open(filename, 'w') as txtw:
			for line in buf:
				if 'Comments: ' in line:
					line = line + "\n\t%s\n" % (comment)
					print comment
				txtw.write(line)
		text_effect("\nComment submitted successfully.")
		time.sleep(1)
	menu_return()
		
		
def menu_return():
	text_effect("\nProcede to menu?")
	user_answer = raw_input("\n>>> ")
	if user_answer in ('Yes', 'y', 'ye', 'yeah', 'yes', 'K', 'k'):
		menu_()
	else:
		text_effect('\n\n\t\tThank you for using Lexicon 1.')
		time.sleep(.25)
		text_effect(' Come again.\n\n')
		time.sleep(2)
		quit()

			
def menu_start():
	text_effect(print_this1)
	text_effect(print_this2)
	text_effect(print_this3)
	text_effect(print_this4)
	text_effect(print_this5)
	text_effect(print_this6)
	text_effect(print_this7)
	text_effect(print_this8)
	print "\n"*5
	while True:
		user_answer = raw_input("\n>>> ")
		if user_answer in ('1', 'Add', 'add'):
			add_word()
			return False
		elif user_answer in ('2', 'Search', 'search'):
			search_word()
			return False
		elif user_answer in ('3', 'Edit', 'edit'):
			time.sleep(2)
			text_effect("This program doesn't have an edit feature...")
			time.sleep(1)
			text_effect("yet.")
		elif user_answer in ('4', 'Leave', 'leave', 'Comment', 'comment'):
			time.sleep(.5)
			text_effect("\nOne moment please...\n")
			time.sleep(1)
			text_effect("\nPlease enter your comment.")
			time.sleep(.1)
			text_effect(" Your opinions mean highly to us.")
			comment = raw_input("\n\n>>> ")
			comment_(comment)
			return False
		elif user_answer in ('5', 'Quit', 'quit'):
			text_effect('\n\n\t\tThank you for using Lexicon 1.')
			time.sleep(.25)
			text_effect(' Come again.\n\n')
			time.sleep(2)
			quit()
			return False
		else:
			text_effect("Answer not clear.")
			
def menu_():
	text_effect(print_this3)
	text_effect(print_this4)
	text_effect(print_this5)
	text_effect(print_this6)
	text_effect(print_this7)
	text_effect(print_this8)
	while True:
		user_answer = raw_input("\n>>> ")
		if user_answer in ('1', 'Add', 'add'):
			add_word()
			return False
		elif user_answer in ('2', 'Search', 'search'):
			search_word()
			return False
		elif user_answer in ('3', 'Edit', 'edit'):
			time.sleep(2)
			text_effect("This program doesn't have an edit feature...")
			time.sleep(1)
			text_effect("yet.")
		elif user_answer in ('4', 'Leave', 'leave', 'Comment', 'comment'):
			time.sleep(.5)
			text_effect("\nOne moment please...\n")
			time.sleep(1)
			text_effect("\nPlease enter your comment.")
			time.sleep(.1)
			text_effect(" Your opinions mean highly to us.")
			comment = raw_input("\n\n>>> ")
			comment_(comment)
			return False
		elif user_answer in ('5', 'Quit', 'quit'):
			text_effect('\n\n\t\tThank you, for using Lexicon 1.')
			time.sleep(.25)
			text_effect(' Come again.\n\n')
			time.sleep(2)
			quit()
			return False
		else:
			text_effect("Answer not clear.")
			

menu_start()			


raw_input()