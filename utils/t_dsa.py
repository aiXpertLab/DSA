import streamlit as st

def _general():
    st.image('./images/dsa.png')
    st.write('''## 逻辑结构

1. 集合：彼此无关
2. 线性：栈：先进后出。队列：先进先出，后进后出。，相对于线性表而言，站和队列是操作受限的线性表。
3. 树形：1-n
4. 图形：n-n

## 物理结构/存储结构
1. 顺序存储：排队。顺序存储结构（Sequential Storage Structure）：这种结构将数据元素存储在一块连续的存储空间中。每个元素占据一段连续的内存空间，并且相邻元素之间在内存中也是相邻的。数组就是一种典型的顺序存储结构，可以通过下标来直接访问元素。顺序存储结构的特点是随机访问速度快，但插入和删除操作需要移动大量元素1。
2. 链式存储：叫号。链式存储结构（Linked Storage Structure）：链式存储结构通过节点之间的指针连接来存储数据元素。每个节点包含数据和指向下一个节点的指针，最后一个节点的指针为空。链式存储结构的特点是插入和删除操作方便快捷，不需要移动元素，但访问元素需要遍历链表1。
3. 索引存储结构（Indexed Storage Structure）：索引存储结构使用一个索引表来存储数据元素的地址或者指针。索引表中的每个条目包含一个关键字和对应数据元素的地址或指针。通过索引表可以快速定位和访问数据元素，而无需遍历整个数据集。索引存储结构适用于静态数据集或者数据集更新较少的情况1。
4. 散列存储结构（Hashed Storage Structure）：散列存储结构使用散列函数将数据元素的关键字映射为存储位置。存储位置可以是数组或者其他数据结构，称为散列表。通过散列函数，可以直接计算出数据元素的存储位置，从而实现快速的插入、查找和删除操作。散列存储结构适用于需要快速查找和访问数据的情况，但可能存在散列冲突的问题，需要解决冲突并保证散列函数的均匀性。

            ''')
    
def _ai():
    st.write('''
## Data Structures Demystified
#### 1. Tensors
Tensors are the backbone of data in AI/ML. These multi-dimensional arrays can be 
- 0D (Scalar): A single numerical value, like a temperature reading.
- 1D (Vector): An ordered list of values, e.g., a one-dimensional array of sensor readings.
- 2D (Matrix): A table of data where each column represents an attribute, and each row represents an observation, like a spreadsheet or CSV file.
- 3D (e.g., Time Series): This is where data starts to get interesting. Time series data is represented as a tensor with dimensions like (duration, time steps, features). For instance, consider daily stock prices over a year, where each day's price is a feature, and you track it over a year.
- 4D (e.g., Video): Videos are essentially sequences of 2D frames. Thus, video data is represented as a 4D tensor, where the dimensions could be (frames, height, width, channels). Here, channels can represent color channels like red, green, and blue.
- 5D (e.g., Hyperspectral Imaging): In remote sensing, hyperspectral data contains not only spatial and temporal information but also spectral details. This type of data can be represented as a 5D tensor: (scenes, rows, columns, spectral bands, time). Each scene consists of rows and columns with specific spectral bands captured over time.

#### 2. Vectors
Vectors are one-dimensional arrays, often used for `feature vectors`. 

Each element represents a feature or variable, making it ideal for data points in linear algebra and machine learning models.

Example (Text Data): In natural language processing (NLP), each word in a sentence can be encoded as a unique vector, forming a vector space model. These vectors enable various text-based AI applications like document clustering, sentiment analysis, and semantic similarity.

#### 3. Matrices
Matrices are two-dimensional arrays widely used in AI/ML. Each cell contains data, allowing for complex relationships to be represented effectively.

Example (Tabular Data): In tabular data, each row could represent a customer, and each column an attribute like age, income, or purchase history. Predictive modeling, such as customer churn prediction, relies on matrices to handle such data.

#### 4. Data Dimensions
Data dimensions are critical for understanding the structure and characteristics of your data. 
These dimensions can affect how you preprocess, model, and analyze data.

1D: When to Use — For univariate data, like a single variable over time.
2D: When to Use — Ideal for tabular data, such as spreadsheets or SQL tables.
3D: When to Use — Time series data, which involves sequences of data over time, can be efficiently represented using 3D tensors.
4D: When to Use — Videos, where each frame is a 2D image, and the temporal dimension is added.
5D: When to Use — Hyperspectral imaging, which combines spatial, spectral, and temporal data.

#### 5. Scaling Data
Data scaling, or `normalization`, is a crucial preprocessing step. 
It ensures that features with different ranges or units have a similar scale, preventing certain features from dominating the others in a machine learning model.

Example: In a tabular dataset, you might have columns representing age and income. 
Age values typically range from 0 to 100, while income can range from a few thousand to millions. 
By scaling these features, both contribute equally to the model.

#### 6. Data structures play a vital role in AI/ML:

They enable efficient data manipulation, making it easier to preprocess and prepare data for modeling.
The choice of data structure often depends on the nature of the data and the ML model used.
Understanding data dimensions helps you grasp how your data evolves, improving feature engineering and model design.
Exploring Data Dimensions

1. 1D Data: Linear Sequences

1D data structures represent simple linear sequences of values. They are often used for text data, where each element can represent a character or a word in a sentence. Example: [1, 2, 3]

2. 2D Data: Rows and Columns

2D data structures are grids with rows and columns, ideal for tabular data. Each row typically represents an instance, and each column corresponds to a feature. Example: [[1, 2, 3], [4, 5, 6]]

3. 3D Data: Adding Depth to 2D

3D data structures introduce depth to 2D. They are commonly used for time series data, where each row can denote a specific time, and each cell contains values associated with that time point. Example: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

4. 4D Data: Adding an Extra Dimension

4D data structures are employed in more complex scenarios. They can represent video data, with dimensions accounting for height, width, time, and color channels. Example: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

5D Data: Complex Volumes

5D data describes dynamic 3D volumes evolving over time. It’s often used in medical imaging or simulations. Example: [[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]], [[[[17, 18], [19, 20]], [[21, 22], [23, 24]]], [[[25, 26], [27, 28]], [[29, 30], [31, 32]]]]]

Examples

1D Data (1-Dimensional Data):

Example: A simple list of numbers.
Application: Time series data where each element represents a single point in time.
2D Data (2-Dimensional Data):

Example: A table or matrix, like a spreadsheet.
Application: Tabular data where each row represents an observation or record, and each column represents a different attribute or variable.
3D Data (3-Dimensional Data):

Example: A stack of 2D matrices.
Application: Volumetric data in medical imaging, where each slice of the stack represents a cross-sectional image of a patient.
4D Data (4-Dimensional Data):

Example: A video sequence, where each frame is a 2D image.
Application: Video data where each frame is 2D, and the additional dimension represents time, capturing changes over time.
5D Data (5-Dimensional Data):

Example: Hyperspectral data captured by remote sensors.
Application: Hyperspectral imaging in remote sensing, where each data point has five dimensions: spatial (2D), spectral (wavelength), and temporal.
Conclusion

Mastering data structures is a cornerstone of AI/ML. From text and tabular data to time series and videos, each data type and dimension has its own characteristics and usage. By choosing the right data structure and understanding its dimension, you’re better equipped to handle the complexities of AI and machine learning, ensuring that your models are built on a solid foundation.
             
             
             
             ''')