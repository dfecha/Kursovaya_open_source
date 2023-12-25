import traceback
import logging
import pdb
import time
import inspect

# Настройка логгера
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def debug_exception(e):
    # Получение информации об исключении и трассировке стека
    exception_info = traceback.format_exc()

    # Вывод информации об исключении на экран
    print(f"Произошло исключение: {e}")
    print(f"Информация об исключении: {exception_info}")

    # Предложение решения для общих типов ошибок
    if isinstance(e, ZeroDivisionError):
        print("Эта ошибка произошла из-за того, что вы пытались разделить на ноль. Убедитесь, что знаменатель не равен нулю, прежде чем выполнять деление.")
    elif isinstance(e, NameError):
        print("Эта ошибка произошла из-за того, что вы пытались использовать переменную, которая не была определена. Убедитесь, что все переменные определены перед их использованием.")
    elif isinstance(e, TypeError):
        print("Эта ошибка произошла из-за попытки выполнить операцию, которая не поддерживается для данного типа объекта. Убедитесь, что все объекты, с которыми вы работаете, имеют правильные типы.")
    elif isinstance(e, IndexError):
        print("Эта ошибка произошла из-за попытки обратиться к элементу списка или строки по индексу, который выходит за пределы длины этих объектов. Убедитесь, что вы не пытаетесь обратиться к элементу, который не существует.")
    elif isinstance(e, KeyError):
        print("Эта ошибка произошла из-за попытки обратиться к ключу в словаре, которого нет. Убедитесь, что ключ, к которому вы обращаетесь, существует в словаре.")
    elif isinstance(e, FileNotFoundError):
        print("Эта ошибка произошла из-за попытки открыть файл, которого нет. Убедитесь, что путь к файлу указан правильно и файл существует.")
    elif isinstance(e, ImportError):
        print("Эта ошибка произошла из-за попытки импортировать модуль, которого нет. Убедитесь, что модуль установлен и правильно импортирован.")
    elif isinstance(e, AttributeError):
        print("Эта ошибка произошла из-за попытки обратиться к атрибуту или методу объекта, которого нет. Убедитесь, что атрибут или метод существует.")
    elif isinstance(e, ValueError):
        print("Эта ошибка произошла из-за передачи функции аргумента правильного типа, но неправильного значения. Убедитесь, что аргументы функции имеют правильные значения.")
    elif isinstance(e, RecursionError):
        print("Эта ошибка произошла из-за бесконечного вызова функции. Убедитесь, что функция имеет условие выхода из рекурсии.")
    elif isinstance(e, SyntaxError):
        print("Эта ошибка произошла из-за синтаксических ошибок в коде. Убедитесь, что ваш код соответствует правилам синтаксиса Python.")
    elif isinstance(e, RuntimeError):
        print("Эта ошибка произошла во время выполнения программы. Убедитесь, что ваш код не содержит ошибок логики.")
    else:
        print("Это неизвестная ошибка. Возможно, вам потребуется ознакомиться с документацией или обратиться за помощью к компетентному источнику.")

   # Логирование информации об исключении
    logging.error(f"Произошло исключение: {e}")
    logging.error(f"Информация об исключении: {exception_info}")
def ask_and_set_breakpoint():
    user_input = input("Вы хотите установить точку остонова (yes/no): ")
    if user_input.lower() == "yes":
        frame = inspect.currentframe()
        pdb.set_trace()

def view_variable(var):
    frame = inspect.currentframe().f_back
    value = frame.f_locals.get(var)
    if value is not None:
        print(f"{var} = {value}")
    else:
        value = frame.f_globals.get(var)
        if value is not None:
            print(f"{var} = {value}")
        else:
            print(f"Переменная {var} не найдена")

def change_variable(var, value):
    frame = inspect.currentframe().f_back
    frame.f_locals[var] = value

def call_function(func, func_dict, *args, **kwargs):
    if func in func_dict and callable(func_dict[func]):
        return func_dict[func](*args, **kwargs)
    else:
        raise ValueError(f"Функция {func} не существует или не может быть вызвана")

def profile_code(func, func_dict, *args, **kwargs):
    if func in func_dict and callable(func_dict[func]):
        start_time = time.time()
        result = func_dict[func](*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func}: {end_time - start_time} секунд")
        return result
    else:
        raise ValueError(f"Функция {func} не существует или не может быть вызвана")

