# LeetCode Medium
# Search Suggestions System Question: Strings
# return top 3 products, no duplicate items in the products list


class Solution:

    # need to optimize
    # brute force solution
    # O(n + n*m*n) -> O(n^2*m) time complexity since along with the double for loop, we check for equivalence
    # with the start of the string everytime which will eventually come to the entire searchWord (therefore
    # another n term)
    # We aren't using any extra space since we must return a list of a list, so it should be O(1) space complexity
    # the threeProducts array will always be of size 3 and will never go over, gets reset on every substring
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        m = len(products)
        products.sort()
        subString = ""
        returnList = []
        for i in range(0, n):
            returnList.append([])

        for i in range(0, n):
            threeProducts = []
            subString += searchWord[i]

            for j in range(0, m):
                # also products[j][:len(subString)] == subString could work here
                # but startswith seems faster in the general case
                if products[j].startswith(subString):
                    if len(threeProducts) == 3:
                        break
                    else:
                        threeProducts.append(products[j])
            returnList[i] = threeProducts

        return returnList
