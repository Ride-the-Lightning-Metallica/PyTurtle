import tkinter

class TurtleEditor(tkinter.Tk):
	def __init__(self, size, title, resizable_width, resizable_height, help_text):
		super().__init__()
		self.geometry(size)
		self.title(title)
		self.resizable(width=resizable_width, height=resizable_height)
		self.help_text = help_text
		self.make_widgets()

	def make_widgets(self):
		self.label = tkinter.Label(self, text=self.help_text, font='Arial 11')
		self.frame = tkinter.Frame(self, height=15)
		self.scrollbar = tkinter.Scrollbar(self.frame)
		self.textarea = tkinter.Text(self.frame, width=46, height=20, font='Arial 12')
		self.numbers = tkinter.Text(self.frame, width=4, height=20, bg='lightgray',
									font='Arial 12')
		self.number_the_line()
		self.button = tkinter.Button(self, text='Run', font='Arial 12', width=5, command=self.run)

		self.textarea.focus()
		self.textarea.bind('<<Modified>>', self.on_edit)
		self.scrollbar.config(command=self.textarea.yview)
		self.textarea.config(yscrollcommand=self.on_yscrollcommand)
		self.numbers.insert('1.0', '1.\n')
		self.numbers.config(state='disabled')

		self.label.pack(fill=tkinter.X)
		self.frame.pack()
		self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
		self.numbers.pack(side=tkinter.LEFT)
		self.textarea.pack()
		self.button.pack(side=tkinter.RIGHT, pady=10, padx=12)

	def on_yscrollcommand(self, *args):
		self.scrollbar.set(*args)
		self.numbers.yview_moveto(args[0])

	def number_the_line(self):
		count_of_lines = self.textarea.get('1.0', 'end').count('\n') + 1

		self.numbers.config(state='normal')
		self.numbers.delete('1.0', 'end')
		self.numbers.insert('1.0', '\n'.join(map(str, range(1, count_of_lines))))
		self.numbers.config(state='disabled')

	def on_edit(self, event):
		self.number_the_line()
		self.textarea.edit_modified(0)

	def run(self):
		print('Override this method in a subclass')


