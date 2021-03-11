## PinterestC2
Proof of Concept project:
Using webpages as a Command Center to remote execute python.

### 1) The context.
On a discord server I am a part of, a message was sent that caught my eye:
``` "making a botnet using pinterest" ```
At first, I was baffled. What? Why? What? But the more I thought about it, the more I had to give it a shot. 
Here's a brief PoC writeup on how it works. All of the code used in this project can be found in the "FOLDER" folder.
#
### 2) The plan.
Although the original idea was to use a pinterest bio to relay the code, for demonstration purposes we're going to build our own web-app.
Since I am already familiar with Flask, that is what we're going to be using for the frontend. 
The whole setup consists of 3 separate, distinct apps.
#### 1st app: reads in consistent intervals the predefined html page that has the instructions. 
  Finds the keywords and continues accordingly.
#### 2nd app: is our webapp, that we can locate on a external server. 
  Display a html, and have functionality to change the contents according to "user input".
  On a social media platform this "user input" could be i.e changing your bio or name.
#### 3rd app: works as an automated script to insert user input into our webapp.
  To actually control our C2 remotely, we might want to create a script that could change the "user input" on the site.
  In the example of pinterest this would mean a script that takes your input in terminal, and then inserts this input 
  into your pinterest profile, as either name or a sentence in your bio.
 #
 ### 3) The execution.
I wanted to start by building a simple website to test my scraper.  
  ```
  @app.route('/')  
  def home():  
    return "Welcome to rest a pint!"  
  ``` 
  Afterwhich I could test my scraper. This has one problem though,
if I do a simple
``` page = requests.get(url); print(page.text) ```  
It gives me a plain string, ``` "Welcome to rest a pint!" ```. If we did the same to, say pinterest.com the output would be the whole HTML of the mainpage.
To test out the parsing and coming closer to a real use case, we shall make it return a simple .html template, called "mainpage"
