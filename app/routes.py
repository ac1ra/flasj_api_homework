from app import app


@app.route("/hello")
def hello():
    return "Hello, world!"


@app.route("/info")
def info():
    return "This is an informaional page."


# Задание 2: Динамические маршруты
# Реализуйте маршрут /calc//, который возвращает сумму двух чисел.
# Пример: /calc/3/5 вернет "The sum of 3 and 5 is 8.".

# Доп.задание. Добавьте обработку ошибок для неправильных данных (например, /calc/a/b).


@app.route('/calc/<int:first>/<int:second>')
def calculate(first, second):
    return f"The sum of {first} and {second} is {first+second}"


@app.route('/calc/<string:first>/<string:second>')
def calculate_1(first, second):
    return f"Type error. Please start again."

# Задание 3. Создайте маршрут /reverse/, который переворачивает текст.

# Пример: /reverse/hello → "olleh".

# Доп.задание: Для маршрута /reverse/ добавьте проверку, чтобы текст содержал хотя бы один символ.


@app.route('/reverse/<name>')
def reverseword(name):
    # return checksymbol(name)
    if len(name) > 0:
        return f"{name[::-1]}"

# Задание 4. Реализуйте маршрут /user//, возвращающий:
# Доп.задание: Для маршрута /user// добавьте валидацию возраста (например, не допускайте возраст меньше 0).


@app.route('/user/<name>/<age>')
def checker(name, age):
    if int(age) > 0:
        return f"Hello, {name.capitalize()}. You are {age} years old."
    else:
        return f"Error. You entered the wrong age."
