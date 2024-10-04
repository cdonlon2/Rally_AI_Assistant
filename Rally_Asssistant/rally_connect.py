import os  
from dotenv import load_dotenv
from pyral import Rally, rallyWorkset  

# Replace with your Rally API key  
API_KEY=os.getenv("RALLY_API_KEY"),

# Rally server and workspace details  
RALLY_SERVER = "rally1.rallydev.com"  
WORKSPACE = "OPTUM"  # Replace with your workspace name if known  

# Initialize Rally object  
rally = Rally(server=RALLY_SERVER, apikey=API_KEY, workspace=WORKSPACE)  

# Query for projects  
response = rally.get('Project', fetch=True)  

# Check for errors  
if response.errors:  
    print("Errors encountered:")  
    for error in response.errors:  
        print(error)  
else:  
    # Print project details  
    for project in response:  
        print(f"Project Name: {project.Name}, Project ID: {project.ObjectID}")  