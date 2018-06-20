class count:
    def count_ovverlapping_occurrences(s, ss):  # String, SubString
        # Needed Data Structures
        temp = []
        count = 0
        pos = 0

        for i in s:
            if not temp:
                if i == ss[pos]:
                    temp.append(i)
                    pos += 1
            else:
                if i == ss[pos]:
                    temp.append(i)
                    pos += 1
                else:
                    if temp[-1] == ss[0]:
                        last = temp[-1]
                        temp.clear()
                        temp.append(last)
                        pos = 1
                    else:
                        temp.clear()
                        pos = 0
            if "".join(temp) == ss:
                count += 1
                if temp[-1] == ss[0]:
                    last = temp[-1]
                    temp.clear()
                    temp.append(last)
                    pos = 1
                else:
                    temp.clear()
                    pos = 0
        return count

    def count_non_overlapping_occurrences(s, ss):  # String, SubString
        return s.count(ss)