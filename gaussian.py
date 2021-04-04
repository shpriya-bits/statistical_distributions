import math
import matplotlib.pyplot as plt


class Gaussian:

    def __init__(self, mu=0, sigma=1):

        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean of thew dataset.

        Args:
            None

        Returns:
             Float: mean of the dataset
        """

        average = 1.0 * sum(self.data)/len(self.data)

        self.mean = average

        return self.mean

    def calculate_stdev(self, sample=True):
        """Method to calculate the standard deviation of the dataset.

        Args:
            sample(bool): whether the data represents the sample or the population

        Returns:
            Float: standard deviation of the dataset.
        """

        # If the sample is used, n would be replaced by n - 1 in the stdev formula.
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        sigma = 0  # standard deviation
        squared_sum = 0
        mean = self.mean

        for x in self.data:
            squared_sum += (x - mean) ** 2

        sigma = math.sqrt(squared_sum/n)
        self.stdev = sigma

        return self.stdev
