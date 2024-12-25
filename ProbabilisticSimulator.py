import random
from types import MappingProxyType
from typing import Final

def sim_test(test_id="TEST"):
    print(f"\n### ProbabilisticSimulator.py ### {test_id} #******************#")
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
      results from get_results
    """

    return self.get_results(num_trials)
  
  def get_results(self, num_trials):
    sim_test(f"{type(self)}::get_results(self, num_trials):")
    """
    Returns:
      A dictionary where the keys are event names and the values are the number of times
      each event occurred.
    """
    ### DEBUG
    # print(f"events {self.events}")

    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    results = {event_name: 0 for event_name in self.events}

    ### DEBUG
    # print(f"{type(self)}::get_results: initialized results: {results}")

    for _ in range(num_trials):
      random_number = random.random()
      cumulative_probability = 0
      # print(f"Doing results")
      for event_name, probability in self.events.items():
        # print(f"Result\n\tevent_name: {event_name}\n\tprobabiliity: {probability}")
        cumulative_probability += probability
        if random_number <= cumulative_probability:
          results[event_name] += 1
          break
      # print(f"cumulative_probability: {cumulative_probability}")

    ### DEBUG
    # print(f"returning results: {results}")
    
    return results

######
###### BinarySimulator
###### n IS THE NUMBER OF NEW OBJECTS TO CREATE,
###### AND RUN THE SIMULATION ON WITH PROBABILITY
###### EQUALLY DISTRIBUTED
class BinarySimulator(ProbabilisticSimulator):
  def __init__(self, n=1):
    super().__init__()
    self.setup(n)

  def setup(self, n):
    probability = 100/n/100
    print("Equal probability: "+str(probability))
    for i in range(0, n):
      self.add_event(SimObject(name="object-"+str(i)), probability)

  def add_event(self, object, probability):
    self.events[object.NAME] = probability

######
###### BitSimulator
######
class BitSimulator(BinarySimulator):
  def __init__(self, n=1):
    super().__init__(n)

  def setup(self, n):
    ### DEBUG
    # print(f"{type(self)}::setup(self, n)")

    for i in range(0, n):
      self.add_event(BitObject(name="bit-"+str(i)))

  def add_event(self, bit, probability=None):
    ### DEBUG
    # print(f"{type(self)}::add_event: adding events for: {bit}")

    tmp0 = {}
    for k, v in bit.states.items():
      ### DEBUG
      # print(f"k is {k} v is {v}")

      tmp1 = {f"{bit.NAME}-{k}":v}
      tmp0.update(tmp1.items())

      ### DEBUG
      # print(f"tmp1: {tmp1}")

    ### DEBUG
    # print(f"tmp0: {tmp0}")

    self.events[f"{bit.NAME}"] = tmp0

  def get_results(self, num_trials):
    sim_test(f"{type(self)}::get_results(self, num_trials):")

    ### DEBUG
    # print(f"{type(self)}::get_results: events {self.events}")

    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    d = {}
    for k1 in self.events.keys():
      d.update(self.events[k1])
    results = {event_name: 0 for event_name in d.keys()}

    ### DEBUG
    # print(f"{type(self)}::get_results: initialized results: {results}")

    for _ in range(num_trials):
      # print(f"Doing results")
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        # print(f"Result\n\tevent_name: {event_name} is a {type(event_name)}\n\tprobabiliity: {probability} is a {type(probability)}")
        for ref, dict in probability.items():
          # print(f"\t\tref: {ref} is a {type(ref)}\n\t\tdict: {dict} is a {type(dict)}")
          cumulative_probability += dict["probability"]
          if random_number <= cumulative_probability:
            results[ref] += 1
            break

    ### DEBUG
    # print(f"{type(self)}::get_results: returning results: {results}")

    return results

######
###### TresSimulator
######
class TresSimulator(BitSimulator):
  def __init__(self, n=1):
    super().__init__(n)

  def setup(self, n):
    for i in range(0, n):
      self.add_event(TresObject(name="tres-"+str(i)))

######
###### SimObject
######
class SimObject:
  def __init__(self, state=None, name="object"):
    self.ERROR_MESSAGE = "Invalid state."
    self.state = state
    self.NAME : Final = name

  def __str__(self):
      return f"object {type(self)} is: {self.NAME} is: {self.get_state()}"
  
  def print(self):
      print(f"object {type(self)} is: {self.NAME} is: {self.get_state()}")
      return self

  def get_state(self):
      return self.state

  def set_state(self, state):
    self.state = state
  
######
###### BitObject
######
class BitObject(SimObject):
  def __init__(self, state=0, name="bit"):
    super().__init__(state, name)
    self.set_state(state)

    ### DEBUG
    print(f"{type(self)} state: {self.state}")

    if self.state not in [0, 1]:
      raise ValueError("Invalid state. State must be 0 or 1.")

    self.states = MappingProxyType({
      0:{"state":"Off","probability":.5},
      1:{"state":"On","probability":.5}
    })

    ### DEBUG
    # print(f"{type(self)}::init: {self.NAME} number of states: {len(self.states)}")

  def __str__(self):
      return f"object {type(self)} {self.NAME} is: {self.states.get(self.get_state())}"
  
  def print(self):
      print(f"object {type(self)} {self.NAME} is: {self.states.get(self.get_state())}")
      return self

  def set_on(self):
    self.state = 1
    return self

  def set_off(self):
    self.state = 0
    return self

  def set_state(self, state):
    super().set_state(state)
    if self.state not in [0, 1]:
        raise ValueError("Invalid state. State must be 0 or 1.")
    return self

  def toggle(self):
    self.state=int(bin(self.state ^ 1), 2)
    return self
  
######
###### TresObject
######
class TresObject(SimObject):
  def __init__(self, state=0, name="tres"):
    super().__init__(state, name)
    self.set_state(state)

    ### DEBUG
    print(f"{type(self)} state: {self.state}")

    self.ERROR_MESSAGE = "Invalid state. State must be 0, 1, or 2."
    if self.state not in [0, 1, 2]:
      raise ValueError(self.ERROR_MESSAGE)

    self.states = MappingProxyType({
      0:{"state":"STATE_ZERO","probability":.33},
      1:{"state":"STATE_ONE","probability":.34},
      2:{"state":"STATE_TWO","probability":.33}
    })

    ### DEBUG
    # print(f"{type(self)}::init: {self.NAME} number of states: {len(self.states)}")

  def __str__(self):
      return f"object {type(self)} {self.NAME} is: {self.states.get(self.get_state())}"
  
  def print(self):
      print(f"object {type(self)} {self.NAME} is: {self.states.get(self.get_state())}")
      return self

  def set_state(self, state):
    super().set_state(state)
    if self.state not in [0, 1, 2]:
        raise ValueError(self.ERROR_MESSAGE)
    return self

import hashlib
######
###### StatesSimulator
######
class StatesSimulator(ProbabilisticSimulator):
  def __init__(self, n=1, states={}):
    super().__init__()
    self.states = states
    self.setup(n, states)

  def setup(self, n, states):
    for i in range(0, n):
      self.add_event(states)

  def add_event(self, obj, probability=None):
    tmp0 = {}
    for k, v in obj.items():
      tmp1 = {f"{k}":v}
      tmp0.update(tmp1.items())
    self.events[f"{hashlib.sha256(str(obj).encode()).hexdigest()}"] = tmp0

  def get_results(self, num_trials):
    sim_test(f"{type(self)}::get_results(self, num_trials):")
    d = {}
    for k1 in self.events.keys():
      d.update(self.events[k1])
    results = {event_name: 0 for event_name in d.keys()}

    for _ in range(num_trials):
      # print(f"Doing results")
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        # print(f"Result\n\tevent_name: {event_name} is a {type(event_name)}\n\tprobabiliity: {probability} is a {type(probability)}")
        for ref, dict in probability.items():
          # print(f"\t\tref: {ref} is a {type(ref)}\n\t\tdict: {dict} is a {type(dict)}")
          cumulative_probability += dict["probability"]
          if random_number <= cumulative_probability:
            results[ref] += 1
            break

    return results

