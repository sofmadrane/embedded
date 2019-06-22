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
    
    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p3.state == _PHASE_FINISH and not self.manager.pb2.state \
                and not (self.manager.pb1.state and self.manager.pb3.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p6 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p6.state == _PHASE_FINISH and not self.manager.pb2.state \
                and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p83 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p83.state == _PHASE_FINISH and not self.manager.pb2.state:
            self.state = _PHASE_ORANGE
            return
        # p73 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p73.state == _PHASE_FINISH and not self.manager.f.state:
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
            return
        # p1 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p2.update_self()
        self.manager.p5.update_self()
        self.manager.p71.update_self()
        self.manager.p81.update_self()
        return


class Phase2(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p1 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p1.state == _PHASE_FINISH and not self.manager.pb3.state \
                and not (self.manager.pb2.state and self.manager.pb1.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p81 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p81.state == _PHASE_FINISH and not self.manager.pb3.state:
            self.state = _PHASE_ORANGE
            return
        # p4 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p4.state == _PHASE_FINISH and not self.manager.pb3.state \
                and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p71 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p71.state == _PHASE_FINISH and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p2 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p2 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p2 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p3.update_self()
        self.manager.p6.update_self()
        self.manager.p72.update_self()
        self.manager.p82.update_self()
        return


class Phase3(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p2 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p2.state == _PHASE_FINISH and not self.manager.pb1.state \
                and not (self.manager.pb2.state and self.manager.pb3.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p5 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p5.state == _PHASE_FINISH and not self.manager.pb1.state \
                and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p82 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p82.state == _PHASE_FINISH and not self.manager.pb1.state:
            self.state = _PHASE_ORANGE
            return
        # p72 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p72.state == _PHASE_FINISH and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p3 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p3 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p3 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p1.update_self()
        self.manager.p4.update_self()
        self.manager.p73.update_self()
        self.manager.p83.update_self()
        return


class Phase4(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p3.state == _PHASE_FINISH and self.manager.pb2.state and \
                (not self.manager.pb1.state and not self.manager.pb3.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p6 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p6.state == _PHASE_FINISH and self.manager.pb2.state and \
                not self.manager.pb3.state and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p8_3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p83.state == _PHASE_FINISH and self.manager.pb2.state:
            self.state = _PHASE_ORANGE
            return
        # p4 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p4 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p4 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p2.update_self()
        self.manager.p5.update_self()
        self.manager.p71.update_self()
        self.manager.p81.update_self()
        return


class Phase5(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p1 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p1.state == _PHASE_FINISH and self.manager.pb3.state and \
                not self.manager.pb2.state and not self.manager.pb1.state and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p81 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p81.state == _PHASE_FINISH and self.manager.pb3.state:
            self.state = _PHASE_ORANGE
            return
        # p4 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p4.state == _PHASE_FINISH and self.manager.pb3.state and \
                not self.manager.pb1.state and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p5 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p5 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p5 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p3.update_self()
        self.manager.p6.update_self()
        self.manager.p72.update_self()
        self.manager.p82.update_self()
        return

class Phase6(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p2 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p2.state == _PHASE_FINISH and self.manager.pb1.state and \
                not self.manager.pb2.state and not self.manager.pb3.state and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p82 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p82.state == _PHASE_FINISH and self.manager.pb1.state:
            self.state = _PHASE_ORANGE
            return
        # p5 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p5.state == _PHASE_FINISH and self.manager.pb1.state \
                and not self.manager.pb2.state and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p6 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p6 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p6 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p1.update_self()
        self.manager.p4.update_self()
        self.manager.p73.update_self()
        self.manager.p83.update_self()
        return


class Phase7_1(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p1 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p1.state == _PHASE_FINISH and \
                ((self.manager.pb1.state and self.manager.pb2.state) or (self.manager.pb2.state and self.manager.pb3.state) or
                 (self.manager.pb1.state and self.manager.pb3.state)) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p4 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p4.state == _PHASE_FINISH and \
                (self.manager.pb1.state and self.manager.pb3.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p7_1 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p7_1 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p7_1 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p2.update_self()
        self.manager.p81.update_self()
        return


class Phase7_2(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p2 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p2.state == _PHASE_FINISH and \
                ((self.manager.pb1.state and self.manager.pb2.state) or
                 (self.manager.pb2.state and self.manager.pb3.state) or
                 (self.manager.pb1.state and self.manager.pb3.state)) and \
                not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p5 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p5.state == _PHASE_FINISH and \
                (self.manager.pb1.state and self.manager.pb2.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p7_2 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p7_2 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p7_2 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p3.update_self()
        self.manager.p82.update_self()
        return


class Phase7_3(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p3.state == _PHASE_FINISH and \
                ((self.manager.pb1.state and self.manager.pb2.state) or
                 (self.manager.pb2.state and self.manager.pb3.state) or
                 (self.manager.pb1.state and self.manager.pb3.state)) \
                and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p6 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p6.state == _PHASE_FINISH and \
                (self.manager.pb2.state and self.manager.pb3.state) and not self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p7_3 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p7_3 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p7_3 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p1.update_self()
        self.manager.p83.update_self()
        return


class Phase8_1(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p1 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p1.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p4 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p4.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p7_1 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p71.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p8_1 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p8_1 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p8_1 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p2.update_self()
        self.manager.p5.update_self()
        return


class Phase8_2(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p2 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p2.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p5 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p5.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p72 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p72.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p8_2 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p8_2 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p8_2 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p3.update_self()
        self.manager.p6.update_self()
        return


class Phase8_3(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # DONE
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

    def update_related_firemen(self) :
        self.manager.f.update_self()

    def update_self(self):
        # DONE
        # p3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p3.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p6 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p6.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # p7_3 finish
        if self.state == _PHASE_DEACTIVATE and self.manager.p73.state == _PHASE_FINISH and self.manager.f.state:
            self.state = _PHASE_ORANGE
            return
        # 8_3 red
        if self.state == _PHASE_ORANGE:
            self.state = _PHASE_RED
            return
        # p8_3 green
        if self.state == _PHASE_RED:
            self.state = _PHASE_GREEN
            return
        # none
        if self.state == _PHASE_GREEN:
            self.state = _PHASE_FINISH
            return
        # p8_3 finish
        if self.state == _PHASE_FINISH:
            self.activate_next_phase()
            self.state = _PHASE_DEACTIVATE
            return

    def activate_next_phase(self):
        # DONE
        self.manager.p1.update_self()
        self.manager.p4.update_self()
        return
