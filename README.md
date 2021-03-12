## PinterestC2
Proof of Concept project:
Using webpages as a Command Center to remotely execute python.

### 1) The context.
On a discord server I am a part of, a message was sent that caught my eye:
``` "making a botnet using pinterest" ```
At first, I was a bit mixed. What? Why? What? But the more I thought about it, the more I had to give it a shot. 
Here's a brief writeup on how it should work. All of the code used in this project can be found in the "Code" folder.
#
### 2) The plan.
Although the original idea was to use a pinterest bio to relay the code, for demonstration purposes we're going to build our own web-app.
Since I am already familiar with Flask, that is what we're going to be using for the frontend. 
The whole setup would consist of 3 separate, distinct apps.
#### 1st app: reads in consistent intervals the predefined html page that has the instructions. 
  Finds the keywords and reads everything inbetween them.
#### 2nd app: is our webapp, that we can locate on a external server. 
  Display a html, and have functionality to change the contents according to "user input".
  On a social media platform this "user input" could be i.e changing your bio or name.
#### 3rd app: works as an automated script to insert user input into our webapp.
  To actually control our C2 remotely, we might want to create a script that could change the "user input" on the site.
  In the example of pinterest this would mean a script that takes your input in terminal, and then inserts this input 
  into your pinterest profile, as either name or a sentence in your bio.
  ###### However in this project, we will not do the 3rd app, since we're not actually using a real social media site with well built frameworks.
 #
 ### 3) The execution.  
  
#### Setting up the website
I wanted to start by building a simple website to test my scraper.  
  ```
  @app.route('/')  
  def home():  
    return "Welcome to rest a pint!"  
  ```
This has one problem though,
if I do a simple
``` page = requests.get(url); print(page.text) ```  
It gives me a plain string, ``` "Welcome to rest a pint!" ```. If we did the same to, say pinterest.com the output would be the whole HTML of the mainpage.
In order to come closer to our real use case, we'll make it return a simple .html template, called "mainpage". This will be stored in the templates folder.
#### Setting up the scraper
This was fairly easy. 
What you do is set up a loop, wait a set amount of time, pull your desired url as "page". Then assing page.text to a variable to later handle its contents.
```  
import time  
import requests as req  
  
while True:  
    page = req.get(YourUrlHere)  
    content = page.text  
```
We can now handle the contents of the html page. To find our command, we want to set up a keyword on the page. Let's use something distinct, like !pC2.
```  
if "!pC2" in content:  
  content = content.split("!pC2")
  return content[1]
```  
The script finds everything inbetween "!pC2". We can now set up a command on the site, i.e !pC2OFFLINE!pC2.
Now we can start having actions execute on our device. Although kind of dumb, we can use the previous example to make the machine stop listening completely. Why would you want it to do this? No clue. Lets do it.    
Let's make the previous code a function called "listen", and move the while loop into our main(). To add interest, 
lets also add a command "ECHO" that prints everything after it to our terminal.
Now we have something like this:
```  
while True:
    time.sleep(1)
    command = listen()
    if command == "OFFLINE":
        break  
    if "ECHO" in command:
        print(command.replace("ECHO",""))
```  
#### Testing this all out.
To make sure that it really does work, I set up my simple webapp on a VPS. Connecting to https://my.vps.ip:5000/ on my browser shows our mainpage.html, meaning that the page is up. Now when I insert that url into my reader.py,   ```url = my.vps.ip:5000 ``` and run the .py, the terminal stays clear and our VPS terminal shows that someone is visiting our site roughly every second. Now let's go back to our template.html, and add one line below line 12:  
```  
12 <h1 style="color:white;">Welcome to rest a pint!</h1>     
13 <p style="color:white;">!pC2OFFLINE!pC2</p>  
```  
This now adds one line to our website, which we can imagine to represent, say, our profile name on pinterest. If we run the reader.py again, surely enough the program just cleanly exits after one second of running, implying it works as it should.
#
### 4) Final thoughts.
All in all, the basic idea should work just as thought: remotely executing code based on strings on a webpage. How useful it is, on the otherhand, relies on many things. 
To an siteowner, even a few bots on a botnet pinging once every second or so your site looks awfully lot like a DDoS. Maybe if you ran the page on a proxy, and all the bots would req that instead of a real site, you could get away with it. Though then it wouldn't be a Pinterest Botnet now would it?  
