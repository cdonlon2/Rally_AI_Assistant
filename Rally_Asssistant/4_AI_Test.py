import os  
import json
from dotenv import load_dotenv  
from langchain_openai import AzureChatOpenAI  
from openai import AzureOpenAI  
from test_rally import create_user_story  
  
load_dotenv()  
#with open('Roles_examples.json', 'r') as file:  
#    roles_data = json.load(file)

clientAzOpenAiEmb = AzureOpenAI(  
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),  
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")  
)  
  
def query_ai(prompt, role):  
    az_chat = AzureChatOpenAI(  
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),  
        openai_api_version=os.getenv("OPENAI_API_VERSION"),  
        temperature=0.7,  
        max_tokens=None,  
        timeout=None,  
        max_retries=2,  
    )  
    messages = [
    ("system", "You are a Scrum Master creating user stories based on the prompts from a product owner. Create a title that summerises the prompt in no more than 20 words. Create a Description in the form 'As a [role], I want to [Identified problem], So that [Identified reason for creating the user story]'. Return a list of acceptance criteria that make sense for the provided information"),
    ("human", "I want to create a log in screen for my users to access the site. It should take a user name and password. A link to create a new account should be included as a button. It should only allow 3 failed attempts. It should have 2 text boxes."),
    ("assistant", "Title: 'Create a login screen' Description: 'As a user, I want to sign into my account with a user ID and password, so I can view my account securely.' Acceptance Criteria: 1. Create a login screen with 2 text boxes, one for User ID and one for Password. 2. If the incorrect password is submitted 3 times, lock the account. 3. A button is available to sign up to the application. 4. A link for forgotten passwords is availabe. 5. The login screen is tested and passes before deployment"),
    ("human", prompt)
    ]
      
    response = az_chat.invoke(messages).content  
    return response.strip()  
  
def user_story_generator(prompt):   
  
        # Instance 1: Summarize the prompt  
        ai_summary_prompt = f"Summarize the following prompt:\n\n{prompt}"  
        AI_Summary = query_ai(ai_summary_prompt, "summarizer")  
        #print(f"AI_Summary: {AI_Summary}")  
  
        # Instance 2: Create a single sentence summary  
        ai_title_prompt = f"Create a single sentence no more than 20 words long that summarizes the following text:\n\n{AI_Summary}"  
        AI_Title = query_ai(ai_title_prompt, "title generator")  
        #print(f"AI_Title: {AI_Title}")  
  
        # Instance 3: Create a Gherkin format story  
        ai_story_prompt = f"Create a Gherkin format story from the following text:\n\n{AI_Summary}"  
        AI_Story = query_ai(ai_story_prompt, "gherkin story creator")  
        #print(f"AI_Story: {AI_Story}")  
  
        # Instance 4: Create a bullet point list of actionable items  
        ai_acceptance_prompt = f"Create a bullet point list of actionable items from the following text:\n\n{AI_Summary}"  
        AI_Acceptance = query_ai(ai_acceptance_prompt, "acceptance criteria generator")  
        #print(f"AI_Acceptance: {AI_Acceptance}")  
  
        # Create user story in the system  
        #create_user_story(AI_Title, AI_Story, AI_Acceptance, "U2 Commercial Analytic Engineering New Implementations")  
        user_story_components = {
            "title":AI_Title,
            "description":AI_Story,
            "acceptanceCriteria":AI_Acceptance
        }
        return user_story_components
  
# Main function to execute the workflow  
def main():  
    user_story_generator("I want to create a ham sandwich with cheese. If there are tomatoes about then I'll add some Mayo too")  
  
if __name__ == "__main__":  
    main()  
