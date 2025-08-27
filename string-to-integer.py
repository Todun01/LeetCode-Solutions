class Solution(object):
    def myAtoi(self, s):
        number = str(s).strip()
        final_num = 0
        final_num_str = ""
        signs = "-+"
        digits = "1234567890"
        isNegative = False
        for l in range(len(number)):
            if number[l] not in digits and number[l] not in signs:
                print("not in any")
                break
            if number[l] == signs[0] and int(l) == 0:
                print("neg found")
                isNegative = True
            if number[l] == signs[1] and int(l) == 0:
                print("pos found")
                pass
            if number[l] in signs and int(l) != 0:
                print(l)
                print(number[l])
                return final_num
            if number[l] in digits:
                print("num found")
                print(number[l])
                final_num_str += number[l]
                final_num = int(final_num_str)
                print(isNegative)
                if final_num != 0 and isNegative:
                    final_num = -1 * final_num
        if final_num < -2 ** 31:
            final_num = -2 ** 31
        if final_num > (2 ** 31) - 1:
            final_num = (2 ** 31) - 1
        print(final_num)
        return final_num
        

        