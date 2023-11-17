import numpy as np
import pandas as pd
from sklearn import tree

input_file = "PastHires.csv"
df = pd.read_csv(input_file,header= 0)

print(df.head())

#scikit-learn nedds everything to be numerical for decison trees to work, so we need to map
#our data to numerical form using the map function
d = {'Y' : 1, 'N' : 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {"BS" : 0, 'MS' : 1, "PhD" : 2 }
df['Level of Education'] = df['Level of Education'].map(d)
print(df.head())

#Seperate features from the target column that we are building a tree for 
features = list(df.columns[:6])
print(features)

#Construct the decision tree 
y = df["Hired"]
x = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#pip install pydotplus
#pip insatll graphviz
#Possibly add path of graphviz\bin directory to Windows PATH vaiable
from IPython.display import Image
from six import StringIO
import pydotplus

#The export_graphviz fuction converts the decision tree calssifier into a dot file, and
#pydotplus convets this dot file to png or displayable form on Jupyter

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=features)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
graph.write_png('job.png')


























