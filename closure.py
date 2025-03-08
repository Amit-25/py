def outer(firstName):
    middleName = "kumar"

    def inner1(lastName):
        return firstName + " " + middleName + " " + lastName
    return inner1


name = outer('Amit')('Singh')
print(name)
