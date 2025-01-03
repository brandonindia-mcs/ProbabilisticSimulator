import random
import logging
from SimObject import SimObject
from SimObject import BitObject
from SimObject import TresObject
from types import MappingProxyType
from typing import Final

def sim_test(test_id="TEST"):
    logging.info(f"\n### ProbabilisticSimulator.py ### {test_id} #******************#")
######
###### ProbabilisticSimulator
######
class ProbabilisticSimulator:

  # Configure the logging module
  FORMAT='%(asctime)s:%(levelname)8s:<%(filename)s:%(lineno)s>%(funcName)s()] %(message)s'
  logging.basicConfig(filename=f"{__name__}.log", level=logging.ERROR, format=FORMAT)

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
    self.logger = logging.getLogger(__name__)
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

    return self

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
    self.logger.debug(f"{type(self)}::setup(self, n)")

    for i in range(0, n):
      self.add_event(BitObject(name="bit-"+str(i)))

    ### DEBUG
    self.logger.debug(f"{type(self)}::setup(self, n): events {self.events}")

  def add_event(self, bit, probability=None):
    ### DEBUG
    self.logger.debug(f"{type(self)}::add_event: adding events for: {bit}")

    tmp0 = {}
    for k, v in bit.states.items():
      ### DEBUG
      self.logger.debug(f"k is {k} v is {v}")

      tmp1 = {f"{bit.NAME}-{k}":v}
      tmp0.update(tmp1.items())

      ### DEBUG
      self.logger.debug(f"tmp1: {tmp1}")

    ### DEBUG
    self.logger.debug(f"tmp0: {tmp0}")

    self.events[f"{bit.NAME}"] = tmp0

  def get_results(self, num_trials):
    sim_test(f"{type(self)}::get_results(self, num_trials):")

    ### DEBUG
    self.logger.debug(f"{type(self)}::get_results: events {self.events}")

    # INITIALIZE RESULTS, SET KEYS TO 0 FOR THE SIZE OF EVENTS
    tmp = {}
    for k1 in self.events.keys():
      tmp.update(self.events[k1])
    results = {event_name: 0 for event_name in tmp.keys()}

    ### DEBUG
    self.logger.debug(f"{type(self)}::get_results: initialized results: {results}")

    for _ in range(num_trials):
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        self.logger.info(f"\nrandom_number: {round(random_number, 2)}")
        self.logger.info(f"cumulative_probability: {cumulative_probability}")
        self.logger.debug(f"Result\n\tevent_name: {event_name} is a {type(event_name)}\n\tprobabiliity: {probability} is a {type(probability)}")
        for ref, dict in probability.items():
          self.logger.debug(f"\t\tref: {ref} is a {type(ref)}\n\t\tdict: {dict} is a {type(dict)}")
          cumulative_probability += dict[SimObject.PROBABILITY]
          self.logger.debug(f"cumulative_probability: {cumulative_probability}")
          self.logger.info(f"is: {round(random_number, 2)} <= {cumulative_probability}: {random_number <= cumulative_probability}")
          if random_number <= cumulative_probability:
            results[ref] += 1
            self.logger.info(f"{event_name} is {dict[SimObject.STATE]}")
            break

      ### DEBUG
      self.logger.debug(f"{type(self)}::get_results: results:\n\t{results}")

    ### DEBUG
    self.logger.debug(f"{type(self)}::get_results: returning results: {results}")

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
          cumulative_probability += dict[SimObject.PROBABILITY]
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
        results[f"{dict1[SimObject.STATE]}"] = 0

    ### DEBUG
    logging.debug(f"self.events: {self.events}")
    logging.debug(f"results initialized: {results}")

    for _ in range(num_trials):
      for event_name, probability in self.events.items():
        random_number = random.random()
        cumulative_probability = 0
        for ref, dict1 in probability.items():
          cumulative_probability += dict1[SimObject.PROBABILITY]
          if random_number <= cumulative_probability:
            results[f"{dict1[SimObject.STATE]}"] += 1
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
      tmp1 = {"probability": obj[SimObject.PROBABILITY]}
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
        cumulative_probability += probability[SimObject.PROBABILITY]
        if random_number <= cumulative_probability:
          results[f"{event_name}-{100*probability[SimObject.PROBABILITY]}"] += 1
          break

    return results
  
