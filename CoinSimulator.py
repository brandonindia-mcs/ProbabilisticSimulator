import logging
from types import MappingProxyType
from typing import Final
from ProbabilisticSimulator import BitObject
from ProbabilisticSimulator import BitSimulator
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
###### Coin
######
class Coin(BitObject):
  def __init__(self, state="HEADS", name="coin"):
    super().__init__(state, name)

    ### DEBUG
    logging.debug(f"{type(self)} state: {self.state}")

    self.ERROR_MESSAGE = "Invalid state. State must be HEADS or TAILS."
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
      raise ValueError(self.ERROR_MESSAGE)

  def toggle(self):
    if self.state == "HEADS":
      return self.set_on()
    return self.set_off