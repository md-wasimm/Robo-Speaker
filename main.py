import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 Created by Wasim")
    while True:
        x = input("Enter what do you want me to speak: ")
        if x == "q":
            print("Robo Speaker Exit. Thank You.")
            break
        command = f"{x}"
        speaker.speak(command)
