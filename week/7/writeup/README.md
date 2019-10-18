# Writeup 7 - Forensics I

Name: Dalton Fowler
Section 0101:

I pledge on my honor that I have not given or recieved any unauthorized assistance on this assignment or examination

Digital ackknowledgement: DALTON FOWLER

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it?
	The file type associated with the 'image' file is JPEG

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.
	Photo was taken at 41deg53'54.87"N, 87deg37'22.53"W
	These coordiantes relate to the John Hancock Center located in Chicago, Illinois

3. When was this photo taken? Provide a timestamp in your answer.
	Photo was taken on 08/22/2018 at 11:33:24 AM

4. What kind of camera took this photo?
	An iPhone 8 camera took the photo.

5. How high up was this photo taken? Provide an answer in meters.
	This photo was taken 539.5 meters above sea level.

6. Provide any found flags in this file in standard flag format.
	After doing a binwalk with the option --dd="png:png" I extracted another file which provided a png file that contained a flag: CMSC389R-{abr@cadabra}.
