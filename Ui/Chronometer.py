from PySide.QtCore import QTimer

from Observer import ObserverSubject


NEW_TIME_UPDATE = "New Time Update"
INTERVAL = 10

class Chronometer(ObserverSubject):
    
    def __init__(self):
        ObserverSubject.__init__(self)
        self._time = 0   
        self._timer = QTimer()
        self._timer.setInterval(INTERVAL)
        self._timer.timeout.connect(self._increment_time)
    
    def start(self):
        self._timer.start()
    
    def pause(self):
        self._timer.stop()
    
    def restart(self):
        self._timer.stop()
        self._time = 0
        self.notify(NEW_TIME_UPDATE)
    
    def get_time(self):
        min_sec, ms = divmod(self._time/10, 100)
        m, s = divmod(min_sec, 60)
        
        return "%02d:%02d:%02d" % (m, s, ms)
    
    def _increment_time(self):
        self._time += INTERVAL
        self.notify(NEW_TIME_UPDATE)