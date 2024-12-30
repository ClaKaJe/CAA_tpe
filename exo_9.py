import math

def Norme(complex_number):
    x, y = complex_number
    return math.sqrt(x**2 + y**2)

def find_min_max_positions(norms):
    min_pos = norms.index(min(norms))
    max_pos = norms.index(max(norms))
    return min_pos, max_pos

def main():
    Tab = []
    total_norm = 0

    while total_norm < 100:
        real_part = float(input("Enter the real part of the complex number: "))
        imaginary_part = float(input("Enter the imaginary part of the complex number: "))
        complex_number = (real_part, imaginary_part)
        norm = Norme(complex_number)
        
        if total_norm + norm >= 100:
            break
        
        Tab.append(norm)
        total_norm += norm

    if not Tab:
        print("the norm of the complex number you entered it's higher than 100")
        return
    
    min_pos, max_pos = find_min_max_positions(Tab)
    print(f"Norms: {Tab}")
    print(f"Position of smallest norm: {min_pos}")
    print(f"Position of largest norm: {max_pos}")

if __name__ == "__main__":
    main()  