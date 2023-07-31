import burmese_initials_dictionary as initialsdict
import binary_rhymes_dictionary as rhymesdict

consonants = {
'က':	'k', 	
'ခ':	'kʰ', 	
'ဂ':	'ɡ', 	
'ဃ':	'ɡ', 	
'င':	'ŋ',	
'စ':	's',	
'ဆ': 	'sʰ',	
'ဇ':	'z',	
'ဈ':	'z',	
'ဉ':	'ɲ',
'ည': 	'ɲ',
'ဋ':	't',	
'ဌ':	'tʰ', 	
'ဍ':	'd',
'ဎ':	'd', 	
'ဏ':	'n',	
'တ':	't',	
'ထ':	'tʰ', 	
'ဒ':	'd',	
'ဓ':	'd', 	
'န':		'n',	
'ပ':	'p',	
'ဖ':	'pʰ', 	
'ဗ':	'b',	
'ဘ': 	'b', 	
'မ':	'm',	
'ယ': 	'j',	
'ရ':	'j',	
'လ': 	'l',	
'ဝ':	'w',	
'သ': 	'θ',
'ဟ':	'h', 	
'ဠ':	'l',	
'အ': 	'ʔ',
'ဣ':	'ʔḭ', 	
'ဤ':	'ʔì',
'ဥ':	'ʔṵ', 	
'ဦ':	'ʔù',
'ဧ':	'ʔè', 	
'ဩ': 	'ʔɔ́',
'ဪ': 'ʔɔ̀',
'ၐ':	'ʃ',
'ၑ':	'ʃ',
'ဿ':	's',
}

alternate_initials_dict = {
'က':	'k', 	
'ခ':	'kʰ', 	
'ဂ':	'ɡ', 	
'ဃ':	'ɡ', 	
'င':	'ŋ',	
'စ':	's',	
'ဆ': 	'sʰ',	
'ဇ':	'z',	
'ဈ':	'z',	
'ဉ':	'ɲ',
'ည': 	'ɲ',
'ဋ':	't',	
'ဌ':	'tʰ', 	
'ဍ':	'd',
'ဎ':	'd', 	
'ဏ':	'n',	
'တ':	't',	
'ထ':	'tʰ', 	
'ဒ':	'd',	
'ဓ':	'd', 	
'န':		'n',	
'ပ':	'p',	
'ဖ':	'f',
'ဗ':	'b',	
'ဘ': 	'b', 	
'မ':	'm',	
'ယ': 	'j',	
'ရ':	'j',	
'လ': 	'l',	
'ဝ':	'w',	
'သ': 	'θ',
'ဟ':	'h', 	
'ဠ':	'l',	
'အ': 	'ʔ',
'ဣ':	'ʔḭ', 	
'ဤ':	'ʔì',
'ဥ':	'ʔṵ', 	
'ဦ':	'ʔù',
'ဧ':	'ʔè', 	
'ဩ': 	'ʔɔ́',
'ဪ': 'ʔɔ̀',
'ၐ':	'ś',
'ၑ':	'ṣ',
'ဿ':	's',
'ရှ':	'ʃ',
'ယှ':	'ʃ',
}

vowels = {
	'ါ':	'á',
	'ာ':	'á',
	'ိ':	'i',
	'ီ':	'i',
	'ု':	'ṵ',
	'ူ':	'́u',
	'ေ':	'e',
	'ဲ':	'ɛ́',
	'ဳ':	'i',
	'ဴ':	'o',
	'ဵ':	'e',
	'ံ':	'm',
	'ျ':	'j',
	'ြ':	'j',
	'ွ':	'w',
	'ှ':	'h',	

	#Pali
	'ၒ':	'r',
	'ၓ':	'rr',
	'ၔ':	'l',
	'ၕ':	'll',
	#Sanskrit
	'ၖ':	'r',
	'ၗ':	'rr',
	'ၘ':	'l',
	'ၙ':	'll',
}



