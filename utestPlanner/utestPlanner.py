
import requests

# TODO: Add user types to code
# TODO: Allow for tentative cities in a particular country or region
# TODO:

def convertCurrency(amount, toCurrency):
    try:
        fromCurrency = "USD"
        toCurrency = toCurrency
        amount = amount

        url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (fromCurrency, toCurrency)

        request = requests.get(url)
        conversionRate = request.json()['v']
        convertedAmount = amount * conversionRate

        return convertedAmount

    except Exception as error:
        print "can't convert currency"
        return "XXX"



class Project:
    price = 150 # in USD
    tasks = [] #all project tasks
    duration = 0 #total project duration

    def __init__(self):
        print "Adding project"

####
class Task:
    price = 0 #in USD
    duration = 0 #in working days
    def __init__(self):
        print "Adding task"

    def getPrice(self):
        print "My price is:", self.price

    def getDuration(self):
        return self.duration

####
class UsabilityTest(Task):
    def __init__(self, includeTraining=False, userGroups=[], locations=[], prepareMemo = False, reportFormat = "PPT", submitToIRB=False, submitToFDA=False, recruitExtra = True, conductPilot = False):
        self.includeTraining = includeTraining
        self.userGroups = userGroups
        self.locations = locations
        self.prepareMemo = prepareMemo
        self.reportFormat = reportFormat
        self.submitToIRB = submitToIRB
        self.submitToFDA = submitToFDA
        self.recruitExtra = recruitExtra
        self.conductPilot = conductPilot


    def addUserGroup(self, userGroup):
        self.userGroups.append(userGroup)

####
class FormativeUsabilityTest(UsabilityTest):
    def whatAmI(self):
        print "Adding formative usability test"

class UserGroup:
    def __init__(self, name, sessionDuration, numParticipants, compensation, recruitingRate):
        self.name = name
        self.numParticipants = numParticipants
        self.compensation = compensation #in usd
        self.recruitingRate = recruitingRate #in usd
        self.sessionDuration = sessionDuration # in minutes
        print "Added user group"

class Location:
    def __init__(self,city, state="MA", country="US", type="usability lab", pricePerDay=500):
        self.city = city
        self.country = country
        self.state = state
        self.type = type
        self.pricePerDay = pricePerDay
    def __repr__(self):
        return "LocationObj: " + " ".join([self.city, self.country, self.type, str(self.pricePerDay)])

usabilityTest = FormativeUsabilityTest()

concordLab = Location("Concord")
schlesinger = Location("Boston", type="market research facility", pricePerDay=1500)

labs = []

labs.append(concordLab)
labs.append(schlesinger)

print labs

for lab in labs:
    print lab

usabilityTest.getPrice()