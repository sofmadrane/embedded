# Constants
import numpy as np
_TL_RED = 0
_TL_GREEN = 1
_TL_ORANGE = 2

_PB_DEACTIVATE = False
_PB_ACTIVATE = True

_YES = True
_NO = False

_PHASE_DEACTIVATE = 0
_PHASE_ORANGE = 1
_PHASE_RED = 2
_PHASE_GREEN = 3
_PHASE_FINISH = 4


class Firemen:
    def __init__(self, init_state=_NO):
        self.state = init_state
        self.manager = None

    def needs_to_cross(self):
        return np.random.choice([True, False], 1, p=[0.1, 0.9])

    def update_self(self):
        # DONE
        # p1_green
        if self.state == _NO:
            if self.needs_to_cross():
                self.state = _YES
            return

        if self.state == _YES and (self.manager.p81.state == _PHASE_RED or
                                   self.manager.p82.state == _PHASE_RED or
                                   self.manager.p83.state == _PHASE_RED):
            self.state = _NO
