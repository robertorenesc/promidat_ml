class Logger:

    # Constructor
    def __init__(self, enabled = False):
        self.__enabled = enabled

    # Public Methods
    def debug(self, message):
        if self.enabled:
            print(message)

    def info(self, message):
        print(message)
        
    # Getters and Setters
    @property
    def enabled(self):
        return self.__enabled