class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort()
        stack=[]
        for car in cars[::-1]:
            pos=car[0]
            spd=car[1]
            time=(target-pos)/spd
            if len(stack)==0 or time>stack[-1]:
                stack.append(time)
        return len(stack)