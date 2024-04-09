## 1장. 철학과 개념
- Pythonic
  - 파이썬을 파이썬답고, 파이썬스럽게 사용하기 위한 코드 작성 가이드 라인
  - Python2 에서는 dictionary 의 함수중 has_key가 있었으나 Python3 에서는 in으로 대체
  - 같다는 조건문은 boolean 자료형 그 자체를 사용하도록 권고, ==, is 전부 잘못된 표현
  - 네임 스페이스 Local, Enclosed, Global, Built-in
  - nonlocal 변수 global도 local도 아닌 변수를 Free variable라고 함수
  
- First-Class Citizen
  - 어떤 개체를 다른 개체의 매개변수로 전달, 반환값으로 사용 가능
  - integer, floating-point 는 First-Class Citizen

- 고차함수(Higher-Order Function)
  - 함수를 매개변수를 전달 또는 반환값으로 사용하는 것

- 중첩함수(Nested Function)
  - 함수 안에 함수
  - 외부함수, 내부함수로 나뉨
  - 내부함수들은 scope chain에 의해서 자신을 감싸고 있는 외부 함수의 메모리에 접근 가능

- 클로저(Closure)
  - 함수의 반환값으로 내부 함수를 사용하는 함수
  - nonlocal 변수는 이론적으로 메모리에서 제거되는 것임
  - 그러나 클로저는 "함수와 함수가 사용하는 환경을 저장" 하기에 문제가 안됨
  - 클로저를 확인하려면 클로저함수().__closure__[0].cell_contents 로 가능
  - 사용 시기
    - 첫번째 : global 변수를 사용하고 싶지 않을 때
    - 두번째 : 클래스를 사용하지 않기 위해서, 모든 것을 클래스로 만들 필요 없음(변수, 함수 적을 경우)
    - 세번째 : 데코레이터(함수 실행 전후로 특정 로직을 수행하기 위한 기능)를 사용하기 위해서
  - 주의할 점: nonlocal 변수에는 시간이나 흐름에 따라 변하는 값을 사용하지 않음

- Partial Application
  - 고정 매개변수와 가변 매개변수가 있을 때, 가변 매개변수를 wrapping 하여 전달하는 기법
  

