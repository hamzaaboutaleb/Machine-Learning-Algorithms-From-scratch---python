# Machine learning 

### Introduction : 

- Data is cheap and abundant (data warehouses , data marts) , the knowledge is expensive and scarce. 
- Build a model that is good and useful approximation to the data. 
- A branch of artificial intelligence, concerned with the design and development of algorithms that allow computers to evolve behaviors based on empirical data.
- As intelligence requires knowledge, it is necessary for the computers to acquire knowledge.
![alt text](images/image.png)
- The image above illustrates a very useful concept. There are some problems in the IT world that are difficult or even impossible to solve by explicitly writing rules in code, such as image recognition. The solution we have today is to train a machine learning model on data, allowing it to learn patterns and relationships and effectively create its own algorithm for making predictions.
- So what is Machine learning ? is the study of algorithms that improve their performances at some task with experience
- training is the process of making the system able to learn. 
- The success of Machine learning system depends also on the algorithm used , the algorithm control the search to find and build the structure of knowledge.
- the algorithm should extract some useful informations from the training data.
- Algorithm : Supervised Learning - Unsupervised learning - Semi supervised learning and Reinforcement learning.
 ![alt text](images/image-1.png)
 - ML in nutshell : tens of thousands of ML algorithm, hundrends new each year , Every machine learning algorithm has 3 components : the presentation , the evaluation and the optimization. 
 - Representation :Decision trees
 Sets of rules / Logic programs
 Instances
 Graphical models (Bayes/Markov nets)
 Neural networks
 Support vector machines
 Model ensembles
 Etc.
 - Evaluation : Accuracy
 Precision and recall
 Squared error
 Likelihood
 Posterior probability
 Cost / Utility
 Margin
 Entropy
 K-L divergence
 Etc.
 - Optimization : Combinatorial optimization
 E.g.: Greedy search
 Convex optimization
 E.g.: Gradient descent
 Constrained optimization
 E.g.: Linear programming
 ![alt text](images/image-2.png)

 ## Steps of developing a machine learning application : 
1. Collect the data
2. prepare the input data 
3. analyze the input data
4. filter the garbage
4. train the model on the data
5. test the model 
6. Use the model 
![alt text](images/image-3.png)
![alt text](images/image-4.png)

## 1. Data preparation : 
![alt text](images/image-5.png)
### Steps to construct your data 
- to construct your dataset (and before doing data transformation), you should :
1. Collect raw data 
2. Identify feature and label sources 
3. Select a sampling strategy 
4. Split the data
- These steps depend a lot on how you’ve framed your ML problem. Use the self-check below to refresh your memory about problem framing and to check your assumptions about data collection.
- For me : Pick as many features as you can, so you can start observing which features have the strongest predictive power.
- Garbage in , garbage out -> at the enf your model is as good as your data is .

## how to measure the data quality to improve it ? 
### Size of the dataset : 
---
- As a rough rule of thumb, your model should train on at least an order of magnitude more examples than trainable parameters. Simple models on large data sets generally beat fancy models on small data sets. 
 ![alt text](images/image-6.png)
- it is no matter only of having a lot of data,  quality matters too 
### quality of data : 
- when you are collecting the data , you must define the term "quality" for your data.Certain aspects of quality tend to correspond to better-performing models:
1. reliability : measures the degree to which you trust your data, a model trained on a reliable data is most likely to yield a mode useful predictions than a model trained on unreliable data. In measuring reliability , you must determine : 
- how common are label errors ? for example , if your data is labeled by humans , sometimes humans make mistakes.
- are your features noisy ? for example GPS measurements fluctuate, some noise is okay. Youll never purge your data set of all noise. You can collect more examples too.
- Is the data properly filtered for your problem ? for example should your data set include search queries from bots ? if you re building a spam detection system then likely the answer is yes but if you re trying to improve search results for humans then no. 
<b>
what makes data unreliable : 
- examples : 
- Comitted values , for instance a person forgot to enter a value for house age
- Duplicate examples, a server mistakenly uploaded the same record twice 
. bad labels : for instance , a person mislabeled a picture of an aak traa as a maple 
- bad feature values, for example someone typed an extra digit or a thermometer was left out in the sun. 
2. feature representation :
- Representation is the mapping of data to useful features. You'll want to consider the following questions : 
- how is data shown to the model ? 
- should you normalize numeric values ? 
- how should you handle outliers ? 

