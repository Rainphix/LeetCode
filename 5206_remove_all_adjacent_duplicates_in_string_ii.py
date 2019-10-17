class Solution:
    def removeDuplicates(self, s, k) -> str:

        if len(s) < k:
            return s

        str_l = list(s)
        back = []
        back.append("forerver")
        back.append(str_l[0])
        conti = 1

        for i in range(1, len(str_l)):
            if str_l[i] == back[-1]:
                back.append(str_l[i])
                conti = conti + 1

                if conti == k:
                    for j in range(k):
                        back.pop(-1)
                    conti = 0
            else:
                back.append(str_l[i])
                conti = 1

        back.pop(0)
        return self.removeDuplicates(''.join(back), k) if len(s) != len(''.join(back)) else  ''.join(back)

if __name__ == '__main__':
    s = "dtpdtaaaaaaaaappppppppppppppppppppaaaaaaaaaaxxxxxxxxxxxxxxsssssssssjjjjjjjjjjjjjjjjjjjjxxxxxxxxxxxxxxxxxxxxsssssssjjjjjjjjjjjjjjjjjjjjssssxxxxxxatdwvvpctpggggggggggggggggggggajagglaaaaaaaaaaaaaaaaaaaa"
    k = 20
    so = Solution()
    print(so.removeDuplicates(s,k))