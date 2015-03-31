class CountryResult(object):

    def __init__(self, country_name, score=1.0):

        self.country_name = country_name
        self.score = score

    def __eq__(self, other):
        return self.country_name == other.country_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.country_name)