"""
Finnish Declension Tables Tester
--------------------------------
This is a simple GUI-based python program that helps with
learning Finnish nominal declension tables.
Updated for Python 3.
"""

# Max line length w/ --- w/o flowing text blocks (PEP 8 style guide): 72 --- 79

import tkinter as tk
from tkinter import font as tkFont
import random
import io
import json

# Make root widget
root = tk.Tk()
root.title("Finnish Declension Tables Tester")
root.config(bg="steel blue")

# Globals and contants
# Template that shows the data structure for one declension table
TEMPLATE = (
	"nominative_sg", "genitive_sg", ("accusative_sg_1", "accusative_sg_2"),
	"partitive_sg", "illative_sg", "inessive_sg",
	"allative_sg", "adessive_sg", "elative_sg",
	"ablative_sg", "essive_sg", "abessive_sg",
	"translative_sg", "instructive_sg", "comitative_sg",
	"nominative_pl", "genitive_pl", "accusative_pl",
	"partitive_pl", "illative_pl", "inessive_pl",
	"allative_pl", "adessive_pl", "elative_pl",
	"ablative_pl", "essive_pl", "abessive_pl",
	"translative_pl", "instructive_pl", "comitative_pl", "english"
	)
GAME_LENGTH = 10
# Define layout measures based on screen size
screen_height = root.winfo_screenheight()
title_text_size = int(screen_height / 1080 * 32)
label_text_size = int(screen_height / 1080 * 14)
table_padding = int(screen_height / 1080 * 40)
toolbar_padding = int(screen_height / 1080 * 20)
int_padding = int(screen_height / 1080 * 5)
button_font = tkFont.Font(
	family='Helvetica', size=(int(screen_height / 1080 * 20)), weight='bold'
	)
title_str = ""
word_str = ""
# Keep track of the current word's number in a game:
word_counter = GAME_LENGTH
max_words = 0
words = []
points = 0
max_points = 0
start_flag = True    # Boolean flag to mark the start of the game

# Load declension data from tables.txt json document
declension_tables = []
with io.open('tables.txt', mode='r', encoding="utf-8") as tables_file:
	declension_tables = json.load(tables_file)

# Make frames and labels
frm_master = tk.Frame(root, bg="steel blue")
frm_master.grid()
lbl_title = tk.Label(
	frm_master, font=("Helvetica", title_text_size), bg="steel blue"
	)
lbl_title.config(text=title_str)
lbl_title.grid(row=0, column=0, columnspan=2, pady=title_text_size)

frm_table = tk.Frame(
	frm_master, pady=table_padding, bg="light steel blue",
	bd=3, relief=tk.RIDGE
	)
frm_table.grid(row=1, rowspan=2, column=0)

lbl_table_null = tk.Label(
	frm_table, text="", font=("Helvetica", label_text_size),
	bg="light steel blue"
	)
lbl_table_null.grid(row=0, column=0, pady=toolbar_padding)
lbl_table_sg = tk.Label(
	frm_table, text="singular", font=("Helvetica", label_text_size, 'bold'),
	bg="light steel blue"
	)
lbl_table_sg.grid(row=0, column=1, pady=toolbar_padding)
lbl_table_pl = tk.Label(
	frm_table, text="plural", font=("Helvetica", label_text_size, 'bold'),
	bg="light steel blue"
	)
lbl_table_pl.grid(row=0, column=2, pady=toolbar_padding)

labels = [
"nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative"
]

# Create Label widgets from labels, assign them grid positions
label_mapping = []
row_counter = 1
for label in labels:
	label_mapping.append(tk.Label(frm_table))
	label_mapping[row_counter-1].config(
		text=label, font=("Helvetica", label_text_size),
		bg="light steel blue"
		)
	label_mapping[row_counter-1].grid(
		row=row_counter, column=0, sticky=tk.W,
		pady=int_padding, padx=table_padding
		)
	row_counter += 1

