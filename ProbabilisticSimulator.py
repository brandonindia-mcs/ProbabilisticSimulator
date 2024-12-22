import random
from types import MappingProxyType
from typing import Final

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
    results = {event_name: 0 for event_name in self.events}
    for _ in range(num_trials):
      random_number = random.random()
      cumulative_probability = 0
      for event_name, probability in self.events.items():
        cumulative_probability += probability
        if random_number <= cumulative_probability:
          results[event_name] += 1
          break
    return results

######
###### BinarySimulator
######
class BinarySimulator(ProbabilisticSimulator):
  def __init__(self, n):
    super().__init__()
    probability = 100/n/100
    print("Equal probability: "+str(probability))
    for i in range(1, n + 1):
      self.add_event(Bit(name="bit-"+str(i)), probability)

  # def get_results(self, num_trials):
  #   print("These are the results:")
  #   results = {}
  #   for k,v in self.events.items():
  #     print(k)
  #     print(v)
  #     results[k]=v
  #   return results

  def add_event(self, bit, probability):
    """
    Adds an event to the simulator with a given probability.

    Args:
      event_name: The name of the event.
      probability: The probability of the event occurring (between 0 and 1).
    """
    if not (0 <= probability <= 1):
      raise ValueError("Probability must be between 0 and 1.")
    self.events[bit.NAME] = probability

######
###### QuantumSimulator
######
class QuantumSimulator(ProbabilisticSimulator):
  def __init__(self):
    self.events = {}

######
###### Bit
######
class Bit:
  def __init__(self, state=0, name="bit"):
    if state not in [0, 1]:
      raise ValueError("Invalid state. State must be 0 or 1.")
    self.state = state
    self.NAME : Final = name

    self.states = MappingProxyType({
      0:"Off",
      1:"On"
    })
  
  def print(self):
      print("bit " + self.NAME + " is: "+self.states.get((self.get_state())))

  def get_state(self):
      return self.state

  def set_on(self):
    self.state = 1

  def set_off(self):
    self.state = 0

  def set_state(self, state):
    if state not in [0, 1]:
        raise ValueError("Invalid state. State must be 0 or 1.")
    self.state = state

  def toggle(self):
    self.state=int(bin(self.state ^ 1), 2)

  def __str__(self):
      return "bit " + self.NAME + " is: "+self.states.get((self.get_state()))
