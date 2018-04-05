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
                'Porch Light':11,
                'Door Lock':13
            }
        },
        'livingroom':{
                'label':'Living Room',
                'page':'livingroom',
                'switches':{
                    'Main':15,
                    'Fan':19,
                    'Table Lamp 1':29,
                    'Table Lamp 2':31
                }
        },
        'kitchen': {
            'label': 'Kitchen',
            'page': 'kitchen',
            'switches': {
                'Kitchen Main': 15,
                'Kitchen Lamp': 29,
            }
        },
        'bedroom': {
            'label': 'Bedroom',
            'page': 'bedroom',
            'switches': {
                'Main Light': 21,
                'Lamp 1': 16,
                'Lamp 2': 18,
            }
        },
    }

    def getSetupSwitches(self):
        return self.setup_switches

    def getRooms(self):
        return self.all_configuration

    def __init__(self):
        pass

