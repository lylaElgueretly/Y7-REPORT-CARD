# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# =========================================

import random
import streamlit as st
from docx import Document
import io
from statements import *

TARGET_CHARS = 499

# ---------- HELPERS ----------
def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    return "they", "their"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def pick(bank, key):
    """Pick a random option from a bank entry that may be a list or a string."""
    val = bank[key]
    if isinstance(val, list):
        return random.choice(val)
    return val

def truncate_comment(comment, target=TARGET_CHARS):
    if len(comment) <= target:
        return comment
    truncated = comment[:target].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    attitude_sentence = f"{opening} {name} {pick(attitude_bank, att)}."
    reading_sentence = f"In reading, {p} {pick(reading_bank, read)}."
    writing_sentence = f"In writing, {p} {pick(writing_bank, write)}."
    reading_target_sentence = f"For the next year, {p} should {lowercase_first(pick(reading_target_bank, read_t))}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(pick(writing_target_bank, write_t))}."
    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""
    closer_sentence = random.choice(closer_bank) + "."

    comment_parts = [
        attitude_sentence + attitude_target_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
        closer_sentence
    ]

    comment = " ".join(comment_parts)
    comment = truncate_comment(comment, TARGET_CHARS)
    return comment

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown("Fill in the student details and click **Generate Comment**.")

if "all_comments" not in st.session_state:
    st.session_state["all_comments"] = []

if "generated_comment" not in st.session_state:
    st.session_state["generated_comment"] = ""

if "generated_name" not in st.session_state:
    st.session_state["generated_name"] = ""

# ---------- STUDENT FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40,0])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40,0])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40,0])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40,35])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40,35])
    attitude_target = st.text_input("Optional Attitude Next Steps")
    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    pronouns = get_pronouns(gender)
    st.session_state["generated_comment"] = generate_comment(
        name, att, read, write, read_t, write_t, pronouns, attitude_target
    )
    st.session_state["generated_name"] = name

if st.session_state["generated_comment"]:
    edited = st.text_area(
        "Generated Comment (editable)",
        value=st.session_state["generated_comment"],
        height=200,
        key="edit_area"
    )
    st.write(f"Character count: {len(edited)} / {TARGET_CHARS}")

    if st.button("Add Comment to Report"):
        st.session_state["all_comments"].append(
            f"{st.session_state['generated_name']}: {edited}"
        )
        st.session_state["generated_comment"] = ""
        st.session_state["generated_name"] = ""
        st.rerun()

# ---------- ALL COMMENTS ----------
if st.session_state["all_comments"]:
    st.markdown("### All Generated Comments:")
    for c in st.session_state["all_comments"]:
        st.write(c)

    # ---------- DOWNLOAD ----------
    file_stream = io.BytesIO()
    doc = Document()
    for c in st.session_state["all_comments"]:
        doc.add_paragraph(c)
    doc.save(file_stream)
    file_stream.seek(0)

    st.download_button(
        label="Download Full Report (Word)",
        data=file_stream,
        file_name="English_Report_Comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
