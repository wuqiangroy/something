"""
八 皇后问题
"""


class EightQueens:

    @classmethod
    def conflict(cls, status: tuple, col: int):
        """
        :param status: 皇后当前状态
        :param col: col 为当前列
        :return:
        """
        # 行
        row = len(status)

        for i in range(row):
            # 判断当前行列是否冲突
            if abs(status[i]-col) in [0, row-1]:
                return True
        return False

    @classmethod
    def queens(cls, num=8, status=()):
        """
        生成皇后位置
        :param num:
        :param status:
        :return:
        """
        for i in range(num):
            if not cls.conflict(status, i):
                if len(status) == num - 1:
                    yield(i, )

                else:
                    for result in cls.queens(num, status+(i, )):
                        yield (i, ) + result


if __name__ == "__main__":
    solution = EightQueens()
    print(len(list(solution.queens())))
