# Logger System

## Описание

`Logger` - это система для управления потоками сообщений, которая обеспечивает:
- Печать сообщений с временными метками.
- Ограничение времени существования уникальных сообщений.
- Очистку системы в случае переполнения.
- Проверку возможности печати сообщений и очистки системы.

## Установка

Для использования этого кода, вам нужно просто склонировать репозиторий и запустить Python скрипт. Убедитесь, что у вас установлен Python 3.6 или выше.

 ```bash
    git clone https://github.com/gulnarkaz/project01.git
    cd project01
    ```

2. Убедитесь, что у вас установлен Python 3.6 или выше.

## Пример использования

### Импорт и создание экземпляра `Logger`

```python
from logger import Logger

# Создание экземпляра Logger
logger = Logger()

## Проверка возможности печати сообщения
print(logger.shouldPrintMessage(1, "foo"))  # Возвращает True
print(logger.shouldPrintMessage(2, "bar"))  # Возвращает True
print(logger.shouldPrintMessage(3, "foo"))  # Возвращает False
print(logger.shouldPrintMessage(8, "bar"))  # Возвращает False
print(logger.shouldPrintMessage(10, "foo")) # Возвращает False
print(logger.shouldPrintMessage(11, "foo")) # Возвращает True
