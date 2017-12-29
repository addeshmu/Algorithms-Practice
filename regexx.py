#courtesy :HackerRank
import re

Test_String = raw_input()

Regex_Pattern = r"[\d]{2}[\D]{1}[\d]{2}[\D]{1}[\d]{4}"	# /d finds all 0-9 and /D finds all non-ints and {}number inside this tells how many of that type
Regex_Pattern = r"[^\n]{3}[.][^\n]{3}[.][^\n]{3}[.][^\n]{3}"	# for getting xxx.xxx.xxx.xxx format.
Regex_Pattern = r'hackerrank'	# Do not delete 'r,r means raw string input ,will ignore python escapes and use regex ones equivalent to using \\'.
Regex_Pattern = r"[\S]{2}[\s][\S]{2}[\s][\S]{2}"	# \s matches any whitespace character [ \r\n\t\f ].\S matches any non-white space character.
Regex_Pattern = r"[\w]{3}[\W][\w]{10}[\W][\w]{3}"	# Do not delete 'r'.The expression \w will match any word character.Word characters include alphanumeric characters (A-Z, 0-9 and a-z) and underscores (_).\W non word
Regex_Pattern = r"^[\d]{1}[\w]{4}[.]$"	# ^ ddenotes start of the string and $ as end
Regex_Pattern = r'^[123]{1}[120]{1}[xs0]{1}[30Aa]{1}[xsu]{1}[.,]{1}$'	# Do not delete 'r'.The character class [ ] matches only one out of several characters placed inside the square brackets.
Regex_Pattern = r'^[^\d]{1}[^aeiou]{1}[^bcDF]{1}[^\s]{1}[^AEIOU]{1}[^.,]{1}$'	# The negated character class [^] matches any character that is not in the square brackets.
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# A hyphen inside a character class specifies a range of characters. For example:[A-Z]=[ABCD........Z]
Regex_Pattern = r'^[a-zA-z02468]{40}[\s13579]{5}$'	# The tool {x} will match exactly repetitions of character/character class/groups.
Regex_Pattern = r'^[\d]{1,2}[a-zA-Z]{3,}[.]{0,3}$'	# The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group.{3,} means 3 or more
Regex_Pattern = r'^[\d]{2,}[a-z]*[A-Z]*$'	# The * tool will match zero or more repetitions of character/character class/group.
Regex_Pattern = r'^[\d]+[A-Z]+[a-z]+$'	# The + tool will match one or more repetitions of character/character class/group.for ex:w+ : It will match the character w, 1 or more times.
Regex_Pattern = r'^[a-zA-Z]*s$'	# ending with s,given by $
Regex_Pattern = r'\b[aeiouAEIOU]{1}[A-Z,a-z]*\b'	# \b assert position at a word boundary.Three different positions qualify for word boundaries :Before the first character in the string, if the first character is a word character.Between two characters in the string, where one is a word character and the other is not a word character. After the last character in the string, if the last character is a word character.
Regex_Pattern = r'(ok){3,}?' #Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group.here we search for 3 or more consecutive ok
Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)[.][a-zA-Z]+$' #(Bob|Kevin|Stuart) : It will match either Bob or Kevin or Stuart.
Regex_Pattern = r'^([a-z][\w]\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1$'#This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.\2\3.. similarly can be used
Regex_Pattern = r"^[1-9]{2}(([-]{1})?)[1-9]{2}(([-]{1})?)[1-9]{2}(([-]{1})?)[1-9]{2}$"
Regex_Pattern = r'^\d\d(-?)\d\d\1\d\d\1\d\d$'#Backreference to a capturing group that match nothing is different from backreference to a capturing group that did not participate in the match at all.
##$Regex_Pattern = '/^\d\d(?|(:)|(\.)|(\-)|(\-{3}))\d\d\1\d\d\1\d\d$/'; //A branch reset group consists of alternations and capturing groups. (?|(regex1)|(regex2))##Only woks for php,delphi,r,perl
#$Regex_Pattern = '/^(\2tic|(tac))+$/'; //Do not delete '/'. Replace __________ with your regex.  forward ref ,doesnt work with py
Regex_Pattern = r'/o(?=oo)/';#The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. The lookahead is excluded from the match. It does not return matches of regex_2. The lookahead only asserts whether a match is possible or not.
Regex_Pattern = r'/(([\S])(?!\2))/'; #The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2. Lookahead is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not
Regex_Pattern = r"((?<=[13795])[0-9])" #The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
Regex_Pattern = r"(?<![aeiouAEIOU])." #The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.

Regex_Pattern =r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])\w{8,}$"

regularExpression = r'(^[a-z])(.*(\1))?$'











match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)
