dat = []
xs = []

def pars():
    with open('05.csv', 'r') as file:
        d = file.read()

    data_list = d.split('\n')

    data = [[] for _ in range(len(data_list))]

    for i in range(len(data_list)):
        data[i] = data_list[i].split(',')

    for i in range(1, len(data) - 1):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])

    return data


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       dat = []
xs = []

def pars():
    with open('05.csv', 'r') as file:
        d = file.read()

    data_list = d.split('\n')

    data = [[] for _ in range(len(data_list))]

    for i in range(len(data_list)):
        data[i] = data_list[i].split(',')

    for i in range(1, len(data) - 1):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])

    return data


