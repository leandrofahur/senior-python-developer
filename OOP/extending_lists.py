class SuperList(list):
    def __init__(self, list):
        super().__init__(list)

    def __len__(self):
        return 1000


print('--- Extending Lists ---')
super_list1 = SuperList([1, 2, 3, 4, 5])
print(len(super_list1))
print(super_list1)
super_list1.append(6)
print(super_list1)
