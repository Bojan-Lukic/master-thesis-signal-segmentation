import statistics
import random
import numpy as np
from statistics import variance as var


def create_test_signal():
    arr = []
    tot = []
    for i in range(0, 3):
        if i == 0:
            a = 0
            b = 60
            c = 40
            d = 100
        elif i == 1:
            a = 40
            b = 50
            c = 30
            d = 40
        else:
            a = 50
            b = 60
            c = 80
            d = 90
        for i in range(0, 4):
            rint = random.randint(0, 50)
            rint2 = random.randint(0, 50)
            if rint > rint2:
                temp = rint
                rint = rint2
                rint2 = temp
            arr = arr + [random.randint(rint, rint2) for _ in range(5)]
        for i in range(0, 2):
            for i in range(0, 4):
                rint = random.randint(c, d)
                rint2 = random.randint(c, d)
                if rint > rint2:
                    temp = rint
                    rint = rint2
                    rint2 = temp
                arr = arr + [random.randint(rint, rint2) for _ in range(5)]
            for i in range(0, 4):
                rint = random.randint(a, b)
                rint2 = random.randint(a, b)
                if rint > rint2:
                    temp = rint
                    rint = rint2
                    rint2 = temp
                arr = arr + [random.randint(rint, rint2) for _ in range(5)]
        arr = arr + [random.randint(rint, rint2)]
        tot.append(arr)
        arr = []
    
    return(tot)