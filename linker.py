from pathlib import Path
from sys import argv

from easygui import diropenbox, enterbox, fileopenbox

link_name = enterbox('Please name your link')

match argv[1]:
	case 'dir':
		parser = diropenbox
	case 'file':
		parser = fileopenbox

# noinspection PyUnboundLocalVariable
linked_fichier = parser('Choose your linked folder')

link = Path(argv[2]).joinpath(link_name)

link.symlink_to(target = linked_fichier, target_is_directory = argv[1] == 'dir')
