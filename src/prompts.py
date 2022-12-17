import random
import json

def get_random_prompt():
    # load prompts from json file
    promptJSON = open('prompts.json', 'r')
    promptData = json.load(promptJSON)
    promptJSON.close()

    # assemble prompt
    promptTemplate = random.choice(promptData['prompts'])
    promptTopic = random.choice(promptData['topics'])
    
    promptAttributes = ', '.join([x + '' for x in promptData['attributes']]) + '.'
    promptAttributes = promptAttributes.capitalize()
    
    promptConstraints = ', '.join([x + '' for x in promptData['constraints']]) + '.'
    promptConstraints = promptConstraints.capitalize()

    promptWildcard = random.choice(promptData['wildcards'])
    
    prompt = promptTemplate.replace('{topic}', promptTopic) 
    prompt += ' ' + promptAttributes + ' ' + promptWildcard + '. ' + promptConstraints
    prompt = prompt.replace('"', '')
    return prompt
