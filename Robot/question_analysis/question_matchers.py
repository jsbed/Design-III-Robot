import re
import operator


class InfoMatcher(object):

    def __init__(self, info_key, pattern):
        self._info_key = info_key
        self._regex = re.compile(pattern, re.IGNORECASE)

    def get_key(self):
        return self._info_key

    def match(self, info_data):
        return self._regex.search(info_data) is not None


class NumericApproximationInfoMatcher(InfoMatcher):

    def __init__(self, info_key, expected_info):
        pattern = r'([\d,.\s]+)'
        self._expected_info = self._cast_to_float(expected_info)
        super(NumericApproximationInfoMatcher, self).__init__(info_key, pattern)

    def _cast_to_float(self, number):
        number = number.replace(',', '').replace(' ', '')
        if number[-1] == '.':
            number = number[:-1]
        try:
            number = float(number)
        except:
            number = None
        return number

    def match(self, info_data):
        self._info_data = info_data
        match = self._regex.search(info_data)
        if match and any(char.isdigit() for char in info_data):
            actual_info = self._cast_to_float(match.group(1))
            if actual_info:
                return self._expected_info - 0.5 < actual_info < self._expected_info + 0.5
        return None


class NumericInfoMatcher(InfoMatcher):

    def __init__(self, info_key, expected_info, op):
        pattern = r'([\d,.\s]+)'
        self._expected_info = self._cast_to_float(expected_info)
        self._ops = {'=': operator.eq, '>': operator.gt, '<': operator.lt}
        self._op = self._ops[op]
        super(NumericInfoMatcher, self).__init__(info_key, pattern)

    def _cast_to_float(self, number):
        number = number.replace(',', '').replace(' ', '')
        try:
            if number[-1] == '.':
                number = number[:-1]

            number = float(number)
        except:
            number = None
        return number

    def match(self, info_data):
        self._info_data = info_data
        match = self._regex.search(info_data)
        if match and any(char.isdigit() for char in info_data):
            actual_info = self._cast_to_float(match.group(1))
            if actual_info:
                return self._op(actual_info, self._expected_info)
        return None


class BetweenMatcher(InfoMatcher):

    def __init__(self, info_key, lower_bound, upper_bound):
        self._lower_bound = self._cast_to_float(lower_bound)
        self._upper_bound = self._cast_to_float(upper_bound)
        pattern = r"([\d.,]+)"
        super(BetweenMatcher, self).__init__(info_key, pattern)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            actual_value = match.group(1)
            actual_value = self._cast_to_float(actual_value)
            return self._lower_bound < actual_value < self._upper_bound
        else:
            return None

    def _cast_to_float(self, number):
        number = number.replace(',', '').replace(' ', '')
        if number[-1] == '.':
            number = number[:-1]
        return float(number)


class InfoListMatcher(InfoMatcher):

    def __init__(self, info_key, info_list):
        self._info_list = info_list
        pattern = self._build_pattern()
        super(InfoListMatcher, self).__init__(info_key, pattern)
        print(self._regex)

    def _build_pattern(self):
        base_pattern = r'(?=.*\b{0}\b)'
        pattern = r'^'
        for info in self._info_list:
            pattern += base_pattern.format(info)
        pattern += r'.*$'
        return pattern


class LengthMatcher(InfoMatcher):
    def __init__(self, info_key, length):
        self._length = int(length)
        pattern = r'([\s\w]+)'
        super(LengthMatcher, self).__init__(info_key, pattern)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            return len(match.group(1).split()) == self._length
        return None


class NationalAnthemMatcher(InfoMatcher):

    def __init__(self, national_anthem):
        info_key = 'national anthem'
        regex = re.compile(national_anthem, re.IGNORECASE)
        super(NationalAnthemMatcher, self).__init__(info_key, regex)


class ClimateMatcher(InfoMatcher):

    def __init__(self, info_key, climate):
        pattern = climate
        super(ClimateMatcher, self).__init__(info_key, pattern)


class IllicitDrugsActivitiesMatcher(InfoMatcher):

    def __init__(self, info_key, activities):
        pattern = activities
        super(IllicitDrugsActivitiesMatcher, self).__init__(info_key, pattern)
        print(self._regex)