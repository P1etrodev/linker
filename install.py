if __name__ == '__main__':
	import sys
	from pathlib import Path
	from winreg import HKEYType, REG_SZ, CreateKey, SetValueEx, HKEY_CLASSES_ROOT
	from winotify import Notification
	
	frozen: bool = hasattr(sys, 'frozen')
	
	location: Path = Path(sys.executable).parent if frozen else Path(__file__).parent
	
	linker: str = 'linker.exe' if frozen else 'linker.py'
	
	icons_folder = location.joinpath('Icons')
	
	
	class Commands:
		DIR: str = f'"{str(location.joinpath(linker))}" dir "%V"' if frozen \
			else f'python "{str(location.joinpath(linker))}" dir "%V"'
		FILE: str = f'"{str(location.joinpath(linker))}" file "%V"' if frozen \
			else f'python "{str(location.joinpath(linker))}" file "%V"'
	
	
	class Icons:
		MASTER: str = str(icons_folder.joinpath("Master.ico"))
		DIR: str = str(icons_folder.joinpath("Dir.ico"))
		FILE: str = str(icons_folder.joinpath("File.ico"))
		LINKER: str = str(icons_folder.joinpath('Linker.ico'))
	
	
	master_key_path: Path = Path(r'Directory\\Background\\shell\\Pietrodev')
	master_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(master_key_path))
	SetValueEx(master_key, 'MUIVerb', 0, REG_SZ, 'Pietrodev')
	SetValueEx(master_key, 'subcommands', 0, REG_SZ, '')
	SetValueEx(master_key, 'SeparatorAfter', 0, REG_SZ, '')
	SetValueEx(master_key, 'SeparatorBefore', 0, REG_SZ, '')
	SetValueEx(master_key, 'Icon', 0, REG_SZ, Icons.MASTER)
	
	master_key_path_shell: Path = master_key_path.joinpath('shell')
	master_key_shell: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(master_key_path_shell))
	
	linker_key_path: Path = master_key_path_shell.joinpath('Linker')
	linker_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(linker_key_path))
	SetValueEx(linker_key, 'MUIVerb', 0, REG_SZ, 'Linker')
	SetValueEx(linker_key, 'subcommands', 0, REG_SZ, '')
	SetValueEx(linker_key, 'Icon', 0, REG_SZ, Icons.LINKER)
	
	linker_shell_key_path: Path = linker_key_path.joinpath('shell')
	linker_shell_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(linker_shell_key_path))
	
	dirlink_key_path: Path = linker_shell_key_path.joinpath('Dirlink')
	dirlink_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(dirlink_key_path))
	SetValueEx(dirlink_key, 'MUIVerb', 0, REG_SZ, 'Create link to directory...')
	SetValueEx(dirlink_key, 'Icon', 0, REG_SZ, Icons.DIR)
	
	dirlink_command_key_path: Path = dirlink_key_path.joinpath('command')
	dirlink_command_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(dirlink_command_key_path))
	SetValueEx(dirlink_command_key, '', 0, REG_SZ, Commands.DIR)
	
	filelink_key_path: Path = linker_shell_key_path.joinpath('Filelink')
	filelink_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(filelink_key_path))
	SetValueEx(filelink_key, 'MUIVerb', 0, REG_SZ, 'Create link to file...')
	SetValueEx(filelink_key, 'Icon', 0, REG_SZ, Icons.FILE)
	
	filelink_command_key_path: Path = filelink_key_path.joinpath('command')
	filelink_command_key: HKEYType = CreateKey(HKEY_CLASSES_ROOT, str(filelink_command_key_path))
	SetValueEx(filelink_command_key, '', 0, REG_SZ, Commands.FILE)
	
	Notification(
		app_id = 'Pietrodev', title = 'Linker',
		msg = 'Linker has been installed. Please do not move the containing folder, icons can stop working.',
		icon = Icons.LINKER
	).show()
