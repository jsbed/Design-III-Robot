import re


class InfoMatcher(object):

    def __init__(self, info_key, regex):
        self._info_key = info_key
        self._regex = regex

    def get_key(self):
        return self._info_key

    def match(self, info_data):
        return self._regex.search(info_data) is not None


class InfoListMatcher(InfoMatcher):

    def __init__(self, info_key, info_list):
        self._info_list = info_list
        regex = self._build_regex()
        super(InfoListMatcher, self).__init__(info_key, regex)

    def _build_regex(self):
        base_pattern = r'(?=.*\b{0}\b)'
        pattern = r'^'
        for info in self._info_list:
            pattern += base_pattern.format(info)
        pattern += r'.*$'
        return re.compile(pattern, re.IGNORECASE)


class ReligionsMatcher(InfoListMatcher):

    def __init__(self, religions):
        info_key = 'religions'
        super(ReligionsMatcher, self).__init__(info_key, religions)


class IndustriesMatcher(InfoListMatcher):

    def __init__(self, industries):
        info_key = 'industries'
        super(IndustriesMatcher, self).__init__(info_key, industries)


class UrbanAreasMatcher(InfoListMatcher):

    def __init__(self, urban_areas):
        info_key = 'major urban areas'
        super(UrbanAreasMatcher, self).__init__(info_key, urban_areas)


class UnemploymentRateMatcher(InfoMatcher):

    def __init__(self, rate):
        info_key = 'unemployment rate'
        regex = re.compile('{0}%'.format(rate))
        super(UnemploymentRateMatcher, self).__init__(info_key, regex)


class TotalAreaMatcher(InfoMatcher):

    def __init__(self, total_area):
        info_key = 'total area'
        regex = re.compile('([\d,]+) sq km')
        self._total_area = total_area.replace(',', '')
        super(TotalAreaMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            population = match.group(1)
            population = population.replace(',', '')
            print(population, self._total_area)
            return population == self._total_area
        else:
            return None


class NationalAnthemMatcher(InfoMatcher):

    def __init__(self, national_anthem):
        info_key = 'national anthem'
        regex = re.compile(national_anthem, re.IGNORECASE)
        super(NationalAnthemMatcher, self).__init__(info_key, regex)
