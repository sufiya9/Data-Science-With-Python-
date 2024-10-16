from data import story

print(f"total chars in the story : {len(story)}")

word= story.split()
print(f"total word in the story : {len(word)}")

print(f"total unique words in the story: {len(set(word))}")
print(word)

sentences=story.split('.')
print(f"total sentences in the story: {len(sentences)}")
print(sentences)

lines=story.split('\n')
print(f"total lines in the story: {len(lines)}")
print(lines)

poem_list=[
    'Twinkle, Twinkle, little star,',
    'How I wonder what you are!',
    'Up above the world so high,',
    'Like a dimond in the sky.'
]

poem="\n".join(poem_list)
print(poem)
