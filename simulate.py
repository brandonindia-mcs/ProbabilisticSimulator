from ProbabilisticSimulator import *
import sys
def sim_test(test_id="TEST"):
    print("\n#### "+str(test_id)+" ###")
def is_positive_int(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def print_a_bit(bit):
    print("bit is:"+str(bit.get_state()))

if __name__ == "__main__":
    all_positive_ints = True

    sim_test("ARGUMENTS")
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", sys.argv)

    sim_test("ARGV")
    print(sys.argv[1])
    print(sys.argv[2])

    sim_test("ProbabilisticSimulator")
    simulator = ProbabilisticSimulator()
    simulator.add_event("Heads", 0.5)
    simulator.add_event("Tails", 0.5)

    results = simulator.simulate(100)
    print("Results:")
    print(results)

    sim_test("POSITIVE INTEGERS")
    for arg in sys.argv[1:]:  # Skip the script name (sys.argv[0])
        if not is_positive_int(arg):
            print(f"{arg} is not a positive integer.")
            all_positive_ints = False
            break  # No need to check further

    if all_positive_ints:
        print("All arguments are positive integers.")
    
    sim_test("BIT CUSTOM PRINT")
    b1 = Bit(name="bit1")
    print(b1)
    b1.NAME = "should not be changed"
    print(b1)

    sim_test("BIT STATE")
    b=Bit()
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

    sim_test("OBJECT INSTANCES/TYPES")
    print(type(simulator))
    print(isinstance(simulator, ProbabilisticSimulator))
    print(type(b))
    print(isinstance(b, Bit))

    sim_test("BinarySimulator")
    binary_simulator = BinarySimulator(int(sys.argv[1]))
    print(binary_simulator.simulate(int(sys.argv[2])))

