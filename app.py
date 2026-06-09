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
    val = bank[key]
    return random.choice(val) if isinstance(val, list) else val

def truncate_comment(comment, target=TARGET_CHARS):
    if len(comment) <= target:
        return comment
    truncated = comment[:target].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p, _ = pronouns
    opening = random.choice(opening_phrases)
    parts = [
        f"{opening} {name} {pick(attitude_bank, att)}." + (f" {lowercase_first(attitude_target)}" if attitude_target else ""),
        f"In reading, {p} {pick(reading_bank, read)}.",
        f"In writing, {p} {pick(writing_bank, write)}.",
        f"For the next year, {p} should {lowercase_first(pick(reading_target_bank, read_t))}.",
        f"In addition, {p} should {lowercase_first(pick(writing_target_bank, write_t))}.",
        random.choice(closer_bank) + "."
    ]
    return truncate_comment(" ".join(parts), TARGET_CHARS)

# ---------- SESSION STATE ----------
for key, default in {
    "all_comments": [],
    "generated_comment": "",
    "generated_name": "",
    "last_inputs": None,
    "generate_count": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ---------- APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown("Fill in the details and click **Generate Comment**. Use **Regenerate** to get a different variant before adding it.")

# ---------- FORM ----------
with st.form("report_form"):
    name       = st.text_input("Student Name")
    gender     = st.selectbox("Gender", ["Male", "Female"])
    att        = st.selectbox("Attitude band",            [90,85,80,75,70,65,60,55,40,0])
    read       = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40,0])
    write      = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40,0])
    read_t     = st.selectbox("Reading target band",      [90,85,80,75,70,65,60,55,40,35])
    write_t    = st.selectbox("Writing target band",      [90,85,80,75,70,65,60,55,40,35])
    attitude_target = st.text_input("Optional Attitude Next Steps")
    submitted  = st.form_submit_button("Generate Comment")

if submitted and name:
    inputs = (name, gender, att, read, write, read_t, write_t, attitude_target)
    st.session_state["last_inputs"] = inputs
    st.session_state["generated_name"] = name
    st.session_state["generated_comment"] = generate_comment(
        name, att, read, write, read_t, write_t, get_pronouns(gender), attitude_target
    )
    st.session_state["generate_count"] += 1

# ---------- COMMENT DISPLAY ----------
if st.session_state["generated_comment"]:
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Regenerate Variant"):
            inputs = st.session_state["last_inputs"]
            name_s, gender_s, att_s, read_s, write_s, read_t_s, write_t_s, att_target_s = inputs
            st.session_state["generated_comment"] = generate_comment(
                name_s, att_s, read_s, write_s, read_t_s, write_t_s,
                get_pronouns(gender_s), att_target_s
            )
            st.session_state["generate_count"] += 1
            st.rerun()
    with col2:
        if st.button("✅ Add Comment to Report"):
            # grab the current text area value via session state before clearing
            edit_key = f"edit_{st.session_state['generate_count']}"
            final = st.session_state.get(edit_key, st.session_state["generated_comment"])
            st.session_state["all_comments"].append(
                f"{st.session_state['generated_name']}: {final}"
            )
            st.session_state["generated_comment"] = ""
            st.session_state["generated_name"] = ""
            st.session_state["last_inputs"] = None
            st.rerun()

    edited = st.text_area(
        "Generated Comment (editable)",
        value=st.session_state["generated_comment"],
        height=200,
        key=f"edit_{st.session_state['generate_count']}"
    )
    st.caption(f"Character count: {len(edited)} / {TARGET_CHARS}")

# ---------- ALL COMMENTS ----------
if st.session_state["all_comments"]:
    st.markdown("---")
    st.markdown("### All Generated Comments")
    for i, c in enumerate(st.session_state["all_comments"], 1):
        st.write(f"**{i}.** {c}")

    # ---------- DOWNLOAD ----------
    file_stream = io.BytesIO()
    doc = Document()
    for c in st.session_state["all_comments"]:
        doc.add_paragraph(c)
    doc.save(file_stream)
    file_stream.seek(0)

    st.download_button(
        label="📄 Download Full Report (Word)",
        data=file_stream,
        file_name="English_Report_Comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
