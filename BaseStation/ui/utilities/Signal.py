from PySide.QtCore import QObject, Signal


class Signal(QObject):
    custom_signal = Signal(str)
