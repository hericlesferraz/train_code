class Logger:

    def __init__(self):
        self.hash_msg = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hash_msg or timestamp >= self.hash_msg[message]:
            self.hash_msg[message] = timestamp+10
            return True
        
        return False
        
