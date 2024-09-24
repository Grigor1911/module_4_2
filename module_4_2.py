def test_function():
    def inner_function():
        print("Я в области видимости фнкции test_function")
    inner_function() # Не возвращает


#inner_function() # Ошибка "NameError: name 'inner_function' is not defined"




test_function() # Если закомментировать 7-ю строчку, то функция работает