syllable_enders = {
	'႟': '!',
	'၊': ',',
	'။': '.',
	'၏': 'genitive',
    '၍': ' and ',
    '၌': ' locative ',
    '၍': ' completed ',
    '၎င်း': ' ditto ',
    '၀': '0',
	'၁': '1',
	'၂': '2',
	'၃': '3',
	'၄': '4',
	'၅': '5',
	'၆': '6',
	'၇': '7',
	'၈': '8',
	'၉': '9',
}

medials_b_dict = { #medials binary dictionary
b'\xe1\x80\xbb': b'j', #ya pin
b'\xe1\x80\xbb\xe1\x80\xbe': b'\xcc\xa5j',	#ya pin + ha hto
b'\xe1\x80\xbb\xe1\x80\xbd': b'w',	#ya pin + wa hswe
b'\xe1\x80\xbb\xe1\x80\xbd\xe1\x80\xbe':	b'\xcc\xa5w', # ya pin + ha hto + wa hswe
b'\xe1\x80\xbc': b'j',	#ya yit
b'\xe1\x80\xbc\xe1\x80\xbe':	b'\xcc\xa5j', #ha hto
b'\xe1\x80\xbc\xe1\x80\xbd':	b'w',	#ya yit + wa hswe
b'\xe1\x80\xbc\xe1\x80\xbd\xe1\x80\xbe':	b'\xcc\xa5w', #ya yit + ha hto + wa hswe
b'\xe1\x80\xbd':	b'w',	#wa hswe
b'\xe1\x80\xbd\xe1\x80\xbe':	b'\xcc\xa5w', #ha hto + wa hswe
b'\xe1\x80\xbe':	b'\xcc\xa5',	#ha hto
#Sanskrit r
b'\xe1\x81\x96': b'r\xcc\xa5',
b'\xe1\x81\x97': b'r\xcc\xa5\xcc\x84',

}



class Buffer:
	def __init__(self):
		self.buffer1 = ''
		self.buffer2 = ''


