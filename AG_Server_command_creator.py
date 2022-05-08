#Program for mass creation of configuration files that require a device password to change settings. For server software AutoGraph.
#Designed to work from the parent directory.
from pathlib import Path
import os

count = 0

work_path = input('Введите полный адрес до рабочего каталога.\nВ рабочем каталоге должна быть папка с паролями от приборов. Пример /Users/USERNAME/Documents/:\n') #Рабочий каталог
pass_dir = input('Введите имя директории с файлами содержащими пароли:\n')
pass_path = work_path + pass_dir #Directory with password files
file_suffix = input('Введите суфикс конечного файла, если такой необходимости нет, оставьте ввод пустым:\n')

command_file = (input('Введите адрес расположения файла с необходимыми командами, заполненный согласно руководству по созданию команд для приборов. Пример /Users/USERNAME/Documents/commands.txt:\n'))
command_file_read = open(command_file, 'r')
command_file = command_file_read.read()
command_file_read.close()

#Create a list of files with passwords

filelist = []

for root, dirs, files in os.walk(pass_path):
	for file in files:
		filelist.append(os.path.join(root,file))

#Determining the target file containing the password from the device

for i in filelist:
    if 'pass.txt' in i:
        path = Path(i)
        pass_file = open(i, "r", encoding="utf-8")
        password = pass_file.read()

        #Assignment to a variable based on the filename with the password.

        c_number = str(path.stem)
        number_fix = c_number.replace('pass', '')
        c_number = number_fix
        number = c_number + str(file_suffix)

        #Create catalog by device number

        os.makedirs(work_path + 'atc/' + '{}'.format(c_number), exist_ok=True)

        #Formation of the contents of the configuration file and its output to the file system

        with open(work_path + 'atc/' + c_number + '/' + number + ".atc", "w") as atc_file:
            add_text = 'ENTERSPASSWORD=' + password + ';\n' + command_file
            print(add_text, file=atc_file)
            atc_file.close()
        count += 1

print('Всего создано', count, 'файлов.\nBy Rud Oleg')