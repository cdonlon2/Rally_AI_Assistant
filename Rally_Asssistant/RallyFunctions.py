from pyral import Rally, rallyWorkset, RallyRESTAPIError
from datetime import datetime, timedelta 

#This function lists all default colours available in Rally. Other colours can be added here if users request it.
def get_default_colours():
    colours = {
        "Blue":"#21a2e0",
        "Dark Blue":"#105cab",
        "Green":"#107c1e",
        "Purple":"#4a1d7e",
        "Pink":"#df1a7b",
        "Burnt Orange":"#ee6c19",
        "Orange":"#f9a814",
        "Yellow":"#fce205",
        "Grey":"#848689"
    }
    return colours

#Get all features currently in a project. Return a dictionary with a Key feature_id: Name, State
def get_features(projectName):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project=projectName)
    except Exception as e:  
        print(f"An error occurred: {e}")

    #Define the query to get all Features (Portfolio Items of type 'Feature')  
    query_criteria = 'PortfolioItemType.Name = "Feature"'  
    response = rally.get('PortfolioItem', fetch="FormattedID,Name,State,ObjectID", query=query_criteria, project=projectName)  
    
    #Create the features dictionary
    features = {} 

    # Process and print the results  
    for feature in response:  
        feature_id = feature.FormattedID  
        feature_name = feature.Name  
        feature_state = feature.State.Name   
        features[feature_id] = {  
            'Name': feature_name,  
            'State': feature_state,
            'ObjectID':feature.ObjectID,
        }
        print(f"ID: {feature_id}, Name: {feature_name}, State: {feature_state}, ObjectID: {feature.ObjectID}")
    return features

#Used to find the colours associated with stories in the project
def get_user_stories_with_colors(projectName):       
    # Initialize your Rally instance  
    RALLY_SERVER = 'rally1.rallydev.com'  
    API_KEY = '_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U'  # Replace with your API key  
    PROJECT = projectName 
    
    # Connect to Rally  
    rally = Rally(server=RALLY_SERVER, apikey=API_KEY, project=PROJECT)  
    
    # Define the query to get user stories  
    query_criteria = 'Project.Name = "{}"'.format(PROJECT)  
    response = rally.get('UserStory', fetch="Name,DisplayColor", query=query_criteria)  
    
    # Extract and print the user story names and display colors  
    for story in response:  
        print(f"User Story Name: {story.Name}, Display Color: {story.DisplayColor}")  

#Create a user story in a given project. User supplies the new user story name, description, acceptance criteria, feature(default to null) and colour (default blue)
def create_user_story(title, description, acceptance_criteria, project_name, feature=None, colour="#21a2e0"):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project='Rally AI Assistant')  
  
        
        # Create user story data
        # Note the Portfolio item is the feature ObjectID(EG 813146813405) and not the formatted id (EG F38435) and is a string
        user_story_data = {  
            "Name": title,  
            "DisplayColor": colour,  
            "Description": description,  
            "Notes": acceptance_criteria,
            'PortfolioItem': feature,
        }  
  
        # Create user story in Rally  
        response = rally.create('HierarchicalRequirement', user_story_data)  
  
        # Check for errors  
        if hasattr(response, 'errors') and response.errors:  
            print("Errors encountered while creating user story:")  
            for error in response.errors:  
                print(error)  
        elif hasattr(response, 'Object'):  
            print(f"User story '{title}' created successfully with ObjectID: {response.Object.ObjectID}")  
        else:  
            print("Unexpected response format received from Rally API.")  
  
    except RallyRESTAPIError as e:  
        print(f"Rally REST API Error: {e}")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  


#get_features('Rally AI Assistant')
create_user_story('Test', 'TEST2', 'TEST 3', 'Rally AI Assistant', '813146813405', '#107c1e')