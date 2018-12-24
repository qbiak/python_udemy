#
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 100
  
# conditional flow uses if, elif, else
    if x < y:
        st = "true is here"
    elif x == y:
        st = "very hard case"
    else:
        st = "this is false!"
    print(st)

    result = "true" if x < y else "false"

    print(result)
# conditional statements let you use "a if C else b"
  

if __name__ == "__main__":
    main()
