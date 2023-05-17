from tinytag import TinyTag
import os

def main():

	file = os.listdir('music')
	
	for i in file:

		tag = TinyTag.get('music/'+i)

		if tag.artist != None and tag.title != None:

			file_oldname = os.path.join("music", i)
			file_newname_newfile = os.path.join("music", tag.artist+"-"+tag.title+".mp3")
			os.rename(file_oldname, file_newname_newfile)

			print("Файл переименован: " + 'Исполнитель - "%s",' % tag.artist + ' Название - "%s"' % tag.title)
		else:
			print('Исполнитель-название нет в метаданных или одного из них')


if __name__ == '__main__':
	main()