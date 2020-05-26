from abc import ABCMeta, abstractmethod

class Base(metaclass =  ABCMeta):
    
    LINE_SEPARATOR = "+-----------------------------------------------+\n"

    DOUBLE_LINE_SEPARATOR = "================================================="

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def captura(self):
        pass