# Create Entry widgets, two for each label
entry_mapping = []
for column_idx in range(2):
	row_counter = 1
	for label in labels:
		entry = tk.Entry(frm_table)
		entry.config(
			font=("Helvetica", label_text_size),
			insertbackground="black", insertontime=500, insertofftime=500,
			readonlybackground="light steel blue"
			)
		entry.grid(
			row=row_counter, column=column_idx+1,
			pady=int_padding, padx=table_padding
			)
		entry_mapping.append(entry)
		row_counter += 1

lbl_info = tk.Label(frm_master)
lbl_info.config(
	text="<info text>", font=("Helvetica", label_text_size),
	bg="steel blue", width=table_padding+10
	)
lbl_info.grid(row=1, column=1)

btn_skip = tk.Button(frm_master, text="Skip", font=button_font, width=10)
btn_skip.grid(row=2, column=1)


def change_info_text(game_state):
	"""Change the info text in the info label (lbl_info)
	based on the state of the game.
	'game_state' can be "START", "ONGOING", "WORD_DONE" or "END".
	"""

	counter = max_words - word_counter
	if game_state == "START":
		info_text = "New session.\n"
		info_text += "You earn 1 point for each correct answer\n"
		info_text += "and 5 points for finishing the whole table.\n\n"
	elif game_state == "WORD_DONE":
		info_text = "Good job!\n"
		info_text += "You received 5 points for completing the table.\n"
		info_text += "Press 'Next' to continue.\n\n"
		counter += 1
	elif game_state == "END":
		info_text = "Session over.\n"
		info_text += "Your score is " + str(points)
		info_text += " out of " + str(max_points) + ".\n\n"
	else:
		info_text = ""
	
	info_text += str(counter) + "/" + str(max_words) + " declensions done.\n"
	if game_state != "END":
		info_text += " Points: " + str(points)

	lbl_info.config(text=info_text)


def change_color_scheme(dark, light):
	"""
	Changes the window's color scheme.

	"dark" is used as background color for the master frame,
	"light" is background color for the table.
	"""

	root.config(bg=dark)
	frm_master.config(bg=dark)
	lbl_title.config(bg=dark)
	frm_table.config(bg=light)
	lbl_table_null.config(bg=light)
	lbl_table_sg.config(bg=light)
	lbl_table_pl.config(bg=light)
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(readonlybackground=light)
	for idx in range(len(label_mapping)):
		label_mapping[idx].config(bg=light)
	lbl_info.config(bg=dark)


def print_info(event):
	"""Print some info to the console in mainloop."""
	pass


def resize_frames():
	"""Function that resizes widgets based on width of the labels
	and the dimensions of the screen.
	"""
	
	pixels_height = tkFont.Font(family='Helvetica').metrics('linespace')
	table_height = frm_table.grid_bbox()[3]
	new_height = int(table_height*0.6/pixels_height)
	lbl_info.config(height=new_height)


def end_game():
	"""Runs when the game is out of words."""

	global info_text, word_counter
	word_counter -= 1
	change_info_text("END")
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(state="readonly")
	btn_skip.config(text="New Game", width=15)
	btn_skip.bind("<Button-1>", init_game)

	change_color_scheme("forest green", "lime green")


