import abc


class RobotInstruction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError
