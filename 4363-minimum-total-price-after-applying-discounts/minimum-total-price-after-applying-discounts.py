class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        for i in range(min(len(discounts),len(prices))):
            prices[i]=(prices[i]*(100-discounts[i]))/100.0
        return sum(prices)