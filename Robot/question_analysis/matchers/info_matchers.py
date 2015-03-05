import re
import operator


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


class InfoWithNumberMatcher(InfoMatcher):

    def __init__(self, info_key, regex, expected_info, op):
        self._expected_info = expected_info.replace(',', '')
        self._ops = {'=': operator.eq, '>':operator.gt, '<': operator.lt}
        self._op = self._ops[op]
        super(InfoWithNumberMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            actual_info = match.group(1).replace(',', '')
            return self._op(actual_info, self._expected_info)
        return None


class InternetUsersMatcher(InfoWithNumberMatcher):

    def __init__(self, internet_users_amount):
        info_key = 'internet users'
        regex = re.compile('([\d,.]+\smillion?)')
        op = '='
        super(InternetUsersMatcher, self).__init__(info_key, regex, internet_users_amount, op)


class TotalAreaMatcher(InfoWithNumberMatcher):

    def __init__(self, total_area):
        info_key = 'total area'
        regex = re.compile('([\d,]+) sq km')
        op = '='
        super(TotalAreaMatcher, self).__init__(info_key, regex, total_area, op)


class NationalAnthemMatcher(InfoMatcher):

    def __init__(self, national_anthem):
        info_key = 'national anthem'
        regex = re.compile(national_anthem, re.IGNORECASE)
        super(NationalAnthemMatcher, self).__init__(info_key, regex)
