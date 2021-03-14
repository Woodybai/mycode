import pynput.keyboard as pk

def a(Key):
	if Key.char=="a":
		import winsound
		winsound.Beep(555,555)
	if Key.char=="b":
		import winsound
		winsound.Beep(655,555)
	if Key.char=="c":
		import winsound
		winsound.Beep(755,555)
	if Key.char=="d":
                import winsound
                winsound.Beep(855,555)
        if Key.char=="e":
            
                import winsound
                winsound.Beep(955,555)
        if Key.char=="f":
                import winsound
                winsound.Beep(1055,555)


lis=pk.Listener(on_press=a)
lis.start()
lis.join()
