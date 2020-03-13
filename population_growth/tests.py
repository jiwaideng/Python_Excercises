from unittest import TestCase, main
from solution import pop_growth_years


class TestPopulationGrowth(TestCase):

    def test_pop_growth_years(self):
        self.assertEquals(15, pop_growth_years(1500, 5, 100, 5000))
        self.assertEquals(10, pop_growth_years(1500000, 2.5, 10000, 2000000))
        self.assertEquals(94, pop_growth_years(1500000, 0.25, 1000, 2000000))



if __name__ == '__main__':
    main()