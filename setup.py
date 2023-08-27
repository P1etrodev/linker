import sys
from pathlib import Path

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
	version = '2.1',
	name = "Linker",
	executables = [
		Executable(
			"install.py", base = base, target_name = 'Install', uac_admin = True, icon =
			Path.cwd().joinpath('Icons').joinpath(
				'Linker.ico'
			)
		),
		Executable(
			"uninstall.py", base = base, target_name = 'Uninstall', uac_admin = True, icon =
			Path.cwd().joinpath('Icons').joinpath(
				'Linker.ico'
			)
		),
		Executable(
			"linker.py", base = base, target_name = 'Linker', uac_admin = True, icon =
			Path.cwd().joinpath('Icons').joinpath(
				'Linker.ico'
			)
		)
	],
	options = {
		'build_exe': {
			'include_files': ['Icons'],
			'silent_level': 1
		},
	}
)