def main():

	while True:

		burmese_text = input("Enter Burmese to transliterate or 'exit' to exit: ")

		if burmese_text == 'exit':
			break

		if burmese_text == '\n':
			continue

		next_char_is_doubled_cons = False

		ipa_and_burmese = ''
		ipa_only = ''
		syllable_ender_reached = False
		char_is_bottom_of_stack = False
		second_consonant_already_hit = False
		virama = False
		anusvara = False
		
		syllable1 = Buffer()

		burmese_string = ''

		burmese_syllables = []

		last_char = ''

		for char in burmese_text:
			burmese_string += char

			if ord(char) >= 0x1000 and ord(char) <= 0x109F: #Burmese Unicode Range

				if char in syllable_enders.keys():

					if syllable1.buffer1 != '':
						if second_consonant_already_hit == False:
							if virama: #eg. syllable1.buffer1 == ဒေါ် 
								burmese_syllables.append(syllable1.buffer1)
								burmese_syllables.append(char)
								syllable1 = Buffer()
								# virama = False
							else: #same code
								burmese_syllables.append(syllable1.buffer1)
								burmese_syllables.append(char)
								syllable1 = Buffer()


						elif second_consonant_already_hit: #if buffer2 has value
							if virama: #if 2nd Consonant (buffer2) is part of the syllable structure
								burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
								burmese_syllables.append(char)
								syllable1 = Buffer()
	
								# second_consonant_already_hit = False #see below
								# virama = False
							elif anusvara:
								burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
								burmese_syllables.append(char)
								syllable1 = Buffer()

								# second_consonant_already_hit = False #see below
								# anusvara = False
							else: #Each consonant is its own syllable
								burmese_syllables.append(syllable1.buffer1)
								burmese_syllables.append(syllable1.buffer2)
								burmese_syllables.append(char)
								

					
					else: 
						if syllable1.buffer1 == '':
							burmese_syllables.append(char) #leave syllable1.buffer1 empty and append syllable ender char
					
					syllable1 = Buffer()

					second_consonant_already_hit = False
					next_char_is_doubled_cons = False
					virama = False
					anusvara = False




				
				elif char in consonants.keys():
			
					if syllable1.buffer1 == '':
						syllable1.buffer1 = char
					else:
						if char_is_bottom_of_stack == False:
							if second_consonant_already_hit == False:
								if virama: #eg. syllable1.buffer1 == ဒေါ် 
									burmese_syllables.append(syllable1.buffer1)
									syllable1 = Buffer()
									syllable1.buffer1 = char
									# second_consonant_already_hit = False
									virama = False
								else:
									second_consonant_already_hit = True
									syllable1.buffer2 = char


							elif second_consonant_already_hit == True: #if this is the third consonant 
								if virama: #if 2nd Consonant (buffer2) is part of the syllable structure
									burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
									syllable1 = Buffer()
									syllable1.buffer1 = char
									second_consonant_already_hit = False
									virama = False
								elif anusvara: #anusvara always stays in syllable1.buffer2
									burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
									syllable1 = Buffer()
									syllable1.buffer1 += char
									second_consonant_already_hit = False
									anusvara = False
								else: # At least first consonant has its own complete syllable
									burmese_syllables.append(syllable1.buffer1)		
									syllable1.buffer1 = syllable1.buffer2 #start new buffer with 2nd cons
									syllable1.buffer2 = char

						else: #if char is bottom of stack
							syllable1.buffer1 += char
							char_is_bottom_of_stack = False


				elif char == '္': #combines consonants
					if second_consonant_already_hit:
						burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
						syllable1 = Buffer()
						second_consonant_already_hit = False
						virama = False
					else: #doubled initial
						syllable1.buffer1 += char
						char_is_bottom_of_stack = True
				

				elif char == '်': #changes a consonant into a vowel
					virama = True
					if second_consonant_already_hit:
						syllable1.buffer2 += char #add to second cons
					else:
						syllable1.buffer1 += char
						if last_char == 'ာ' or last_char == 'ါ':	
							burmese_syllables.append(syllable1.buffer1)
							syllable1 = Buffer()
							virama = False			
							second_consonant_already_hit = False


				elif char == 'ံ': #anusvara- shorthand for nasal consonant
					anusvara = True
					if second_consonant_already_hit: #anusvara belongs to 2nd consonant
						burmese_syllables.append(syllable1.buffer1)
						syllable1.buffer1 = syllable1.buffer2 
						syllable1.buffer2 = char
						second_consonant_already_hit = True

						virama = False			

					else:
						second_consonant_already_hit = True
						syllable1.buffer2 += char


				elif char == "့" or char == "း": 
					if second_consonant_already_hit:
						syllable1.buffer2 += char
					else:
						syllable1.buffer1 += char


				elif char in vowels.keys():
					if second_consonant_already_hit:
						burmese_syllables.append(syllable1.buffer1)
						syllable1.buffer1 = syllable1.buffer2 + char
						syllable1.buffer2 = ''
						second_consonant_already_hit = False
					else:
						syllable1.buffer1 += char

			else: #if char is a syllable-ending Non Burmese Character outside Burmese unicode range

				if syllable1.buffer1 != '':
					if second_consonant_already_hit == False:
						if virama: #eg. syllable1.buffer1 == ဒေါ် 
							burmese_syllables.append(syllable1.buffer1)
							burmese_syllables.append(char)
							syllable1 = Buffer()
							# virama = False
						else: #same code
							burmese_syllables.append(syllable1.buffer1)
							burmese_syllables.append(char)
							syllable1 = Buffer()


					elif second_consonant_already_hit: #if buffer2 has value
						if virama: #if 2nd Consonant (buffer2) is part of the syllable structure
							burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
							burmese_syllables.append(char)
							syllable1 = Buffer()
							# second_consonant_already_hit = False #see below
							# virama = False
						if anusvara:
							burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
							burmese_syllables.append(char)
							syllable1 = Buffer()
							# second_consonant_already_hit = False #see below
							# anusvara = False
						else: #Each consonant is its own syllable
							burmese_syllables.append(syllable1.buffer1)
							burmese_syllables.append(syllable1.buffer2)
							burmese_syllables.append(char)

				
				elif syllable1.buffer1 == '':
					burmese_syllables.append(char) #leave syllable1.buffer1 empty and append syllable ender char
				
				syllable1 = Buffer()
				second_consonant_already_hit = False
				next_char_is_doubled_cons = False
				virama = False
				anusvara = False
			
			last_char = char




		#at end of string
		if virama:
			burmese_syllables.append(syllable1.buffer1 + syllable1.buffer2)
		else:
			if second_consonant_already_hit:
				burmese_syllables.append(syllable1.buffer1)
				burmese_syllables.append(syllable1.buffer2)
			else:
				if syllable1.buffer1 != '':
					burmese_syllables.append(syllable1.buffer1)


		syllable1 = Buffer()

		second_consonant_already_hit = False
		next_char_is_doubled_cons = False
		virama = False



		
		# print(burmese_syllables)

		not_burmese_syllable = False
		burmese_string = ''
		for syllable in burmese_syllables:
			ipa = ''
			burmese_string += syllable
			# print(burmese_string)
			# print("Burmese syllable: "+ syllable)
			if syllable == 'ဦး':
				ipa = 'Ú' 
			elif syllable == 'ဣး':
				ipa = 'Ɂí'
			elif syllable == 'ဤး':
				ipa = 'Ɂí'
			elif syllable == 'ဥး':
				ipa = 'Ɂú'
			elif syllable == 'ဧး':
				ipa = 'Ɂé'
			elif syllable == 'ဪး':
				ipa = 'Ɂó'
			elif syllable == '':
				ipa = ''
			elif not (ord(syllable[0]) >= 0x1000 and ord(syllable[0]) <= 0x109F): #Burmese Unicode range
				not_burmese_syllable = True
				ipa = syllable
			elif syllable[0] in syllable_enders:
				ipa = syllable_enders[syllable]
			elif syllable != '':
				
				initial = ''
				initial_ipa = ''
				initial_is_doubled_cons = False
				not_burmese_syllable = False
				rhyme = ''
				rhyme_ipa = ''
				
				#first build up the initial, then build up the rhyme separately.
				for pos, char in enumerate(syllable):
					
					added_to_initial = False

					if pos == 0:
						initial = char
						added_to_initial = True
					elif pos == 1 and char == '္': 
							initial += char
							initial_is_doubled_cons = True
							added_to_initial = True
					elif pos == 2 and initial_is_doubled_cons:
							initial += char
							added_to_initial = True
							initial_is_doubled_cons = False
					elif char.encode('utf-8') in medials_b_dict: #ya pin, ya yit, wa hswe, ha hto
						initial += char
						added_to_initial = True


					if not added_to_initial: #then part of rhyme
						rhyme += char


				# print("burmese_syllable: " + syllable)
				# print("initial: " + initial)
				initial_ipa = initialsdict.initials_dict[initial]
				# print("initial ipa: " + initial_ipa)
				# print("rhyme: " + rhyme)

				if rhyme == '':
					rhyme_ipa = 'a̰'

				elif rhyme == '်':
					initial_ipa = alternate_initials_dict[initial]
					rhyme_ipa = ''
				else:
					rhyme_ipa = rhymesdict.binary_rhymes_dictionary[rhyme.encode("utf-8")]
				# print("rhyme ipa: " + rhyme_ipa)
				ipa = initial_ipa + rhyme_ipa


			# print("Added " + ipa)
			if not not_burmese_syllable:
				ipa_and_burmese +=  syllable + " " + ipa + '  '
			ipa_only += ipa + ' '

		# print("\n" + burmese_text)
		print("\n" + ipa_only)
		print("\n" + ipa_and_burmese)


main()




		




