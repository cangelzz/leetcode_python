class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        min_price = prices[0]
        mins = []
        for price in prices:
            if price < min_price:
                mins.append(price)
                min_price = price
            else:
                mins.append(min_price)

        profits = [x - y for x, y in zip(prices, mins)]
        return max(profits)