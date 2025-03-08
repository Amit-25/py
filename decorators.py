def deco(func):
    def wrapper(*args: str):
        data = []
        for arg in args:
            data.append(arg.capitalize())
        return data
    return wrapper


@deco
def str_to_upper_case(name):
    pass


res = str_to_upper_case('amit', 'kumar', 'singh')
# print(res)


def deco_2(func):
    def wrapper(**kwargs: str):
        res = func(**kwargs)
        #print(**kwargs)
        if res:
            print(f'Hey {kwargs["data"]["name"]}!, you are eligible to give votes')
        else:
            print('You are not eligible')
    return wrapper


@deco_2
def func(data):
    if data['age'] > 21:
        return True
    return False


data = {
    'name': "amit singh",
    'age': 25
}
func(data=data)
# func(age=25, name='amit')
