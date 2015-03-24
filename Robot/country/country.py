from Robot.cycle.objects.color import Color


class Country:

    def __init__(self, name, flag):
        self.name = name
        self.flag = flag
        self.number_of_cubes = sum([1 for x in flag if x != Color.NONE])
