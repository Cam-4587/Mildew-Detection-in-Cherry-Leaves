import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
    f"**General Information**\n"
    f"* The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. "
    f"Currently, the process is manual verification to see if a given cherry tree contains powdery mildew. An employee spends around 30 minutes on each tree, "
    f"taking a few samples of tree leaves and verifying visually if the tree leaf is healthy or has powdery mildew. If there is powdery mildew, "
    f"the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. "
    f"The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable "
    f"due to the time spent in the manual inspection process.\n\n"
    f"* To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, "
    f"if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, "
    f"there is a realistic chance to replicate this project for all other crops.\n\n"
    f"**Project Dataset**\n"
    f"* The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops. The original dataset can be found here [Cherry leaf dataset](https://www.kaggle.com/codeinstitute/cherry-leaves)"
)


    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Cam-4587/Mildew-Detection-in-Cherry-Leaves/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )
