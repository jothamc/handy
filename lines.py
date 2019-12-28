import os

counter = 0
line_counter = 0

exclude_list = ["tests.py","__init__.py","apps.py","lines.py","manage.py"]
for folder,subfolder,files in os.walk(os.getcwd()):
	for file in files:
		if (file.endswith(".py") or file.endswith(".html")) and folder.endswith("migrations") is False and folder.endswith("handy") is False and file not in exclude_list:
			full_name = os.path.join(folder,file)
			this_file = open(full_name,"r")
			filelength = len(this_file.read())
			# for line in this_file:
				# line_counter = line_counter + 1
			counter = counter + filelength
			print(full_name)

print("You've typed "+ str(counter) +" letters of code")
# print("You've typed "+ str(line_counter) +" lines of code")