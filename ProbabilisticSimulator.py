import random
from types import MappingProxyType
from typing import Final

def sim_test(test_id="TEST"):
    print(f"\n### ProbabilisticSimulator.py ### {test_id} ###")
######
###### ProbabilisticSimulator
######
class ProbabilisticSimulator:
  """
  A simple probabilistic simulator that allows you to define events with probabilities
  and simulate their occurrence.
  """

  def __init__(self):
    self.events = {}

  def add_event(self, event_name, probability):
    """
    Adds an event to the simulator with a given probability.

    Args:
      event_name: The name of the event.
      probability: The probability of the event occurring (between 0 and 1).
    """
    if not (0 <= probability <= 1):
      raise ValueError("Probability must be between 0 and 1.")
    self.events[event_name] = probability

  def simulate(self, num_trials):
    """
    Runs a simulation of the events for a given number of trials.

    Args:
      num_trials: The number of trials to run.

    Returns:
      A dictionary where the keys are event names and the values are the number of times
      each event occurred.
    """

    return self.get_results(num_trials)
  
  def get_results(self, num_trials):
    sim_test("get_results")
    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    results = {event_name: 0 for event_name in self.events}

    ### DEBUG
    print(f"results initialized: {results}")

    for _ in range(num_trials):
      random_number = random.random()
      cumulative_probability = 0
      for event_name, probability in self.events.items():
        cumulative_probability += probability
        if random_number <= cumulative_probability:
          results[event_name] += 1
          break
      # print(f"cumulative_probability: {cumulative_probability}")

    ### DEBUG
    print(f"returning results: {results}")
    
    return results

######
###### ObjectSimulator
######
class ObjectSimulator(ProbabilisticSimulator):
  def __init__(self, n):
    super().__init__()
    probability = 100/n/100
    print("Equal probability: "+str(probability))
    for i in range(1, n + 1):
      self.add_event(SimObject(name="object-"+str(i)), probability)

  def add_event(self, object, probability):
    """
    Adds an event to the simulator with a given probability.

    Args:
      event_name: The name of the event.
      probability: The probability of the event occurring (between 0 and 1).
    """
    if not (0 <= probability <= 1):
      raise ValueError("Probability must be between 0 and 1.")
    self.events[object.NAME] = probability

######
###### QuantumSimulator
######
class QuantumSimulator(ProbabilisticSimulator):
  def __init__(self):
    self.events = {}

######
###### SimObject
######
class SimObject:
  def __init__(self, state=None, name="object"):
    self.state = state
    self.NAME : Final = name

  def __str__(self):
      return f"object {self.NAME} is: {self.get_state()}"
  
  def print(self):
      print(f"object {self.NAME} is: {self.get_state()}")
      return self

  def get_state(self):
      return self.state

  def set_state(self, state):
    self.state = state

######
###### Bit
######
class Bit(SimObject):
  def __init__(self, state=0, name="bit"):
    super().__init__(state, name)
    if self.state not in [0, 1]:
      raise ValueError("Invalid state. State must be 0 or 1.")

    self.states = MappingProxyType({
      0:"Off",
      1:"On"
    })

  def __str__(self):
      return f"{type(self)} {self.NAME} is: {self.states.get(self.get_state())}"
  
  def print(self):
      print(f"{type(self)} {self.NAME} is: {self.states.get(self.get_state())}")
      return self

  def set_on(self):
    self.state = 1
    return self

  def set_off(self):
    self.state = 0
    return self

  def set_state(self, state):
    super(Bit, self).set_state(state)
    if self.state not in [0, 1]:
        raise ValueError("Invalid state. State must be 0 or 1.")
    return self

  def toggle(self):
    self.state=int(bin(self.state ^ 1), 2)
    return self

