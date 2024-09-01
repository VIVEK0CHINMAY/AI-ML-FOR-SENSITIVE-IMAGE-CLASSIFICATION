<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sensitive Image Classification README</title>
</head>
<body>
    <h1>Sensitive Image Classification</h1>

    <h2>Overview</h2>
    <p>This project focuses on classifying images as either sensitive or non-sensitive using deep learning models. The project utilizes a Convolutional Neural Network (CNN) and MobileNet to achieve accurate image classification. A Tkinter GUI is implemented to make the model accessible and user-friendly. The dataset for training and testing was downloaded from Kaggle.</p>

    <h2>Project Structure</h2>
    <p>The project is organized into the following directories and files:</p>
    <ul>
        <li><strong>data/</strong>: Contains the dataset downloaded from Kaggle, including training, validation, and test images.</li>
        <li><strong>models/</strong>: Stores the saved models after training (CNN and MobileNet).</li>
        <li><strong>scripts/</strong>: Contains the Python scripts used for data preprocessing, model training, evaluation, and the GUI.</li>
        <li><strong>gui.py</strong>: Main file that runs the Tkinter-based GUI for image classification.</li>
        <li><strong>requirements.txt</strong>: Lists the Python dependencies required to run the project.</li>
    </ul>

    <h2>Dataset</h2>
    <p>The dataset used in this project was sourced from Kaggle. It includes a variety of sensitive and non-sensitive images, divided into training, validation, and testing sets.</p>
    <ul>
        <li><strong>Sensitive Images</strong>: Images deemed inappropriate or unsuitable for general audiences.</li>
        <li><strong>Non-Sensitive Images</strong>: General images that are safe for viewing by all audiences.</li>
    </ul>

    <h2>Installation</h2>
    <p>To run this project, ensure you have Python installed on your system. The necessary Python packages are listed in the <code>requirements.txt</code> file.</p>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/sensitive-image-classification.git
cd sensitive-image-classification</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Download the dataset from Kaggle and place it in the <code>data/</code> directory.</li>
    </ol>

    <h2>Model Training</h2>
    <p>The models were trained using the following approaches:</p>
    <ul>
        <li><strong>Convolutional Neural Network (CNN)</strong>: A basic CNN was implemented and trained on the dataset. The model architecture consists of multiple convolutional layers followed by pooling layers and fully connected layers.</li>
        <li><strong>MobileNet</strong>: A pre-trained MobileNet model was fine-tuned on the dataset to improve classification performance.</li>
    </ul>
    <p>Both models were evaluated on the validation and test sets to assess their accuracy in classifying images.</p>

    <h2>GUI Implementation</h2>
    <p>A Tkinter-based GUI was developed to allow users to upload an image and classify it as sensitive or non-sensitive using the trained models. The GUI provides a simple interface for selecting an image and displaying the classification result.</p>

    <h2>Usage</h2>
    <ol>
        <li>Run the GUI:
            <pre><code>python gui.py</code></pre>
        </li>
        <li>Use the GUI to upload an image. The model will classify the image and display whether it is sensitive or non-sensitive.</li>
    </ol>

    <h2>Results</h2>
    <p>The project achieved the following results on the test set:</p>
    <ul>
        <li><strong>CNN Model Accuracy</strong>: XX%</li>
        <li><strong>MobileNet Model Accuracy</strong>: XX%</li>
    </ul>
    <p>The MobileNet model demonstrated superior performance compared to the CNN model, likely due to its pre-trained features and deeper architecture.</p>

    <p align="center">
        <img src="images/results_chart.png" alt="Results Chart" width="600">
    </p>

    <h2>Future Work</h2>
    <p>Potential improvements for this project include:</p>
    <ul>
        <li><strong>Data Augmentation</strong>: Implementing data augmentation techniques to increase the robustness of the model.</li>
        <li><strong>Model Optimization</strong>: Experimenting with different model architectures and hyperparameters to further improve classification accuracy.</li>
        <li><strong>Real-Time Classification</strong>: Extending the GUI to support real-time image classification using a webcam or video feed.</li>
    </ul>

    <h2>Contributions</h2>
    <p>Feel free to open issues or submit pull requests if you have any ideas for improvements or new features.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
</body>
</html>
