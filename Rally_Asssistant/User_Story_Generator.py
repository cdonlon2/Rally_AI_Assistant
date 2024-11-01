import os  
from dotenv import load_dotenv  
from langchain_openai import AzureChatOpenAI  
from openai import AzureOpenAI

load_dotenv() 
clientAzOpenAiEmb = AzureOpenAI(  
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),  
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")  
) 

def get_acceptance(prompt):
    # Define few-shot learning examples  

    examples = """  
    Example 1:  
    Input: SW100 requires updates to the functionality that was previously implemented in US366514.  We need to support the user to get these changes successfully deployed in order to deploy SW100 to production.
    Output: The deployment package for SW100 includes all updates from US366514.
    The deployment process follows the standard deployment pipeline and guidelines.
    The deployment does not introduce any new critical or major defects into the production environment.
    The deployment process includes appropriate rollback mechanisms in case of failure.
    The deployment is documented with clear steps and instructions for end-users and administrators
    """  
  
    # Define the prompt for summarization with examples
    full_prompt = [
        {
            "role": "system",
            "content": "You are a helpful scrum master who is helping a product owner. You will take requiremetnts froim a product owner and write acceptance criteria points. They should be clear points, be actionable, and not include the solution. All you are required to write is the acceptance critera points, not the title or story summary."
        },
        {
            "role": "user",
            "content": f"{examples}\nInput: {prompt}\nOutput:"
        }
    ]
  
    # Parameters for the API call  
    response = AzureChatOpenAI(  
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),  
        openai_api_version=os.getenv("OPENAI_API_VERSION"),  
        temperature=0.7,  
        max_tokens=None,  
        timeout=None,  
        max_retries=2,  
    )  
  
    # Extract the summary from the response  
    acceptance = response.invoke(full_prompt).content  

    return acceptance

def get_description_classic(prompt):
    # Define few-shot learning examples  

    examples = """  
    Example 1:  
    Input: SW100 requires updates to the functionality that was previously implemented in US366514.  We need to support the user to get these changes successfully deployed in order to deploy SW100 to production.
    Output: As an end user, I need SW100 updated with the latest functionality, so that I can deploy it to production\n The team needs to provide support to the user to implement the changes to SW100 that were implemented in US36651. Once implemented we need to provide support in deploying the updated SW100 to production environment.
    """  
  
    # Define the prompt for summarization with examples
    full_prompt = [
        {
            "role": "system",
            "content": "You are a helpful scrum master who is helping a product owner. You will take som requirements from the product owner and create a user story in the scrum style of As a [end user], I need [identify the requirement being asked], so that [identify the benefit of the requirement]. Follow that with a summary of the requirements being asked from the prompt"
        },
        {
            "role": "user",
            "content": f"{examples}\nInput: {prompt}\nOutput:"
        }
    ]
  
    # Parameters for the API call  
    response = AzureChatOpenAI(  
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),  
        openai_api_version=os.getenv("OPENAI_API_VERSION"),  
        temperature=0.7,  
        max_tokens=None,  
        timeout=None,  
        max_retries=2,  
    )  
  
    # Extract the summary from the response  
    description = response.invoke(full_prompt).content  

    return description  

def get_description_gherkin(prompt):
    # Define few-shot learning examples  

    examples = """  
    Example 1:  
    Input: SW100 requires updates to the functionality that was previously implemented in US366514.  We need to support the user to get these changes successfully deployed in order to deploy SW100 to production.
    Output: Feature: Update and Deploy SW100 functionality   
  
    As a user,  
    I want to update the functionality that was previously implemented in US366514,  
    So that I can successfully deploy SW100 to production.  
  
    Scenario: Successful update and deployment of SW100 functionality  
    Given the functionality from US366514 is already implemented,  
    When I apply the required updates to the functionality,  
    Then the updates should be validated and tested,  
    And I should be able to deploy SW100 to production successfully. 
    """  
  
    # Define the prompt for summarization with examples
    full_prompt = [
        {
            "role": "system",
            "content": "You are a scrum master who takes requirements from a product owner and writes a user story using Gherkin methodology." 
        },
        {
            "role": "user",
            "content": f"{examples}\nInput: {prompt}\nOutput:"
        }
    ]
  
    # Parameters for the API call  
    response = AzureChatOpenAI(  
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),  
        openai_api_version=os.getenv("OPENAI_API_VERSION"),  
        temperature=0.7,  
        max_tokens=None,  
        timeout=None,  
        max_retries=2,  
    )  
  
    # Extract the summary from the response  
    description = response.invoke(full_prompt).content  

    return description  

def get_title(prompt):  
  
    # Define few-shot learning examples  
    examples = """  
    Example 1:  
    Input: SW100 requires updates to the functionality that was previously implemented in US366514.  We need to support the user to get these changes successfully deployed in order to deploy SW100 to production.
    Title: Support SW100 updates and deployment to production
  
    Example 2:  
    Input: We need a new page in our wiki that explains the github repos and how the relate to each other. A link should be added to all the read-me.txt files in the repos to link to the new page.
    Title: Document github repos in wiki and add link to read-me files  
  
    Example 3:  
    Input: Add a new field `total_days` (int) to the `client_enriched` database table. Calculate `total_days` as the difference between `check_out` and `check_in` fields. Set `total_days` to null if `check_in` or `check_out` fields are empty.
    Title: Add new field total_days to client_enriched database table  
    """  
  
    # Define the prompt for summarization with examples
    fullPrompt = [
        {
            "role": "system",
            "content": "You are a helpful scrum master who is helping a product owner. You will take requirements from the product owner and create a user story title that will summarise the requirements in 20 words or less. Do not include Title: at the start of your reosponse"
        },
        {
            "role": "user",
            "content": f"{examples}\nInput: {prompt}\nTitle:"
        }
    ]
  
    # Parameters for the API call  
    response = AzureChatOpenAI(  
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),  
        openai_api_version=os.getenv("OPENAI_API_VERSION"),  
        temperature=0.7,  
        max_tokens=None,  
        timeout=None,  
        max_retries=2,  
    )  
  
    # Extract the summary from the response  
    title = response.invoke(fullPrompt).content  

    return title

def user_story_generator(prompt):   
    #Get story Title
    title = get_title(prompt)
    #Get story Description
    description = get_description_classic(prompt)
    #Get Acceptance Criteria
    acceptanceCriteria = get_acceptance(prompt)
    #Compile into Dictionary for use in AI
    user_story_components = {
        "title":title,
        "description":description,
        "acceptanceCriteria":acceptanceCriteria
    }
    return user_story_components

prompt = "The subscribed user needs a page to view their recurring billing cycle. Include the last paid date and amount, and the upcomming due date and amount owed. Display the payment method selected to the user. include a link to change the payment method"

story = user_story_generator(prompt)
for key, value in story.items():
    print("---------------------------------------")
    print(value) 