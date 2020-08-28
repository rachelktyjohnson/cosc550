def print_status():
    print(f'Oh hey, this is what we are up to')


# fitness function(s)
def check_fit(solution_test):
    fit = 0

    #	The Toyota Camry was hired at 6:00am by a British couple.
    for position_dict in solution_test:
        if position_dict['make'] == 'Toyota Camry' and position_dict['time'] == '6am'\
                and position_dict['person'] == 'British':
            fit += 1

    #	The car in the middle had a black colour.
    if solution[2]['color'] == 'black':
        fit += 1

    #	The Hyundai Accent left the depot at 9:00am.
    for position_dict in solution_test:
        if position_dict['make'] == 'Hyundai Accent' and position_dict['time'] == '9am':
            fit += 1

    #	The Holden Barina with a blue colour was to the left of the car that carries the British couple.
    for index, position_dict in enumerate(solution_test):
        if position_dict['make'] == 'Holden Barina' and position_dict['color'] == 'blue':
            if index+1 < 5 and solution_test[index+1]['person'] == 'British':
                fit += 1

    #	To the right of the car hired by a French lady was the car going to Gold Coast.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'French':
            if index+1 < 5 and solution_test[index+1]['destination'] == 'Gold Coast':
                fit += 1

    #	The Nissan X-Trail was heading for Sydney.
    for position_dict in solution_test:
        if position_dict['make'] == 'Nissan X-Trail' and position_dict['destination'] == 'Sydney':
            fit += 1

    #	To the right of the car carrying a Chinese businessman was the car with a green colour.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'Chinese':
            if index+1 < 5 and solution_test[index+1]['color'] == 'green':
                fit += 1

    #	The car going to Newcastle left at 5:00am.
    for position_dict in solution_test:
        if position_dict['destination'] == 'Newcastle' and position_dict['time'] == '5am':
            fit += 1

    #	The Honda Civic left at 7:00am and was on the right of the car heading for Gold Coast.
    for index, position_dict in enumerate(solution_test):
        if position_dict['destination'] == 'Gold Coast':
            if index+1 < 5 and solution_test[index+1]['time'] == '7am' and solution_test[index+1]['make'] == 'Honda Civic':
                fit += 1

    #	The car with a red colour was going to Tamworth.
    for position_dict in solution_test:
        if position_dict['color'] == 'red' and position_dict['destination'] == 'Tamworth':
            fit += 1

    #	To the left of the car that left at 7:00am was the car with a white colour.
    for index, position_dict in enumerate(solution_test):
        if position_dict['color'] == 'white':
            if index+1 < 5 and solution_test[index+1]['time'] == '7am':
                fit += 1

    #	The last car was hired by an Indian man.
    if solution[4]['person'] == 'Indian':
        fit += 1

    #	The car with a black colour left at 8:00am.
    for position_dict in solution_test:
        if position_dict['color'] == 'black' and position_dict['time'] == '8am':
            fit += 1

    #	The car carrying an Indian man was to the right of the car hired by a Chinese businessman.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'Chinese':
            if index+1 < 5 and solution_test[index+1]['person'] == 'Indian':
                fit += 1

    #	The car heading for Tamworth left at 6:00am.
    for position_dict in solution_test:
        if position_dict['destination'] == 'Tamworth' and position_dict['time'] == '6am':
            fit += 1

    return fit


# variables
position = [1, 2, 3, 4, 5]
color = ['black', 'blue', 'green', 'red', 'white']
make = ['Holden Barina', 'Honda Civic', 'Hyundai Accent', 'Nissan X-Trail', 'Toyota Camry']
time = ['5am', '6am', '7am', '8am', '9am']
person = ['British', 'Canadian', 'Chinese', 'French', 'Indian']
destination = ['Gold Coast', 'Newcastle', 'Port Macquarie', 'Sydney', 'Tamworth']

# solution
solution = [
    {'color': 'blue', 'make': 'Holden Barina', 'time': '5am', 'person': 'Canadian', 'destination': 'Newcastle'},
    {'color': 'red', 'make': 'Toyota Camry', 'time': '6am', 'person': 'British', 'destination': 'Tamworth'},
    {'color': 'black', 'make': 'Nissan X-Trail', 'time': '8am', 'person': 'French', 'destination': 'Sydney'},
    {'color': 'white', 'make': 'Hyundai Accent', 'time': '9am', 'person': 'Chinese', 'destination': 'Gold Coast'},
    {'color': 'green', 'make': 'Honda Civic', 'time': '7am', 'person': 'Indian', 'destination': 'Port Macquarie'},
]

print(check_fit(solution))
