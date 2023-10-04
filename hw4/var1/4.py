with open ('students2.txt', 'r') as file:
    all = file.read()
    each = all.split('\n')
    for person in each:
        each_person = person.split()
        each_person[3] = '301-' + each_person[3]
        each_person[0] = each_person[0].capitalize()
        with open ('students3.txt', 'a') as file2:
            file2.write(each_person[0] + ' ' + each_person[1] + '\n' + each_person[3] + "\n")