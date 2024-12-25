from ProbabilisticSimulator import *
import sys
def sim_test(test_id="TEST"):
    print(f"\n### simulate.py ### {test_id} test ######################")
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
    print("Results:")
    print(results)

    sim_test("ARGUMENTS")
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", sys.argv)

    try:
        print("sys.argv[1]:"+sys.argv[1])
        print("sys.argv[2]:"+sys.argv[2])
        NUMBER_OF_OBJECTS_UNDER_TEST = int(sys.argv[1])
        NUMBER_OF_SIMULATIONS = int(sys.argv[2])
    except:
        NUMBER_OF_OBJECTS_UNDER_TEST = 19
        NUMBER_OF_SIMULATIONS = 5000
    print("NUMBER_OF_OBJECTS_UNDER_TEST:" + str(NUMBER_OF_OBJECTS_UNDER_TEST))
    print("NUMBER_OF_SIMULATIONS:" + str(NUMBER_OF_SIMULATIONS))

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
    object_simulator = BinarySimulator(NUMBER_OF_OBJECTS_UNDER_TEST)
    print(object_simulator.simulate(NUMBER_OF_SIMULATIONS))

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


    sim_test("BIT SIMULATOR")
    bit_sim = BitSimulator(5)
    results = bit_sim.simulate(1000)
    print("Results:")
    print(results)

    for state, result in results.items():
        print(f"state: {state} result: {result}")

    sim_test("TRES SIMULATOR")
    tres_sim = TresSimulator(5)
    results = tres_sim.simulate(1000)
    print(results)
    print("Results:")
    for state, result in results.items():
        print(f"state: {state} result: {result}")
        
if __name__ == "__main__":
    # testing_round_1()

    sim_test("STATES SIMULATOR")
    states_sim = StatesSimulator({
      0:{"state":"STATE_ZERO","probability":.10},
      1:{"state":"STATE_ONE","probability":.20},
      2:{"state":"STATE_TWO","probability":.70}
    })
    results = states_sim.simulate(2)
    print(f"Results:\n\t{results}")

    for sim_run, result in results.items():
      print(f"\n\tsim_run: {sim_run}\n\t\tresult: {result}")
