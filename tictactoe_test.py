from tictactoe import check_pattern, is_move_valid

def test_pattern_1():
    assert True == check_pattern("XXX456789")

def test_pattern_2():
    assert True == check_pattern("XXX4567X9")

def test_pattern_3():
    assert False == check_pattern("X2X4567X9")

def test_pattern_4():
    assert True == check_pattern("123XXX789")

def test_pattern_5():
    assert True == check_pattern("X23XXX789")

def test_pattern_6():
    assert False == check_pattern("123X5X789")

def test_pattern_7():
    assert True == check_pattern("123456XXX")

def test_pattern_8():
    assert True == check_pattern("12X456XXX")

def test_pattern_9():
    assert False == check_pattern("12345XX8X")

def test_pattern_10():
    assert True == check_pattern("X23X45X89")

def test_pattern_11():
    assert False == check_pattern("X23X56789")

def test_pattern_12():
    assert False == check_pattern("123XX6X89")

def test_pattern_13():
    assert True == check_pattern("1X34X67X9")

def test_pattern_14():
    assert True == check_pattern("1X3XX67X9")

def test_pattern_15():
    assert True == check_pattern("12X45X78X")

def test_pattern_16():
    assert True == check_pattern("X234X678X")

def test_pattern_17():
    assert True == check_pattern("12X4X6X89")

def test_pattern_18():
    assert False == check_pattern("OXXXOOXOX")

# def test_move_1():
#     assert True == is_move_valid(move="1x")

# def test_move_2():
#     assert False == is_move_valid(move="0x")

# def test_move_3():
#     assert False == is_move_valid(move="7a")

# def test_move_4():
#     assert False == is_move_valid(move="10O")
