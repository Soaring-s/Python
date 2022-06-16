"""
 * Python_CS101_CHAPTER01
 *
 * @author soaring(yongseok.dev@gmail.com)
 *
 * 2022.06.16.
"""
"""
 * Python 미로 탈출 예제
"""

#c1
hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
#c2
hubo.drop_beeper()
if not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
#c3
hubo.drop_beeper()
while not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

"""
확인 사항
    1. comment(주석) 과도한 주석은 코드가독성을 낮춤
    2. 코드에 의미 있는 이름 붙이기(함수명)
    3. 주요원칙
        간단하게 시작하기(단계적 개발)
        한번에 하나의 작은 작업만 수행하기(상세화)
        각각의 작업들이 이전 작업에 영향 주지 않기
        알기 쉬운 유용한 주석 달기
"""