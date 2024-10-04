import os  
from dotenv import load_dotenv
from pyral import Rally

# Replace with your Rally API key  
API_KEY=os.getenv("RALLY_API_KEY"),

# Rally server and workspace details  
RALLY_SERVER = "rally1.rallydev.com"  
WORKSPACE = "Optum"  # Replace with your workspace name if known  

# Initialize Rally object  
rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum', project='U2 Commercial Analytic  Engineering New Implementations')

response = rally.get('UserStory', fetch=True, query='Iteration.Name = "Sprint 21"', projectScopeDown=True)

# Iterate over the user stories and print their FormattedIDs and names
for user_story in response:
    print(f"{user_story.FormattedID}: {user_story.Name}: {user_story.Description}: {user_story.AcceptanceCriteria}")
    print("*****")

response = rally.get('UserStory', fetch=True, querry='FormattedID = US418943')
story = response.next()
#Iterate over the fields associated with the story
for attr_name in dir(story):
    if not attr_name.startswith('_'):
        attr_value = getattr(story, attr_name)
        if not callable(attr_value):
            print(f"{attr_name}: {attr_value}")
            print("*****")
