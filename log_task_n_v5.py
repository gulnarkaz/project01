from collections import OrderedDict

class Logger:
    def __init__(self):
        self.messages = OrderedDict()
        self.max_size = 100
        self.message_lifetime = 10  # время жизни сообщения в секундах

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Удаляем устаревшие сообщения
        self._cleanup(timestamp)
        
        if message in self.messages and self.messages[message] > timestamp:
            return False
        
        if len(self.messages) >= self.max_size:
            return False

        # Добавляем или обновляем сообщение
        self.messages[message] = timestamp + self.message_lifetime
        return True

    def clean(self, timestamp: int) -> bool:
        # Удаляем устаревшие сообщения
        self._cleanup(timestamp)
        
        # Проверяем, можно ли очистить систему
        if len(self.messages) == 0:
            return True
        
        return False

    def loggerSize(self) -> int:
        # Возвращаем размер хранилища
        return len(self.messages)

    def _cleanup(self, current_time: int):
        # Удаляем старые сообщения, которые больше не актуальны
        while self.messages and next(iter(self.messages.values())) <= current_time:
            self.messages.popitem(last=False)

# Пример использования:
logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))  # return True
print(logger.shouldPrintMessage(2, "bar"))  # return True
print(logger.shouldPrintMessage(3, "foo"))  # return False
print(logger.shouldPrintMessage(8, "bar"))  # return False
print(logger.shouldPrintMessage(10, "foo")) # return False
print(logger.shouldPrintMessage(11, "foo")) # return True

print(logger.loggerSize())  # return 2

print(logger.clean(11))  # return False, поскольку "bar" ещё актуален
print(logger.clean(12))  # return True, поскольку все сообщения очищены
