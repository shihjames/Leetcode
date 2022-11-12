class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n == 0
            
        count = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        count += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        count += 1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        count += 1
                        flowerbed[i] = 1
        
        return count >= n