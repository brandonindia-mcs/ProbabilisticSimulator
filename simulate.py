from ProbabilisticSimulator import *
import sys
def sim_test(test_id="TEST"):
    print(f"\n##### simulate.py ### {test_id} test #####")
def is_positive_int(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def print_object(object):
    print("object is:"+str(object.get_state()))

if __name__ == "__main__":
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

    print("sys.argv[1]:"+sys.argv[1])
    print("sys.argv[2]:"+sys.argv[2])
    NUMBER_OF_OBJECTS_UNDER_TEST = sys.argv[1]
    NUMBER_OF_SIMULATIONS = sys.argv[2]
    print("NUMBER_OF_OBJECTS_UNDER_TEST:" + NUMBER_OF_OBJECTS_UNDER_TEST)
    print("NUMBER_OF_SIMULATIONS:" + NUMBER_OF_SIMULATIONS)

    sim_test("POSITIVE INTEGERS")
    for arg in sys.argv[1:]:  # Skip the script name (sys.argv[0])
        if not is_positive_int(arg):
            print(f"{arg} is not a positive integer.")
            all_positive_ints = False
            break  # No need to check further

    if all_positive_ints:
        print("All arguments are positive integers.")
    
    sim_test("OBJECT CUSTOM PRINT")
    b1 = SimObject(name="object1")
    print(b1)
    b1.NAME = "should not have been changed"
    print(b1)

    sim_test("OBJECT INSTANCES/TYPES")
    print(type(simulator))
    print(isinstance(simulator, ProbabilisticSimulator))
    print(type(b1))
    print(isinstance(b1, SimObject))

    sim_test("OBJECT STATE")
    b = SimObject()
    b.print()
    b.set_on()
    b.print()
    b.set_off()
    b.print()
    b.set_state(1)
    b.print()
    b.set_state(0)
    b.print()
    b.toggle()
    b.print()
    b.toggle()
    b.print()
    b.toggle()
    b.print()

    sim_test("ObjectSimulator")
    object_simulator = ObjectSimulator(int(NUMBER_OF_OBJECTS_UNDER_TEST))
    print(object_simulator.simulate(int(NUMBER_OF_SIMULATIONS)))

