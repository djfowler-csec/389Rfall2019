# Writeup 1 - Web I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)
	
	Inititally I tried several LFI techniques such as directory traversal and other things. Then I was stuck until figuring out that there was a SQL database lurking in the backgroung. In hindsight the keywords 'item?id=' should have been a giveaway but know I know better. I tried several injections that don't workand return a "ERROR: ATTEMPTED SQL INJECTION DETECTED". I tried variations trying to bypass the filter such as "item?id=0'%20OR%201=1--", "item?id=0%27%20OR%201=1--", and "item?id=0'/**/OR/**/1=1--" among others that have similar variations. All of which have provided the same error. I initially thought this was the result of some firewall blocking the injection however I'm using Firefox on Kali with burp as my proxy, I intercept the GET request with my proxy and modify it in burp before forwarding the request so I don't believe I'm geting  blocked by a firewall.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.
	The first level was rather simple. The objective is to raise an alert by injecting a script. At first I tried <script>alert</script> and it didn't work so i looked up some syntax things and <script>aler(1)</script> worked!
	The second level was kind of fun to figure out after sitting around a few minutes I tried just posting some html code and it worked so I understand that I write an html line that results in an alert by using some element that can raise an alert for this i used <img src="random.jpg" onerror="javascript:alert(1)"/> to raise an alert
	The third level I took time scrolling through the 'Taget code' to get an idea of what is happening. At some point the code dynamically loads the appropriate image (given comment) and adds a img element to the html line. So we can play around with the formatting and insert another onerror into the img element to raise an alert. Since it gives us the image number (i.e #1,#2,#3) we can hardcode whichever one into this then add ' onerror='alert(1)'; The quotes are important to breaking up the quotes in the current context, adding the onerror, then continuing.
	The fourth level i had to resort to the code and hints for help. The hitns gave away that i should try using decoded values when adding input. I basically seperated the code from timer.html into something different in order to inject the alert() command. I used ')%Balert(1)%3B(' the quotes basically make it so it just inserts nicely into the current code where the startTimer function is called. and %3B are decoded semicolons.
	The fifth level I just added a javascript line to the url so when the email was entered and 'next' was clicked an alert popped up. Once you get to the signup page, remove 'confirm' and add javascript:alert(1) this will make it so when 'Next >>' is clicked the alert is executed because since the program uses next=... you can insert somthing such as the alert to change the next page. Looking at the code was extremely beneficial for this one.
	The last level went over my head. After sifting through the code and get a very general idea of what was going on, I exhausted my hints and still was somewhat lost on what to do. The code kind of gave a hint in a comment which read "This will totally prevent us from loading evil URLs" and so that code i took a closer look at. It utilizes a regex in order to match with https:// and its apparent that the regex only checks one case, that is http. so i tried all caps because HTTP won't get caught by a regex looking for http. knowing it would take a website i created a pastebin to host a script that was just utilized the alert(1) function. and provided a remote file inclusion on the pastebin making sure i used HTTPS instead of https.
### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
