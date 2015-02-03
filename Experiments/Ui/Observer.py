# observer.py
# pyton implementation of the observer design pattern
#
# Created by Jon Black, May 16th 2012.
# Released into the public domain.
# License: GPL 3

class ObserverSubject(object):

    def __init__(self):
        self._observers = {}

    def attach(self, hint, observer):
        if hint not in self._observers:
            self._observers[hint] = [observer,]
        else:
            if observer not in self._observers[hint]:
                self._observers[hint].append(observer)
            else:
                raise ValueError("Observer is already registered to hint: ",   
                                hint)

    def detach(self, hint, observer):
        if hint not in self._observers:
            raise KeyError("No observers are registered for the hint: ", hint)
        else:
            if observer not in self._observers[hint]:
                raise ValueError("Observer is not registered for the hint: ",   
                                hint)
            else:
                self._observers[hint].remove(observer)

    def notify(self, hint):
        if hint in self._observers:
            for observer in self._observers[hint]:
                observer.update(hint)