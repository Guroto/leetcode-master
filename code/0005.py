import numpy as np

def longest_palindrome(string):
    """
    - 回文表示前后元素一致, 顾最直接的想法是通过双指针来解
    - 遍历所有回文后, 求得最长的回文串
    :param string:
    :return:
    """
    length = len(string)
    index_tuple = (0, 0)
    for i in range(length):
        left = i
        right = length - 1

        # 记录指针移动的步长
        step = 0

        # 防止最后回到起始点
        while right >= left and right != i:
            # 如果当前左右指针元素相等, 向中间递进
            if string[left] == string[right]:
                left += 1
                right -= 1

                if left == right:
                    step += 1
                else:
                    step += 2
            else:
                right -= 1
                # 置为0方便后续进行计算
                step = 0

        if step > index_tuple[1] - index_tuple[0]:
            index_tuple = (i, i+step-1)

    return index_tuple


def longest_palindrome_dp(string):
    """
    - 由于双指针的解法过程中其实有大量重复计算的过程
    - 顾通过动态规划的方式来优化
    - dp[i][j] 如果是回文, 则其子字符串一定是回文, 即dp[i+1][j-1]为true
    :param string:
    :return:
    """
    length = len(string)
    dp = np.zeros((length, length))
    for i in range(length-1, -1, -1):
        for j in range(i, length):
            print(i, j)
            if string[i] == string[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                elif dp[i+1][j-1]:
                    dp[i][j] = 1
    return dp


if __name__ == '__main__':
    # res = longest_palindrome("cabbac")
    res = longest_palindrome_dp("cabbac")
    print(res)