# read from a db
# we will marge date from a database
class Config:

    all_configuration={
        'livingroom':{
                'label':'Living Room',
                'page':'livingroom.html',
                'switches':{
                    'Main Living Room':13,
                    'Living Room Lamp 1':15,
                    'Living Room Lamp 2':17
                }
        },
        'kitchen': {
            'label': 'Kitchen',
            'page': 'kitchen.html',
            'switches': {
                'Kitchen Main': 19,
                'Litchen Lamp': 21,
            }
        },
    }

    setup_switches = {
        'kitchen': 11,
        'livingroom': 13,
        'bedroom': 15,
        'lamp1': 17,
        'lamp2': 19
    }

    navigation_bar={

        'community':'community.html',
        'frontdoor':'frontdoor.html',
        'livingrooom':'livingroom.html',
        'bedroom':'bedroom.html',
        'utilities':'utilities.html',
        'remote':'remote'
    }

    def getNavigationBar(self):
        return self.navigation_bar

    def getSetupSwitches(self):
        return self.setup_switches


    def getRooms(self):
        return self.all_configuration

    def __init__(self):
        pass