3. minimizing skew
- the results work well offline , then in your live experiment , those results dont hold up ! what could be happening ? 
- this problem suggests training/serving skew - that is different results are computed for your metrics at training time vs serving time. 
- causes of skew can be subtle but have deadly effects on your results. always consider what data is available to your model at preiction time. During training , use only the features that youll have available in serving , and make sure that your training set is representative of your serving traffic. 

## Identifying labels and sources 
### Direct vs Derived Lables 
- machine learning is easier when your label is well defined
- the ebst label is the direct label : "is the user a fan of Taylor swift"
- derived label : user has watched a taylor swift video on youtube , your model will be as good as the connection between your derived label and your desired prediction.
### label sources : 
- the output of your model could be either an event or an attribute. this results in the following two type of labels : 
1. Direct label for events : such as "did the used click the top search result ? "
2. Direct label for attributes: such as "will the advertiser spend more than &X in the next week? "


### why use human labeled data  ? 
- there are advantages and disadvantages to using human labeled data : 
- + : Human raters can perform a wide range of tasks.
- the data forces you to have a clear problem definition
- - : the data is expensive for cetrain domains 
- Good data typically requires multiple iterations.

## Sampling and splitting the data : 
- it's ofren a struggle to gather enough data for a machine learning project and sometimes you got much data and you must select a subset of examples of training.
- How do you select that subset ? 
- example of google search. At what granularity would you sample its massive amounts of data? would you use random queries ? random sessions ? random users? 
- the answer depends on the problem: what do you want to predict, and what features do you want ? 

### Imbalanced data : 
- a classification dataset with skewed class proportions is called imbalances. Classes that make up a large proportion of the data set are called majority classes. Those who make up the small part are called the minority classes.

- what called as imbalanced ? The answer could range from mild to extreme, as the table below shows : 
![alt text](images/image-7.png)
### why to look out for imbalancecd data ? 
- consider the following example : a model that detect fraud , instances of fraud happen once per 200 transactions in this data set , so in the true distribution about 0.5 percent of the data is positive 
![alt text](images/image-8.png)
- why would this problematic ? 
- with so few positives relative to negatives , the training model will spend most of its time on negative examples and not learn enough from positive ones. 
- if you have imbalanced data set , first try training on the true distribution.If the model works well and generalizes, you're done ! if not try the following techniques : 
### Downsampling and Upweighting : 
- An effective way to handle imbalanced data is to downsample and upweight the majority class. Let's start by defining those two new terms : 
- *Downsampling* : means training on a disproportionately low subset of the majority class examples 
- *Upweighting* means addingg an example weight to the downsampled class equal to the factor by which you downsampled.

### step 1 : downsample the majority class _ 
- consider again our example of fraud dataset with 1 positive to 200 negatives. We can downsample by a factor of 20 , taking 1/10 negatives , now about 10 % of our data is positive , which will be much better for training our model. 
### step 2 : upweight the downsampled class 
- the last step is to add example weights to t he downsampled class . Since we downsampled by a factor of 20, the exampe weight should be 20 
![alt text](images/image-9.png)

### weights : 
- here we're talking about example weights, which means counting an individual example more importantly during training. An example weight of 10 means the model treats the examples as 10 times as important (when computing loss) as it would an example of weight 1. 
- the weight should be equal to the factor you used to downsample : example weight= origin example weight x downsampling factor 
### why downsampling and upweight ? 
- it may seem odd to add example weights after downsampling. We were trying to make our model improve on the minority class -- why would we upweight the majority ? these are the resulting changes : 
1. faster convergence : during training, we see the minority class more often , which will help the model converge faster.
2. Disk space : By consolidating the mojority class into fewer examples with larger weights, we spend less disk space storing them. this saving allows more disk space for the minority class . so we can collect a greater number and a wider range of examples from that class 
3. Calibration:  Upweighting ensures or model is still calibrated , the outputs can stoll be interpreted as probabilites

### Datasplitt examples : 

