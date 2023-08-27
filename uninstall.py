if __name__ == '__main__':
	import sys
	from pathlib import Path
	from winreg import HKEY_CLASSES_ROOT, DeleteKey
	from winotify import Notifier, Registry
	
	frozen: bool = hasattr(sys, 'frozen')
	
	location: Path = Path(sys.executable).parent if frozen else Path(__file__).parent
	
	registry: Registry = Registry('Pietrodev')
	
	notifier: Notifier = Notifier(registry)
	
	notifier.set_icon(location.joinpath("Icons/Master.ico"))
	
	try:
		DeleteKey(HKEY_CLASSES_ROOT, r'Directory\\Background\\shell\\Pietrodev\\shell\\Linker')
		
		notification = notifier.create_notification(
			title = 'Linker', msg = 'Linker has been uninstalled.'
		)
	except:
		notification = notifier.create_notification(
			title = 'Linker', msg = 'Linker has not been installed yet.'
		)
	
	notification.show()
