# Nie da się wywołać tej funkcji ponieważ argument *others jest przed age
def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


# wlasna funkcja

def fun(*args, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    print("args: ", args)
    print("kwargs: ", kwargs)


fun(1, 2, 'three',  first="one",  second="two", three=3)
