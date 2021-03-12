import time
import requests as req

# 
url = "http://your-url-here/"

def listen():
    page = req.get(url)
    content = page.text
    if "!pC2" in content:  
        content = content.split("!pC2")
        return content[1]
    return content[0]
    

def main():
    while True:
        command = listen()
        time.sleep(1)   
        if command == "OFFLINE":
            break  
        if "ECHO" in command:
            print(command.replace("ECHO",""))

if __name__ == "__main__":
    main()