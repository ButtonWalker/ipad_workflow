# import dependacies
import random

# Set the code variables or responses

messages = ['Its is certain', 
           'It is decidedly so',
           'Yes For sure',
           'Reply with haze',
           'ask again later',
           'Please concentrate',
           'My reply is no',
           'Outlook isnt great',
           'Hell Nawl']
           
# Print the magic 8 balls responses

print(messages[random.randint(0, len(messages) -1)])