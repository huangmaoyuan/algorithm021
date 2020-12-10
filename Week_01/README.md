第一周学习笔记

1，leetcode官方题解不一定是最好的。
2，每道题刷5遍。
3，数组增加删除的时间复杂度是o（n），查找是o（1）。
4，链表增加删除的时间复杂度是o（1），查找是o（n）。
5，跳表里的元素始终是有序的，对标的是平衡树和二分查找。跳表插入删除查找都是logn的复杂度。实现原理是多级索引。缺点是增删后索引地址会变，维护成本高。实例有Redis（用作缓存）。
6，栈是先进后出，添加删除o（1），查询o（n）。
7，队列是先进先出，添加删除o（1），查询o（n）。
8，双端队列是两端进出，添加删除o（1），查询o（n）。
9，peek（）查看栈顶元素。pop（）弹出栈顶元素查看。
10，优先队列，按照元素优先级取出，插入复杂度是o（logn），取出是o（1）。底层实现方法可以是heap，bst，treap。
11，如果一个东西有最近相关性，就可以用栈解决。
12，用两个队列可以实栈，用两个栈可以实现队列。


python 库相关官方文档
python Heap queue algorithm
https://docs.python.org/2/library/heapq.html

python High-performance container datatypes
https://docs.python.org/2/library/collections.html

#最近在学go语言，所以同一个算法题也用go写了一遍。
