from pyral import Rally, rallyWorkset, RallyRESTAPIError  

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

def get_features(projectName):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project='Rally AI Assistant')
    except Exception as e:  
        print(f"An error occurred: {e}")

    #Define the query to get all Features (Portfolio Items of type 'Feature')  
    query_criteria = 'PortfolioItemType.Name = "Feature"'  
    response = rally.get('PortfolioItem', fetch="FormattedID,Name,State", query=query_criteria, project=projectName)  
    
    # Process and print the results  
    for feature in response:  
        feature_id = feature.FormattedID  
        feature_name = feature.Name  
        feature_state = feature.State.Name   
        
        print(f"ID: {feature_id}, Name: {feature_name}, State: {feature_state}")   
  
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

def create_user_story(title, description, acceptance_criteria, project_name):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project='Rally AI Assistant')  
  
        
        # Create user story data  
        user_story_data = {  
            "Name": title,  
            "DisplayColor": "#4a1d7e",  
            "Description": description,  
            "Notes": acceptance_criteria,  
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
