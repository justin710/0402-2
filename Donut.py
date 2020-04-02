
import math

def getCircleArea(redius):
    return math.pow(redius,2) * math.pi

def getDonutArea(r1, r2):

    Area1 = getCircleArea(r1)
    Area2 = getCircleArea(r2)

    return abs(Area1 - Area2)

if __name__ == "__main__":
    result = getDonutArea(5,10)
    print(result)

    