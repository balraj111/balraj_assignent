from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import  os

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    string=''
    items = []
    if request.method == 'POST':
        string = request.form['string']

        absolute_path = os.path.abspath(os.path.dirname('data.csv'))
        print(absolute_path)
        path=absolute_path+'/data.csv'
        df=pd.read_csv(path)
        df=pd.DataFrame(df)
        df=(df.loc[df["givenName"].str.startswith(string)==True])
        s = df.givenName.str.len().sort_values().index
        df1 = df.reindex(s)
        df1 = df1.reset_index(drop=True)
        for row in df1.itertuples():
            item=dict(name=row[1],mname=row[2],sname=row[3])
            items.append(item)

    return render_template('search2.html',items=items,string=string)


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)