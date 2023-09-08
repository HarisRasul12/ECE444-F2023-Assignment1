from utils import *

def util_tests():
    
    number = 25
    
    result = utils.reversed(number)
    assert result == 52, f"Expected 52 but got {result}"
    print("T1 reverse: Integer Test Pass")
    
    result = utils.reversed(-number)
    assert result == -52, f"Expected -52 but got {result}"
    print("T2 reverse: Negative Integer Test Pass")
    
    try:
        result = utils.reversed(float(number))
    except:
        print("T3 reverse: Float Test Failed:cannot work with float requires type int")

    try:
        result = utils.reversed(str(number))
    except:
        print("T4 revese: Str Test Failed:cannot work with str requires type int")


    #formatter

    result1, result2 = utils.formatter(number)
    assert ((result1 == '0b11001') and (result2 == '0o31')),"fomatter test case 1 failed"
    print("T5 fomatter: Integer Test Pass")
    
    result1,result2 = utils.formatter(-number)
    assert ((result1 == '-0b11001') and (result2 == '-0o31')),"fomatter test case 2 failed"
    print("T6 formatter: Negative Integer Test Pass")
    
    try:
        result = utils.formatter(float(number))
    except:
        print("T7 formatter: Float Test Failed:cannot work with float requires type int")

    try:
        result = utils.formatter(str(number))
    except:
        print("T8 formatter: Str Test Failed:cannot work with str requires type int")


if __name__ == "__main__":
    util_tests()
    print("Test Cases Complete")
