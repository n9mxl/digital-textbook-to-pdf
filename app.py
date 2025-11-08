import streamlit as st
import pdfkit
import tempfile
import os

st.set_page_config(page_title="디지털 교과서 → PDF 변환기", layout="centered")

st.title("📘 디지털 교과서 고화질 PDF 변환기")
st.write("디지털 교과서 링크를 입력하면 자동으로 고화질 PDF로 변환합니다!")

url = st.text_input("🔗 교과서 링크를 입력하세요:")

if st.button("PDF로 변환하기"):
    if not url:
        st.warning("링크를 입력해주세요!")
    else:
        with st.spinner("페이지를 PDF로 변환 중입니다..."):
            try:
                temp_dir = tempfile.mkdtemp()
                pdf_path = os.path.join(temp_dir, "교과서.pdf")

                options = {
                    'enable-local-file-access': None,
                    'zoom': 1.5,  # 고화질 옵션
                    'encoding': "UTF-8",
                    'no-outline': None
                }

                pdfkit.from_url(url, pdf_path, options=options)

                with open(pdf_path, "rb") as f:
                    st.success("✅ PDF 변환 완료!")
                    st.download_button("📥 PDF 다운로드", f, file_name="교과서.pdf")

            except Exception as e:
                st.error(f"🚨 오류 발생: {e}")
