import time
current_time = time.time()
# t = time.localtime()
# time_now = time.strftime()
# print(time_now)

print(current_time)


#
def speed_calc_decorator(function):
    def wrapper_func():
        fast_funcion()
        time1 = current_time
        slow_function()
        time2 = current_time
        print(time1 - time2)

    return wrapper_func

@speed_calc_decorator
def fast_funcion():
    for i in range(10000000):
        i * i



@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_funcion()