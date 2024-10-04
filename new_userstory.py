import os  
from dotenv import load_dotenv
from pyral import Rally, rallyWorkset  
from pyral.context import RallyRESTAPIError  

# Replace with your Rally API key  
API_KEY=os.getenv("RALLY_API_KEY"),

# Rally server and workspace details  
RALLY_SERVER = "rally1.rallydev.com"  
WORKSPACE = "Optum"  # Replace with your workspace name if known  

# Initialize Rally object  



def create_user_story(title, description, acceptance_criteria, project_name):  
    try:  
        # Initialize Rally object  
        rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum', project=project_name)

        # Create user story data  
        user_story_data = {  
            "Name": title,  
            "DisplayColor": "#4a1d7e",
            "Description": description,  
            "Notes": acceptance_criteria,  
            "Project": project_name  
        }  
  
        # Create user story in Rally  
        response = rally.create('HierarchicalRequirement', user_story_data)  
  
        # Check for errors  
        if response.errors:  
            print("Errors encountered while creating user story:")  
            for error in response.errors:  
                print(error)  
        else:  
            print(f"User story '{title}' created successfully with ObjectID: {response.ObjectID}")  
  
    except RallyRESTAPIError as e:  
        print(f"Rally REST API Error: {e}")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}") 


title = "Add In_date column to Client_A database"  
description = "As a database administrator, I want to add a new column called In_date to the Client_A database, so that we can store the date and time of certain events."  
acceptance_criteria = "1. The new column should be named In_date.  2. The In_date column should be of DATETIME type.  3. The In_date column should be added to the appropriate table within the Client_A database.  4. The In_date column should accept NULL values initially.  5. The changes should be documented and communicated to relevant team members.  6. Ensure that the database schema update is tested in a staging environment before applying it to production."
project_name = "U2 Commercial Analytic  Engineering New Implementations"

create_user_story(title, description, acceptance_criteria, project_name)
