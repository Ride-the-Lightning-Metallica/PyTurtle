'''Creates a window with an editing area for entering commands in a conditional language.
After clicking the "Run" button checks for errors, if there are none launches a new window
with drawing "turtle graphics". If errors are present, it displays a message indicating
the line, in which the error occurred.'''
import turtle
import tkinter
from turtle_gui import TurtleEditor
from functools import partial

help_text = '''
Control the turtle by entering commands from the commands file on
each separate line and end the line with a semicolon:
'''

commands = {
	'FORWARD': 'turtle.forward($ARGUMENTS$)',
	'BACKWARD': 'turtle.backward($ARGUMENTS$)',
	'LEFT': 'turtle.left($ARGUMENTS$)',
	'RIGHT': 'turtle.right($ARGUMENTS$)',
	'CIRCLE': 'turtle.circle($ARGUMENTS$)',
	'DEGREE_CIRCLE': 'turtle.circle($ARGUMENTS$)',
	'GOTO': 'turtle.goto($ARGUMENTS$)',
	'DOWN': 'turtle.down($ARGUMENTS$)',
	'UP': 'turtle.up($ARGUMENTS$)',
	'WIDTH': 'turtle.width($ARGUMENTS$)',
	'СOLOR': 'turtle.сolor($ARGUMENTS$)',
	'BEGIN_FILL': 'turtle.begin_fill($ARGUMENTS$)',
	'END_FILL': 'turtle.end_fill($ARGUMENTS$)',
	'RESET': 'turtle.reset($ARGUMENTS$)',
	'CLEAR': 'turtle.clear($ARGUMENTS$)',
}

class PyTurtle(TurtleEditor):
	def run(self):
		code = self.textarea.get('1.0', 'end').splitlines()
		if self.validate_code(code):
			self.run_code(code)

	def validate_code(self, code):
		for number_of_line, line in enumerate(code, start=1):
			open_parenthesis = line.find('(')
			closing_parenthesis = line.find(')')

			if line.strip() == '':
				continue

			if not line.endswith(';'):
				print(f'There is no ";" at the end of the line. Line: {number_of_line}')
				return False

			if ';' in line[:-1]:
				print('The symbol ";" must occur once and be at the end of the line.', 
					  f'Line: {number_of_line}')
				return False

			if open_parenthesis == -1 or closing_parenthesis == -1:
				print(f'The line is missing parentheses. Line: {number_of_line}')
				return False
			
			if line[:open_parenthesis].upper() not in commands:
				print(f'The line contains an unknown command. Line: {number_of_line}')
				return False
		return True

	def run_code(self, code):
		turtle.TurtleScreen._RUNNING = True
		for line in code:
			if line.strip() == '':
				continue

			open_parenthesis = line.find('(')
			closing_parenthesis = line.find(')')

			command = commands[line[:open_parenthesis].upper()]
			command_arguments = line[open_parenthesis+1:closing_parenthesis]
			
			exec(command.replace('$ARGUMENTS$', command_arguments))
		

if __name__ == '__main__':
	root = PyTurtle('500x500', 'PyTurtle', resizable_width=False, resizable_height=False,
					help_text=help_text)
	root.mainloop()
