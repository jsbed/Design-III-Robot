from PySide.QtCore import QObject, Signal


class Signal(QObject):
    customSignal = Signal(str)
