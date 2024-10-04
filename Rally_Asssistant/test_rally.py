from pyral import Rally, rallyWorkset, RallyRESTAPIError  
  
def create_user_story(title, description, acceptance_criteria, project_name):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project='U2 Commercial Analytic  Engineering New Implementations')  
  
        
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