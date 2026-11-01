from abc import ABC, abstractmethod
import logging
import time

# Налаштування логування, щоб бачити повідомлення в консолі
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class OperationWork(ABC):
    @abstractmethod
    def operation(self):
        pass

class Calculator(OperationWork):
    def __init__(self, number: int, number2: int, operation: str) -> None:
        # Перевіряємо, чи є числа цілими, а операція — рядком
        if isinstance(number, int) and isinstance(number2, int) and isinstance(operation, str):
            self.number = number
            self.number2 = number2
            self.operation = operation
            self.result = 0  # Результат краще обчислювати, аніж передавати ззовні
        else:
            logging.info('ошибочка с вводом даных')
            time.sleep(3)
            raise ValueError('не то ввели')

    def operation(self):
        # Виконуємо математичні операції та записуємо в self.result
        if self.operation == '+':
            self.result = self.number + self.number2
        elif self.operation == '-':
            self.result = self.number - self.number2
        elif self.operation == '/':
            if self.number2 == 0:
                raise ZeroDivisionError("Ділення на нуль!")
            self.result = self.number / self.number2
        elif self.operation == '*':
            self.result = self.number * self.number2
        else:
            raise ValueError('сбой в работе програмы (невідомий оператор)')
            
        return self.result

# --- Приклад використання ---
try:
    calc = Calculator(10, 5, '+')
    print(f"Результат: {calc.operation()}")  # Виведе: 15
except (ValueError, ZeroDivisionError) as e:
    print(f"Помилка: {e}")


            
            




            

        
