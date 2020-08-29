import random
import math
import pprint


def print_status():
    print(f'Oh hey, this is what we are up to')


# fitness function(s)
def check_fit(solution_test):
    this_fit = 15

    tests_passed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #1	The Toyota Camry was hired at 6:00am by a British couple.
    for position_dict in solution_test:
        if position_dict['make'] == 'Toyota Camry' and position_dict['time'] == '6am' \
                and position_dict['person'] == 'British':
            this_fit -= 1
            tests_passed[0] = 1
            break

    #2	The car in the middle had a black colour.
    if solution[2]['color'] == 'black':
        this_fit -= 1
        tests_passed[1] = 1

    #3	The Hyundai Accent left the depot at 9:00am.
    for position_dict in solution_test:
        if position_dict['make'] == 'Hyundai Accent' and position_dict['time'] == '9am':
            this_fit -= 1
            tests_passed[2] = 1
            break

    #4	The Holden Barina with a blue colour was to the left of the car that carries the British couple.
    for index, position_dict in enumerate(solution_test):
        if position_dict['make'] == 'Holden Barina' and position_dict['color'] == 'blue':
            if index + 1 < 5 and solution_test[index + 1]['person'] == 'British':
                this_fit -= 1
                tests_passed[3] = 1
                break

    #5	To the right of the car hired by a French lady was the car going to Gold Coast.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'French':
            if index + 1 < 5 and solution_test[index + 1]['destination'] == 'Gold Coast':
                this_fit -= 1
                tests_passed[4] = 1
                break

    #6	The Nissan X-Trail was heading for Sydney.
    for position_dict in solution_test:
        if position_dict['make'] == 'Nissan X-Trail' and position_dict['destination'] == 'Sydney':
            this_fit -= 1
            tests_passed[5] = 1
            break

    #7	To the right of the car carrying a Chinese businessman was the car with a green colour.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'Chinese':
            if index + 1 < 5 and solution_test[index + 1]['color'] == 'green':
                this_fit -= 1
                tests_passed[6] = 1
                break

    #8	The car going to Newcastle left at 5:00am.
    for position_dict in solution_test:
        if position_dict['destination'] == 'Newcastle' and position_dict['time'] == '5am':
            this_fit -= 1
            tests_passed[7] = 1
            break

    #9	The Honda Civic left at 7:00am and was on the right of the car heading for Gold Coast.
    for index, position_dict in enumerate(solution_test):
        if position_dict['destination'] == 'Gold Coast':
            if index + 1 < 5 and solution_test[index + 1]['time'] == '7am' and solution_test[index + 1][
                'make'] == 'Honda Civic':
                this_fit -= 1
                tests_passed[8] = 1
                break

    #10	The car with a red colour was going to Tamworth.
    for position_dict in solution_test:
        if position_dict['color'] == 'red' and position_dict['destination'] == 'Tamworth':
            this_fit -= 1
            tests_passed[9] = 1
            break

    #11	To the left of the car that left at 7:00am was the car with a white colour.
    for index, position_dict in enumerate(solution_test):
        if position_dict['color'] == 'white':
            if index + 1 < 5 and solution_test[index + 1]['time'] == '7am':
                this_fit -= 1
                tests_passed[10] = 1
                break

    #12	The last car was hired by an Indian man.
    if solution[4]['person'] == 'Indian':
        this_fit -= 1
        tests_passed[11] = 1

    #13	The car with a black colour left at 8:00am.
    for position_dict in solution_test:
        if position_dict['color'] == 'black' and position_dict['time'] == '8am':
            this_fit -= 1
            tests_passed[12] = 1

    #14	The car carrying an Indian man was to the right of the car hired by a Chinese businessman.
    for index, position_dict in enumerate(solution_test):
        if position_dict['person'] == 'Chinese':
            if index + 1 < 5 and solution_test[index + 1]['person'] == 'Indian':
                this_fit -= 1
                tests_passed[13] = 1
                break

    #15	The car heading for Tamworth left at 6:00am.
    for position_dict in solution_test:
        if position_dict['destination'] == 'Tamworth' and position_dict['time'] == '6am':
            this_fit -= 1
            tests_passed[14] = 1
            break

    return this_fit, tests_passed


