try:
    number = "abc"
    result = number / 0

    print(result)

except Exception as e:
    print("Error occurred:")
    print(e)