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


class PedestrianLight1:
    def __init__(self, init_state=_TL_RED):
        self.state = init_state
        self.manager = None

    def update_self(self):
        # DONE
        # p1_red
        if self.state == _TL_GREEN and self.manager.p1.state == _TL_RED:
            self.state = _TL_RED
            return
        # p2_red
        if self.state == _TL_GREEN and self.manager.p2.state == _TL_RED:
            self.state = _TL_RED
            return
        # p3_red
        if self.state == _TL_GREEN and self.manager.p3.state == _TL_RED:
            self.state = _TL_RED
            return
        # p4_red
        if self.state == _TL_GREEN and self.manager.p4.state == _TL_RED:
            self.state = _TL_RED
            return

        # p6_green
        if self.state == _TL_RED and self.manager.p6.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p7_1_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p7_2_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return

        # p7_3_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p8_1_red
        if self.state == _TL_GREEN and self.manager.p81.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p8_2_red
        if self.state == _TL_GREEN and self.manager.p82.state == _PHASE_RED:
            self.state = _TL_RED
            return


class PedestrianLight2:
    def __init__(self, init_state=_TL_RED):
        self.state = init_state
        self.manager = None

    def update_self(self):
        # DONE
        # p1_red
        if self.state == _TL_GREEN and self.manager.p1.state == _TL_RED:
            self.state = _TL_RED
            return
        # p2_red
        if self.state == _TL_GREEN and self.manager.p2.state == _TL_RED:
            self.state = _TL_RED
            return
        # p3_red
        if self.state == _TL_GREEN and self.manager.p3.state == _TL_RED:
            self.state = _TL_RED
            return
        # p4_green
        if self.state == _TL_RED and self.manager.p4.state == _TL_GREEN:
            self.state = _TL_GREEN
            return

        # p5_red
        if self.state == _TL_GREEN and self.manager.p5.state == _TL_RED:
            self.state = _TL_RED
            return
        # p7_1_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p7_2_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return

        # p7_3_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p8_1_red
        if self.state == _TL_GREEN and self.manager.p81.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p8_2_red
        if self.state == _TL_GREEN and self.manager.p82.state == _PHASE_RED:
            self.state = _TL_RED
            return


class PedestrianLight3:
    def __init__(self, init_state=_TL_RED):
        self.state = init_state
        self.manager = None

    def update_self(self):
        # DONE
        # p1_red
        if self.state == _TL_GREEN and self.manager.p1.state == _TL_RED:
            self.state = _TL_RED
            return
        # p2_red
        if self.state == _TL_GREEN and self.manager.p2.state == _TL_RED:
            self.state = _TL_RED
            return
        # p3_red
        if self.state == _TL_GREEN and self.manager.p3.state == _TL_RED:
            self.state = _TL_RED
            return
        # p5_green
        if self.state == _TL_RED and self.manager.p5.state == _TL_GREEN:
            self.state = _TL_GREEN
            return

        # p6_red
        if self.state == _TL_GREEN and self.manager.p6.state == _TL_RED:
            self.state = _TL_RED
            return
        # p7_1_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p7_2_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return

        # p7_3_green
        if self.state == _TL_RED and self.manager.p71.state == _TL_GREEN:
            self.state = _TL_GREEN
            return
        # p8_1_red
        if self.state == _TL_GREEN and self.manager.p81.state == _PHASE_RED:
            self.state = _TL_RED
            return
        # p8_2_red
        if self.state == _TL_GREEN and self.manager.p82.state == _PHASE_RED:
            self.state = _TL_RED
            return
