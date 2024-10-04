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
 
# Function to query ChromaDB using Azure OpenAI  
def query_ai(query): 
    az_chat = AzureChatOpenAI(
        azure_deployment=os.getenv("OPENAI_API_DEPLOYMENT_NAME"),
        openai_api_version=os.getenv("OPENAI_API_VERSION"),
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    messages = [
        ("system", "You are a Scrum Master creating user stories based on the prompts from a product owner. Create a title that summerises the prompt in no more than 20 words. Return the responses in the form 'As a [role], I want to [Identified problem], So that [Identified reason for creating the user story]'. Return a list of acceptance criteria that make sense for the provided information"),
        ("human", "I want to create a log in screen for my users to access the site. It should take a user name and password. A link to create a new account should be included as a button. It should only allow 3 failed attempts. It should have 2 text boxes."),
        ("assistant", "Title: 'Create a login screen' Description: 'As a user, I want to sign into my account with a user ID and password, so I can view my account securely. Acceptance Criteria: 1. Create a login screen with 2 text boxes, one for User ID and one for Password. 2. If the incorrect password is submitted 3 times, lock the account. 3. A button is available to sign up to the application. 4. A link for forgotten passwords is availabe. 5. The login screen is tested and passes before deployment"),
        ("human", query)
    ]
    message_from_ai = az_chat.invoke(messages).content
    return message_from_ai  


def start_chat():
    while True:  
        # Get the query from the user input  
        query = input("Please enter your query (or type 'exit' to quit): ")  
        if query.lower() == 'exit':  
            print("Exiting the program.")  
            break  
        response = query_ai(query)  
        # Print the response  
        print("-----------------------------")  
        print("Response from AI Scrum Master:")  
        print(response)  

# Main function to execute the workflow  
def main():  
    #start user chat
    start_chat()   
  
if __name__ == "__main__":  
    main()  
