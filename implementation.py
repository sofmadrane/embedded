"""Implémentation du modèle Prism"""
import numpy as np
# Pycharm says there's an error here, it's a Pycharm bug
from sync_singleton_container import *
import fileinput

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


# This is an abstract class, never directly instantiate from this!
# Contains the part of the state and behaviour shared by all Phases
class DefaultPhase:
    def __init__(self, init_state):
        self.state = init_state

    def is_activated(self):
        return self.state != _PHASE_DEACTIVATE


class Phase1(DefaultPhase):
    def __init__(self, init_state=_PHASE_DEACTIVATE):
        DefaultPhase.__init__(self, init_state)

    def update_related_traffic_lights(self):
        # TODO
        x = 1

    def update_related_pedstrian_lights(self):
        # TODO
        x = 1

    def update_related_push_buttons(self):
        # TODO
        x = 1

    def update_self(self):
        # TODO: update self.state depending on the state of the push buttons.
        x = 1

    def activate_next_phase(self):
        # TODO: either (return self) or (return next phase and deactivate self)
        x = 1

# TODO class Phase_x (x in 2 to 8_2)

# TODO class Traffic_light_x (x in 1 to 7)

# TODO class Pedestrian_light_x (x in 1 to 3)

# TODO class Push_Button_x (x in 1 to 3)

# TODO class Fire_Men (only one)


class Intersection:
    def __init__(self):
        self.phase_1 = 0
        self.phase_2 = 0
        self.phase_3 = 0
        self.phase_4 = 0
        self.phase_5 = 0
        self.phase_6 = 0
        self.phase_7_1 = 0
        self.phase_7_2 = 0
        self.phase_8_1 = 0
        self.phase_8_2 = 0

        self.tl_1 = 0
        self.tl_2 = 0
        self.tl_3 = 0
        self.tl_4 = 0
        self.tl_5 = 0
        self.tl_6 = 0
        self.tl_7 = 0

        self.pl_1 = _TL_GREEN
        self.pl_2 = 0
        self.pl_3 = _TL_RED

        self.pb_1 = 0
        self.pb_2 = 0
        self.pb_3 = 0

        self.fire = True

    def print_state(self):

        intersection_representation = "######################################################\n"
        fire_symbol = self.fire_to_symbol(self.fire)
        #                              "################# FIREMEN INCOMING ###################"
        intersection_representation += "################# " + fire_symbol + " ###################\n"
        pl_1_symbol = self.pl_state_to_symbol(self.pl_1)
        pl_3_symbol = self.pl_state_to_symbol(self.pl_3)
        intersection_representation += "_________________|       "+pl_1_symbol+"       |___________________\n"
        intersection_representation += "                                                      \n"
        intersection_representation += "                                                      \n"
        intersection_representation += "_________________                 ____________________\n"
        intersection_representation += "               | |       "+pl_3_symbol+"       | |                  \n"
        intersection_representation += "               | |               | |                  \n"
        intersection_representation += "               | |               | |                  \n"
        intersection_representation += "               | |               | |                  \n"
        intersection_representation += "               | |               | |                  \n"

        print(intersection_representation)

    def tl_state_to_symbol(self, state):
        if state == _TL_GREEN: return "OO"
        if state == _TL_ORANGE: return "=="
        if state == _TL_RED: return "XX"

    def pl_state_to_symbol(self, state):
        if state == _TL_GREEN: return "o"
        if state == _TL_ORANGE: return "="
        if state == _TL_RED: return "x"

    def pb_state_to_symbol(self, state):
        if state == _PB_ACTIVATE: return "!!"
        if state == _PB_DEACTIVATE: return "?"

    def fire_to_symbol(self, state):
        if state: return "FIREMEN INCOMING"
        if state: return "                "


def main():

    continue_loop = True
    counter = 0

    # TODO init all phases, traffic lights, pedestrian lights, push buttons
    phase_1 = Phase1(_PHASE_ORANGE)
    # TODO set first phase's state to _PHASE_ORANGE. All other phases are in state _PHASE_DEACTIVATE.
    # TODO set all traffic lights' states and pedestrian lights to _TL_RED, push-buttons to _PB_DEACTIVATE

    # TODO set current_phase to the first one
    current_phase = phase_1

    inter = Intersection()
    inter.print_state()

    while continue_loop:

        # Continue loop condition update every 5 loops
        print(str(counter))
        if counter % 5 == 0:
            line = input("Enter to continue, or press n to stop: ")
            if line == "n":
                continue_loop = False
        counter += 1

        # TODO update all push_buttons probabilistically

        # TODO call current_phase.update_self

        # TODO call current_phase = current_phase.get_next_phase() -> can return either the current or next phase

        # TODO call current_phase.update_related_push_buttons() (as some need to be deactivated)

        # TODO call current_phase.update_related_traffic_lights()

        # TODO call current_phase.update_related_pedestrian_lights()

        # TODO print the current state of the intersection


if __name__ == '__main__':
    main()




