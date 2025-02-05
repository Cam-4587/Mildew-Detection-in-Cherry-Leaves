import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect cherry leaves with powdery mildew will have clearly show white mildew powder \n" 
        f"that can differentiate them from a healthy leaf.\n"
        f"* An image montage shows that an infected cheery leaf has clear spots and patches of white mildew powder "
        f"across the leaf and in some cases can be seen along the midrib of the leaf and the veins of that leaf. \n"
        f"* Variability Image and Difference between Averages did not reveal any clear pattern to differentiate one from another."
        f"However, a small difference in the colour pigment of the average images is seen for both labels."
    )