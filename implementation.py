"""Implémentation du modèle Prism"""
from phases import *
from trafficlights import *
from pushbuttons import *
from pedestrianlights import *
from firemen import *

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

# TODO class Phase_x (x in 2 to 8_3)

# TODO class Traffic_light_x (x in 1 to 7)

# TODO class Pedestrian_light_x (x in 1 to 3)

# TODO class Push_Button_x (x in 1 to 3)

# TODO class Fire_Men (only one)


def addManagerToObjects(manager, p1, p2, p3, p4, p5, p6, p71, p72, p73, p81, p82, p83, tl1, tl2, tl3, tl4, tl5, tl6, tl7, pb1, pb2
                 , pb3, pl1, pl2, pl3, f):
    p1.manager = manager
    p2.manager = manager
    p3.manager = manager
    p4.manager = manager
    p5.manager = manager
    p6.manager = manager
    p71.manager = manager
    p72.manager = manager
    p73.manager = manager
    p81.manager = manager
    p82.manager = manager
    p83.manager = manager

    tl1.manager = manager
    tl2.manager = manager
    tl3.manager = manager
    tl4.manager = manager
    tl5.manager = manager
    tl6.manager = manager
    tl7.manager = manager

    pl1.manager = manager
    pl2.manager = manager
    pl3.manager = manager

    pb1.manager = manager
    pb2.manager = manager
    pb3.manager = manager

    f.manager = manager


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

    def get_current_phase_id(self):
        if self.p1.state != _PHASE_DEACTIVATE: return "1  "
        if self.p2.state != _PHASE_DEACTIVATE: return "2  "
        if self.p3.state != _PHASE_DEACTIVATE: return "3  "
        if self.p4.state != _PHASE_DEACTIVATE: return "4  "
        if self.p5.state != _PHASE_DEACTIVATE: return "5  "
        if self.p6.state != _PHASE_DEACTIVATE: return "6  "
        if self.p71.state != _PHASE_DEACTIVATE: return "7.1"
        if self.p72.state != _PHASE_DEACTIVATE: return "7.2"
        if self.p73.state != _PHASE_DEACTIVATE: return "7.3"
        if self.p81.state != _PHASE_DEACTIVATE: return "8.1"
        if self.p82.state != _PHASE_DEACTIVATE: return "8.2"
        if self.p83.state != _PHASE_DEACTIVATE: return "8.3"


def show_detailed_path(manager, step):
    line = str(step)+"\t"
    line += "\t " + str(manager.p1.state)
    line += "\t\t " + str(manager.p2.state)
    line += "\t\t " + str(manager.p3.state)
    line += "\t\t " + str(manager.p4.state)

    line += "\t\t " + str(manager.p5.state)
    line += "\t\t " + str(manager.p6.state)
    line += "\t\t " + str(manager.p71.state)
    line += "\t\t " + str(manager.p72.state)

    line += "\t\t " + str(manager.p73.state)
    line += "\t\t " + str(manager.p81.state)
    line += "\t\t " + str(manager.p82.state)
    line += "\t\t " + str(manager.p83.state)

    line += "\t\t " + str(manager.tl1.state)
    line += "\t\t " + str(manager.tl2.state)
    line += "\t\t " + str(manager.tl3.state)
    line += "\t\t " + str(manager.tl4.state)
    line += "\t\t " + str(manager.tl5.state)
    line += "\t\t " + str(manager.tl6.state)
    line += "\t\t " + str(manager.tl7.state)

    line += "\t\t " + str(manager.pl1.state)
    line += "\t\t " + str(manager.pl2.state)
    line += "\t\t " + str(manager.pl3.state)

    line += "\t\t " + str(manager.pb1.state)
    line += "\t " + str(manager.pb2.state)
    line += "\t " + str(manager.pb3.state)

    line += "\t " + str(manager.f.state)

    return line

def show_detailed_path_colnames():
    print( "Step\tP_1\t\tP_2\t\tP_3\t\tP_4\t\tP_5\t\tP_6\t\tP_7.1\tP_7.2\tP_7.3\tP_8.1\tP_8.2\tP_8.3\tTL_1\tTL_2\tTL_3\tTL_4\tTL_5\tTL_6\tTL_7\tPL_1\tPL_2\tPL_3\tPB_1\tPB_2\tPB_3\tFiremen")


