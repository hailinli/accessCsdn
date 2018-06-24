csdn既没有做接口ip访问量的限制，访问量统计时也没有做同一ip相同时间段的重复访问重复计数的处理。这也时这个程序能够刷访问量的原因。

------

## 一、思路介绍
1. 从页面中 https://blog.csdn.net/linhai1028/article/list/2 解析出所有文章链接 
2. 依次访问这些文章 
由于csdn的浏览量要过30多秒后再一次看就又可一加了，所以我们设置一个定时器，每30秒后执行一次，所以我们的浏览量过万也不是什么事了。
## 二、使用
```
git clone git@github.com:hailinli/accessCsdn.git
cd acceseeCsdn.git
python accessCsdn.py
```
------

## 参考
1. https://blog.csdn.net/m0_37499059/article/details/79183236
## 环境
1. python3
2. requests2.18
3. lxml4.2
