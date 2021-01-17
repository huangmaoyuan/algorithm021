class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <1: 
            return []
        result=[]
        cols=set()
        pie=set()
        na=set()
        def dfs(n,row,cur_state):
            print(cur_state)
            if row>=n:
                result.append(cur_state)
                return
            for col in range(n):
                if col in cols or row + col in pie or row - col in na:
                    continue
                cols.add(col)
                pie.add(row+col)
                na.add(row-col)
                dfs(n,row+1,cur_state + [col])
                cols.remove(col)
                pie.remove(row+col)
                na.remove(row-col)
        def generate_result(n):
            board = []
            for res in result:
                for i in res:
                    board.append("."*i + "Q" + "."*(n-i-1))
            return [board[i:i+n] for i in range(0,len(board),n)]
        dfs(n,0,[])
        print(result)
        return generate_result(n)
