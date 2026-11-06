class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Process p into a list of sub strings separated by if they have a star or not: ".*ab.a.a*i" -> ['.*', 'ab.a.', 'a*', 'i']
        next_star = p.find('*')
        p_sub_strs = []

        while next_star != -1:
            p_sub_strs.append(p[ : next_star - 1])
            p_sub_strs.append(p[next_star - 1 : next_star + 1])
            p = p[next_star + 1 : ]
            next_star = p.find('*')

        p_sub_strs.append(p)
                
        for i in range(p_sub_strs.count('')):
            p_sub_strs.remove('')

        return matcher(s, p_sub_strs)

def get_priority(s: str) -> int:
    if '.' not in s and '*' not in s:
        return 3
    elif '.' in s and '*' not in s:
        return 2
    elif '.' not in s and '*' in s:
        return 1
    elif '.' in s and '*' in s:
        return 0
    else:
        return -1

def equal(s1: str, s2: str) -> bool:
    if '*' in s2:
        if s2[0] == '.':
            return True
        elif len(list(filter(lambda x : x != s2[0], s1))) == 0:
            return True
        else:
            return False
    else:
        if len(s1) != len(s2):
            return False
        else:
            for i in range(len(s1)):
                if s1[i] != s2[i] and s1[i] != '.' and s2[i] != '.':
                    return False
            return True

def matcher(s: str, p: List[str]) -> bool:
    #Base cases
    if s == "" and p == []:
        return True
    elif s != "" and p == []:
        return False

    else:
        compare = 0
        for i in range(len(p)):
            if get_priority(p[i]) > get_priority(p[compare]):
                compare = i
        

        for i in range(len(s) + 1): #Since split notation is being used, we avoid out of bounds errors since a would-be out of bounds split notation just returns and empty string
            if "*" in p[compare]:
                largest = 0
                for j in range(len(s)):
                    if equal(s[i : i + j + 1], p[compare]):
                        largest = j + 1
                if equal(s[i : i + largest], p[compare]): #Better readibility if I make this all a compound condition but it saved 32 ms doing it this way (avoids some needless calculation)
                    if matcher(s[ : i], p[ : compare]):
                        if matcher(s[i + largest : ], p[compare + 1 : ]):
                            return True

            else:
                if equal(s[i : i + len(p[compare])], p[compare]):
                    if matcher(s[ : i], p[ : compare]):
                        if matcher(s[i + len(p[compare]) : ], p[compare + 1 : ]):
                            return True

        return False           