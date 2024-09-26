'''
Sentence Smash
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
'''


teste = print(f'{words[0]} {words[1]} {words[2]} {words[3]} {words[4]} ')
def mash(words):
    # string = ''

    # for word in words:
    #     string += word + " "

    # return string.strip()

    return " ".join(words)

