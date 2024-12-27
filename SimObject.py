import random
import logging
from types import MappingProxyType
from typing import Final

######
###### SimObject
######
class SimObject:
  STATE : Final = "state"
  PROBABILITY : Final = "probability"

  def __init__(self, state=None, name="object"):
    self.state = state
    self.NAME : Final = name
    self.ERROR_MESSAGE = f"Invalid state for {__name__} ({self.get_state()})."

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

    self.ERROR_MESSAGE = "Invalid state. State must be 0 or 1"
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
      raise ValueError(self.ERROR_MESSAGE)

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
    logging.debug(f"{type(self)} state: {self.state}")

    self.ERROR_MESSAGE = "Invalid state. State must be 0, 1, or 2."
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