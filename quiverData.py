import requests, json, pandas as pd
from secrets import TOKEN

url = "https://api.quiverquant.com/beta/live/congresstrading"
headers = {'accept': 'application/json',
'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
'Authorization': 'Token '+ TOKEN}
r = requests.get(url, headers=headers)
jsData = json.loads(r.content)
df = pd.DataFrame(jsData)
df["ReportDate"] = pd.to_datetime(df["ReportDate"])
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
df.to_csv('data.csv')
print(df)

# import quiverquant
# #Connect to the API using your token
# #Replace <TOKEN> with your token
# quiver = quiverquant.quiver(TOKEN)

# #Get data on WallStreetBets discussion
# dfWSB = quiver.wallstreetbets()

# #Get recent trades by members of U.S. Congress
# dfCongress = quiver.congress_trading()

# #Get trades of a Tesla by members of congress
# #dfCongress_Tesla = quiver.congress_trading("TSLA")

# #Get trades made by U.S. Senator Richard Burr
# #dfCongress_Burr = quiver.congress_trading("Richard Burr", politician=True)

# #Get data on WallStreetBets discussion of Virgin Galactic
# #dfWSB_Virgin = quiver.wallstreetbets("SPCE")

# #Get recent corporate lobbying
# #dfLobbying = quiver.lobbying()

# #Get corporate lobbying by Apple
# #dfLobbying_Apple = quiver.lobbying("AAPL")

# #Get data on government contracts
# #dfContracts = quiver.gov_contracts()

# #Get data on government contracts to Lockheed Martin
# #dfContracts_Lockheed = quiver.gov_contracts("LMT")

# #Get data on Wikipedia page views
# #dfWiki = quiver.wikipedia()

# #Get data on Wikipedia page views of Microsoft
# #dfWiki_Microsoft = quiver.wikipedia("MSFT")
# print(dfWSB)