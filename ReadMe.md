# Tester Bot
## This Bot mainly serves as a "google" search Bot.
## Commands:
- '.Hello' : A simple greeting nothing much
- '.Time' : Shows the current time when you ran this command
- '.Delete {1,2,..}' : Delete Text that was sent before
- '.Coinflip {heads/tails}' : A simple game with a 50/50 odds of winning
- '.Morning' : Basically does nothing
- '.Google [What you're looking for]' : Perfoms a google search and get the top result 

# In order to use this code you'll need the following:
-Python 3.6+
-discord.py Library
-Google API Key
-Custom Search Engine ID
-Your Bot's Token

# Installation
Install the required Python libraries:
#  ``` bash
   ("p1p install discord.py pytz asyncio requests")

# After Installing 
1.Go To : https://discord.com/developers/applications
2.Create New Application,Enter Your Desired Bot's Name
3.Go To oAuth2 -> general -> Click Default Authorization Link -> Press In-app Authorization Then Choose Bot(You can give the bot any permission)
4.Now Go To Bot Under oAuth2 Then You Want To Allow Everything Except "REQUIRES OAUTH2 CODE GRANT"(Optional)
5.Still At Bot,What You Want To Find Is The Token Next to the Bot.png -> Reset The token and copy the new one(Hold onto the token)
6.Back to oAuth2 Again(Make Sure you Saved The Changes) -> Pick URL Generator -> Pick Bot In the Box Then Copy the Url And paste it in Your browser
7.Now what it does is basically Invites the Bot Into Your server

# Now for the Google API Key
1.Go To : https://console.cloud.google.com/
2.Click on the project drop-down and create a new project (or select an existing project)
3.In the Cloud Console, navigate to the "APIs & Services" > "Library" section
4.Search for "Custom Search JSON API" and enable it
5.In the Cloud Console, navigate to the "APIs & Services" > "Credentials" section
6.Click the "Create credentials" dropdown and select "API key"
7.n the "API key created" notification, you will see your API key
8.Copy the API key and save it securely
9.Open your bot's code.
10.Locate the part of the code where you set GOOGLE_API_KEY
11.Replace YOUR_API_KEY_HERE with the API key you obtained

# Now for The Custom Search Engine ID
1.Go to the Google Custom Search page
2.Click the "Add" button to create a new Custom Search Engine
3.Provide a name for your search engine, e.g., "Discord Bot Search."
4.Under "Sites to Search," select "Search the entire web but emphasize included sites."
5.In the "Sites to Search" section, specify the websites you want your bot to search(Or you can allow everything)
6.Click the "Create" button to create your custom search engine
7.After creating the search engine, you'll be taken to the "Setup" tab
8.Scroll down to the "Details" section, and you will find your "Search engine ID."
9.Open your bot's code
10.Locate the part of the code where you set SEARCH_ENGINE_ID
11.Replace YOUR_SEARCH_ENGINE_ID_HERE with the Search Engine ID you obtained

# Token Bot
1.Since you Have the Bot's token,all you need to do is
"client.run('Key Goes here')"

Under all of the main code
Make sure to use replit since you can run the code without any configuration(If there is,The AI can help)
