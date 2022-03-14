from cmath import sqrt
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
            print("\nLeibniz formula states, that the sum from n=0 to infinity of [(-1)^n]/(2n + 1) = π/4")
            print("The first few elements: 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = π/4")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(numberOfElements + 1):
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

    def newtonFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        if printBasicInfo:
            print("\nNewton formula states, that the sum from n=0 to infinity of 2^n*(k!)^2/(2n + 1)! = π/2")
            print("The first few elements: 1 + 1/3(1 + 2/5(1 + 3/7(1 + ...))) = π/2")
        pi = 0
        for i in range(0, numberOfElements + 1):
            pi += (2**i)*math.factorial(i)**2/math.factorial(2*i + 1)
        pi *= 2
        print("\nπ calculated with Newton's formula, using " + str(numberOfElements) + " elements (n) is equal to: " + str(pi))
        return pi

    def nilakanthaFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        if printBasicInfo:
            print("\nNulakantha's formula states, that the sum from n=1 to infinity of [(-1)^(n - 1)]/[2n*(2n + 1)*(2n + 2)] = (π - 3)/4")
            print("The first few elements: 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ... = (π - 3)/4")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(1, numberOfElements + 1):
            pi += (-1)**(i - 1)/(2*i*(2*i + 1)*(2*i + 2))
        pi = 4*pi + 3
        print("\nπ calculated with Nalikantha's formula, using " + str(numberOfElements) + " elements (n) is equal to: " + str(pi))
        return pi
    
    def ramanujanFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        if printBasicInfo:
            print("\nRamanujan's formula states, that the product of the 2*sqrt(2)/9801 and the sum from n=0 to infinity of (4n)!(1103 + 26390n)/[(n!)^4*396^(4n)]= 1/π")
            # print("The first few elements: 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ... = 1/π")
            # print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(0, numberOfElements + 1):
            pi += math.factorial(4*i)*(1103 + 26390*i)/(math.factorial(i)**4*396**(4*i))
        pi *= 2*math.sqrt(2)/9801
        pi = 1/pi
        print("\nπ calculated with Ramanujan's formula, using " + str(numberOfElements) + " elements (n) is equal to: " + str(pi))
        return pi
    
    def chudnovskyFormula(self, numberOfElements: int, printBasicInfo: bool=True):
        print("")

if __name__ == "__main__":
    piApproximations = calculatePi()
    piApproximations.printBasicInfoAboutPi()
    piApproximations.leibnizFormula(10)
    piApproximations.johnWallisFormula(10)
    piApproximations.newtonFormula(10)
    piApproximations.nilakanthaFormula(10)
    piApproximations.ramanujanFormula(1)
