from twilio.rest import TwilioRestClient
"""
  Configure:
	account_sid = Your Twillo Account SID
	auth_token = Your Twillo Auth Token
	toNumber = A default number to call
	fromNumber = Your Twillo number
	xmlPath = Public readable path to your xml. Dropbox will work for this.
	
	Change URL to wav file in xml file
"""
account_sid = "12345"
auth_token = "12345"

timesToCall = 1
toNumber = "+8765309"
fromNumber = "+8675309"
xmlPath = "https://PATHTO/PlayRecording.xml"

print("Enter number to call <Default=", toNumber, ">: ", end="")
toNumber = input() or toNumber

print()

print("Enter number of times to call <Default=", timesToCall, ">: ", end="")
timesToCall = int(input() or timesToCall)

print()

print("Will call number", toNumber, timesToCall, "times.")
print("Proceed? (y/n): ", end="")

answer = input()

if answer == "y":

	client = TwilioRestClient(account_sid, auth_token)

	for count in range(timesToCall):
		call = client.calls.create(to= toNumber,
									from_= fromNumber,
									url= xmlPath)
		print("Building call: #", count + 1, end="\r")
	print("Call building: COMPLETE")

else:
	print("Exiting")

input("Press enter to close window...")
