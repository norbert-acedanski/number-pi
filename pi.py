import math

class calculatePi():
    def __init__(self):
        pass

    def printBasicInfoAboutPi(self):
        print("The number π is a mathematical constant, approximately equal to " + str(math.pi) + ". It is defined in Euclidean geometry as the ratio of a circle's circumference to its diameter, and also has various equivalent definitions.")
        print("π can be approximated with some fractions:")
        print("• 22/7         ≈ " + str(22/7) + " which is different from π after 2-nd decimal place")
        print("• 333/106      ≈ " + str(333/106) + " which is different from π after 4-th decimal place")
        print("• 355/113      ≈ " + str(355/113) + " which is different from π after 6-th decimal place")
        print("• 52163/16604  ≈ " + str(52164/16604) + " which is different from π after 7-th decimal place")
        print("• 103993/33102 ≈ " + str(103993/33102) + " which is different from π after 9-th decimal place")
        print("The first 50 decimal digits are 3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510...")
        print("π shows up in many different equations such as e^(iπ) + 1 = 0")

    def leibnizFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        if printBasicInfo:
            print("\nLeibniz formula states, that the sum from n=0 to infinity of (-1)^n/(2n + 1) = π/4")
            print("The first few elements: 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = π/4")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(numberOfElements):
            pi += (-1)**i/(2*i + 1)
        pi *= 4
        print("\nπ calculated with Leibniz formula, using " + str(numberOfElements) + " elements (n) is equal to: " + str(pi))
        return pi

    def johnWallisFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        if printBasicInfo:
            print("\nJohn Wallis formula states, that the product from n=1 to infinity of 2n/(2n - 1)*2n/(2n + 1) = π/2")
            print("The first few elements: 2/1*2/3 * 4/3*4/5 * 6/5*6/7 * ... = π/2")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 1
        for i in range(1, numberOfElements + 1):
            pi *= 2*i/(2*i - 1)*2*i/(2*i + 1)
        pi *= 2
        print("\nπ calculated with John Wallis formula, using " + str(numberOfElements) + " elements (n) is equal to: " + str(pi))
        return pi

    def newtonEulerFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        pass

    def nilakanthaFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        pass
    
    def ramanujanFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        print("")
    
    def chudnovskyFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        print("")

if __name__ == "__main__":
    piApproximations = calculatePi()
    piApproximations.printBasicInfoAboutPi()
    piApproximations.leibnizFormula(10)
    piApproximations.johnWallisFormula(10)
