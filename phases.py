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


class DefaultPhase:
    def __init__(self, init_state):
        self.state = init_state
        self.manager = None

    def is_activated(self):
        return self.state != _PHASE_DEACTIVATE


class Phase1(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
        # tl1 not impacted by p1
        self.manager.tl1.update_self()
        self.manager.tl2.update_self()
        self.manager.tl3.update_self()
        self.manager.tl4.update_self()
        self.manager.tl5.update_self()
        self.manager.tl6.update_self()
        self.manager.tl7.update_self()

    def update_related_pedestrian_lights(self):
        # DONE
        self.manager.pl1.update_self()
        self.manager.pl2.update_self()
        self.manager.pl3.update_self()

    def update_related_push_buttons(self):
        # DONE
        self.manager.pb1.update_self()
        self.manager.pb2.update_self()
        self.manager.pb3.update_self()

    def update_self(self):
        # DONE
        # p3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p3.state == _PHASE_FINISH and not self.manager.pb2 and \
                not (self.manager.pb1 and self.manager.pb3) and not self.manager.f:
            self.state = _PHASE_ORANGE
            return
        # p6 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p6.state == _PHASE_FINISH and not self.manager.pb2 and \
                not self.manager.f:
            self.state = _PHASE_ORANGE
            return
        # p83 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p83.state == _PHASE_FINISH and not self.manager.pb2:
            self.state = _PHASE_ORANGE
            return
        # p73 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p73.state == _PHASE_FINISH and not self.manager.f:
            self.state = _PHASE_ORANGE
            return
        # p1 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p1 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            self.activate_next_phase()
            return
        # p1 finish
        if self.state == _PHASE_FINISH:
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p2.update_self()
        self.manager.p5.update_self()
        self.manager.p71.update_self()
        self.manager.p81.update_self()
        return
