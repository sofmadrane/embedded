import numpy as np


# This class produces singletons and stores them in a singleton matrix.
# It is mainly used to provide singletons for synchronisations purposes
# between our simulated 'Prism-like' modules (see how we synchronised the modules
# in the Prism code for the embedded systems design part of the project)
class SyncSingletonsContainer:
    # Constants used to access the singleton matrix
    GREEN_SYNC = 0
    RED_SYNC = 1
    FINISH_SYNC = 2
    # each phase generates a need for three synchronisation singletons
    # being {green, red, finish} (see the Prism code)
    nbr_singletons_needed_for_each_phase = 3

    def __init__(self):
        # gets incremented every time a new singleton is created,
        # making each singleton unique
        self.singleton_counter = 0

        # the arrays start at 1 for readability and easy comparisons with Prism purposes
        self.singleton_container = {}
        self.singleton_container[1] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        self.singleton_container[2] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        self.singleton_container[3] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        self.singleton_container[4] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        self.singleton_container[5] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        self.singleton_container[6] = np.zeros(self.nbr_singletons_needed_for_each_phase)
        # Pedestrian-only phases (two dimensional array, contains 7_1, 7_2 and 7_3)
        self.singleton_container[7] = np.zeros((4, self.nbr_singletons_needed_for_each_phase))
        # Firemen-only phases
        self.singleton_container[8] = np.zeros((4, self.nbr_singletons_needed_for_each_phase))

        # Fill the whole matrix with unique singletons
        self._fill_singleton_container()

    def _fill_singleton_container(self):
        for i in range(1, 7):
            for j in range(0, self.nbr_singletons_needed_for_each_phase):
                self.singleton_container[i][j] = self._generate_singleton()
        for i in range(7, 9):
            for j in range(1, 4):
                for k in range(0, self.nbr_singletons_needed_for_each_phase):
                    self.singleton_container[i][j][k] = self._generate_singleton()

    @staticmethod
    def _p_name_to_idx(phase_name):
        phase = 0
        sub_phase = 0
        if "_" in phase_name:
            # the 7 in 7_1
            phase = int(phase_name[0], 10)
            # the 1 in 7_1
            sub_phase = int(phase_name[2], 10)
        else:
            phase = int(phase_name, 10)
        return phase, sub_phase

    def _generate_singleton(self):
        self.singleton_counter += 1
        return self.singleton_counter

    def get_sync(self, phase_name, sync_value):
        # sync_value can only be either self.GREEN_SYNC, self.RED_SYNC, or self.FINISH_SYNC
        phase, sub_phase = self._p_name_to_idx(phase_name)
        if phase < 7:
            return self.singleton_container[phase][sync_value]
        return self.singleton_container[phase][sub_phase][sync_value]
