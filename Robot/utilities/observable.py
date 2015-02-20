class Observable:

    def __init__(self):
        self._observers = {}

    def attach(self, event, observer):
        if event not in self._observers:
            self._observers[event] = [observer, ]
        else:
            if observer not in self._observers[event]:
                self._observers[event].append(observer)
            else:
                raise ValueError("Observer is already registered to event: ",
                                 event)

    def detach(self, event, observer):
        if event not in self._observers:
            raise KeyError("No observers are registered for the event: ",
                           event)
        else:
            if observer not in self._observers[event]:
                raise ValueError("Observer is not registered for the event: ",
                                 event)
            else:
                self._observers[event].remove(observer)

    def notify(self, event):
        if event in self._observers:
            for observer in self._observers[event]:
                observer.update(event)
