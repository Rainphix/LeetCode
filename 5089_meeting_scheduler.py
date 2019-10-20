class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        exist1 = False
        exist2 = False
        slots = []
        for i in slots1:
            if i[1]-i[0] >= duration:
                exist1 = True
                slots.append(i)
        for j in slots2:
            if j[1]-j[0] >= duration:
                exist2 = True
                slots.append(j)
        if exist1 == False or exist2 == False:
            return []

        slots = sorted(slots)

        for s in range(len(slots) - 1):
            if slots[s][1] > slots[s+1][0]:
                start = slots[s+1][0]
                end = min(slots[s][1], slots[s+1][1])
                if end - start >= duration:
                    return [start, start + duration]
        return []

if __name__ == '__main__':
    s = Solution()
    slots1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
    slots2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
    duration = 456085
    print(s.minAvailableDuration(slots1,slots2,duration))
    ans = [98730764,99186849]