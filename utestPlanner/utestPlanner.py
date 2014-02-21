
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
    price = 0  # in USD
    duration = 0  # in working days

    def __init__(self):
        print "Adding task"

    def get_price(self):
        print "My price is:", self.price

    def get_duration(self):
        return self.duration


####
class UsabilityTest(Task):
    def __init__(self, include_training=False, user_groups=[], locations=[], prepare_memo = False, report_format = "PPT", submit_to_IRB=False, submit_to_FDA=False, recruit_extra = True, conduct_pilot = False):
        self.include_training = include_training
        self.user_groups = user_groups
        self.locations = locations
        self.prepare_memo = prepare_memo
        self.report_format = report_format
        self.submit_to_IRB = submit_to_IRB
        self.submit_to_FDA = submit_to_FDA
        self.recruit_extra = recruit_extra
        self.conduct_pilot = conduct_pilot

    def calculate_expenses(self):
        self.expenses = 0

    def calculate_labor(self):
        self.labor_price = 0

    def add_user_group(self, user_group):
        self.user_groups.append(user_group)

####
class FormativeUsabilityTest(UsabilityTest):
    def what_am_I(self):
        print "Adding formative usability test"

class UserGroup:
    def __init__(self, name, session_duration, num_participants, compensation, recruiting_rate):
        self.name = name
        self.num_participants = num_participants
        self.compensation = compensation  # in usd
        self.recruiting_rate = recruiting_rate  # in usd
        self.session_duration = session_duration  # in minutes
        print "Added user group"

class Location:
    def __init__(self, city, state="MA", country="US", type="usability lab", price_per_day=500):
        self.city = city
        self.country = country
        self.state = state
        self.type = type
        self.price_per_day = price_per_day
    def __repr__(self):
        return "LocationObj: " + " ".join([self.city, self.country, self.type, str(self.price_per_day)])

usabilityTest = FormativeUsabilityTest()

concordLab = Location("Concord")
schlesinger = Location("Boston", type="market research facility", price_per_day=1500)

labs = [ ]

labs.append(concordLab)
labs.append(schlesinger)

print labs

for lab in labs:
    print lab

usabilityTest.get_price()