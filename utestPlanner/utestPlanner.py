
import requests

# TODO: Add user types to code
# TODO: Allow for tentative cities in a particular country or region


def convert_currency(amount, to_currency):
    try:
        from_currency = "USD"
        to_currency = to_currency
        amount = amount

        url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (from_currency, to_currency)

        request = requests.get(url)
        conversion_rate = request.json()['v']
        converted_amount = amount * conversion_rate

        return converted_amount

    except Exception as error:
        print "can't convert currency"
        return "XXX"


class Project:
    price = 150  # in USD
    tasks = []  # all project tasks
    duration = 0  # total project duration

    def __init__(self):
        print "Adding project"


####
class Task:
    price = 0 # in USD
    duration = 0 # in working days

    def __init__(self):
        print "Adding task"

    def get_price(self):
        print "My price is:", self.price

    def get_duration(self):
        return self.duration


####
class UsabilityTest(Task):
    def __init__(self, include_training=False, user_groups=[], locations=[], prepare_memo = False, report_format = "PPT", submit_to_IRB=False, submit_to_FDA=False, recruitExtra = True, conductPilot = False):
        self.includeTraining = include_training
        self.userGroups = user_groups
        self.locations = locations
        self.prepareMemo = prepare_memo
        self.reportFormat = report_format
        self.submitToIRB = submit_to_IRB
        self.submitToFDA = submit_to_FDA
        self.recruitExtra = recruitExtra
        self.conductPilot = conductPilot

    def calculateExpenses(self):
        self.expenses = 0
        pass

    def calculateLabor(self):
        self.laborPrice = 0
        pass


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

usabilityTest.get_price()