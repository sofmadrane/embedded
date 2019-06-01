"""Implémentation du modèle Prism"""
from phases import *
from trafficlights import *
from pushbuttons import *
from pedestrianlights import *

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

    def update_self(self):
        self.state = _TL_RED


class PedestrianLight1:
    def __init__(self, init_state=_TL_RED):
        self.state = init_state

    def update_self(self):
        self.state = _TL_RED


class PushButton1:
    def __init__(self, init_state=_PB_DEACTIVATE):
        self.state = init_state

    def update_self(self):
        self.state = _PB_DEACTIVATE


class Firemen:
    def __init__(self, init_state=False):
        self.state = init_state

    def update_self(self):
        self.state = False

# TODO class Phase_x (x in 2 to 8_3)

# TODO class Traffic_light_x (x in 1 to 7)

# TODO class Pedestrian_light_x (x in 1 to 3)

# TODO class Push_Button_x (x in 1 to 3)

# TODO class Fire_Men (only one)


class IntersectionManager:
    def __init__(self, p1, p2, p3, p4, p5, p6, p71, p72, p73, p81, p82, p83, tl1, tl2, tl3, tl4, tl5, tl6, tl7, pb1, pb2
                 , pb3, pl1, pl2, pl3, f):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p71 = p71
        self.p72 = p72
        self.p73 = p73
        self.p81 = p81
        self.p82 = p82
        self.p83 = p83

        self.tl1 = tl1
        self.tl2 = tl2
        self.tl3 = tl3
        self.tl4 = tl4
        self.tl5 = tl5
        self.tl6 = tl6
        self.tl7 = tl7

        self.pl1 = pl1
        self.pl2 = pl2
        self.pl3 = pl3

        self.pb1 = pb1
        self.pb2 = pb2
        self.pb3 = pb3

        self.f = f

    def get_current_phase(self):
        if self.p1.state != _PHASE_DEACTIVATE: return self.p1
        if self.p2.state != _PHASE_DEACTIVATE: return self.p2
        if self.p3.state != _PHASE_DEACTIVATE: return self.p3
        if self.p4.state != _PHASE_DEACTIVATE: return self.p4
        if self.p5.state != _PHASE_DEACTIVATE: return self.p5
        if self.p6.state != _PHASE_DEACTIVATE: return self.p6
        if self.p71.state != _PHASE_DEACTIVATE: return self.p71
        if self.p72.state != _PHASE_DEACTIVATE: return self.p72
        if self.p73.state != _PHASE_DEACTIVATE: return self.p73
        if self.p81.state != _PHASE_DEACTIVATE: return self.p81
        if self.p82.state != _PHASE_DEACTIVATE: return self.p82
        if self.p83.state != _PHASE_DEACTIVATE: return self.p83


class Intersection:
    def __init__(self, manager):
        self.manager = manager
        self.phase_1 = 0
        self.phase_2 = 0
        self.phase_3 = 0
        self.phase_4 = 0
        self.phase_5 = 0
        self.phase_6 = 0
        self.phase_7_1 = 0
        self.phase_7_2 = 0
        self.phase_7_3 = 0
        self.phase_8_1 = 0
        self.phase_8_2 = 0
        self.phase_8_3 = 0

        self.tl_1 = 0
        self.tl_2 = 0
        self.tl_3 = 0
        self.tl_4 = 0
        self.tl_5 = 0
        self.tl_6 = 0
        self.tl_7 = 0

        self.pl_1 = _TL_GREEN
        self.pl_2 = _TL_GREEN
        self.pl_3 = _TL_RED

        self.pb_1 = 0
        self.pb_2 = 0
        self.pb_3 = 0

        self.fire = False

    def print_state(self):
        pl_1_symbol = self.pl_state_to_symbol(self.pl_1)
        pl_2_symbol = self.pl_state_to_symbol(self.pl_2)
        pl_3_symbol = self.pl_state_to_symbol(self.pl_3)

        pb_1_symbol = self.pb_state_to_symbol(self.pb_1)
        pb_2_symbol = self.pb_state_to_symbol(self.pb_2)
        pb_3_symbol = self.pb_state_to_symbol(self.pb_3)

        fire_symbol = self.fire_to_symbol(self.fire)

        # TODO do the traffic lights to symbol but la flemme pour le moment

        intersection_representation = "######################################################\n"
        intersection_representation += "################# " + fire_symbol + " ###################\n"

        intersection_representation += "_________________|               |____________________\n"
        intersection_representation += "                =                = X        ←         \n"
        intersection_representation += "                =                = X        ←         \n"
        intersection_representation += "- - - - - - -  ["+pl_3_symbol+","+pb_3_symbol+"]              ["+pl_1_symbol+","+pb_1_symbol+"] - - - - - - - - - \n"
        intersection_representation += "         →    X =                =                    \n"
        intersection_representation += "_________↴____X_=                =____________________\n"
        intersection_representation += "                 | || ||["+pl_2_symbol+","+pb_2_symbol+"]|| || |                    \n"
        intersection_representation += "                 |       |  X  X |                    \n"
        intersection_representation += "                 |       |       |                    \n"
        intersection_representation += "                 |       |  ↰  ↱ |                    \n"
        intersection_representation += "                 |       |       |                    \n"

        print(intersection_representation)

    def tl_state_to_symbol(self, state):
        if state == _TL_GREEN: return "OO"
        if state == _TL_ORANGE: return "~~"
        if state == _TL_RED: return "XX"

    def pl_state_to_symbol(self, state):
        if state == _TL_GREEN: return "o"
        if state == _TL_ORANGE: return "~"
        if state == _TL_RED: return "x"

    def pb_state_to_symbol(self, state):
        if state == _PB_ACTIVATE: return "!"
        if state == _PB_DEACTIVATE: return "?"

    def fire_to_symbol(self, state):
        if state: return "FIREMEN INCOMING"
        else: return "               "


