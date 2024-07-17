calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    lowUp = (len(string), string.upper(), string.lower())
    print(lowUp)
    count_calls()


def is_contains(string, list_to_search):
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()


string_info('До инфаркта')
is_contains("Настя", ['Лиза', 'Маша'])
string_info('До инфаркта')
is_contains("Лиза", ['Лиза', 'Маша'])
print(calls)