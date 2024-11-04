#A quick tool to create 10 Sprints for which ever team project you point to. Set the Sprint number to the latest sprint number is.

from pyral import Rally, rallyWorkset, RallyRESTAPIError
from datetime import datetime, timedelta  
  
def create_iteration(project_name, new_iteration_name):  
    # Initialize Rally connection  
    rally = Rally(server="rally1.rallydev.com", apikey="_oQYm9R1VSkCWO3p6ecD2VeDAs6Jf3UG5ifrDABpwm8U", workspace='Optum',  project=project_name)  
      
    # Fetch the latest iteration based on the EndDate  
    response = rally.get('Iteration', fetch="EndDate", order="EndDate desc", limit=1)  
      
    latest_iteration = None  
    for iteration in response:  
        latest_iteration = iteration  
        break  
      
    if not latest_iteration:  
        raise ValueError("No iterations found.")  
      
    lastDate = latest_iteration.EndDate  
  
    # Convert the lastDate to a datetime object and calculate the new start and end dates  
    last_date_dt = datetime.strptime(lastDate, '%Y-%m-%dT%H:%M:%S.%fZ')  
    new_start_date = last_date_dt + timedelta(days=0)  
    new_end_date = new_start_date + timedelta(days=14)  # 14 days including the start date  
      
    # Convert the new dates to the appropriate string format  
    new_start_date_str = new_start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3] + 'Z'  # Adjust microseconds precision  
    new_end_date_str = new_end_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3] + 'Z'  
  
    # Fetch the project reference  
    project_ref = rally.getProject()  
  
    # Create the new iteration  
    iteration_fields = {  
        "Name": new_iteration_name,  
        "Project": project_ref.ref,  # Use the reference ID for the project  
        "StartDate": new_start_date_str,  
        "EndDate": new_end_date_str,  
        "State": "Planning"  
    }  
  
    try:  
        new_iteration = rally.create('Iteration', iteration_fields)  
        print(f"New iteration '{new_iteration_name}' created with start date {new_start_date_str} and end date {new_end_date_str}")  
    except Exception as e:  
        print(f"Failed to create iteration: {e}")   
  
# Example usage:  
sprint_number = 29
name = "Sprint "
#project = "Rally AI Assistant"
project = "U2 Commercial Analytic  Engineering New Implementations"
#project = "U2 Commercial Post Pay Client Implementation"
#project = "U2 Commercial Pre Pay Migration"

for i in range(1, 11):
    sprint_number += 1
    sprint = f"{name}{sprint_number}"
    create_iteration(project, sprint)
