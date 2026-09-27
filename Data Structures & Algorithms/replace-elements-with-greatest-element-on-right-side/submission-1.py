class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_i = -1
        for i in range(-1, -len(arr)-1, -1): #start, stop, step
            current = arr[i] # need to save the i val first cuz next line replaces and we would loose the real value to check for the max. 
            arr[i] = max_i
            if current > max_i:
                max_i = current
        return arr

