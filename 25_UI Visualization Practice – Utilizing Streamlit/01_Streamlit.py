"""
- Streamlit: Data Science를 위한 맞춤형 웹 애플리케이션을 만들 수 있는 파이썬의 라이브러리.
* 구성요소: 텍스트 요소, 인풋 위젯, 이미지 및 상태바
"""
# 필요한 라이브러리 임포트
import streamlit as st


def main():
    # 웹 페이지 제목 설정
    st.title('Streamlit 예제 애플리케이션')

    # 사이드바에 메뉴 추가
    menu = st.sidebar.selectbox(
        '메뉴 선택',
        ['홈', '정보', '데이터 입력']
    )

    if menu == '홈':
        # 홈 화면에 표시할 내용
        st.write('이곳은 홈 화면입니다.')

    elif menu == '정보':
        # 정보 화면에 표시할 내용
        st.write('이곳은 정보 화면입니다.')

    elif menu == '데이터 입력':
        # 사용자로부터 데이터 입력 받기
        name = st.text_input('이름을 입력하세요.')
        age = st.number_input('나이를 입력하세요.', min_value=0, max_value=100)
        occupation = st.selectbox('직업을 선택하세요.', ['학생', '개발자', '기타'])

        # 입력 받은 데이터 화면에 출력
        st.write(f'이름: {name}')
        st.write(f'나이: {age}')
        st.write(f'직업: {occupation}')


if __name__ == '__main__':
    main()
