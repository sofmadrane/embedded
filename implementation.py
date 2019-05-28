"""Implémentation du modèle Prism"""
import numpy as np
# Pycharm says there's an error here, it's a Pycharm bug
from sync_singleton_container import *

# Constantes
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
    def __init__(self, sync_values_container):
        self.state = _PHASE_RED
        self.sync_values_container = sync_values_container

    def call_sync(self, sync_value):
        # must be implemented by the child class, or it crashes
        exit(0)


class Phase1(DefaultPhase):
    def __init__(self, sync_values_container):
        DefaultPhase.__init__(self, sync_values_container)

    def call_sync(self, sync_value):
        if sync_value == self.sync_values_container\
                                .get_sync("3", self.sync_values_container.FINISH_SYNC):
                self.p3_finish()
        if sync_value == self.sync_values_container\
                                .get_sync("6", self.sync_values_container.FINISH_SYNC):
                self.p6_finish()
        if sync_value == self.sync_values_container\
                                .get_sync("8_3", self.sync_values_container.FINISH_SYNC):
                self.p8_3_finish()
        if sync_value == self.sync_values_container \
                .get_sync("7_3", self.sync_values_container.FINISH_SYNC):
            self.p7_3_finish()
        if sync_value == self.sync_values_container \
                .get_sync("1", self.sync_values_container.RED_SYNC):
            self.p1_red()
        if sync_value == self.sync_values_container \
                .get_sync("1", self.sync_values_container.GREEN_SYNC):
            self.p1_green()
        if sync_value == self.sync_values_container \
                .get_sync("1", self.sync_values_container.FINISH_SYNC):
            self.p1_finish()

    def call_non_sync(self):
        self.no_sync()

    def p3_finish(self):
        # todo: appliquer les conditions
        # [p3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & !s_pb2 & !(s_pb1 & s_pb3) & !s_fire
        # -> (s_phase_1'=PHASE_ORANGE);
        self.state = _PHASE_ORANGE
        # [p3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & (s_pb2 | (s_pb1 & s_pb3)) | s_fire
        # -> (s_phase_1'=PHASE_DEACTIVATE);
        self.state = _PHASE_DEACTIVATE

    def p6_finish(self):
        # todo
        pass

    def p8_3_finish(self):
        # todo
        pass

    def p7_3_finish(self):
        # todo
        pass

    def p1_red(self):
        # todo
        pass

    def p1_green(self):
        # todo
        pass

    def p1_finish(self):
        # todo
        pass

    def no_sync(self):
        # todo
        # [] s_phase_1=PHASE_GREEN -> (s_phase_1'=PHASE_FINISH);
        pass


def main():
    container = SyncSingletonsContainer()
    print("Exemple d'utilisation du containter de singletons de synchronisation:")
    print("Accès au sync_singleton p7_3_green:")
    print(container.get_sync("7_3", container.GREEN_SYNC))

    p1 = Phase1(container)


if __name__ == '__main__':
    main()