- after  collecting your data and sampling where needed, the next step is to split your data into training sets, validation sets and testing sets 

### why random splitting isnt the best approach 
- while it is the best approach for many ML problems. it isnt always the right solution
![alt text](images/image-10.png)
![alt text](images/image-11.png)
![alt text](images/image-12.png)

### imbalanced data -- overfitting : 
- if the training data is overly imbalanced, then the model will predict a non meaningful result -> this is called *Overfitting* 
- to prevent overfiting there needs to be a fairly equal distribution of training samples for each classification, or range if label is a real value. 
### overfitting : 
- in data science courses, overfit model is explained as having high variance and low bias on the training set which leads to poor generalization on new testing data. 

### how to limit overfitting 
- Both overfitting and underfitting can lead to poor model performance. But by far the most common problem in applied machine learning is overfitting. 
- overfitting is such a problem because the evaluation of machine learning algorithms on training data is different from the evaluation we actually care the most about, namely how well the algorithm well perform on unseen data.

### how to limit overfitting : 
- there are two important techniques that you can use : 
1. Use a resampling technique to estimate the model accuracy.
2. Hold back a validation test 

### underfitting :
- refers to a model that can neither model the training data or to generalize to new data. 
- an underfit machine learning model is not a suitable model and will be obvius as it will have poor performance on the training data. 

# Basic :
Machine learning must  seem complex but it is really built out of a series of basic building blocks : 
- overfitting : too much reliance on the training data
- underfitting : a failure to learn the relationships in the training data
- High variance : model changes significantly based on the training data
- High bias : assumption about model lead to ignoring training data
- Overfitting and underfitting cause poor generalization on the test set 
- a validation set for model tuning can prevent under and overfitting. 
- ...

# FEATURE ENGINEERING : 
![alt text](images/image-13.png)
![alt text](images/image-14.png)
Feature engineering is the art/science of representing the data the best way possible for a problem, Good feature engineering involves an elegant blend of domain knowledge , intuition and basic mathematical abilities 
![alt text](images/image-15.png)

### what best ? 
---
- the way yoy present your data in essence should denote the pertinent structures/properties of the underlying information in the most effective way possible. When you do feature engineering, you are essentially converting your data attributes into data features.

### Attributes : 
---
- Attributes are basically all the dimensions present in your data. But do all of them , in the raw format , represent the underlying tends you want to learn in the best way possible ? maybe not 

### Features : 
---
- so what you do in feature engineering is pre process your data so that your model algorithm has to spend minimus effort on wading through noise.
- noise is any information that is not relevant to learning/predicting your ultimate goal. 
- In fact using good features can even let you use considerably simpler models.

- as with any technique in machine learning , always use validation to make sure that the new features you introduce really do improve your predictyions, instead of adding unecessary complexity to your pipeline.

### decomposing categorical attributes: 
why ?
- since ML is based on mathematical equations, it would cause a problem when we keep categorical variables as is. 
<br>
*encoding methodologies* :
- Nominal encoding : where order of the data does not matter 
- Ordinal encoding : where the order of the data does matter 

1. One hot encoding. 
2. bel Encoding 
3. Ordinal Encoding 
4. Helmert Encoding 
5. Binary Encoding
6. Frequency Encoding
7. Mean Encoding
8. Weight of Evidence Encoding
9. Probability Ratio Encoding
10. Hashing Encoding
11. Backward Difference Encoding
12. Leave One Out Encoding
13. James-Stein Encoding
14. M-estimator Encoding

## Binning / Bucketing : 
---
- sometimes , it makes more sense to represent a numerical attribute as a categorical one. 
- example : consider a problem where preficting whether a person owns a certain item of clothing or not.
- age might definitely be a factor here. what actually more pertinet is the age group 
- 1-10 , 11-18,19-25,26-40 ...

### binning : 
- binning or grouping data is an important tool in preparing numerical data for machine learning 


- binning also reduces the effect of tiny errors by rounfing off a given value to the nearest representative. 
- Binning does not make sense if the number of your ranges is comparable to the total possible values, or if precision is very important to you. 

### Bucketing
- bucketing makes sense when the domain of your attribute can be divided into neat ranges, where all numbrs falling in a range imply a common characteristic 
- it reduces overfitting in certain applications. 
![alt text](images/image-16.png)

