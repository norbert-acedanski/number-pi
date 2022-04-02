import math
import matplotlib.pyplot as plt
import sys

class CalculatePi():
    def __init__(self):
        self.plot_number = 0

    def print_basic_info_about_pi(self):
        print("The number π is a mathematical constant, approximately equal to " + str(math.pi) + ". It is defined in Euclidean geometry as the ratio of a circle's circumference to its diameter, and also has various equivalent definitions.")
        print("π can be approximated with some fractions:")
        print("• 22/7         ≈ " + str(22/7) + " which is different from π after 2-nd decimal place")
        print("• 333/106      ≈ " + str(333/106) + " which is different from π after 4-th decimal place")
        print("• 355/113      ≈ " + str(355/113) + " which is different from π after 6-th decimal place")
        print("• 52163/16604  ≈ " + str(52164/16604) + " which is different from π after 7-th decimal place")
        print("• 103993/33102 ≈ " + str(103993/33102) + " which is different from π after 9-th decimal place")
        print("The first 50 decimal digits are 3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510...")
        print("π shows up in many different equations such as e^(iπ) + 1 = 0")

    def leibniz_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nLeibniz formula states, that the sum from n=0 to infinity of [(-1)^n]/(2n + 1) = π/4")
            print("The first few elements: 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = π/4")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(number_of_elements + 1):
            pi += (-1)**i/(2*i + 1)
        pi *= 4
        print("\nπ calculated with Leibniz formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi

    def john_wallis_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nJohn Wallis formula states, that the product from n=1 to infinity of 2n/(2n - 1)*2n/(2n + 1) = π/2")
            print("The first few elements: 2/1*2/3 * 4/3*4/5 * 6/5*6/7 * ... = π/2")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 1
        for i in range(1, number_of_elements + 1):
            pi *= 2*i/(2*i - 1)*2*i/(2*i + 1)
        pi *= 2
        print("\nπ calculated with John Wallis formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi

    def newton_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nNewton formula states, that the sum from n=0 to infinity of 2^n*(k!)^2/(2n + 1)! = π/2")
            print("The first few elements: 1 + 1/3(1 + 2/5(1 + 3/7(1 + ...))) = π/2")
        pi = 0
        for i in range(0, number_of_elements + 1):
            pi += (2**i)*math.factorial(i)**2/math.factorial(2*i + 1)
        pi *= 2
        print("\nπ calculated with Newton's formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi

    def nilakantha_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nNulakantha's formula states, that the sum from n=1 to infinity of [(-1)^(n - 1)]/[2n*(2n + 1)*(2n + 2)] = (π - 3)/4")
            print("The first few elements: 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ... = (π - 3)/4")
            print("It is one of the methods, that takes a very large number of the \"n\" to see the convergence")
        pi = 0
        for i in range(1, number_of_elements + 1):
            pi += (-1)**(i - 1)/(2*i*(2*i + 1)*(2*i + 2))
        pi = 4*pi + 3
        print("\nπ calculated with Nalikantha's formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi
    
    def ramanujan_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nRamanujan's formula states, that the product of the 2*sqrt(2)/9801 and the sum from n=0 to infinity of (4n)!(1103 + 26390n)/[(n!)^4*396^(4n)] = 1/π")
            # print("The first few elements: 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ... = 1/π")
            print("It is one of the methods, that takes a very small number of the \"n\" to see the convergence (1 is enough)")
        pi = 0
        for i in range(0, number_of_elements + 1):
            pi += math.factorial(4*i)*(1103 + 26390*i)/(math.factorial(i)**4*396**(4*i))
        pi *= 2*math.sqrt(2)/9801
        pi = 1/pi
        print("\nπ calculated with Ramanujan's formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi
    
    def chudnovsky_formula(self, number_of_elements: int, print_basic_info: bool=True):
        if print_basic_info:
            print("\nDavid Chudnovsky and Gregory Chudnovsky's formula states, that the product of 12 and the sum from n=0 to infinity of (-1)^n*(6n)!*(13591409 + 545140134n)/[(3n)!*(n!)^3*640320^(3n + 3/2)] = 1/π")
            # print("The first few elements: 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - ... = 1/π")
            print("It is one of the methods, that takes a very small number of the \"n\" to see the convergence (1 is enough)")
        pi = 0
        for i in range(0, number_of_elements + 1):
            pi += ((-1)**i*math.factorial(6*i)*(13591409 + 545140134*i))/(math.factorial(3*i)*math.factorial(i)**3*640320**(3*i + 3/2))
        pi *= 12
        pi = 1/pi
        print("\nπ calculated with Chudnovsky formula, using " + str(number_of_elements) + " elements (n) is equal to: " + str(pi))
        return pi

    def graph_convergence(self, function_to_work_with, number_of_elements: int, start_index: int=0, stop_index: int=-1):
        element_list = [function_to_work_with(element) for element in range(number_of_elements)]
        # if stop_index == -1:
        #     stop_index = len(element_list)
        stop_index = len(element_list) if stop_index == -1 else stop_index
        if start_index < 0 or stop_index > len(element_list):
            print("Value of start_index or stop_index exceeded")
            sys.exit()
        # plt.figure(self.plot_number)
        plt.figure("Convergence of the " + function_to_work_with.__name__)
        plt.plot(range(start_index, len(element_list[start_index: stop_index]) + start_index), element_list[start_index: stop_index], label=function_to_work_with.__name__, marker="o")
        plt.plot([start_index, len(element_list)], [math.pi, math.pi], ":")
        plt.text(-len(element_list)/50 + start_index, math.pi, "Exact value\nof π", horizontalalignment='center')
        plt.xlabel("x - number of elements from the series")
        plt.ylabel("y - calculated value of π")
        plt.title("π calculations")
        plt.legend(loc='center right', framealpha=0.5)
        plt.show()
        self.plot_number += 1

if __name__ == "__main__":
    pi_approximations = CalculatePi()
    pi_approximations.print_basic_info_about_pi()
    pi_approximations.leibniz_formula(10)
    pi_approximations.john_wallis_formula(10)
    pi_approximations.newton_formula(10)
    pi_approximations.nilakantha_formula(10)
    pi_approximations.ramanujan_formula(1)
    pi_approximations.chudnovsky_formula(1)
    pi_approximations.graph_convergence(pi_approximations.leibniz_formula, 100)
    pi_approximations.graph_convergence(pi_approximations.nilakantha_formula, 50, 10, 50)