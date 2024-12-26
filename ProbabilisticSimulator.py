import random
import logging
from types import MappingProxyType
from typing import Final

def sim_test(test_id="TEST"):
    logging.info(f"\n### ProbabilisticSimulator.py ### {test_id} #******************#")
######
###### ProbabilisticSimulator
######
class ProbabilisticSimulator:

  # Configure the logging module
  logging.basicConfig(filename=f"{__name__}.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

  # Log a message
  # logging.debug("This is a debug message")
  # logging.info("This is an info message")
  # logging.warning("This is a warning message")
  # logging.error("This is an error message")
  # logging.critical("This is a critical message")

  """
  A simple probabilistic simulator that allows you to define events with probabilities
  and simulate their occurrence.
  """

  def __init__(self):
    # self.logger = logging.getLogger(__name__)
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
    logging.debug(f"events {self.events}")

    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    results = {event_name: 0 for event_name in self.events}

    ### DEBUG
    logging.debug(f"{type(self)}::get_results: initialized results: {results}")

    for _ in range(num_trials):
      random_number = random.random()
      cumulative_probability = 0
      logging.debug(f"Doing results")
      for event_name, probability in self.events.items():
        logging.debug(f"Result\n\tevent_name: {event_name}\n\tprobabiliity: {probability}")
        cumulative_probability += probability
        if random_number <= cumulative_probability:
          results[event_name] += 1
          break

    ### DEBUG
    logging.debug(f"returning results: {results}")
    
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
    logging.info("Equal probability: "+str(probability))
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
    logging.debug(f"{type(self)}::setup(self, n)")

    for i in range(0, n):
      self.add_event(BitObject(name="bit-"+str(i)))

    ### DEBUG
    logging.debug(f"{type(self)}::setup(self, n): events {self.events}")

  def add_event(self, bit, probability=None):
    ### DEBUG
    logging.debug(f"{type(self)}::add_event: adding events for: {bit}")

    tmp0 = {}
    for k, v in bit.states.items():
      ### DEBUG
      logging.debug(f"k is {k} v is {v}")

      tmp1 = {f"{bit.NAME}-{k}":v}
      tmp0.update(tmp1.items())

      ### DEBUG
      logging.debug(f"tmp1: {tmp1}")

    ### DEBUG
    logging.debug(f"tmp0: {tmp0}")

    self.events[f"{bit.NAME}"] = tmp0

  def get_results(self, num_trials):
    sim_test(f"{type(self)}::get_results(self, num_trials):")

    ### DEBUG
    logging.debug(f"{type(self)}::get_results: events {self.events}")

    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    tmp = {}
    for k1 in self.events.keys():
      tmp.update(self.events[k1])
    results = {event_name: 0 for event_name in tmp.keys()}

    ### DEBUG
    logging.debug(f"{type(self)}::get_results: initialized results: {results}")

    for _ in range(num_trials):
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        logging.info(f"\nrandom_number: {round(random_number, 2)}")
        logging.info(f"cumulative_probability: {cumulative_probability}")
        logging.debug(f"Result\n\tevent_name: {event_name} is a {type(event_name)}\n\tprobabiliity: {probability} is a {type(probability)}")
        for ref, dict in probability.items():
          logging.debug(f"\t\tref: {ref} is a {type(ref)}\n\t\tdict: {dict} is a {type(dict)}")
          cumulative_probability += dict["probability"]
          logging.debug(f"cumulative_probability: {cumulative_probability}")
          logging.info(f"is: {round(random_number, 2)} <= {cumulative_probability}: {random_number <= cumulative_probability}")
          if random_number <= cumulative_probability:
            results[ref] += 1
            logging.info(f"{event_name} is {dict["state"]}")
            break

      ### DEBUG
      logging.debug(f"{type(self)}::get_results: results:\n\t{results}")

    ### DEBUG
    logging.debug(f"{type(self)}::get_results: returning results: {results}")

    return results

######
###### CoinSimulator
######
class CoinSimulator(BitSimulator):
  def __init__(self, n=1):
    super().__init__(n)

  def setup(self, n):
    for i in range(0, n):
      self.add_event(Coin(name="coin-"+str(i)))

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

  ### MOVE TO NEW "PARENT CLASS"
  def set_states(self, states):
    self.states = states
  
######
###### BitObject
######
class BitObject(SimObject):
  def __init__(self, state=0, name="bit"):
    super().__init__(state, name)
    self.set_state(state)

    ### DEBUG
    logging.debug(f"{type(self)} state: {self.state}")

    self.set_states(MappingProxyType({
      0:{"state":"Off","probability":.5},
      1:{"state":"On","probability":.5}
    }))

    ### DEBUG
    logging.debug(f"{type(self)}::init: {self.NAME} number of states: {len(self.states)}")

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
    self.validate_state()
    return self

  def validate_state(self):
    if self.state not in [0, 1]:
        raise ValueError("Invalid state. State must be 0 or 1.")

  def toggle(self):
    self.state=int(bin(self.state ^ 1), 2)
    return self

######
###### Coin
######
class Coin(BitObject):
  def __init__(self, state="HEADS", name="coin"):
    super().__init__(state, name)

    ### DEBUG
    logging.debug(f"{type(self)} state: {self.state}")

    self.set_states(MappingProxyType({
      "HEADS":{"state":"heads","probability":.5},
      "TAILS":{"state":"tails","probability":.5}
    }))

  def set_on(self):
    self.state = "TAILS"
    return self

  def set_off(self):
    self.state = "HEADS"
    return self

  def validate_state(self):
    if self.state not in ["HEADS", "TAILS"]:
        raise ValueError("Invalid state. State must be HEADS or TAILS.")

  def toggle(self):
    if self.state == "HEADS":
      return self.set_on()
    return self.set_off
  
######
###### TresObject
######
class TresObject(SimObject):
  def __init__(self, state=0, name="tres"):
    super().__init__(state, name)
    self.set_state(state)

    ### DEBUG
    logging.debug(f"{type(self)} state: {self.state}")

    self.ERROR_MESSAGE = "Invalid state. State must be 0, 1, or 2."
    if self.state not in [0, 1, 2]:
      raise ValueError(self.ERROR_MESSAGE)

    self.set_states(MappingProxyType({
      0:{"state":"STATE_ZERO","probability":.33},
      1:{"state":"STATE_ONE","probability":.34},
      2:{"state":"STATE_TWO","probability":.33}
    }))

    ### DEBUG
    logging.debug(f"{type(self)}::init: {self.NAME} number of states: {len(self.states)}")

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

######
###### StatesSimulator
######
class StatesSimulator(ProbabilisticSimulator):
  def __init__(self, states={}, bit_count=1):
    super().__init__()
    logging.debug(f"*** {type(self)}::constructor")
    self.states = states
    self.bit_count = bit_count
    self.add_event(states)

  def add_event(self, obj, probability=None):
    tmp0 = {}
    for k, v in obj.items():
      tmp1 = {f"{k}":v}
      tmp0.update(tmp1.items())
    self.events[f"{k}"] = tmp0

  def get_results(self, num_trials):
    results = {}
    for k, dict in self.events.items():
      for k1, dict1 in dict.items():
        results[k1] = 0

    ### DEBUG
    logging.debug(f"results: {results}")

    for _ in range(num_trials):
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        for ref, dict in probability.items():
          cumulative_probability += dict["probability"]
          if random_number <= cumulative_probability:
            results[ref] += 1
            break

    return results

  def simulate(self, num_trials):
    results = {}
    for i in range(0, num_trials):
      results[i] = self.get_results(num_trials)
    return results
  
######
###### NamedStatesSimulator
######
class NamedStatesSimulator(StatesSimulator):
  def __init__(self, states={}, bit_count=1):
    super().__init__(states, bit_count)
    logging.debug(f"*** {type(self)}::constructor")

  def get_results(self, num_trials):
    # sim_test(f"{type(self)}::get_results(self, num_trials):")
    results = {}
    for k, dict in self.events.items():
      for k1, dict1 in dict.items():
        results[f"{dict1["state"]}"] = 0

    ### DEBUG
    logging.debug(f"self.events: {self.events}")
    logging.debug(f"results initialized: {results}")

    for _ in range(num_trials):
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        for ref, dict1 in probability.items():
          cumulative_probability += dict1["probability"]
          if random_number <= cumulative_probability:
            results[f"{dict1["state"]}"] += 1
            break

    return results

######
###### StatesListSimulator
######
class StatesListSimulator(ProbabilisticSimulator):
  def __init__(self, states=[]):
    super().__init__()
    logging.debug(f"*** {type(self)}::constructor")
    self.states = states
    self.add_event(states)

  def add_event(self, list, probability=None):
    for obj in list:
      tmp1 = {"probability": obj["probability"]}
      self.events[f"{id(tmp1)}"] = tmp1

    logging.debug(f"self.events: {self.events}")

  def simulate(self, num_trials):
    return self.get_results(num_trials)

  def get_results(self, num_trials):
    ### DEBUG
    logging.debug(f"self.events: {self.events}")

    results = {}
    cumulative_probability = 0
    for k, dict in self.events.items():
      for k1, v1 in dict.items():
        cumulative_probability += v1
        results[f"{k}-{100*v1}"] = 0
    if cumulative_probability != 1.0:
      raise ValueError(f"list of probabilities does not total 1.0: {cumulative_probability}")

    ### DEBUG
    logging.debug(f"results initialized: {results}")

    for _ in range(num_trials):
      random_number = random.random()
      cumulative_probability = 0
      for event_name, probability in self.events.items():
        cumulative_probability += probability["probability"]
        if random_number <= cumulative_probability:
          results[f"{event_name}-{100*probability["probability"]}"] += 1
          break

    return results
  
