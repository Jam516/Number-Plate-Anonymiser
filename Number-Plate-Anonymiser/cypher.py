from random import SystemRandom

# Valid numberplate characters - A-Z, 1-9
VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class NumberplateCypher:
    """A cypher to anonymise numberplates.
    """

    def __init__(self):
        """Initialises the cypher, including the set-up of character lookups.
        """
        self._cyphers = [VALID_CHARS for _ in range(7)]
        self.randomise_cyphers()

    @staticmethod
    def _shuffle(seq):
        rng = SystemRandom()
        return sorted(seq, key=lambda _: rng.random())

    def randomise_cyphers(self):
        """Randomises the cyphers to allow for a new equivalence to be made,
        e.g. if two data sets may contain the same numberplate and the end-user
        should not be able to connect the two together, the cyphers should be
        shuffled between processing the two data sets to ensure this should
        not be the case.
        """
        self._cyphers = [self._shuffle(c) for c in self._cyphers]

    def anonymise(self, plate):
        """Anonymises a provided numberplate in the following manner:
        - Any spaces are removed from the plate
        - Characters that are not A-Z or 0-9 are ignored
        - Only the first 7 non-space characters are anonymised

        :param plate: the numberplate to be anonymised
        :type plate: str
        :return: the anonymised numberplate (contains no spaces)
        :rtype: str
        """
        no_spaces = plate.upper().replace(" ", "")
        new_plate = []
        for i, c in enumerate(no_spaces[:7]):
            if c in VALID_CHARS:
                char_index = VALID_CHARS.index(c)
                new_plate.append(self._cyphers[i][char_index])
        return "".join(new_plate)


if __name__ == "__main__":
    nc = NumberplateCypher()
    print(nc.anonymise("P584 PVT"))
    help(NumberplateCypher)