def get_next_word(event):
	"""
	Event handler for a skip button. It jumps to the next declension table.
	It's also used upon initialization.
	"""

	global words, answers, answered, word_str, title_str
	global info_text, word_counter, start_flag
	
	# Commence the end of the game if there are no words left
	# when user presses skip
	if word_counter == 1:
		end_game()
		return

	# Initialize next declension table
	answers = words.pop()
	answered = [False for dummy_idx in range(len(answers)-1)]
	answered[0] = True
	word_str = answers[0]
	title_str = answers[0] + "   –   " + answers[30]
	lbl_title.config(text=title_str)
	
	# Set all entry boxes to be empty
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(
			state=tk.NORMAL, fg="black", justify=tk.LEFT, takefocus=1
			)
		entry_mapping[idx].delete(0, tk.END)

	# Set nominative singular to be solved
	entry_mapping[0].insert(0, word_str)
	entry_mapping[0].config(
		state="readonly", fg="green4", takefocus=0
	)

	# Set all entry fields that have no valid answers to be blank
	for idx in range(len(answers)):
		if answers[idx] == '':
			entry_mapping[idx].insert(0, "–")
			entry_mapping[idx].config(
				state="readonly", justify=tk.CENTER, takefocus=0
				)
			answered[idx] = True

	# Transform the Next button back into a Skip button after word-completion
	btn_skip.config(text="Skip", width=10)
	# Set initial focus to be in genitive singular entry box
	entry_mapping[1].focus_set()
	
	if start_flag:
		change_info_text("START")
	else:
		word_counter -= 1
		change_info_text("ONGOING")
	
	start_flag = False
	change_color_scheme("steel blue", "light steel blue")
	resize_frames()


def init_game(event):
	"""Function to help initialize a game."""

	global word_counter, max_words, words
	global points, max_points, start_flag
	
	# Set the max_words global to the maximally possible length of the game
	max_words = len(declension_tables)
	
	# Pick words for the game
	if max_words < GAME_LENGTH:
		words = random.sample(declension_tables, max_words)
		# Set the word_counter global to the maximally possible game length
		# The max_words global now functions as the length of the game
		word_counter = max_words
	else:
		words = random.sample(declension_tables, GAME_LENGTH)
		# Set the word_counter global to the predetermined game length
		word_counter = GAME_LENGTH
		# The max_words global now functions as the length of the game
		max_words = word_counter

	points = 0

	# Calculate the maximum score achievable
	blanks = 0
	for word in words:
		blanks += word.count('')
	max_points = max_words * 34 - blanks
	
	# Set a flag so the program knows the game has just started
	start_flag = True

	change_color_scheme("steel blue", "light steel blue")
	btn_skip.config(text="Skip", width=10)
	btn_skip.bind("<Button-1>", get_next_word)
	get_next_word("<Button-1>")


def return_press_handler(event):
	"""Event handler for an 'Enter key' press."""

	global points, answered

	current_widget = root.focus_get()
	# If focus isn't an Entry widget, do nothing
	if not isinstance(current_widget, tk.Entry):
		return

	input_text = current_widget.get()
	# If the Entry box is empty, do nothing
	if len(input_text) == 0:
		return
	# Entry_mapping's Entry widgets and the corresponding answers
	# have the same indices
	answer_idx = entry_mapping.index(current_widget)

	# Handle the fact that there can be multiple correct forms for each answer
	current_answers = []
	if isinstance(answers[answer_idx], list):
		current_answers.extend(answers[answer_idx])
	else:
		current_answers.append(answers[answer_idx])

	if input_text in current_answers:
		# If the answer given was correct
		entry_mapping[answer_idx].config(
			state="readonly", fg="green4", takefocus=0
			)
		answered[answer_idx] = True
			
		points += 1
		
		change_info_text("ONGOING")

		if False not in answered:
			if word_counter == 1:
				# Commence the end of the game if there's no words left
				end_game()
				return
			else:
				# Idle on completion screen if the table is complete
				points += 5
				change_info_text("WORD_DONE")
				change_color_scheme("LightGoldenrod3", "LightGoldenrod2")
				btn_skip.config(text="Next", width=10)
				btn_skip.bind(get_next_word)
				btn_skip.focus_set()
				return

		# To find the next focus:
		focus_found = False
		counter = 1
		while not focus_found:
			if not answered[(answer_idx + counter) % 30]:
				entry_mapping[(answer_idx + counter) % 30].focus_set()
				focus_found = True
			else:
				counter += 1
			
	else:
		# If the answer given was incorrect
		entry_mapping[answer_idx].config(fg="red3")



root.bind("<Return>", return_press_handler)
# root.bind("<Key-m>", print_info)
btn_skip.bind("<Button-1>", get_next_word)
root.wait_visibility()
init_game("<Button-1")
root.mainloop()