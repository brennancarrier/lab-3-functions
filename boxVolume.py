def volume(length, width, height):
    return length * width * height

def main():
    length = float(input("Box #1 length (cm): "))
    width = float(input("Box #1 width (cm): "))
    height = float(input("Box #1 height (cm): "))
    print("Box #1 volume is", volume(length, width, height), "ccm")

    length = float(input("Box #2 length (cm): "))
    width = float(input("Box #2 width (cm): "))
    height = float(input("Box #2 height (cm): "))
    print("Box #2 volume is", volume(length, width, height), "ccm")
main()