class Intersection:

    def __init__(self, manager):
        self.manager = manager
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.OKYELLOW = '\033[93m'
        self.OKRED = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'

    def print_state(self):
        pl_1_symbol = self.pl_state_to_symbol(self.manager.pl1.state)
        pl_2_symbol = self.pl_state_to_symbol(self.manager.pl2.state)
        pl_3_symbol = self.pl_state_to_symbol(self.manager.pl3.state)

        pb_1_symbol = self.pb_state_to_symbol(self.manager.pb1.state)
        pb_2_symbol = self.pb_state_to_symbol(self.manager.pb2.state)
        pb_3_symbol = self.pb_state_to_symbol(self.manager.pb3.state)

        tl_1_symbol = self.tl_state_to_symbol(self.manager.tl1.state)
        tl_2_symbol = self.tl_state_to_symbol(self.manager.tl2.state)
        tl_3_symbol = self.tl_state_to_symbol(self.manager.tl3.state)
        tl_4_symbol = self.tl_state_to_symbol(self.manager.tl4.state)
        tl_5_symbol = self.tl_state_to_symbol(self.manager.tl5.state)
        tl_6_symbol = self.tl_state_to_symbol(self.manager.tl6.state)
        tl_7_symbol = self.tl_state_to_symbol(self.manager.tl7.state)

        fire_symbol = self.fire_to_symbol(self.manager.f.state)

        # TODO do the traffic lights to symbol but la flemme pour le moment

        intersection_representation = "######################################################\n"
        intersection_representation += "################# ["+fire_symbol+"] ###################\n"

        intersection_representation += "_________________|      ["+tl_7_symbol+"]       |____________________\n"
        intersection_representation += "                =                = "+tl_2_symbol+"        ←         \n"
        intersection_representation += "                =                = "+tl_1_symbol+"        ←         \n"
        intersection_representation += "- - - - - - ["+pl_3_symbol+","+pb_3_symbol+"]               ["+pl_1_symbol+","+pb_1_symbol+"] - - - - - - - -\n"
        intersection_representation += "         →    "+tl_4_symbol+" =                =                    \n"
        intersection_representation += "_________↴____"+tl_3_symbol+"_=                =_____________________\n"
        intersection_representation += "                 || ||[ "+pl_2_symbol+","+pb_2_symbol+"]|| ||                    \n"
        intersection_representation += "                 |       |  "+tl_5_symbol+"  "+tl_6_symbol+" |                    \n"
        intersection_representation += "   PHASE "+self.manager.get_current_phase_id()+"     |       |       |                    \n"
        intersection_representation += "   "+self.p_state_to_symbol(self.manager.get_current_phase().state)+"   |       |  ↰  ↱ |                    \n"
        intersection_representation += "                 |       |       |                    \n"

        print(intersection_representation)

    def tl_state_to_symbol(self, state):
        if state == _TL_GREEN: return self.OKBLUE+self.BOLD+"O"+self.ENDC
        if state == _TL_ORANGE: return "+"
        if state == _TL_RED: return "X"

    def pl_state_to_symbol(self, state):
        if state == _TL_GREEN: return self.OKBLUE+self.BOLD+"o"+self.ENDC
        if state == _TL_ORANGE: return "+"
        if state == _TL_RED: return "x"

    def pb_state_to_symbol(self, state):
        if state == _PB_ACTIVATE: return self.OKBLUE+self.BOLD+"!!"+self.ENDC
        if state == _PB_DEACTIVATE: return " ?"

    def p_state_to_symbol(self, state):
        if state == _PHASE_RED: return self.OKRED+"red        "+self.ENDC
        if state == _PHASE_DEACTIVATE: return "deactivated"
        if state == _PHASE_ORANGE: return self.OKYELLOW+"orange     "+self.ENDC
        if state == _PHASE_GREEN: return self.OKGREEN+"green      "+self.ENDC
        if state == _PHASE_FINISH: return self.BOLD+"finished   "+self.ENDC

    def fire_to_symbol(self, state):
        if state: return self.OKBLUE+"FIREMEN INCOMING"+self.ENDC
        else: return "               "


def main():

    continue_loop = True
    counter = 0
    path = []

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

    push_button_1 = PushButton1()
    push_button_2 = PushButton2()
    push_button_3 = PushButton3()

    ped_lights_1 = PedestrianLight1()
    ped_lights_2 = PedestrianLight2()
    ped_lights_3 = PedestrianLight3()

    firemen = Firemen()

    # TODO set first phase's state to _PHASE_ORANGE. All other phases are in state _PHASE_DEACTIVATE.
    # TODO set all traffic lights' states and pedestrian lights to _TL_RED, push-buttons to _PB_DEACTIVATE

    # TODO set current_phase to the first one
    current_phase = phase_1

    manager = IntersectionManager(phase_1, phase_2, phase_3, phase_4, phase_5, phase_6, phase_7_1, phase_7_2, phase_7_3,
                                  phase_8_1, phase_8_2, phase_8_3, traff_light_1, traff_light_2, traff_light_3,
                                  traff_light_4, traff_light_5, traff_light_6, traff_light_7, push_button_1,
                                  push_button_2, push_button_3, ped_lights_1, ped_lights_2, ped_lights_3, firemen)

    addManagerToObjects(manager, phase_1, phase_2, phase_3, phase_4, phase_5, phase_6, phase_7_1, phase_7_2, phase_7_3,
                        phase_8_1, phase_8_2, phase_8_3, traff_light_1, traff_light_2, traff_light_3,
                        traff_light_4, traff_light_5, traff_light_6, traff_light_7, push_button_1,
                        push_button_2, push_button_3, ped_lights_1, ped_lights_2, ped_lights_3, firemen)

    inter = Intersection(manager)
    inter.print_state()

    path.append(show_detailed_path(manager, counter))

    while continue_loop:


        # Continue loop condition update every 5 loops

        # if counter % 5 == 0:
        line = input("Enter to continue, or press n to stop: ")
        if line == "n":
            continue_loop = False
        counter += 1

        # TODO update all push_buttons probabilistically

        # TODO call current_phase.update_self
        current_phase.update_self()

        # TODO call current_phase.activate_next_phase()
        # current_phase.activate_next_phase()

        # TODO Set the current phase to the possibly new current phase
        current_phase = manager.get_current_phase()

        # TODO call current_phase.update_related_push_buttons() (as some need to be deactivated)
        current_phase.update_related_push_buttons()

        # TODO call current_phase.update_related_traffic_lights()
        current_phase.update_related_traffic_lights()

        # TODO call current_phase.update_related_pedestrian_lights()
        current_phase.update_related_pedestrian_lights()
        
        # call current_phase.update_related_firemen()
        current_phase.update_related_firemen()

        # TODO print the current state of the intersection
        inter.print_state()

        show_detailed_path_colnames()
        path.append(show_detailed_path(manager, counter))
        for i in range(max((counter-10), 0), counter+1):
            print(path[i])


if __name__ == '__main__':
    main()




