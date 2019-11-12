# Writeup 9 - Forensics II

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details

### Part 1 (45 Pts)
	1. What IP address is being attacked?
		142.93.136.81:21
	2. What kind of assesment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

	3. What are the hackers IP addresses and where are they connecting from?
		The hackers IP address is 159.203.113.181 connected on port 55914

	4. What port are they using to steal files?
		They are connecting to port 21 on the server (FTP) probably to have the ability to transfer files back and fourth.

	5. Which file did they steal? What kind of file is it? Do you recognize it?
		It looks like they retrieved the 'find_me.jpeg' from the server. This is a jpeg file.

	6. Which file did the attackers leave behind on the server?
		The attackers left behind a file called 'greetz.fpff'

	7. What is a countermeasure to prevent this kind of intrusion from happening again?
		I noticed that the password isn't very secure, updating password policies and restrictions would make it harder for the attacker to gain access. You could implement a firewall setting that is implicit-deny, this means that unless the ip address is implicitly whitelisted and allowed than connection from the address will be denied. Other than that you could implement an IPS on the network. This will enable similar capabilities to the implicit-deny I mentioned earlier and go even further since an IPS has additional capabilities.
### Part 2 (55 Pts)
	1. Develop the parser
		See stub.py for code
	2. Parse greetz.fpff and give the following:
		I. When was greetz.fpff generated?
			2019-03-27 00:15:05	
		II. Who authored greetz.fpff?
			f1nch
		III. List each section and give data in it and type.
			Section 1: SECTION_ASCII
			Data: Hey you, keep looking :)

			Section 2: SECTION_COORD
			Data: (52.)

			Section 3: SECTION_PNG
			Data: Picture

			Section 4: SECTION_ASCII
			Data: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC

			Section 5: SECTION_ASCII
			Data: Q01T1zM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=
 
		IV. Report at least one flag hidden in greetz.fpff
			1.CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
			2.CMSC389R-{hey_h3y_yoU_you_I_dont_like_your_base64_encoding}
			3.Probably in the png but my parser isn't 1337 enough