## FEATURE CROSSES
- feature crosses are a unique way to combine two or more categorical attributes into a single one.
- this is extremely useful technique, when certain features together denote a property better than individually by themselves 
     - - mathematically speaking you are doing a cross product between all possible values of the categorical features. 
    ![alt text](images/image-53.png)

- Consider a feature A, with two possible values {A1,A2}.Let B be a feature with possibilities {B1,B2}. then a feature cross between A and B (lets call it AB) would take one of the following values : {(A1, B1), (A1, B2), (A2, B1), (A2, B2)}.

## FEATURE SELECTION
- is the procecss of selecting a subset of relevant features for use in model construction.
- Feature selection is another key part of the applied machine learning process, like model selection.
- It is important to consider feature selection a part of the model selection process. If you do not, you may inadvertently introduce bias into your models which can result in overfitting.
- Feature selection is different from dimensionality reduction.Both methods seek to reduce the number of attributes in tthe dataset, but a dimensionality reduction method do so by creating new combinations of attributes, where as feature selection methods include and exclude attributes present in the data without changing them. 
- feature selection : using certain algorithms to automatically select a subset of your original features, for your final model. 
- here you are not creating/modifying your current features, but rather pruning them to reduce noise/redundancy.

- Feature selection is itself useful but it mostly acts as a filter muting out features thatt arent useful in addition to you existing features. 
- Features selection menthods can be used to identify and remove ineeded, irrelevant and redundant attributes from data that do not contribute to the accuracy of a predictive model or may in fact decrease the accuracy of the model. 

### objective : 
the objective of valiable selection is three-fold : 
1. Improving the prediction performance of the predictors
2. Providing faster and more cost effective predictors 
3. and providing a better understanding of the underlying process that generated the data. 

### Feature selection algorithms : 
there are three general classes of feature selection algos : 
1. filter methods 
2. wrapper methods 
3. and embedded methods 

### Filter feature selection 
- Filter feature selection methods apply a statistical measure to assign a scoring to each feature. 
- the features are ranked by he score and either selected to be kept or removed from the dataset. 
- the methods are often univariate and consider the feature independently or with regard to the dependent variable
- some examples of some filter methods include the Chi squared test , information gain and correlation coefficient scores. 
![alt text](images/image-55.png)
![alt text](images/image-56.png)
### wrapper methods 
- wrapper methods consider the selection of a set of features as a search problem, where different combinations are prepared, evaluated and compared to other combinations.
- a predictive model us used to evaluate a combination of features and assign a score based on model accuracy 
- the search process may be methodical such as a best first search, it may stochastic such as a random hill climbing algorithm or it may use heuristic like forward and backward passes to add and remove features 
- an example of wrapper method is the recursive feature elimination algorithm. 
![alt text](images/image-57.png)

### Embedded methods 
- Embedded methods learn which features best contribute to the accuracy of the model while the model is being created. 
- the most common type of embedded feature selection methods are regularization methods 
- Regularization methods are also called penalization methods that introduce additional constraints into the optimization of a predictive algo (such as a regression algorithm) that bias the model toward lower complexity (fewer coefficients) 
- examples of regularization algos are the LASSO , elastic net and ridge regression 
### Feature selection checklist : 

1. Do you have domain knowledge ? If yes, construct a better set of "ad hoc" features 
2. are you features commensurate ? If no , consider normalizing them. 
3. Do you suspect interdependence of features ? if yes , expand yoyr feature set by constructing conjuctive features or products or features , as much as your computer ressourcecs allow you. 
4. Do you need to prune the input variables (e.g. for cost, speed or data understanding reasons)? if No, construct disjunctive features or weighted sums of feature 
5. Do you need to asses features individually(e.g to understand )
6. Do you need a preditor ? if no , stop 
7. Do you suspect your data is dirty (has a few meaningless input patterns and/or noisy outputs or wrong class labels)? if yes detect the outliers examples using the top ranking variables obtained in step 5 as representation, check and/or discard them. 
8. Do you know what to try first?if no, use a linear predictor. Use a forward selection method with "probe" method as a stopping criterion or use the 0 norm embedded method for comparison, following the ranking of step 5, construct a sequence of predictors of same nature using increasing subsets of features. can you match or improve performance with a smaller subset ? if ues , try a non linear predictor with that subset 
9. Do you have new ideas , time , computational ressourcecs and enough examples ? if yes compare several feature selection methods including your new idea , correlation coefficients, backward selection and embedded methods. Use linear and non linear predictors.Select the best approach with model selection 
10. Do you want a stable solution(to improve performance and/or understanding)? if yes, subsample your data and redo your analysis for several "bootstrap"

