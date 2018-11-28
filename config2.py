# read from a db
# we will marge date from a database
class Config2:


    setup_switches = {
        'kitchen': 11,
        'livingroom': 13,
        'bedroom': 15,
        'lamp1': 17,
        'lamp2': 19
    }

    all_configuration={

        'shield': {
            'label': 'Notifications',
            'page': 'shield',
            'switches': {
                'Shield Alert':35,
                'Notification':37
            }
        }
    }

    def getSetupSwitches(self):
        return self.setup_switches

    def getRooms(self):
        return self.all_configuration

    def __init__(self):
        pass

