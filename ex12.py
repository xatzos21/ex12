## String Regex 1

## Python Regex

# In this exercise, we will focus on the use and manipulation of text  in Python, including:

# - Using the Python regex
# - Creating custom regex patterns

## Tasks

### Task 1

#Create a variable called `text` to store the data:
#  `Berlin is a world city of culture, politics, media and science.` .
#  Then search for the first white space character in the string
#  and print its location using the appropriate label. 

import re

text = "Berlin is a world city of culture, politics, media and science."

pattern = "\s"
x = re.search(pattern,text)
print(x)


### Task 2

#Create a variable called `text` to store the data: 
# `Berlin is surrounded by the State of Brandenburg and 
# contiguous with Potsdam, Brandenburg's capital.` . 
# Then search for the word `Frankfurt` in the string . 

text1 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
pattern1 = "[Frankfurt]"
y = re.search(pattern1, text1)
print(y)


### Task 3

#Create a variable called `text` to store the data: 
# `Berlin is a city of culture.` . Replace the spaces with a hyphen.

text2 = "Berlin is a city of culture."
pattern2 = r"\s"
z = re.sub(pattern2,"-",text2 )
print(z)


### Task 4

#Create a variable called `text` to store the data: 
#`Berlin is a city of culture.` . Search if the phrase `in` appears 
# inside the string. Print the output of the regex function.

text3 = "Berlin is a city of culture."
pattern3 = "[in]"
a = re.match(pattern3, text3)
print(a)