### removing features with low variance : 
- variancethreshold is a simple baseline approach to feature selection.It removes all features whose variance doesnt meet some threshold. By default, it removes all zero-variance features, i.e. features that have the same value in all samples. 
- suppose that we have a dataset with boolean features and we want to remove all features that are one or zero (on and off) in more than 80% of the samples. Boolean features are bernoulli random variables, and the variance of such variables is given by : var[X]=p(1-p) 
- so we can select using the threshold .8*(1-.8)

### The recursive feature elimination (RFE) :
---
- The recursive feature elimination (RFE) method is a feature selection approach. It works by recursively removing attributes and building a model on those attributes that remain. It uses the model accuracy to identify which attributes(and combination of attributes) contribute the most to predicting the target attribute.
![alt text](images/image-58.png)

### feature importance : 
--- 
- Methods that use ensembles of decision trees(like random forest or extra trees) can also compute the relative importance of each attribute. These importance values can be used to inform a feature selection process. 
![alt text](images/image-59.png)

![alt text](images/image-60.png)
### Feature scaling : 
---
- Feature scaling is a method used to standardize the range of independent variables or features of data. In data processing, it is also known as data normalization and is generally performed during the data preprocessing step. 
### Feature scaling -- Standardization : 
- the result of standardization(or z-score normalization) is that the features will be rescaled so that theyll have properties of a standard normal distribution with :![alt text](images/image-61.png)
- where u is the mean(average) and σ is the standard deviation from the mean; standard scores(also called z scores) of the samples are calculated as follows : ![alt text](images/image-62.png)
- standardizating the features so that they are centered around 0 with a standard deviation of 1 is not only important if we are comparing measurements that have different units, but it is also a general requirement for many machine learning algorithms
- with features being on different scales, certain weights may update faster than others since the feature values xj play a role in the weight updates ![alt text](images/image-63.png)
![alt text](images/image-64.png)
- some examples of algos where feature scaling matters are : 
1. K-nearestt neighbors with an euclidean distance measure if want all features to contribute equally 
2. k means (see k nearest neighbors)
3. logistic regression , SVM, perceptrons, neural networks etc. if you are using gradient descent/ascent-based optimization, otherwise some weights will update much faster than others. 
4. linear discriminant analysis, principal component analysis, kernel proncipal component analysis since you wantt to find directions of maximizing the variance 

 ### feature scaling - min max scaling : 

 - in this approach, the data is scaled to a fixed range - usually between 0 and 1. 
 - -> the cost of having this bounded range - in contrast to standardization - is that we will end up with smaller standard deviations, which can suppress the effect of outliers.
 - A min max scaling is tyically done via the following equation :![alt text](images/image-65.png)
- Example : <br>
for example suppose that we have the student's weight data and the student's weight span [160 pounds - 200 pounds]. To rescale thisdata, we first substract 160 from each student's weight and divide the result by 40 (the difference between the maximum and minimum weights)
### mean normalization : 
![alt text](images/image-66.png)
### standardization or min max scalingg ? 
--- 
- there is no obvious answer to this question : it really depends on the application. 
- -> in the clustering analyses, standardization may be especially crucial in order to compare similarities between features based on certain distance measures 
- -> a typical neural network algorithm require data that on a 0-1 scale

## feature extraction : 
![alt text](images/image-67.png)
### what it is ? 
---
- feature extraction is a process of dimensionality reduction by which an initial set of raw data is reduced to more manageable groups for processing 
- A characteristic of these large data sets is a large number of variables that require a lot of computing resosurces to process 
- -> feature extraction is the name for methods that combine variables into features, effectively reducing the amount of data that must be processed while still accurately and completely describing the original data set 

