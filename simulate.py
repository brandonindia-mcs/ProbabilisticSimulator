# from ProbabilisticSimulator import *
from ProbabilisticSimulator import ProbabilisticSimulator
from ProbabilisticSimulator import BinarySimulator
from ProbabilisticSimulator import BitSimulator
from ProbabilisticSimulator import CoinSimulator
from ProbabilisticSimulator import TresSimulator
from ProbabilisticSimulator import StatesListSimulator
from ProbabilisticSimulator import NamedStatesSimulator
from ProbabilisticSimulator import StatesSimulator
from ProbabilisticSimulator import SimObject
from ProbabilisticSimulator import BitObject
from ProbabilisticSimulator import BitObject
import sys
import logging
logging.basicConfig(filename=f"{__name__}.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
def sim_test(test_id="TEST"):
    logging.info(f"\n### simulate.py ### {test_id} test ######################")
def is_positive_int(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def print_object(object):
    print("object is:"+str(object.get_state()))
    
def testing_round_1():
    all_positive_ints = True
    sim_test("CONTROL BASE TEST: ProbabilisticSimulator")
    simulator = ProbabilisticSimulator()
    simulator.add_event("Heads", 0.5)
    simulator.add_event("Tails", 0.5)

    results = simulator.simulate(100)
    logging.debug(f"Results: {results}")

    sim_test("POSITIVE INTEGERS")
    for arg in sys.argv[1:]:  # Skip the script name (sys.argv[0])
        if not is_positive_int(arg):
            print(f"{arg} is not a positive integer.")
            all_positive_ints = False
            break  # No need to check further

    if all_positive_ints:
        print("All arguments are positive integers.")

    sim_test("OBJECT CUSTOM PRINT")
    obj = SimObject(name="object1")
    print(obj)

    sim_test("OBJECT INSTANCES/TYPES")
    print(type(simulator))
    print(isinstance(simulator, ProbabilisticSimulator))
    print(type(obj))
    print(isinstance(obj, SimObject))

    sim_test("BinarySimulator")
    object_simulator = BinarySimulator(NUMBER_OF_OBJECTS)
    print(object_simulator.simulate(NUMBER_OF_SIMULATIONS))

def bit_tests():
    sim_test("BIT STATE")
    b = BitObject().print()
    b.set_on().print()
    b.set_off().print()
    b.set_state(1).print()
    b.set_state(0).print()
    b.toggle().print()
    b.toggle().print()
    b.toggle().print()

    sim_test("BIT INHERITANCE")
    b = BitObject(name="this").print()
    b.toggle().print()
    b.toggle().print()
    b.set_state(1).print()
    try:
        b.set_state(2).print()
    except:
        print(f"*** Error: {type(b)} objects accept a 0 or a 1")
    b.set_state(1).print()
    print(f"bit state is {b.get_state()}")

def bit_simulator(number_of_bits=1, number_of_tests=10):
    sim_test("BIT SIMULATOR")
    results = BitSimulator(number_of_bits).simulate(number_of_tests)
    logging.debug(f"Results: {results}")
    for state, result in results.items():
        print(f"state: {state} result: {result}")

def coin_simulator(number_of_bits=1, number_of_tests=10):
    sim_test("COIN SIMULATOR")
    results = CoinSimulator(number_of_bits).simulate(number_of_tests)
    logging.debug(f"Results: {results}")
    for state, result in results.items():
        print(f"state: {state} result: {result}")

def tres_simulator():
    sim_test("TRES SIMULATOR")
    results = TresSimulator(5).simulate(10)
    logging.debug(f"Results: {results}")
    for state, result in results.items():
        print(f"state: {state} result: {result}")
        
def states_simulator():
    sim_test("STATES SIMULATOR 1")
    states_sim = StatesSimulator({
      0:{"probability":.10},
      1:{"probability":.20},
      2:{"probability":.70}
    })
    results = states_sim.simulate(2)
    logging.debug(f"Results:\n\t{results}")
    for sim_run, result in results.items():
      print(f"\n\tsim_run: {sim_run}\n\t\tresult: {result}")

    sim_test("STATES SIMULATOR 2")
    states_sim = StatesSimulator({
      0:{"probability":.10},
      1:{"probability":.20},
      2:{"probability":.15},
      3:{"probability":.12},
      4:{"probability":.13},
      5:{"probability":.30}
    })
    results = states_sim.simulate(3)
    logging.debug(f"Results:\n\t{results}")
    for sim_run, result in results.items():
      print(f"\n\tsim_run: {sim_run}\n\t\tresult: {result}")

    return

def named_states_simulator():
    sim_test("NAMED STATES SIMULATOR")
    named_states_sim = NamedStatesSimulator({
      0:{"state":"STATE_ZERO","probability":.10},
      1:{"state":"STATE_ONE","probability":.20},
      2:{"state":"STATE_TWO","probability":.70}
    })
    results = named_states_sim.simulate(2)
    logging.debug(f"Results:\n\t{results}")
    for sim_run, result in results.items():
      print(f"\n\tsim_run: {sim_run}\n\t\tresult: {result}")

    return

def state_in_list_simulator():
    sim_test("STATES IN LIST SIMULATOR")
    states_sim = StatesListSimulator([
      {"probability":.10},
      {"probability":.20},
      {"probability":.15},
      {"probability":.12},
      {"probability":.13},
      {"probability":.02},
      {"probability":.06},
      {"probability":.22}
    ])
    try:
        results = states_sim.simulate(10000)
    except ValueError as error:
        raise
    logging.debug(f"Results:\n\t{results}\n")
    for state, result in results.items():
      print(f"\tstate {state}:\t{result}")
    return

if __name__ == "__main__":
    sim_test("ARGUMENTS")
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", sys.argv)

    try:
        print("sys.argv[1]:"+sys.argv[1])
        print("sys.argv[2]:"+sys.argv[2])
        NUMBER_OF_OBJECTS = int(sys.argv[1])
        NUMBER_OF_SIMULATIONS = int(sys.argv[2])
    except:
        NUMBER_OF_OBJECTS = 1
        NUMBER_OF_SIMULATIONS = 10
    print("NUMBER_OF_OBJECTS:" + str(NUMBER_OF_OBJECTS))
    print("NUMBER_OF_SIMULATIONS:" + str(NUMBER_OF_SIMULATIONS))

    testing_round_1()
    bit_tests()
    bit_simulator(1,10)
    coin_simulator(NUMBER_OF_OBJECTS,NUMBER_OF_SIMULATIONS)
    tres_simulator()
    states_simulator()
    named_states_simulator()
    state_in_list_simulator()


