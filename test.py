import pandas as pd,matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
raw = pd.read_csv('data/train.csv')
test=pd.read_csv('data/test.csv')
features = ['Pclass', 'Sex', 'Age', 'SibSp',
       'Parch',  'Fare', 'Embarked']
x=raw[features]
x_test=test[features]

y=raw['Survived']
x['Sex']=x['Sex'].map({'male':0,'female':1})
x['Embarked']=x['Embarked'].map({'S':0,'C':1,'Q':2})
x_test['Sex']=x_test['Sex'].map({'male':0,'female':1})
x_test['Embarked']=x_test['Embarked'].map({'S':0,'C':1,'Q':2})
x['Age']=x['Age'].fillna(x['Age'].mean())
x_test['Age']=x_test['Age'].fillna(x_test['Age'].mean())
x['Fare']=x['Fare'].fillna(x['Fare'].mean())
x_test['Fare']=x_test['Fare'].fillna(x_test['Fare'].mean())
model=RandomForestClassifier(n_estimators=100)
model.fit(x,y)
predictions=model.predict(x_test)
output = pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)