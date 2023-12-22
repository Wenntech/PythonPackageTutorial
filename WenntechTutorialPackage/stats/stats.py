import pandas as pd
from typing import Any
class StatsHelper:
    def __init__(self, data: pd.Series):
        """
        This is a sample of what a resuable helper class could look like!
        You can see that this doc string is represented as the class signature during instantion. If you haven't yet seen you will!
        We typically try to specify what this does so here we go.

        Purpose
        -------
        Stats Helper is built to help easily calculate different statistics given an input series.

        Parameters
        ----------
        - data `(pd.Series)`: The input data of a dataframe. This should be a pandas series aka a pandas dataframe column.

        Accessible Methods:
        --------------
        - StatsHelper().mean()
        - StatsHelper().median()
        - StatsHelper().variance()
        - StatsHelper().standard_deviation()
        """
        if isinstance(data, pd.Series):
            self.data = data
        else:
            raise TypeError("Input must be a pandas DataFrame or Series")

    def mean(self) -> float:
        """
        This is the docstring for the method signature itself.
        This method helps calculate the mean of a given data input series

        Returns
        -------
        - mean: float
        """
        return self.data.mean()

    def median(self) -> float:
        """
        This is the docstring for the method signature itself.
        This method helps calculate the median of a given data input series

        Returns
        -------
        - median: float
        """
        return self.data.median()

    def variance(self) -> Any:
        """
        This is the docstring for the method signature itself.
        This method helps calculate the variance of a given data input series

        Returns
        -------
        - variance: Scalar (Any)
        """
        return self.data.var()

    def standard_deviation(self):
        """
        This is the docstring for the method signature itself.
        This method helps calculate the standard deviation of a given data input series

        Returns
        -------
        - standard deviation: float
        """
        return self.data.std()