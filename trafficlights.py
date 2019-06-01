# Constants
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


class TrafficLight1:
    def __init__(self, init_state=_TL_RED):
        self.state = init_state
        self.manager = None

    def update_self(self):
        # DONE
        # p3_red
        if self.state == _TL_GREEN and self.manager.p3.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p2_green
        if self.state == _TL_RED and self.manager.p2.state == _PHASE_GREEN:
            self.state = _TL_GREEN
            return
        # p5_green
        if self.state == _TL_RED and self.manager.p5.state == _PHASE_GREEN:
            self.state = _TL_GREEN
            return
        # p6_red
        if self.state == _TL_GREEN and self.manager.p6.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p7_2_red
        if self.state == _TL_GREEN and self.manager.p72.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p8_2_red
        if self.state == _TL_GREEN and self.manager.p82.state == _PHASE_RED:
            self.state = _TL_RED
            return
