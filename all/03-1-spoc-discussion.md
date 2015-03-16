# lec5 SPOC思考题


NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy system 分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```

>  优缺点见下表

| 分配算法 | 优点 | 缺点 |
|--------|------|-----|
| 最优匹配 | 尽可能多的利用空间，fragment 较少 | 每次需要遍历所有 block ，较慢 |
| 最差匹配 | 对于分配的大小基本一致的情况，空间利用较好 | 较慢，在现实中不实用 |
| 最快匹配 | 不用遍历，较快 | 空间利用不佳 |
| buddy  | free 较快，只需要 log 时间，external fragment 少 | internal fragment 很多 |

## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种或多种，在应用程序层面(可以 用python,ruby,C++，C，LISP等高语言)来实现，给出你的设思路，并给出测试用例。 (spoc)

>  使用 python 实现了 best fit ，代码包含测试。

[点我查看](https://github.com/cty12/os_exercises/blob/master/src/memory_management.py)

>  结果：

```
➜  src git:(master) ✗ python memory_management.py
alloc:  128
alloc:  128
alloc:  128
used:  [[0, 128], [128, 256], [256, 384]]
free:  [[384, 512]]

free:  128
used:  [[0, 128], [256, 384]]
free:  [[384, 512], [128, 256]]

free:  256
used:  [[0, 128]]
free:  [[128, 512]]

alloc:  64
alloc:  64
used:  [[0, 128], [128, 192], [192, 256]]
free:  [[256, 512]]

free:  127
the block is not used. fail to free.
free:  128
used:  [[0, 128], [192, 256]]
free:  [[256, 512], [128, 192]]

alloc:  128
used:  [[0, 128], [192, 256], [256, 384]]
free:  [[128, 192], [384, 512]]

alloc:  32
used:  [[0, 128], [192, 256], [256, 384], [128, 160]]
free:  [[384, 512], [160, 192]]
```

---

## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。

## “连续内存分配”与视频相关的课堂练习

### 5.1 计算机体系结构和内存层次
MMU的工作机理？

- [x]  

>  http://en.wikipedia.org/wiki/Memory_management_unit

L1和L2高速缓存有什么区别？

- [x]  

>  http://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer
>  Where exactly L1, L2 and L3 Caches located in computer?

>  http://en.wikipedia.org/wiki/CPU_cache
>  CPU cache

### 5.2 地址空间和地址生成
编译、链接和加载的过程了解？

- [x]  

>  

动态链接如何使用？

- [x]  

>  


### 5.3 连续内存分配
什么是内碎片、外碎片？

- [x]  

>  

为什么最先匹配会越用越慢？

- [x]  

>  

为什么最差匹配会的外碎片少？

- [x]  

>  

在几种算法中分区释放后的合并处理如何做？

- [x]  

>  

### 5.4 碎片整理
一个处于等待状态的进程被对换到外存（对换等待状态）后，等待事件出现了。操作系统需要如何响应？

- [x]  

>  

### 5.5 伙伴系统
伙伴系统的空闲块如何组织？

- [x]  

>  

伙伴系统的内存分配流程？

- [x]  

>  

伙伴系统的内存回收流程？

- [x]  

>  

struct list_entry是如何把数据元素组织成链表的？

- [x]  

>  
