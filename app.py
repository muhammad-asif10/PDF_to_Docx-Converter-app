import streamlit as st
from pdf2docx import Converter
import tempfile
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PDF to Word Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.title {
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}
.subtitle {
    font-size: 16px;
    color: #6b7280;
    text-align: center;
    margin-bottom: 20px;
}
.card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}
.footer {
    text-align: center;
    color: gray;
    font-size:12px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">📄 PDF to Word Converter</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload any PDF and get an editable Word document instantly!</div>',
    unsafe_allow_html=True
)

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📄 Converter", "ℹ️ About", "🏷️ Credits"])

# ================= TAB 1: Converter =================
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "🗂️ Choose a PDF file",
        type=["pdf"],
        help="Upload a PDF file to convert into Word (.docx)"
    )

    if uploaded_file:
        st.info(f"**File Name:** {uploaded_file.name}  \n**File Size:** {uploaded_file.size / 1024:.2f} KB")

        # Use temporary directory for cloud-friendly files
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = os.path.join(temp_dir, uploaded_file.name)
            docx_path = pdf_path.replace(".pdf", ".docx")

            # Save uploaded PDF
            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.read())

            if st.button("Convert to Word"):
                with st.spinner("Converting PDF to Word..."):
                    try:
                        cv = Converter(pdf_path)
                        cv.convert(docx_path)
                        cv.close()

                        st.success("🎉 Conversion completed!")

                        with open(docx_path, "rb") as f:
                            st.download_button(
                                label="⬇ Download Word File",
                                data=f,
                                file_name=os.path.basename(docx_path),
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                key='download-docx'
                            )
                    except Exception as e:
                        st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 2: About =================
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("About This App")
    st.write("""
This **PDF to Word Converter** allows you to transform PDFs into editable Word documents instantly.  

**Features:**
- Works directly in the browser (Streamlit Cloud compatible)
- Editable Word output
- Supports multiple PDF pages

**Tech Stack:**
- Python
- Streamlit
- pdf2docx
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 3: Credits =================
with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Credits")
    st.write("""
**Developed by:**  
**Muhammad Asif**  
BS Computer Science | University of Veterinary & Animal Sciences (UVAS), Ravi Campus

Built with ❤️ using Streamlit.
""")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Muhammad Asif</div>', unsafe_allow_html=True)
