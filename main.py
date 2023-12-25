import debugger

def add(a, b):
    return a + b
def complex_math_operation(x, y, z):

    result = x / y
    result *= z
    return result
func_dict = {
    "add": add,
    "complex_math_operation": complex_math_operation
}
if __name__ == "__main__":
    values = [(10, 5, 2), (10, 0, 2), (10, 2, 0), (0, 0, 0)]
    debugger.ask_and_set_breakpoint()
    for value_set in values:
        try:
            x, y, z = value_set
            print(f"Выполняем операцию для значений: {value_set}")
            result = complex_math_operation(x, y, z)
            print(f"Результат: {result}")
        except Exception as e:
            debugger.debug_exception(e)

    x = 5
    debugger.ask_and_set_breakpoint()
    debugger.view_variable("x")
    debugger.change_variable("x", 10)
    debugger.view_variable("x")

    debugger.ask_and_set_breakpoint()
    result = debugger.call_function("add", func_dict, 5, 3)
    print("Результат:", result)

    debugger.ask_and_set_breakpoint()
    profiled_result = debugger.profile_code("add", func_dict, 5, 3)
    print("Результат:", profiled_result)
