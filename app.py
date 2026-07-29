import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="💊")
st.title("💊 حاسبة جرعات باراسيتامول الذكية")

weight = st.number_input("أدخل وزن الطفل بالكيلوجرام:", min_value=0.0, step=0.1)

if weight > 0:
    if weight < 5.5:
        st.error("❌ الوزن أقل من 5.5 كجم. يرجى مراجعة الطبيب لحماية الرضع.")
    elif weight > 60.0:
        st.error("❌ الوزن أعلى من 60 كجم. مخصص للأوزان حتى 60 كجم فقط.")
    else:
        dose = min(weight * 15, 500.0)
        st.success(f"✅ الجرعة الآمنة هي: {dose:.1f} ملجم")

        
        

            
