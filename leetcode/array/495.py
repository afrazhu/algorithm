#!/usr/bin/env python3
# https://leetcode-cn.com/problems/teemo-attacking/
# In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
# You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
# 在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长
# 你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
# 输入: [1,2], 2
# 输出: 3
# 原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
# 但是第 2 秒初，提莫再次攻击了已经处于中毒状态的艾希。
# 由于中毒状态不可叠加，提莫在第 2 秒初的这次攻击会在第 3 秒末结束。
# 所以最终输出 3 。
# 中规中矩
timeSeries = [1, 3, 4, 8, 10]
duration = 2
totalTime = duration
preTime = timeSeries[0]
for point in timeSeries:
    if point > preTime:
        if point - preTime >= duration:
            totalTime = totalTime + duration
        else:
            totalTime = totalTime + (point - preTime)
    preTime = point
print(totalTime)

# 其他操作
# 总时间-重复时间：https://leetcode-cn.com/u/leafin/
res = duration * len(timeSeries) - sum(
    [duration - timeSeries[i + 1] + timeSeries[i] if duration - timeSeries[i + 1] + timeSeries[i] > 0 else 0 for i in
     range(len(timeSeries) - 1)])
print(res)
# 最小值：https://leetcode-cn.com/problems/teemo-attacking/solution/qu-zui-xiao-zhi-ji-ke-by-rabbit-38/
totalTime = 0
size = len(timeSeries)
for i in range(size - 1):
    totalTime += min(duration, timeSeries[i + 1] - timeSeries[i])
totalTime = totalTime + duration
print(totalTime)
