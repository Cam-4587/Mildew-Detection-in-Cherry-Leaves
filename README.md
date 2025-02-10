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

# Hypothesis

Powdery mildew containing cherry leaves  will have clearly showing white mildew powder that can differentiate them clearly from healthy cherry leaves.

## Validation
- I will validate the hypothesis by collecting an image dataset from the client and creating an image montage for both healthy and powdery mildew containing leaves.

- I will test the hypothesis by using image analysis:
    - I will validate the hypothesis by collecting an image dataset from the client and creating an image montage for both healthy and powdery mildew-affected leaves.
    - Creating an **average image** for both the 'powdery mildew' labelled images and the 'healthy' images label for comparison to each other.
    - Creating a **variable image** for both the 'powdery mildew' labelled images and 'healthy' labelled images for comparison to each other.

# Rationale to map the business requirements to the Data Visualizations and ML tasks

- Business requirement 1: the client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

    - An **average** image and a **variability** image both 'healthy' and 'powdery mildew' will be displayed on the dashboard.
    - An **average** image for 'powdery_mildwew' containing leaves and 'healthy' leaves is displayed alongside a **difference** image for comparison between the two on the dashboard.
    - An image montage is created to allow the client to view randomly selected images from either the 'powdery mildew' or 'healthy' image database.
- Business requirement 2: The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

    - A prediction learning model is created to predict if a cherry leaf image (or images) can be classified as being healthy or containing powdery mildew.
    - The prediction model should have at least a 97% accuracy level.
    - The client can download a report of the images that they have selected in the form of an excel file.
# ML Business case
## Page 1: Quick Project Summary
### Quick project summary

- General Information
    - Farmy and Foods are facing a challenge where their cherry leaves have been presenting with powdery mildew.

    - The current process is manual verification, taking a few samples of tree leaves from a cherry tree and verifying visually if the tree leaf is healthy or not. The employee will spend 30 minutes on each tree.
    - The company has thousands of cherry trees located on multiple farms across the country. Therefore, this manual process is not scalable due to the time spent on the manual process.

    - To save times on this, the IT team suggested an ML system that instantly detects whether using an image of a leaf tree image whether it is healthy or has powdery mildew.

- Project Dataset
    - The available dataset contains 4208 images provided by Farmy & Foods, taken from their crops. 
    - Of these images 2104 of these are healthy cherry leaves and 2104 are cherry leaves with powdery mildew.
- Business requirements
    - The client is interested in a study to differentiate between a powdery mildew contained and healthy cherry leaf.
    - The client is interested in telling whether a given cherry leaf contains malaria parasites or not.
## Page 2: Cherry leaves Visualiser
- It will answer business requirement 1
    - Checkbox 1 - Difference between average and variability image
    - Checkbox 2 - Differences between average parasitised and average uninfected cells
    - Checkbox 3 - Image Montage
## Page 3: Mildew detection
- It will answer business requirement 2
    - Link to download a set of powdery mildew contained and healthy cherry leaves.
    - A user interface to upload multiple image files. It will display the image and a prediction statement indicating if the cherry leaf is infected with powdery mildew or not and the probability associated with this statement.
    - Table with the image name and preciction results.
    - A download button to dowload the table.
## Page 4: Project Hypothesis and Validation
- Block for each project hypothesis, describe the   conclusion and how you validated it.
## page 5: ML prediction Metrics
- Label Frequencies for Train, Validation, and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result



# Deployment
## Heroku
- The app live link is [here](https://cherry-leaf-mildew-detector-3-3672595f0fcb.herokuapp.com/).
- Set the runtime.txt Python version to `python-3.12.2`
- The project was deployed to Heroku using the following steps.
    1. Log in to Heroku and create an app, give it an appropriate name and select either 'United States' or 'Europe'.
    2. At the deploy tab, select Github as the deployment method.
    3. Select your respository name and click Search, Once it is found, click Connect.
    4. Select the branch you want to deploy, then click Deploy Branch.
    5. The The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
    6. If the slug size is too large, then add large files not required for the app to the .slugignore file.