# variables
color = ['black', 'blue', 'green', 'red', 'white']
make = ['Holden Barina', 'Honda Civic', 'Hyundai Accent', 'Nissan X-Trail', 'Toyota Camry']
time = ['5am', '6am', '7am', '8am', '9am']
person = ['British', 'Canadian', 'Chinese', 'French', 'Indian']
destination = ['Gold Coast', 'Newcastle', 'Port Macquarie', 'Sydney', 'Tamworth']


# seed for starter solution
random.shuffle(color)
random.shuffle(make)
random.shuffle(time)
random.shuffle(person)
random.shuffle(destination)

# the actual solution (for testing reasons)
# solution = [
#     {'color': 'blue', 'make': 'Holden Barina', 'time': '5am', 'person': 'Canadian', 'destination': 'Newcastle'},
#     {'color': 'red', 'make': 'Toyota Camry', 'time': '6am', 'person': 'British', 'destination': 'Tamworth'},
#     {'color': 'black', 'make': 'Nissan X-Trail', 'time': '8am', 'person': 'French', 'destination': 'Sydney'},
#     {'color': 'white', 'make': 'Hyundai Accent', 'time': '9am', 'person': 'Chinese', 'destination': 'Gold Coast'},
#     {'color': 'green', 'make': 'Honda Civic', 'time': '7am', 'person': 'Indian', 'destination': 'Port Macquarie'},
# ]

# random starter solution
solution = []
for i in range(0, 5):
    solution.append(
        {'color': color[i], 'make': make[i], 'time': time[i], 'person': person[i], 'destination': destination[i]}
    )

temp = 10
cooling = 0.999
fit = 100
iterations = 0

while temp > 0.000000000001:
    iterations += 1
    print(f"Fitness is {fit}")

    # solutionTest = [
    #     {'color': 'blue', 'make': 'Holden Barina', 'time': '5am', 'person': 'Canadian', 'destination': 'Newcastle'},
    #     {'color': 'red', 'make': 'Toyota Camry', 'time': '6am', 'person': 'British', 'destination': 'Tamworth'},
    #     {'color': 'black', 'make': 'Nissan X-Trail', 'time': '8am', 'person': 'French', 'destination': 'Sydney'},
    #     {'color': 'white', 'make': 'Hyundai Accent', 'time': '9am', 'person': 'Chinese', 'destination': 'Gold Coast'},
    #     {'color': 'green', 'make': 'Honda Civic', 'time': '7am', 'person': 'Indian', 'destination': 'Port Macquarie'},
    # ]

    # to find the solutionTest, randomly pick an attribute and swap 2 random members
    solutionTest = solution
    attributes = ['color', 'make', 'time', 'person', 'destination']
    rand_attribute = random.choice(attributes)
    position1 = random.randint(0, 4)
    position2 = random.randint(0, 4)
    while position2 == position1:
        position2 = random.randint(0, 4)
    solutionTest[position1][rand_attribute], solutionTest[position2][rand_attribute] = solutionTest[position2][rand_attribute], solutionTest[position1][rand_attribute]
    print(
        f"Swapped the {rand_attribute}s {solutionTest[position1][rand_attribute]} and {solutionTest[position2][rand_attribute]} from positions {position1} and {position2}")
    print(solutionTest)
    fitTest, tests_passed = check_fit(solutionTest)
    if fitTest < fit:
        solution = solutionTest
        fit = fitTest
    else:
        try:
            swap = math.exp((fit - fitTest) / temp)
        except ZeroDivisionError:
            swap = 1
        if swap > random.choice([0, 1]):
            fit = fitTest
            solution = solutionTest
        temp = temp * cooling

print(f"Solved using {iterations} iterations at {fit} fitness!")
print(tests_passed)
pprint.pprint(solution)