def main():

    continue_loop = True
    counter = 0

    # TODO init all phases, traffic lights, pedestrian lights, push buttons
    phase_1 = Phase1(_PHASE_ORANGE)
    phase_2 = Phase2(_PHASE_DEACTIVATE)
    phase_3 = Phase3(_PHASE_DEACTIVATE)
    phase_4 = Phase4(_PHASE_DEACTIVATE)
    phase_5 = Phase5(_PHASE_DEACTIVATE)
    phase_6 = Phase6(_PHASE_DEACTIVATE)
    phase_7_1 = Phase7_1(_PHASE_DEACTIVATE)
    phase_7_2 = Phase7_2(_PHASE_DEACTIVATE)
    phase_7_3 = Phase7_3(_PHASE_DEACTIVATE)
    phase_8_1 = Phase8_1(_PHASE_DEACTIVATE)
    phase_8_2 = Phase8_2(_PHASE_DEACTIVATE)
    phase_8_3 = Phase8_3(_PHASE_DEACTIVATE)

    traff_light_1 = TrafficLight1()
    traff_light_2 = TrafficLight2()
    traff_light_3 = TrafficLight3()
    traff_light_4 = TrafficLight4()
    traff_light_5 = TrafficLight5()
    traff_light_6 = TrafficLight6()
    traff_light_7 = TrafficLight7()

    # TODO set first phase's state to _PHASE_ORANGE. All other phases are in state _PHASE_DEACTIVATE.
    # TODO set all traffic lights' states and pedestrian lights to _TL_RED, push-buttons to _PB_DEACTIVATE

    # TODO set current_phase to the first one
    current_phase = phase_1

    manager = IntersectionManager(phase_1, phase_2, phase_3, phase_4, phase_5, phase_6, phase_7_1, phase_7_2, phase_7_3,
                                  phase_8_1, phase_8_2, phase_8_3, traff_light_1, traff_light_2, traff_light_3,
                                  traff_light_4, traff_light_5, traff_light_6, traff_light_7)

    inter = Intersection()
    inter.print_state()

    while continue_loop:

        # Continue loop condition update every 5 loops

        if counter % 5 == 0:
            line = input("Enter to continue, or press n to stop: ")
            if line == "n":
                continue_loop = False
        counter += 1

        # TODO update all push_buttons probabilistically

        # TODO call current_phase.update_self
        current_phase.update_self()

        # TODO call current_phase.activate_next_phase()
        current_phase.activate_next_phase()

        # TODO Set the current phase to the possibly new current phase
        current_phase = IntersectionManager.get_current_phase()

        # TODO call current_phase.update_related_push_buttons() (as some need to be deactivated)
        current_phase.update_related_push_buttons()

        # TODO call current_phase.update_related_traffic_lights()
        current_phase.update_related_traffic_lights()

        # TODO call current_phase.update_related_pedestrian_lights()
        current_phase.update_related_pedestrian_lights()

        # TODO print the current state of the intersection
        inter.print_state()


if __name__ == '__main__':
    main()




