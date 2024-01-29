burmese_to_modified_ipa
Python script to transliterate Burmese text into the International Phonetic Alphabet

Burmese Script to Modified IPA
by Brian Oleniacz
	
	This program takes a text in Burmese Script as input and outputs two texts:
	1. A text in a modified version of the International Phonetic Alphabet
	2. A syllable by syllable parallel output where each Burmese Syllable is 
	   followed by its modified IPA equivalent.


	Modified IPA
	The alphabet used here has two main departures from standard IPA:
	-the nasalization sign ŋ̃ which is nonstandard and
	-tone marks including	 ̰ for creaky tone (standard IPA)
       					 ˋ for a high falling tone which is combined 
	with ':' (the standard marker for long high tone in Burmese 
							 ́  for low rising tone

 	ŋ̃ stands here for ɰ̃ which looks like a w to me and always makes me round
	my lips. Technically the sound here described is a partially closed throat.
	I used the ~ from Portuguese to represent the nasalizing effect of only
	partially closing my throat	and ŋ to get me to close my throat instead of 
	rounding my lips.

	Feel free to modify this code to get it to work better. 
	Please only use it for good purposes- no evil allowed.
	Please include my name in some way if you change it and publish it.
	(Brian Oleniacz https://github.com/deersfeet) 
	I haven't finished error handling. This program crashes when unusual 
	consonants are found. I am still working on catching bugs.
	The main logic of the algorithm is to find each syllable in the Burmese
	text using the rules of Burmese spelling. This is a lot harder than it sounds.
	Many Burmese syllables are not pronounced the way they are spelled. This
	Program will not help with such pronunciations.
	I am not a native speaker of Burmese. If you find errors let me know and I 
	will fix them.
	Thank you for using my program.

	Brian J Oleniacz
	soaringenglish@gmail.com
	Carrboro, NC, USA
	30/7/2023
