import streamlit as st


st.title("Final Grade Calculator")
st.write("""
    Calculate your final grade based on the weights of assignments, quizzes, and exams.
    Simply enter your grades and weights below.
""")

# Input fields for grades and weights
st.header("Enter Your Grades and Weights")

# Grades and weights for Assignments
assignment_grade = st.number_input("Assignment Grade (0-100)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)
assignment_weight = st.number_input("Assignment Weight (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)

# Grades and weights for Quizzes
quiz_grade = st.number_input("Quiz Grade (0-100)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)
quiz_weight = st.number_input("Quiz Weight (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)

# Grades and weights for Exams
exam_grade = st.number_input("Exam Grade (0-100)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)
exam_weight = st.number_input("Exam Weight (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)

# Button to calculate the final grade
if st.button("Calculate Final Grade"):
    total_weight = assignment_weight + quiz_weight + exam_weight

    if total_weight != 100:
        st.error("The total weight must equal 100%. Please adjust the weights.")
    else:
        # Calculate the weighted grades
        final_grade = (
            (assignment_grade * assignment_weight / 100) +
            (quiz_grade * quiz_weight / 100) +
            (exam_grade * exam_weight / 100)
        )
        st.success(f"Your Final Grade is: {final_grade:.2f}%")

# Instructions for users
st.info("Make sure the total weight adds up to 100%. If it doesn't, you'll see an error message.")
