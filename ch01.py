import streamlit as st
import streamlit.components.v1 as components

def main():


    st.markdown("HTML JS Streamlit 적용")
    js_code = """ 
    <h3>Hi</h3>
    <script>
    function sayHello() {
        alert('Hello from JavaScript in Streamlit Web');
    }
    </script>
    <button onclick="sayHello()">Click me</button>
    """
    components.html(js_code)
    st.title("도태훈 화이팅~")
    st.header("이것은 메인 태훈입니다")
    st.subheader("이것은 서브태훈입니다")
    st.write("파이썬 문법 사용 가능")
    st.write("-" * 50) # print()랑 비슷한 느낌이다리
    a = 1
    b = 2

    st.write(a + b)

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    st.markdown("""
    # PART 1.
    - 색상 테스트 : ~~~~
    """)

    st.markdown("""
    # Chapter 1.
    - 피타고라스 정리 : :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
    """)

    st.markdown("## Chapter 2. \n"
                "- 다이뇻수 졍진귀~**.\n"
                "   * 엔쒸는 :blue[colored blue], 기아는? **:red[colored] ** and bold.")
    
    st.markdown("HTML CSS 마크다운 적용")
    html_css = """
    <style>
        table.customTable {
        width: 100%;
        background-color: #FFFFFF;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #7ea8f8;
        border-style: solid;
        color: #000000;
        }
    </style>
    <table class="customTable">
      <thead>
        <tr>
          <th>이름</th>
          <th>나이</th>
          <th>직업</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>손아섭</td>
          <td>35</td>
          <td>1번 지명타자</td>
        </tr>
        <tr>
          <td>박민우</td>
          <td>30</td>
          <td>2번 2루수</td>
        </tr>
      </tbody>
    </table>
    """
    st.markdown(html_css, unsafe_allow_html=True)

if __name__ == "__main__":

    main()