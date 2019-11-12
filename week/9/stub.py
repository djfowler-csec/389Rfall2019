#!/usr/bin/env python2
import os
import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp  = struct.unpack("<L", data[8:12])
author = struct.unpack("<Q", data[12:20])
sec_num = struct.unpack("<L",data[20:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if sec_num <= 0:
    bork("Bad Section Number: Got %d, needs to be above 1" % int(sec_num))
else:
    new_dir = sys.argv[1] + "_extracted"
    try:
	os.mkdir(new_dir)
    except OSError:
	print ("Creation of new directory %s failed" % new_dir)
    else:
	print ("Creation of new directory %s success" % new_dir)
 
#Unpacking the timestamp and converting the time to a unix timestamp
(x,) = timestamp
time_conv = datetime.fromtimestamp(float(x))
#Unpacking the section number from tuple
(y,) = sec_num
sec_num = y
#Unpacking the author value from tuple, convert it to hex then from hex covert to ASCII. Then reverse the string since the hex was in little endian.
(r,) = author
temp = str(hex(r))
rev = ''.join(reversed(bytearray.fromhex(temp[2:]).decode()))
author = rev

#Necessary printing of Header Information
print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % time_conv )
print("Author: %s" % author)
print("Section : %d" % int(y))

def sec_type(i):
	switcher={
		1:'SECTION_ASCII',
		2:'SECTION_UTF8',
		3:'SECTION_WORDS',
		4:'SECTION_DWORDS',
		5:'SECTION_DOUBLES',
		6:'SECTION_COORD',
		7:'SECTION_REFERENCE',
		8:'SECTION_PNG',
		9:'SECTION_GIF87',
		10:'SECTION_GIF89'
  	    }
	return switcher.get(i, "Invalid")

#Necessart printing of body information
print("-------  BODY  -------")
start = 24
end = 28
orig_stdout = sys.stdout
for x in range(sec_num):
	#Reset  the stdout after writing a file
	sys.stdout = orig_stdout
	#Prints the section number
	print("Section %d:" % int(int(x)+int(1)))
	type = struct.unpack("<L",data[start:end])
	(stype,) = type
	len = struct.unpack("<L",data[(start+4):(end+4)])
	(slen,) = len
	#(Above) unpack and retreieve values for stype and slen then (below) print the values accordingly
	print("\tSection Type: %s" % sec_type(stype))
	print("\tSection Length: %d" % int(slen))
	if len > 0:
		svalue = 8 + slen
		print("\tSection Value: %d" % int(svalue))

	#if sec_type is SECTION_ASCII it parses the information
	if (sec_type(stype) == sec_type(1)):
		temp = slen/4
		format = ("<" + ("L" * temp))
		body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
		res = ""
		for var in body:
			temp1 = str(hex(var))
			temp2 = ''.join(reversed(bytearray.fromhex(temp1[2:]).decode()))
			res = res + temp2
		file_name = "/SEC_ASCII%d.txt" % int(int(x)+int(1))
		file_name = new_dir + file_name
		print("You can find the extracted file in: %s" % file_name)
		#print(body)
		f = open(file_name, 'w')
		sys.stdout = f
		print(res)
		f.close()

        #if sec_type is SECTION_UTF8 it parses the information
        if (sec_type(stype) == sec_type(2)):
                temp = slen/4
                format = ("<" + ("L" * temp))
                body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = ""
                for var in body:
                        temp1 = str(hex(var))
                        temp2 = ''.join(reversed(bytearray.fromhex(temp1[2:]).decode()))
                        res = res + temp2.decode("utf-8")
                file_name = "/SEC_UTF8Decoded%d.txt" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You can find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f 
                print(res)
                f.close()
	#if sec_type is SECTION_WORDS it parses the information
	if (sec_type(stype) == sec_type(3)):
		temp = slen/4
		format = ("<" + ("L" * temp))
		body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
		res = ""
		for var in body:
			temp1 = ''.join(reversed(var))
			res = res+temp1
		file_name = "/SEC_WORDS%d.txt" % int(int(x)+int(1))
		file_name = new_dir + file_name
		print("You cant find the extracted file in: %s" % file_name)
		#print(body)
		f = open(file_name, 'w')
		sys.stdout = f
		f.close()
	#if sec_type is SECTION_DWORD it parses the information
	if (sec_type(stype) == sec_type(4)):
		temp = slen/8
		format = ("<" + ("Q" * temp ))
		body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = ""
                for var in body:
                        temp1 = ''.join(reversed(var))
                        res = res+temp1
                file_name = "/SEC_DWORDS%d.txt" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You cant find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f
                f.close()
	#if sec-type is SECTION_DOUBLE it parses the information
        if (sec_type(stype) == sec_type(5)):
                temp = slen/8
                format = ("<" + ("d" * temp ))
                body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = ""
                for var in body:
                        temp1 = ''.join(reversed(var))
                        res = res+temp1
                file_name = "/SEC_DOUBLE%d.txt" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You cant find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f
                f.close()

	#if sec_type is SECTION_COORD is parses the information
	if(sec_type(stype) == sec_type(6)):
 		temp = slen/8
		format = ("<" +("d" *temp))
		body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = ""
		file_name = "/SEC_COORD%d" % int(int(x)+int(1))
		file_name = new_dir + file_name
		print("You can find the extracted file in: %s.txt" % file_name)
		f = open(file_name, 'w')
		sys.stdout = f
                print("(%f, %f)" % body)
		f.close()
	#if sec_type is SECTION_REFERENCE it parses the information
	if(sec_type(stype) == sec_type(7)):
		if slen != 4:
			raise Exception("SECTION_REFERENCE slen is not 4")
		else:
			temp = slen/4
			format = ("<" + ("L" * temp))
			body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                	res = ""
                	file_name = "/SEC_REFERENCE%d" % int(int(x)+int(1))
                	file_name = new_dir + file_name
                	print("You can find the extracted file in: %s.txt" % file_name)
                	f = open(file_name, 'w')
               		sys.stdout = f
	                print("(%f,)" % body)
        	        f.close()
	#if sec_type is SECTION_PNG it parses the information
	if(sec_type(stype) == sec_type(8)):
		temp = slen/4
                format = ("<" + ("L" * temp))
                body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = "89504e470d0a1a0a"
                for var in body:
                        temp1 = str(hex(var))
                        temp2 = ''.join(reversed((temp1[2:])))
                        res = res + temp2		
                file_name = "/SEC_PNG%d.png" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You can find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f
                print(res)
                f.close()
	#if sec_type is SECTION_GIF87 it parses the information
	if(sec_type(stype) == sec_type(9)):
                temp = slen/4
                format = ("<" + ("L" * temp))
                body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = "4749463837610000"
                for var in body:
                        temp1 = str(hex(var))
                        temp2 = ''.join(reversed((temp1[2:])))
                        res = res + temp2
                    
                file_name = "/SEC_GIF87_%d.gif87" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You can find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f
                print(res)
                f.close()
        #if sec_type is SECTION_GIF89 it parses the information
        if(sec_type(stype) == sec_type(10)):
                temp = slen/4
                format = ("<" + ("L" * temp))
                body = struct.unpack(format,data[(start+8):(end+4+int(slen))])
                res = "4749463839610000"
                for var in body:
                        temp1 = str(hex(var))
                        temp2 = ''.join(reversed((temp1[2:])))
                        res = res + temp2
                    
                file_name = "/SEC_GIF87_%d.gif89" % int(int(x)+int(1))
                file_name = new_dir + file_name
                print("You can find the extracted file in: %s" % file_name)
                #print(body)
                f = open(file_name, 'w')
                sys.stdout = f
                print(res)
                f.close()

	#Increments the position where we are reading in the file
	start = start + slen + 8
	end = end + slen + 8
	

