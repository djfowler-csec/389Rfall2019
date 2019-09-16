# Operational Security and Social Engineering

## Assignment details

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

You have been hired by a penetration testing firm and have been asked to collect some specific information about the Wattsamp employee from HW2, Eric Norman. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

- What's his mother's maiden name?
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?

Write up a pretext that you would use to social engineer this information out of Eric Norman. What approach would you take and how would you present yourself to elicit this information under the radar? Use the slides and what we covered in lecture to come up with a plan to obtain this information.

I would pose as a employee at a bank. Since social engineering is somewhat delicate in the sense that you can blow your cover doing something small. I would start by calling and asking if Eric was a member of the bank and then if Eric banks elsewhere ask where he banks and what you could do to get his business. If Eric uses another bank then it would be wise to note that information and either start the process of signing Eric up and during the process get into a 'Security Questions' section and use these questions as the security questions to elicit the information from Eric, and as one of the final steps ask him to choose a pin to use for the card he will recieve (many people re-use passwords and likely pins aswell so this pin could be the answer to his other banks pin). Suppose that Eric doesn't want to sign up for this bank then it would be in my best interest to hang up and call later (hours, days, week maybe) then call back assuming the role of an employee from the bank he uses, claim that there was a large number of customers that accounts have been compromised due to fraud and you need to check a few things to verify identity before being able to send out a new card. I would take the same route assuming that Eric turns out to be a customer all along. Verifying identity would include asking questions similar to above and finally asking for the PIN of the current card before asking if they want to change the PIN as it could have been compromised as part of the fraud breach. Since we were able to get Eric Normans address I would look up a legitimate bank around him in order to be able to give a real address for a corresponding bank if Eric were to ask. Finding the local banks also provides insight on what bank Eric might actually be using, also knowing local establishments could establish a sense of familiarity with Eric, this would make the converstation more friendly and as a result Eric would be more willing to give up some of this information without thinking. 

### Part 2

Eric Norman has recently discovered that Watsam's web server has been broken into by the crafty CMSC389R ethical hackers. After reading your published report, he has reached out to you to seek guidance in how he can repair some of the vulnerabilities that you have discovered.
Choose 3 specific vulnerabilities from homework 2 that you have identified (ie. exposed ports, weak passwords, etc.) and write a brief summary of some suggestions you can provide Eric for the Wattsamp web server and admin server. Be as thorough as possible in your answer, use specific examples and citing online research into security techniques that could be applied to the servers (ie. firewall, IDS/IPS, password managers, etc.).

Some techincal vulnerabilities that I discovered is that Eric was using a weak password. Increasing the password complexities on the server side would mitigate this risk. Using complex password including min/max length, require uppercase, lowercase, numbers, and symbols all increase the security of a password and is best practice. As we discovered it's rather simple to brute force into a system using a wordlist, having a complex password will make this option much more difficult and useless. Additionally, Eric should close port 1337 as no services are running on that port. The only service that the server was using was port 80 to host a website server so it is also best practice to disable all unused ports because keeping ports open that aren't being used can become a huge security risk as Eric found out. On the non-technical side Eric should not promote the website on his social media like that. Although it may be a good way to increase his network, maybe adding customers here or there, its not a great idea to mix personal and professinal business. As we learned in class, one of the biggest vulnerabilities are people themselves. The best practices based on password complexities and port security I learned while reading a Security+ book while pursuing my Sec+ certification. Some ways eric could add to his system would be to add and IPS to the network before traffic reaches the server. The IPS will be able to detect and prevent these brute force attacks because it can see that someone is constantly connecting to and failing to connect. As a result the IPS can begin to block the traffic altogether. This will add an additinal layer of security ontop of the identification/authentication that the server itself needs to permit access. In this scenario it would be best to use an IPS due to the amount of traffic the network takes on. However, it would also behove Eric to disable the port altogether in order to prevent that attack vector altogether. 
##Z Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.

### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
