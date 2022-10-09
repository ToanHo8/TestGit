import tryPytest

def test_add() :
    assert tryPytest.add(7,3) == 10
    assert tryPytest.add(7) == 9
    assert tryPytest.add(5) == 7

def test_product() :
    assert tryPytest.product(5,5) == 25
    assert tryPytest.product(5) == 10
    assert tryPytest.product(7) == 14
    assert tryPytest.product(7) == 1

# to test type:         pytest test_tryPytest.py            
                    #   pytest test_tryPytest.py -v         (given more infor)
                    #                            -s         (printout test case)
                    #   py.test                             (shortcut to test the lastest test)



# Trong git(VSCODE): file có màu xanh và có chữ U có nghĩa là mới add vô (new file added), 
# file có màu cam với chữ M là file đang đc chỉnh sửa nhưng chưa commit.