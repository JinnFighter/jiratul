class JiratulService:
    isInitialized: bool

    def __init__(self):
        pass

    def initialize(self):
        self.isInitialized = True
        pass

    def terminate(self):
        self.isInitialized = False
        pass
