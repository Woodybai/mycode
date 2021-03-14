from pynput import keyboard

def p1(key):
    if key.char=="a":
      import winsound
      winsound.Beep(2222,555)
a=keyboard.Listener(on_press=p1)
a.start()
a.join()
