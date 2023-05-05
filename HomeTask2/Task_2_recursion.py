
def check_palindrome(s: str) -> bool:
    s_list = list(s)
    # print(s_list)
    s_list.reverse()
    # print(''.join(s_list))
    if s == ''.join(s_list):
     return True
    else:
     return False
def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()