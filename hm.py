calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    lowUp = (len(string), string.upper(), string.lower())
    print(lowUp)
    count_calls()
    return lowUp


def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()
    return string, list_to_search


string_info('До инфаркта')
is_contains("Настя", ['Лиза', 'Маша'])
string_info('До инфаркта')
is_contains("Лиза", ['Лиза', 'Маша'])
print(calls)
