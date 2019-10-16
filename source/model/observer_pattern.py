from abc import ABC, abstractmethod
from __future__ import annotations


"""
This class declares a set of methods for concrete subjects
"""
class Subject(ABC):

    """
    Add an observer to the Subject

    Parameters:
        - observer -> Observer object to be added
    """
    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    """
    Remove an observer from de subject
    
    Parameters:
        - observer -> Observer object to be removed
    """
    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    """
    Notify all observers about an event
    """
    @abstractmethod
    def notify_observers(self) -> None:
        pass

    """
    Changes the flag to indicate that the state has changed.
    """
    @abstractmethod
    def set_changed(self) -> None:
        pass


"""
This class declares a set of methods for concrete observers
"""
class Observer(ABC):

    """
    Receive an update from a subject
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass
