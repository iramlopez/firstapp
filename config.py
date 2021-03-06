# read from a db
# we will marge date from a database
class Config:


    setup_switches = {
        'kitchen': 11,
        'livingroom': 13,
        'bedroom': 15,
        'lamp1': 17,
        'lamp2': 19
    }

    all_configuration={

        'community': {
            'label': 'Community',
            'page': 'community',
            'switches': {
            }
        },
        'frontdoor': {
            'label': 'Front Door',
            'page': 'frontdoor',
            'switches': {
                'Porch Light':35,
                'Door Lock':37
            }
        },
        'livingroom':{
                'label':'Living Room',
                'page':'livingroom',
                'switches':{
                    'Main':11,
                    'Fan':40,
                    'Table Lamp 1':38,
                }
        },
        'kitchen': {
            'label': 'Kitchen',
            'page': 'kitchen',
            'switches': {
                'Kitchen Main': 13,
                'Kitchen Lamp': 29,
            }
        },
        'bedroom': {
            'label': 'Bedroom',
            'page': 'bedroom',
            'switches': {
                'Main Light': 15,
                'Lamp 1': 31,
            }
        },
    }

    def getSetupSwitches(self):
        return self.setup_switches

    def getRooms(self):
        return self.all_configuration

    def __init__(self):
        pass

