'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


'''


# 2d Array and out put the highest amount
#  

def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    wealth_list = []
    for account in accounts:
        account_wealth = sum(account)
        wealth_list.append(account_wealth)

    return max(wealth_list)
    # richest_person_list = []
    # for wealth in wealth_list: # for each individual wealth e.g [6,19,19]
    #     print(wealth)
    #     if wealth == max(wealth_list): # for each individual wealth, is it equal to the max wealth?
    #         index_value = wealth_list.index(wealth)
    #         print(index_value)
    #         richest_person_list.append(index_value)

    # print(richest_person_list)

    #new_list = max(wealth_list)
    # richest_person = wealth_list.index(max(wealth_list)) + 1
    # print(f'The {richest_person} customer is the richest with a wealth of {max(wealth_list)}')

maximumWealth([[1,2,3],[14,5],[10,9]])

