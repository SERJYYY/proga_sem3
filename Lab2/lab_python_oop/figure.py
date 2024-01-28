from abc import ABC, abstractmethod


class figuresh(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def square(self):
        pass
