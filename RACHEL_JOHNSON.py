#!/usr/bin/env python3

import random
import math
import copy
import operator
import time as tt

# global
iterations = 0
runs = 0
run = True


# fitness function(s)
def check_fit(solution_test):
    this_fit = 15

    for car in solution_test:
        # 1	The Toyota Camry was hired at 6:00am by a British couple.
        if car['make'] == 'Toyota Camry' and car['time'] == '6am' and car['person'] == 'British':
            this_fit -= 1

        #2	The car in the middle had a black colour.
        if car['position'] == 2 and car['color'] == 'black':
            this_fit -= 1

        #3	The Hyundai Accent left the depot at 9:00am.
        if car['make'] == 'Hyundai Accent' and car['time'] == '9am':
            this_fit -= 1

        #4	The Holden Barina with a blue colour was to the left of the car that carries the British couple.
        if car['make'] == 'Holden Barina' and car['color'] == 'blue' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['person'] == 'British':
                    this_fit -= 1

        #5	To the right of the car hired by a French lady was the car going to Gold Coast.
        if car['person'] == 'French' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['destination'] == 'Gold Coast':
                    this_fit -= 1

        #6	The Nissan X-Trail was heading for Sydney.
        if car['make'] == 'Nissan X-Trail' and car['destination'] == 'Sydney':
            this_fit -= 1

        #7	To the right of the car carrying a Chinese businessman was the car with a green colour.
        if car['person'] == 'Chinese' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['color'] == 'green':
                    this_fit -= 1

        #8	The car going to Newcastle left at 5:00am.
        if car['destination'] == 'Newcastle' and car['time'] == '5am':
            this_fit -= 1

        #9	The Honda Civic left at 7:00am and was on the right of the car heading for Gold Coast.
        if car['destination'] == 'Gold Coast' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['make'] == 'Honda Civic' and second_car['time'] == '7am':
                    this_fit -= 1

        #10	The car with a red colour was going to Tamworth.
        if car['color'] == 'red' and car['destination'] == 'Tamworth':
            this_fit -= 1

        #11	To the left of the car that left at 7:00am was the car with a white colour.
        if car['color'] == 'white' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['time'] == '7am':
                    this_fit -= 1

        #12	The last car was hired by an Indian man.
        if car['position'] == 4 and car['person'] == 'Indian':
            this_fit -= 1

        #13	The car with a black colour left at 8:00am.
        if car['color'] == 'black' and car['time'] == '8am':
            this_fit -= 1

        #14	The car carrying an Indian man was to the right of the car hired by a Chinese businessman.
        if car['person'] == 'Chinese' and car['position'] != 4:
            next_index = car['position'] + 1
            for second_car in solution_test:
                if second_car['position'] == next_index and second_car['person'] == 'Indian':
                    this_fit -= 1

        #15	The car heading for Tamworth left at 6:00am.
        if car['destination'] == 'Tamworth' and car['time'] == '6am':
            this_fit -= 1

    return this_fit

print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘\n")

print("Hello! I'm the PLGPS, the Python Logic Grid Puzzle Solver! \n"
      "I was written by Rachel Johnson for COSC550 at UNE.\n"
      "I was programmed to solve this puzzle: http://bit.ly/COSC550_puzzle_description\n"
      "I use simulated annealing to perform my search.\n"
      "Should I get stuck in a local maximum, I am programmed to restart my search from a new starting point\n"
      "(You'll see these as 'runs').\n"
      "So, we're ready? Press ENTER to get me going!")
input()
t0 = tt.time()
# While we want the loop to keep running
while run:
    runs += 1
    iterations = 0
    # GENERATE RANDOM START SOLUTION

    # variables
    position = [0, 1, 2, 3, 4]
    color = ['black', 'blue', 'green', 'red', 'white']
    make = ['Holden Barina', 'Honda Civic', 'Hyundai Accent', 'Nissan X-Trail', 'Toyota Camry']
    time = ['5am', '6am', '7am', '8am', '9am']
    person = ['British', 'Canadian', 'Chinese', 'French', 'Indian']
    destination = ['Gold Coast', 'Newcastle', 'Port Macquarie', 'Sydney', 'Tamworth']

    # seed for starter solution
    random.shuffle(position)
    random.shuffle(color)
    random.shuffle(make)
    random.shuffle(time)
    random.shuffle(person)
    random.shuffle(destination)

    # random starter solution
    solution = []
    for i in range(0, 5):
        solution.append(
            {'position': position[i], 'color': color[i], 'make': make[i], 'time': time[i], 'person': person[i], 'destination': destination[i]}
        )

    # SEARCH ALGO
    while iterations < 5000:
        temp = 0.0015
        cooling = 0.9999
        fit = 100

        while temp > 0.000000001 and fit > 0:
            if iterations % 100 == 0:
                print(f"Run {runs}: Iterations {iterations}-{iterations+100}...")
            iterations += 1

            if iterations > 5000:
                # max runs reached. Restart algo
                break
            # the actual solution (for testing reasons)
            # solutionTest = [
            #     {'position': 0, 'color': 'blue', 'make': 'Holden Barina', 'time': '5am', 'person': 'Canadian', 'destination': 'Newcastle'},
            #     {'position': 1, 'color': 'red', 'make': 'Toyota Camry', 'time': '6am', 'person': 'British', 'destination': 'Tamworth'},
            #     {'position': 2, 'color': 'black', 'make': 'Nissan X-Trail', 'time': '8am', 'person': 'French', 'destination': 'Sydney'},
            #     {'position': 3, 'color': 'white', 'make': 'Hyundai Accent', 'time': '9am', 'person': 'Chinese', 'destination': 'Gold Coast'},
            #     {'position': 4, 'color': 'green', 'make': 'Honda Civic', 'time': '7am', 'person': 'Indian', 'destination': 'Port Macquarie'},
            # ]
            #
            # to find the solutionTest, randomly pick an attribute and swap 2 random cars
            solutionTest = copy.deepcopy(solution)
            attributes = ['position', 'color', 'make', 'time', 'person', 'destination']
            rand_attribute = random.choice(attributes)
            car1 = random.randint(0, 4)
            car2 = random.randint(0, 4)
            while car2 == car1:
                car2 = random.randint(0, 4)
            solutionTest[car1][rand_attribute], solutionTest[car2][rand_attribute] = solutionTest[car2][rand_attribute], solutionTest[car1][rand_attribute]

            fitTest = check_fit(solutionTest)
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
        if fit == 0:
            run = False
            print("\n----------------------------\n")
            print("I solved the puzzle!")
            print(f"I used {iterations} iterations on Run {runs}")
            if runs>1:
                print(f"(Therefore a total of {(runs-1)*5000 + iterations} iterations).")
            print(f"It took me {tt.time() - t0} seconds")
            print("\n----------------------------\n")
            solution.sort(key=operator.itemgetter('position'))
            print("{:<5} {:<7} {:<16} {:<5} {:<10} {:<16}".format('Pos', 'Color', 'Make', 'Time', 'Person', 'Destination'))
            for car in solution:
                print("{:<5} {:<7} {:<16} {:<5} {:<10} {:<16}".format(car['position']+1, car['color'].capitalize(), car['make'], car['time'], car['person'], car['destination']))
                if car['destination'] == 'Port Macquarie':
                    port_mac_car = car['make']
                if car['person'] == 'Canadian':
                    canadian_car = car['make']
            print(f"\nThe {port_mac_car} was going to Port Macquarie. The {canadian_car} was hired by a Canadian couple.\n")
            print("----------------------------\n")
            print(f"Thanks for hanging out! Catch you next time.")
            print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘\n")
        break