### what are ? 
- dimension reduction refers to the process of converting a set of data having vast dimensions into data with lesser dimensions ensuringg that if conveys similar information concisely 
- these techniques are typically used while solving machine learning problems to obtain better features for a classification or regression task 
- with more variables , comes more trouble ! and to avoid this trouble, dimension reduction techniques comes to the rescue 
![alt text](images/image-68.png)
### why is this useful ? 
--- 
- the process of feature extraction is useful when you need to reduce the number of ressources needed for processing without losing important or relevant information. 
- feature extraction can also reduce the amount of redundant data for a given analysis. Also, the reduction of the data and the machine's efforts in building variable combinations (features) faciliate the following learning and generalization steps in the machine learning process. 
### general dimensionality reduction techniques : 
--- 
![alt text](images/image-69.png)
### missing data : 
--- 
- missing data in the training data set can reduce the power / fit of a model or can lead to a biased model because we have not analysed the behavior and relationship with other variables correctly. It can lead to wrong prediction or classification. 
### the common methods to perform dimension reduction ? 
1. Missing values : while exploring the data, if we encounter missing values, what we do ? our first step should be to identify the reason then impute missingg values / drop variables using appropriate methods. 
2. but what if we have too many missing values ? should we impute missing values or drop the variables. 
### high correlation : 
- high correlation : Dimensions exhibiting higher correlation can lower down the performance of mode. Morevover, it is not good to have multiple variables of similar information or variation also known as multicollinearity 
- -> You can use Pearson(continuous variables) or polychoric(discrete variables) correlation matrix to identify the variables with high correlation and select one of them using VIF (Variabce inflation factor). variables having higher value(VIF>5) can be dropped. 
### backward feature elimination : 
- backward feature elimination : in this method, we  start with all n dimensions. Compute the sum of square of error (SSR) after eliminating each variable (n times). Then, identifying variables whose removal has produced the smallest increase the SSR and removing it finally, leaving us with n-1 input features. 
- Repeat this process until no other variables can be dropped. 

### Forward feature selection : 
- reverse to this, we can use forward feature selection method, we select one variable and analyse the performance of model by adding another variable. Here, selection of variable is based on higher improvement in model performance. 

## Factor analysis : 
- Let's say some variables are highly correlated.These variables can be grouped by their correlations i.e. all variables in a particular group can be highly correlated among themselves but low correlation with variables or groups 



# Machine learning algorithms : 
![alt text](images/image-17.png)

## LINEAR REGRESSION : 
- it is used to estimate real values (target variable) based on continuous variable(s).
- Linear Regression is used for finding learning relationship between target and one or more predictors. 
- The core idea is to obtain a line that best fit the data. 
- the best fit line is the one for which total prediction error are as small as possible, error is the distance between the real value and the predicted one. 
- Establish relationship between independent and dependent variables by fitting a best line. This best fit line is known as regression line and represented by a linear equation Y=a*X+b.
![alt text](images/image-18.png)
### Types of linear regression : 
--- 
- simple linear regression 
- multiple linear regression 

### 1 - simple linear regression 
---
- single dimension linear regression has one prediction and one target as input for the training simple. 
- it uses these training sample to derive a line that predict values of y. 
- the training sample are used to derive the values of a and b that minimise the error between actual and predicted values of y.
- a is the slope and b is the y-intercept. 
- dataset -> algo ML -> Function h(x)
- this function will receive later x and give y.
- as been mentionned before we want a line that minimises the error between the Y values in the trainingg samples and the h(x) values that the line passes through. 
- so we define the error function for our algorithm so we can minimise that error. 
### cost function : 
- the cost function helps us figure out the best possible values for a and b which would provide the best fit line for the data points- 
- since we want the best values for a and b , we convert this search problem into a minimization problem where we would like to minimize the error between the predicted value and the actual value. 
![alt text](images/image-19.png)

### minimize the error : 
--- 
- the values a and b must be chosen so that they minimize the error. If sum of squared error is taken as a metric to evaluate the model, then the goal to obtain a line that best reduces the error. 
- Mean absolute error is the mean of the absolute value of errors 
- Mean square error is the mean of the squared error  
- Mean Absolute Percentage Error  
- Mean percentage Error
- Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors.

