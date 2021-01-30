class Solution:
    def reverseWords(self, s):
        s = s.strip() # 删除首尾空格
        print(s)
        strs = s.split() # 分割字符串
        print(strs)
        strs.reverse() # 翻转单词列表
        print(strs)
        return ' '.join(strs) # 拼接为字符串并返回
