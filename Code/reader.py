import time
import requests as req

# The site you want to scrape should be added here. 
# If you run the test locally, you can add:
# http://localhost:5000

url = "http://your-url-here/"

def listen():
    page = req.get(url)
    content = page.text
    if "!pC2" in content:  
        content = content.split("!pC2")
        return content[1]
    # If the site does not contain "!pC2", this returns some value to keep the code running.
    return content[0]
    
def main():
    while True:
        command = listen()
        # You can change the interval of the ping by changing the value of this sleep()
        time.sleep(1)   
        # Here you can set up your own actions and commands
        if command == "OFFLINE":
            break  
        if "ECHO" in command:
            print(command.replace("ECHO",""))

if __name__ == "__main__":
    main()
