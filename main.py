import streamlit as st
import random
import time

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="เจ้าแม่ชิกกะดู้ คำนวณเลขเด็ด",
    page_icon="🙏",
    layout="centered"
)

# 2. แต่งสวย + ซ่อนเมนู (CSS Magic)
st.markdown("""
    <style>
    /* --- ส่วนสำคัญ: ซ่อนเมนู Streamlit และ GitHub --- */
    
    /* 1. ซ่อนแถบด้านบนสุด (ที่มีจุด 3 จุด และปุ่ม Deploy) */
    header {visibility: hidden;}
    
    /* 2. ซ่อน Footer ด้านล่าง (ที่เขียนว่า Made with Streamlit) */
    footer {visibility: hidden;}
    
    /* 3. ซ่อนปุ่ม Manage App (รูปมงกุฎ/ตั้งค่า มุมขวาล่าง) */
    .stAppDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    
    /* ------------------------------------------- */

    /* พื้นหลังแอพสีแดงเข้ม */
    .stApp {
        background-color: #8B0000;
    }
    
    /* หัวข้อสีทอง */
    h1 {
        color: #FFD700 !important;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* ข้อความทั่วไปสีขาว */
    p, label, .stMarkdown, div {
        color: #FFFFFF !important;
        text-align: center;
        font-size: 18px;
    }

    /* กรอบตัวเลข */
    .lucky-number {
        font-size: 80px;
        font-weight: bold;
        color: #FFD700 !important;
        text-align: center;
        background-color: #380000;
        border: 3px solid #FFD700;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-shadow: 0 0 10px #FFD700;
    }

    /* ปุ่มกด (ตัวหนังสือดำ) */
    .stButton > button {
        width: 100%;
        background-color: #FFD700 !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 10px;
        height: 60px;
    }
    .stButton > button p {
        color: #000000 !important;
        font-size: 24px !important;
        font-weight: bold !important;
    }
    .stButton > button:hover {
        background-color: #FFFFFF !important;
        border: 2px solid #FFD700 !important;
    }
    .stButton > button:hover p {
        color: #8B0000 !important;
    }
    
    /* กล่องคำทำนาย */
    .prediction-box {
        background-color: #380000;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #FFD700;
        margin-bottom: 20px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนแสดงผลหลัก
st.title("🙏 เจ้าแม่ชิกกะดู้ ประทานพร 🙏")
st.write("ตั้งจิตอธิษฐาน... แล้วกดปุ่มด้านล่าง")

# รายชื่อคำทำนาย
predictions = [
    "งวดนี้มาแน่! เตรียมกระสอบใส่เงิน",
    "ดวงกำลังพุ่ง บุญหล่นทับ",
    "เลขนี้สวยมาก อย่าลืมกลับด้วยนะ",
    "เจ้าแม่คอนเฟิร์ม! จัดไปหนักๆ",
    "เบาๆ พอกรุบกริบนะลูกเอ๊ย",
    "ถ้าถูกรางวัล อย่าลืมทำบุญนะ",
    "เห็นแล้วชอบ ก็จัดไปเลย!",
    "ระวังเจ้ามืออั้น รีบซื้อด่วน",
    "เลขที่บ้าน เลขรถ ลองเอามาผสมดูนะ",
    "งวดนี้ 3 ตัวตรงต้องมาแล้วแหละ!"
]

# ปุ่มเขย่าเซียมซี
if st.button("🧧 เขย่าเซียมซีขอเลขเด็ด 🧧"):
    # อนิเมชั่น
    progress_text = "กำลังสื่อสารกับสิ่งศักดิ์สิทธิ์..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.015)
        my_bar.progress(percent_complete + 1, text="เจ้าแม่กำลังคำนวณด้วยระบบ AI...")
    
    my_bar.empty()
    
    # สุ่มเลข
    num_2_digit = random.randint(0, 99)
    num_3_digit = random.randint(0, 999)
    quote = random.choice(predictions)

    st.balloons()
    
    # แสดงคำทำนาย (ใช้ CSS class ที่สร้างไว้)
    st.markdown(f"""
        <div class="prediction-box">
            <h3 style='color: #FFD700 !important; margin: 0;'>✨ คำทำนาย: {quote}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("เลขท้าย 2 ตัว")
        st.markdown(f"<div class='lucky-number'>{num_2_digit:02d}</div>", unsafe_allow_html=True)
    with col2:
        st.write("เลขท้าย 3 ตัว")
        st.markdown(f"<div class='lucky-number'>{num_3_digit:03d}</div>", unsafe_allow_html=True)

    st.write("---")
    st.caption("*คำเตือน: เป็นความเชื่อส่วนบุคคล (AI สุ่มมั่วๆ) เล่นอย่างมีสตินะจ๊ะ* 😆")

else:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDd4aWJ4aWJ4aWJ4aWJ4aWJ4aWJ4aWJ4aWJ4aWJ4aWJ4/3o7TKSjRrfIPjeiVyM/giphy.gif", use_container_width=True)
    st.caption("รอกดปุ่มอยู่นะจ๊ะ...")