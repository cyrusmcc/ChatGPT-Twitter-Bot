import random

# Add your own topics
topics = [
    "ChatGPT",
]

# Add your own prompt propositions
prompt_start = [
    "telling me about",
]

# Add your own wildcards
wildcard = [
    "using a mention to a popular person in the field",
]

# Add your own tweet attributes
attributes = [
    "using a popular relevant hashtag",
]

# Add your own constraints
constraints = [
    "in less than 280 characters",
]

def get_random_prompt():
    prompt = "give me a tweet " + random.choice(prompt_start) + " " + random.choice(
        topics) + " " + random.choice(attributes) + " " + random.choice(wildcard) + " " + constraints[0]
    
    prompt = prompt.replace('"', '')
    return prompt
