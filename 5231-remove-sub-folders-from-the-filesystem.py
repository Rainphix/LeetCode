class Solution:
    def removeSubfolders(self, folder):
        if len(folder) <= 1:
            return folder

        l_ = []
        for i in folder:
            l_.append(i.split('/'))

        child = []

        for i in range(len(l_) - 1):
            for j in range(i, len(l_) - 1):
                minSize = min(len(l_[i]), len(l_[j]))
                is_child = True
                for k in range(minSize):
                    if l_[i][k] != l_[j][k]:
                        is_child = False
                if is_child == True:
                    child.append(l_[j])

        print(child)
        print(l_)
        return l_

if __name__ == '__main__':

    s = Solution()
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    print(s.removeSubfolders(folder))
