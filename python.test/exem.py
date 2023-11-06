# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'
word1="Python"
word2="is"
word3="a"
word4="powerful"
word5="language"
print(f"{word1} {word2} {word3} {word4} {word5}")
# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."
theme="strings in Python"


# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."
sentence = "Learning about \"Python\" strings is fun."
print(sentence)

# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.
sentence = "Learning about \"Python\" strings is fun."
print(len(sentence))
print(sentence.count('s'))

# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.
upper_topic = 'strings in Python'
print(upper_topic.upper())
lower_topic = 'strings in Python'
print(lower_topic.lower())
# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."
topic = 'Python'
print("Let's learn about {}.".format(topic))

# Substring Extraction:
# Extract and print the word 'Python' from the topic string.
topic = "strings in Python."
print(topic)
print(topic[11:17])



## Bonus problems


# Substring Search:
# Check if the topic string contains the word 'Python' using the in keyword.
sentence = "Learning about \"Python\" strings is fun."
print("Python" in sentence)


# String Replacement:
# Replace the word 'Python' in the topic string with 'programming' and print the modified string.

# String Splitting:
# Split the string 'Python,Java,C++,Ruby' into a list of programming languages using a comma as the separator.
it_language="Python","Java","C++","Ruby"
print(it_language)
# Character at Index:
# Find and print the character at index 4 in the topic string.
it_language="Python","Java","C++","Ruby"
print(it_language[3])
