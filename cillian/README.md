To run, add .env file to root folder with the following configuration:
```
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://YOUR_ENDPOINT_openai.openai.azure.com"
OPENAI_API_VERSION="2024-02-01"
OPENAI_API_DEPLOYMENT_NAME="gpt4o-intellimap" //adjust to your model deployment.
OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME="text-embedding-3-large-itellimap" //adjust to your model deployment for embeddings
PDF_FOLDER_PATH="/Users/fbarjola/data/embeddings/pdfContents/"
```

## Running the code will load all pdfs documents in your PDF_FOLDER_PATH
```
Processing PDF: Prompt Engineering - Prompts and Responses.pdf
Embeddings stored in ChromaDB:  ['0_1', '0_2', '0_3', '0_4', '0_5', '0_6', '0_7', '0_8', '0_9', '0_10', '0_11', '0_12', '0_13', '0_14', '0_15', '0_16', '0_17', '0_18', '0_19', '0_20', '0_21', '0_22', '0_23', '0_24', '0_25', '0_26', '0_27', '0_28', '0_29', '0_30', '0_31', '0_32', '0_33', '0_34', '0_35', '0_36', '0_37', '0_38', '0_39', '0_40']
```

Splitting the PDF into chunks of 1000 characters, and saving the embeddgins in memory, chromaDB.

Then using the chat input through the console, you can query the documents, before the response of the model we are listing the most relevant embeddings that are included in the context window:

```
Please enter your query (or type 'exit' to quit): how long to wait after secure request is approved?
Documents by distance:
1.2608205080032349 - © 2020 Optum, Inc. All rights reserved.     4. Accept the terms and conditions statement and click t
1.4543647766113281 - not also have the authorizatio n to record the meeting.     The meeting organizer must have authoriz
1.4954837560653687 - recorded  or transcribed  if the meeting organizer  (person who scheduled the meeting)  is  not auth
1.5277198553085327 - © 2020 Optum, Inc. All rights reserved.     Introduction   When you are authorized to do so, any Tea
1.5731887817382812 - © 2020 Optum, Inc. All rights reserved.     Top FAQs     Question  Answer   How do I request Microso
1.666874647140503 - meet ing recording?  Teams meetings recordings are stored in MP4 format and play on  most computers 
1.6929906606674194 - © 2020 Optum, Inc. All rights reserved.            Table of Contents   Introduction  2  How to reque
1.694830060005188 - © 2020 Optum, Inc. All rights reserved.     Teams Meeting Recording   The recording happ ens in the 
1.706421136856079 - screen sharing activity of the meeting. It will display no more than fo ur  peoples' video streams a
1.7191170454025269 - and web apps from the meeting chat or the Teams  Calendar entry for the meeting.   • Note: People wh
-----------------------------
Response from AI + PDF Context:
You should wait a minimum of 48 hours to ensure that the recording capability has been added to your Microsoft Teams meeting functionality.
```