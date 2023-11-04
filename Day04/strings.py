from termcolor import colored

string1 = 'Python is fun!'
string2 = 'Hello world!'
string3 = 'hello world!'
string4 = 'henlo wurld!'

#length of string:
print('string1 has', colored(string1.__len__(), 'yellow', attrs=['bold']),
      'characters.')

#only print the first word
print('Only print the first word:',
      colored(string1[0:6], 'blue', attrs=['bold'])
      )

#count letters in the whole string
print('Count the number of \'p\' in string1:',
      colored(string1.count('p'),
              'red', attrs=['bold']), '\t',
      colored('Oh no! it\'s case sensitive!', 'red', attrs=['bold'])
      )

print('Let\'s just transform the whole string to lower case to count all '
      'occurring \'p\':',
      colored(string1.lower().count('p'), 'green', attrs=['bold'])
      )

print('This also works with upper case! Count all occurring \'T\':',
      colored(string1.upper().count('T'), 'green', attrs=['bold'])
      )

#replace words in the string
print('Replace the first word with a different one:',
      string1.replace('Python', 'Java')
      )

#replace words and insert a new one at a specific spot in the string
print('''
That is not a true statement! We should probably add the \'not\' 
into string1! It has to be added in at index:''',
      colored(string1.index('fun'), 'cyan', attrs=['underline']),
      '\n' +
      string1[:string1.index('fun')].replace('Python', 'Java')
      + 'not', string1[string1.index('fun'):]
      )

print()

#some more string methods:
print(string2, string3.center(60), string4.rjust(60), sep='\n')

#compare
print(string2 == string3)

print(string2.casefold() == string3)

print(string4.title())