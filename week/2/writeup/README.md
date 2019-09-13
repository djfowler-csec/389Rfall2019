# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*
Name: Eric Norman
Eric works for Wattsamp Energy, the website is http://wattsamp.net
The website had a link to the umd csec club and the umdcsec twitter. Additionally, I found an easter egg while looking at the html 'inspect element'
the easter egg is: *CMSC389R-{html_h@x0r_lulz}, this was on the admin login page inspect element.
Used Namechkr to determine what websites the username 'ejnorman84' was used for. I found an account for ejnorman84 on reddit and Instagram
The instagram had a picture with an easter egg labeled "I <3 my power plant" with the flag *CMSC389R{Looking_Closely_Pays}
After doing '$ whois wattsamp.net' I gathered that the doman was registered under Eric Norma, 1300 Adabel Dr El Paso Texas, 79835 United States
with a Phone: +1-202-656-2837 and email: ejnorman84@gmail.com
Did a dns search of wattsamp.net i found a server with an ip of 157.230.179.99
I did an nmap of this ip address and found that ports 22 (ssh)-disabled 80(http) and 1337 were open.
I preformed '$ nmap -sV --script=banner 157.230.179.99' to determine that the server was running a Ubuntu linux OS and an apache web server.
### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*

Knowing that the username was most likely 'ejnorman84' I added to the stub.py to go through the wordlist and hopefully find the right password.
Heres the overall idea of the script:
while there are lines in the wordlist it will create a socket and netcat to the server, it uses pythons re.findall to create a list of the regex
which is just the (digit operand digit). I had to create a try/catch because I got an exception for something based on the list, if the exception got caught
the loop would re-iterate without changing the attempted password. The rest is pretty straight forward, send the captcha, recieve the next bytes of data,
send, recieve, send, then loop if "Fail" was caught in a regular expression, if "Fail" wasn't found the loop broke and printed the password.
After gaining access to the server I found the flag almost instantly in /home/flag.txt after preforming a 'grep -r CMSC389R'.

