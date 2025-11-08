import streamlit as st
import imgkit
import tempfile
from PIL import Image
import os
from fpdf import FPDF

st.set_page_config(page_title="디지털 교과서 → PDF 변환기", layout="centered")

st.title("📘 디지털 교과서 고화질 PDF 변환기")
st.write("디지털 교과서 링크를 입력하면 자동으로 고화질 PDF로 변환합니다!")

url = st.text_input("🔗 교과서 링크를 입력하세요:")

if st.button("PDF로 변환하기"):
    if not url:
        st.warning("링크를 입력해주세요!")
    else:
        with st.spinner("페이지를 변환 중입니다... (조금만 기다려주세요)"):
            try:
                # 임시 폴더 생성
                temp_dir = tempfile.mkdtemp()

                # 변환 옵션 설정
                options = {
                    'format': 'png',
                    'encoding': "UTF-8",
                    'enable-local-file-access': None,
                    'quality': '100'
                }

                # 웹페이지를 이미지로 변환
                img_path = os.path.join(temp_dir, "page.png")
                imgkit.from_url(url, img_path, options=options)

                # PDF 파일 생성
                pdf_path = os.path.join(temp_dir, "output.pdf")
                pdf = FPDF()
                pdf.add_page()
                pdf.image(img_path, x=0, y=0, w=210, h=297)  # A4 사이즈
                pdf.output(pdf_path)

                with open(pdf_path, "rb") as f:
                    st.success("✅ PDF 변환 완료!")
                    st.download_button("📥 PDF 다운로드", f, file_name="교과서.pdf")
            except Exception as e:
                st.error(f"🚨 오류 발생: {e}")
