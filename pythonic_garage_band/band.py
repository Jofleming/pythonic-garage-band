
class Musician:
    instrument = ''
    title = ''

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        return f'{self.title} instance. Name = {self.name}'

    def get_instrument(self):
        return f'{self.instrument}'

class Guitarist(Musician):
    instrument = 'guitar'
    title = 'Guitarist'

    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):
    instrument = 'bass'
    title = 'Bassist'

    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):
    instrument = 'drums'
    title = 'Drummer'

    def play_solo(self):
        return 'rattle boom crash'

class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solo_list = []
        for member in self.members:
            solo_list.append(member.play_solo())
        return solo_list

    def __str__(self):
        return f'The band {self.name}'

    def __repr__(self):
        return f'Band instance. name={self.name}, members={self.members}'

    @classmethod
    def to_list(cls):
        return cls.instances
        


if __name__ == '__main__':
    def one_band():
        members = [
            Guitarist('Kurt Cobain'),
            Bassist('Krist Novoselic'),
            Drummer('Dave Grohl'),
        ]
        some_band = Band('Nirvana', members)
        return some_band
    
    new_band = one_band()
    print(str(new_band))
