from jokes import tell_jokes
def command (command):
  if "joke" in command:
    return tell_jokes()
  else:
    print("sorry command not found")
  
  
  
