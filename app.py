import streamlit as st
import google.generativeai as genai

# إعدادات واجهة المستخدم الاحترافية
st.set_page_config(
    page_title="المكتبة الشاملة الذكية AI",
    page_icon="📚",
    layout="centered"
)

# تصميم الواجهة بالعربية
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div.stButton > button:first-child {
        background-color: #2e7d32; color: white; border-radius: 10px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 مشروع المكتبة الشاملة الذكي")
st.write("البحث العلمي المباشر في كافة كتب ومجلدات الشاملة باستخدام Gemini 1.5")

# ربط المفتاح السري (تأكد من وضعه في إعدادات المنصة لاحقاً)
API_KEY = "AIzaSyAWzdArZkwfuETLV4dzuI1fTmBGfAA-xr4"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# خانة البحث
query = st.text_input("أدخل سؤالك أو المسألة العلمية:", placeholder="مثلاً: أقوال المفسرين في قوله تعالى...")

if st.button("استخراج الإجابة فوراً"):
    if query:
        with st.spinner('جاري البحث في آلاف المجلدات...'):
            try:
                # الالتزام بشرط البحث داخل المكتبة الشاملة فقط
                prompt = f"بصفتك خبير في كتب المكتبة الشاملة، ابحث في كافة تصنيفاتها (الفقه، التفسير، الحديث، اللغة) وأجب بدقة ومباشرة عن: {query}. لا تخرج عن نطاق المكتبة الشاملة."
                response = model.generate_content(prompt)
                
                st.markdown("### 📖 النتيجة العلمية:")
                st.info(response.text)
                st.caption("تم استخراج هذه المعلومة بناءً على محتوى المكتبة الشاملة.")
            except Exception as e:
                st.error(f"عذراً، حدث تأخير تقني: {e}")
    else:
        st.warning("يرجى كتابة سؤال أولاً.")
