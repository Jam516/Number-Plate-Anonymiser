from cypher import NumberplateCypher


class TestNumberplateCypher:
    plate = "P584PVT"
    cypher = NumberplateCypher()

    def test_anonymisation(self):
        TestNumberplateCypher.first_shuffle = TestNumberplateCypher.cypher.anonymise(
            TestNumberplateCypher.plate
        )

        assert TestNumberplateCypher.first_shuffle != TestNumberplateCypher.plate

    def test_randomising(self):
        TestNumberplateCypher.cypher.randomise_cyphers()

        second_shuffle = TestNumberplateCypher.cypher.anonymise(
            TestNumberplateCypher.plate
        )

        assert second_shuffle != TestNumberplateCypher.first_shuffle
