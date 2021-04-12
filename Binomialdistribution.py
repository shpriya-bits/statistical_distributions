import math
import matplotlip.pyplot as py
from .Generaldistribution import Distribution



class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    def __init__(self, prob = 0.5, size = 20):

        Distribution.__inti__(self, self.calculate_mean(), self.calculate_stdev)

        self.p = prob
        self.n = size

    def calculate_mean(self):

        avg = float(self.p * self.n )
        self.mean = avg
        return self.mean
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))
        return self.stdev

        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """

    def replace_stats_with_data(self):

        self.n = len(self.data)
        pos = sum([x for x in data if x == 1])
        self.p = float(pos / trials)
        self.mean = self.calculate_mean
        self.stdev = self.calculate_stdev

        return (self.p ,self.n)
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
    def plot_bar(self):

        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.bar(x=['0', '1'], height = [(1-self.p)*self.n, self.p*self.n])
        plt.title("Bar Chart")
        plt.xlabel("Data")
        plt.ylabel("Count")


        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
    def pdf(self, k):

        coef = math.factorial(self.n)/(math.factorial(k)* math.factorial(self.n - k))
        probf = coef * (self.p**k) * (1 - self.p)**(self.n - k)

        return probf
    # write a method to plot the probability density function of the binomial distribution

    def pdf_plot(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []
        k = 0
        for 0<= k <=self.n:
            x.append(k)
            y.append(self.pdf(k))

        plt.bar(x= x, height= y)
        plt.title("Bar Chart of PDF")
        plt.xlabel("Data")
        plt.ylabel("Probability")
        plt.show()
        return (x, y)
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.

    def __add__(self,other):

        # """Function to add together two Binomial distributions with equal p
        #
        # Args:
        #     other (Binomial): Binomial instance
        #
        # Returns:
        #     Binomial: Binomial distribution
        #
        # """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise


        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        return " mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
