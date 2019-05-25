What Is My Purpose?

A. To find out the best university in all important standards.


How Did I Do This?

A. I have gathered the University data of the various states with respect to SAT,Top10,Accept, SFRatio,Expenses,GradRate. After converting the the data to pandas dataframe. As it is clear that I need to predict the best university, I have made the univeristy as target variable or Y and made all the components such as SAT,Top10,Accept, SFRatio,Expenses,GradRate as inputs. But i have notived taht anot all the inputs are really influential on the output , so i want to reduce the dimentions. so , I have performed PCA(Principal component analysis) which is a dimension reduction algorithm, which gives weightage to important ones. then I have checked the basic EDA process and whether the data is following Normal distribution or not, which is the basic thing to check, to make sure there is no multi collinearity problem. Aftre making sure, I splitted the data into train and test. I have tried to input the data into the linear model and cameout with a prediciton.


