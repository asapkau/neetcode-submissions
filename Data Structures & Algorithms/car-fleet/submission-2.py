class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        times = len(cars) * [0]

        for i in range(len(cars)):
            times[i] = (target - cars[i][0]) / cars[i][1]
        
        if len(times) == 1:
                return 1
                
        for i in range(1,len(times)):
            if not fleets:
                fleets.append(times[0])
            

            if times[i] > fleets[-1]:
                fleets.append(times[i])
            
            elif times[i] <= fleets[-1]:
                continue
        return len(fleets)





        