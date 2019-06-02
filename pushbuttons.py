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


class DefaultPushButton:
    def __init__(self):
        self.manager = None

    def is_pressed(self):
        return np.random.choice([True, False], 1, p=[0.2, 0.8])


class PushButton1(DefaultPushButton):
    def __init__(self, init_state=_PB_DEACTIVATE):
        DefaultPushButton.__init__(self)
        self.state = init_state

    def update_self(self):
        # DONE
        # p1_green
        if self.state == _PB_DEACTIVATE and self.manager.p1.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p2_green
        if self.state == _PB_DEACTIVATE and self.manager.p2.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p3_green
        if self.state == _PB_DEACTIVATE and self.manager.p3.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p4_green
        if self.state == _PB_DEACTIVATE and self.manager.p4.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p5_green
        if self.state == _PB_DEACTIVATE and self.manager.p5.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return

        # p6_red
        if self.state == _PB_ACTIVATE and self.manager.p6.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
        # p7_1_red
        if self.state == _PB_ACTIVATE and self.manager.p71.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
        # p7_2_red
        if self.state == _PB_ACTIVATE and self.manager.p72.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return

        # p7_3_red
        if self.state == _PB_ACTIVATE and self.manager.p73.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return


class PushButton2(DefaultPushButton):
    def __init__(self, init_state=_PB_DEACTIVATE):
        DefaultPushButton.__init__(self)
        self.state = init_state

    def update_self(self):
        # DONE
        # p1_green
        if self.state == _PB_DEACTIVATE and self.manager.p1.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p2_green
        if self.state == _PB_DEACTIVATE and self.manager.p2.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p3_green
        if self.state == _PB_DEACTIVATE and self.manager.p3.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p4_red
        if self.state == _PB_ACTIVATE and self.manager.p4.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
        # p5_green
        if self.state == _PB_DEACTIVATE and self.manager.p5.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return

        # p6_green
        if self.state == _PB_DEACTIVATE and self.manager.p6.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p7_1_red
        if self.state == _PB_ACTIVATE and self.manager.p71.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
        # p7_2_red
        if self.state == _PB_ACTIVATE and self.manager.p72.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return

        # p7_3_red
        if self.state == _PB_ACTIVATE and self.manager.p73.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return


class PushButton3(DefaultPushButton):
    def __init__(self, init_state=_PB_DEACTIVATE):
        DefaultPushButton.__init__(self)
        self.state = init_state

    def update_self(self):
        # DONE
        # p1_green
        if self.state == _PB_DEACTIVATE and self.manager.p1.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p2_green
        if self.state == _PB_DEACTIVATE and self.manager.p2.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p3_green
        if self.state == _PB_DEACTIVATE and self.manager.p3.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p4_green
        if self.state == _PB_DEACTIVATE and self.manager.p4.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p5_red
        if self.state == _PB_ACTIVATE and self.manager.p5.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return

        # p6_green
        if self.state == _PB_DEACTIVATE and self.manager.p6.state == _PHASE_GREEN:
            if self.is_pressed():
                self.state = _PB_ACTIVATE
            return
        # p7_1_red
        if self.state == _PB_ACTIVATE and self.manager.p71.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
        # p7_2_red
        if self.state == _PB_ACTIVATE and self.manager.p72.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return

        # p7_3_red
        if self.state == _PB_ACTIVATE and self.manager.p73.state == _PHASE_RED:
            self.state = _PB_DEACTIVATE
            return
