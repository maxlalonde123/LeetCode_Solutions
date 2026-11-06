class Solution:
    def isHappy(self, n: int) -> bool:
        seen_sums = []
        cycle = False
        num = n
        sum = 0
        
        # If num is 1 or num is in seen_nums we have our answer, otherwise continue searching for 1 or a cycle
        while num != 1 and cycle == False:
            # Get each digit one by one
            last_digit_gotten = False
            
            while last_digit_gotten == False:
                digit = (num % 10)
                num = (num - digit) // 10
                
                if num <= 0:
                    last_digit_gotten = True

                sum += digit**2
 
            if sum in seen_sums:
                cycle = True
            else:
                seen_sums.append(sum)
                num = sum
                sum = 0
        
        if num == 1:
            return True
        elif cycle:
            return False