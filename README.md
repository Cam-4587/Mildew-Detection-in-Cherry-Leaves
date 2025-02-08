# Powdery Mildew detector in Cherry leaves

Mildew detection in Cherry leaves is a streamlit dashboard app that uses Machine Learning to produce a prediction model where the client can upload images of cherry leaves and a report is produced to indicate if those leaves contain powdery Mildew or not.


This app also visualises the cherry leaf data and compares healthy cherry leaves to cherry leaves containing powdery mildew in the following ways:
- Creating both an average image and a variability image for both healthy cherry leaves and cherry leaves containing powdery mildew.
- An image montage where the client can select from either the 'healthy' label or the 'powdery mildew' label from a drop down list and a montage of images are produced to compare images from both labels.

[View live project here!!!](https://cherry-leaf-mildew-detector-3-3672595f0fcb.herokuapp.com/)

![](/docs/am_i_responsive%20_image.png)

# Dataset Content
- The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)  We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains 4208 images taken from the client's crop fields. The images show healthy cherry leaves(2104 images) and cherry leaves that have powdery mildew (2104 images), a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

![](/docs/kaggle_dataset_image.png)

# Business Requirements
- The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.
- To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.
    - 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    - 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
