"""
 * Python_CS101_CHAPTER01
 *
 * @author soaring(yongseok.dev@gmail.com)
 *
 * 2022.06.15.
"""
"""
 * Python 프로그램 작성 예제 hubo를 사용한 함수의 활용
"""
# python
python

# import_library
from cs1robots import *

#opne
create_world()

#create_hubo
hubo = Robot(beepers = 1)

# basic function
hubo.move()
hubo.turn_left()

# turn_right()
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

# for 
for i in range(4):
    print("CS101 is factastic!")