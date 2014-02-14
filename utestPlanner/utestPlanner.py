__author__ = 'Jonathan'

import requests

#nothing to say here


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
    price = 0 # in USD
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
        return self.price

    def getDuration(self):
        return self.duration

####
class UsabilityTest(Task):
    includeTraining = False
    userGroups = []
    def __init__(self):
        print "Adding usability test"

    def addUserGroup(self, userGroup):
        self.userGroups.append(userGroup)

####
class FormativeUsabilityTest(UsabilityTest):
    def __init__(self):
        print "Adding formative usability test"

class UserGroup:
    def __init__(self, name, sessionDuration, numParticipants, compensation, recruitingRate):
        self.name = name
        self.numParticipants = numParticipants
        self.compensation = compensation #in usd
        self.recruitingRate = recruitingRate #in usd
        self.sessionDuration = sessionDuration # in minutes
        print "Added user group"


usabilityTest = FormativeUsabilityTest()

usabilityTest.getPrice()