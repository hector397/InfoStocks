from __future__ import annotations
from abc import ABC, abstractmethod
from typing import *


"""
This class declares a set of methods for concrete subjects
"""
class Subject(ABC):

    """
    Constructor for a Subject class
    Variables:
        - _changed: Protected attribute that represents if the state has changed
        - _observers: List of Subject's observers
    """
    def __init__(self):
        self._changed: bool = False
        self._observers: List[Observer] = []

    """
    Add a observer
    Parameters:
        - observer: Represents a Observer object
    """
    def _add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    """
    Remove a observer
    Parameters:
            - observer: Represents a Observer object
    """
    def _remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Changes the state of the Subject
    """
    def _set_changed(self) -> None:
        self._changed = True

    """
    Notify observers with certain data.
    Parameters:
        - obj: Any object that observers need
    """
    def _notify_observers(self, obj: Any) -> None:
        if self._changed:
            for observer in self._observers:
                observer.update(self, obj)

    """
    Notify observers without data
    """
    def _notify_observers(self) -> None:
        self.notify_observers(None)


"""
This class declares a set of methods for concrete observers
"""
class Observer(ABC):

    """
    Receive an update from a subject
    Parameters:
        - subject: The Subject object that has the data
        - args: The data to update
    """
    @abstractmethod
    def update(self, subject: Subject, args: Any) -> None:
        pass
