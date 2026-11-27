class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index  = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

def find_duplicates(nums):
    results = []
    my_dict = {}
    for i in nums:
        if i in my_dict:
            if i not in results:
                results.append(i)
            else:
                continue
        else:
            my_dict[i] = True
    return results

def first_non_repeating_char(string):
    if len(string) == 0:
        return None
    my_dict = {}
    for i in string:
        if i not in my_dict:
            my_dict[i] = True
        else:
            my_dict[i] = False
    for j in string:
        if my_dict[j] == True:
            return j
    return None

def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        cannonical = "".join(sorted(string))
        if cannonical in anagram_groups:
            anagram_groups[cannonical].append(string)
        else:
            anagram_groups[cannonical] = [string]
    return list(anagram_groups.values())
