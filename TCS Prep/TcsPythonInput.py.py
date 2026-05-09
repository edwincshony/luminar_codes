def input_with_size():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Array (size given):", *arr[:n])

def input_as_string():
    arr = list(map(str, input().split()))
    print("Array (from string using split()):", *arr)

def most_used_input_format():
    line = input()
    num_str = ""
    arr = []

    for ch in line:
        if ch.isdigit():
            num_str += ch
        elif num_str:
            arr.append(int(num_str))
            num_str = ""

    if num_str:
        arr.append(int(num_str))

    print("Array (extracted numbers):", *arr)

if __name__ == "__main__":
    print("Enter size and then numbers:")
    input_with_size()

    print("Enter numbers in a single line:")
    input_as_string()
    
    print("Enter a string containing digits and characters:")
    most_used_input_format()