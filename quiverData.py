import requests



url = "https://api.quiverquant.com/beta/historical/senatetrading/NVDA"
headers = {'accept': 'application/json',
'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
'Authorization': 'c4d32ba06a03af7a421e69c4c3a6e9656f6fdd65'}
r = requests.get(url, headers=headers)
print(r.content)


# #Connect to the API using your token
# #Replace <TOKEN> with your token
# quiver = quiverquant.quiver(secrets/TOKEN)

# #Get data on WallStreetBets discussion
# #dfWSB = quiver.wallstreetbets()

# #Get recent trades by members of U.S. Congress
# #dfCongress = quiver.congress_trading()

# #Get trades of a Tesla by members of congress
# dfCongress_Tesla = quiver.congress_trading("TSLA")

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
# dfWiki_Microsoft = quiver.wikipedia("MSFT")