![alt text](images/image-20.png)

![alt text](images/image-21.png)

### how ?
---
- to determine how to best fit our model with given set of points, we want to minimize the distance between each of these point to our linear model.
- calculating the totalError helps us determine how bad our model is so we can update it every step
- but ... 
### Minimizing the cost function : Gradient Descent 
- Repeat until convergence:
![alt text](images/image-22.png)
- partial derivative
- the derivative of a function of a real variable measures the sensitivity to change of the function value(output value) with respect to a change in its argument(input value)
![alt text](images/image-23.png)
- *slope*
![alt text](images/image-24.png)
- Learning rate : 
![alt text](images/image-25.png)
![alt text](images/image-26.png)
![alt text](images/image-27.png)

## Multi dimension linear regression : 

- Each training sample has an x made up of multiple input values and a corresponding y with a singe value 
- the inputs can be presented as an X matric in which row is sample and each column is a dimension. 
- the outputs can b e represented as y matrix in which each row is a sample 
![alt text](images/image-28.png)
### basic layout : 
- our predicted y value are calculated by multiplying the X matrix by a matrix of param , ϴ. 
- if there are 2 dimension, then this equation defines plane, if there are mode dimension then it define hyperplane. ![alt text](images/image-29.png)

## Logistic Regression : 
![alt text](images/image-30.png)
- in a lot of ways, linear regression and logistic regression are similar. But the biggest difference lies in what they are used for. 
- Linear Regression algorithms are used to predict/forecast values but logistic regression is used for classification tasks
- it is a classification not a regression algorithm 
- it is used to estimate discrete values(binary values like 0 or 1 , yes or no , true or false) based on a given set of independent variable(s)
![alt text](images/image-31.png)
### LIR VS LOR : 
![alt text](images/image-32.png)

- Logistic regression is used when the dependent variable is categorical. 
- to predict whether an email is spam of no , tumor is malignant or not , whether website is fraudulent or not ... 
- LOR : also uses a linear equation with independent predictors to predicte a value. The predicted value can be anywhere between negative infinity and positive infinity
- we need the output of the algorithm to be class variable : 0 no , 1 yes 
- Therefore, we are squashing the output of the linear equation into a range of 0 and 1. to squash that output we use : THE SIGMOID FUNCTION. 
![alt text](images/image-33.png)
### Sigmoid activation function  : 
![alt text](images/image-34.png)
![alt text](images/image-35.png)
### mathematically this can be written as : [alt text](images/image-36.png)

### type pf logistic regression : 

1. Binary logistic regression : there is only two possible output 
2. Multinomial logistic regression : three or more categories without orderingg 
3. Ordinal logistic regression : three or more categories with ordering: example movie rating from 1 to 5 

### cost function 
- since we want to predict class values , we cannot use the same cost function as in linear regression algorithm. Therefore, we use a logarithmic loss function to calculate the cost fo missclassifying. 

![alt text](images/image-37.png)
![alt text](images/image-38.png)

## KNN 

- the principe of this algorithm is very simple : 
- we gave it : training set , distance function d and a number k 
- for each testing point x , we search on D the k nearest points to x using the distance d and we predict that the class of x is the majority class of the k neighbors
- the goal of this algo is to predict the class of unlabled data 
![alt text](images/image-39.png)
![alt text](images/image-40.png)

## Decision tree 
- arbres permettant de classer des enregistrements par division hierarchiques en sous classes. 
- un noeud represente une classe de plus en plus fine depuis la racine. 
- un arc represente un predicat de partitionnement de la classe source 
- un attribut sert d'etiquette de classe(attribut cible a predire), les autres permettant de partitionner

- Objectif : obtenir des classes homogenes , couvrir au mieux les donnees- 
- comment choisir les attributs(Ai)?
- commentt isoler les valeurs discriminantes(vj)?
### arbres = ensemble de regles 
![alt text](images/image-50.png)
![alt text](images/image-51.png)
![alt text](images/image-52.png)
### procedure de construction 
- recherche a chaque niveau de l'attribut le plus discriminant 
- partition (noeud P) 
- si tous