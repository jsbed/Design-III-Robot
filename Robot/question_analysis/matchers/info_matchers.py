import re

class InfoMatcher(object):

    def __init__(self, info_key, regex):
        self._info_key = info_key
        self._regex = regex

    def get_key(self):
        return self._info_key

    def match(self, info_data):
        return self._regex.search(info_data)

class UnemploymentRateMatcher(InfoMatcher):

    def __init__(self, rate):
        info_key = 'unemployment rate'
        regex = re.compile('{0}%'.format(rate))
        super(UnemploymentRateMatcher, self).__init__(info_key, regex)


class PopulationMatcher(InfoMatcher):

    def __init__(self, population):
        info_key = 'population'
        regex = re.compile('{0}'.format(population))
        super(PopulationMatcher, self).__init__(info_key, regex)

class UrbanAreasMatcher(InfoMatcher):

    def __init__(self, urban_areas):
        info_key = 'major urban areas'
        self._urban_areas = urban_areas
        regex = self._build_regex()
        super(UrbanAreasMatcher, self).__init__(info_key, regex)

    def _build_regex(self):
        base_pattern = r'(?=.*\b{0}\b)'
        pattern = r'^'
        for urban_area in self._urban_areas:
            pattern += base_pattern.format(urban_area)
        pattern += r'.*$'
        return re.compile(pattern, re.IGNORECASE)
