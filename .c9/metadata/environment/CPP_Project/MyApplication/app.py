{"filter":false,"title":"app.py","tooltip":"/CPP_Project/MyApplication/app.py","undoManager":{"mark":90,"position":90,"stack":[[{"start":{"row":0,"column":9},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":13},"action":"insert","lines":["import key_config as keys","import boto3 "],"id":2}],[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":16,"column":26},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["d"],"id":10},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["y"]},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["a"],"id":11},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["m"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["o"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["b"],"id":12}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":[" "],"id":13},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":[" "],"id":14},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["b"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["o"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["t"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":15},"action":"remove","lines":["boto"],"id":15},{"start":{"row":19,"column":11},"end":{"row":19,"column":16},"action":"insert","lines":["boto3"]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["."],"id":16},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["r"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["e"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["o"],"id":17},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["u"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["r"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["c"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":27},"action":"insert","lines":["()"],"id":18}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":28},"action":"insert","lines":["''"],"id":19}],[{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["d"],"id":20},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":27},"end":{"row":19,"column":29},"action":"remove","lines":["dy"],"id":21},{"start":{"row":19,"column":27},"end":{"row":19,"column":35},"action":"insert","lines":["dynamodb"]}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":22}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":47},"action":"insert","lines":["","from boto3.dynamodb.conditions import Key, Attr"],"id":23}],[{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":57,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["",""]},{"start":{"row":58,"column":0},"end":{"row":59,"column":0},"action":"insert","lines":["",""]},{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""]},{"start":{"row":60,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":53,"column":0},"end":{"row":108,"column":23},"action":"insert","lines":["","@app.route('/signup', methods=['post'])","def signup():","    if request.method == 'POST':","        name = request.form['name']","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        ","        table.put_item(","                Item={","        'name': name,","        'email': email,","        'password': password","            }","        )","        msg = \"Registration Complete. Please Login to your account !\"","    ","        return render_template('login.html',msg = msg)","    return render_template('index.html')","","@app.route('/login')","def login():    ","    return render_template('login.html')","","","@app.route('/check',methods = ['post'])","def check():","    if request.method=='POST':","        ","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        response = table.query(","                KeyConditionExpression=Key('email').eq(email)","        )","        items = response['Items']","        name = items[0]['name']","        print(items[0]['password'])","        if password == items[0]['password']:","            ","            return render_template(\"home.html\",name = name)","    return render_template(\"login.html\")","@app.route('/home')","def home():","    return render_template('home.html')","","","","","","if __name__ == \"__main__\":","    ","    app.run(debug=True)"],"id":26}],[{"start":{"row":105,"column":0},"end":{"row":108,"column":23},"action":"remove","lines":["","if __name__ == \"__main__\":","    ","    app.run(debug=True)"],"id":27},{"start":{"row":104,"column":0},"end":{"row":105,"column":0},"action":"remove","lines":["",""]},{"start":{"row":103,"column":0},"end":{"row":104,"column":0},"action":"remove","lines":["",""]},{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"remove","lines":["",""]},{"start":{"row":101,"column":0},"end":{"row":102,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["#"],"id":47}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["n"],"id":48},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["i"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["a"]},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["m"]}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["i"],"id":49},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["m"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["d"]},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["e"],"id":50},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["d"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["m"]}],[{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["n"],"id":51},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["d"]},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["e"]},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["x"]}],[{"start":{"row":26,"column":40},"end":{"row":26,"column":41},"action":"insert","lines":[" "],"id":52},{"start":{"row":26,"column":41},"end":{"row":26,"column":42},"action":"insert","lines":["#"]},{"start":{"row":26,"column":42},"end":{"row":26,"column":43},"action":"insert","lines":["t"]},{"start":{"row":26,"column":43},"end":{"row":26,"column":44},"action":"insert","lines":["h"]},{"start":{"row":26,"column":44},"end":{"row":26,"column":45},"action":"insert","lines":["i"]},{"start":{"row":26,"column":45},"end":{"row":26,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":46},"end":{"row":26,"column":47},"action":"insert","lines":[" "],"id":53},{"start":{"row":26,"column":47},"end":{"row":26,"column":48},"action":"insert","lines":["i"]},{"start":{"row":26,"column":48},"end":{"row":26,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":49},"end":{"row":26,"column":50},"action":"insert","lines":[" "],"id":54},{"start":{"row":26,"column":50},"end":{"row":26,"column":51},"action":"insert","lines":["y"]},{"start":{"row":26,"column":51},"end":{"row":26,"column":52},"action":"insert","lines":["o"]},{"start":{"row":26,"column":52},"end":{"row":26,"column":53},"action":"insert","lines":["u"]},{"start":{"row":26,"column":53},"end":{"row":26,"column":54},"action":"insert","lines":["r"]}],[{"start":{"row":26,"column":54},"end":{"row":26,"column":55},"action":"insert","lines":[" "],"id":55},{"start":{"row":26,"column":55},"end":{"row":26,"column":56},"action":"insert","lines":["l"]},{"start":{"row":26,"column":56},"end":{"row":26,"column":57},"action":"insert","lines":["a"]},{"start":{"row":26,"column":57},"end":{"row":26,"column":58},"action":"insert","lines":["n"]},{"start":{"row":26,"column":58},"end":{"row":26,"column":59},"action":"insert","lines":["d"]},{"start":{"row":26,"column":59},"end":{"row":26,"column":60},"action":"insert","lines":["i"]},{"start":{"row":26,"column":60},"end":{"row":26,"column":61},"action":"insert","lines":["n"]},{"start":{"row":26,"column":61},"end":{"row":26,"column":62},"action":"insert","lines":["g"]}],[{"start":{"row":26,"column":62},"end":{"row":26,"column":63},"action":"insert","lines":[" "],"id":56},{"start":{"row":26,"column":63},"end":{"row":26,"column":64},"action":"insert","lines":["p"]},{"start":{"row":26,"column":64},"end":{"row":26,"column":65},"action":"insert","lines":["a"]},{"start":{"row":26,"column":65},"end":{"row":26,"column":66},"action":"insert","lines":["g"]},{"start":{"row":26,"column":66},"end":{"row":26,"column":67},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"remove","lines":[" "],"id":58}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"insert","lines":[":"],"id":59}],[{"start":{"row":26,"column":68},"end":{"row":26,"column":69},"action":"insert","lines":[" "],"id":60},{"start":{"row":26,"column":69},"end":{"row":26,"column":70},"action":"insert","lines":["L"]},{"start":{"row":26,"column":70},"end":{"row":26,"column":71},"action":"insert","lines":["o"]},{"start":{"row":26,"column":71},"end":{"row":26,"column":72},"action":"insert","lines":["g"]},{"start":{"row":26,"column":72},"end":{"row":26,"column":73},"action":"insert","lines":["i"]},{"start":{"row":26,"column":73},"end":{"row":26,"column":74},"action":"insert","lines":["n"]}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"remove","lines":[":"],"id":61}],[{"start":{"row":26,"column":67},"end":{"row":26,"column":68},"action":"insert","lines":[" "],"id":62},{"start":{"row":26,"column":68},"end":{"row":26,"column":69},"action":"insert","lines":["t"]},{"start":{"row":26,"column":69},"end":{"row":26,"column":70},"action":"insert","lines":["o"]}],[{"start":{"row":26,"column":72},"end":{"row":26,"column":76},"action":"remove","lines":["ogin"],"id":63},{"start":{"row":26,"column":71},"end":{"row":26,"column":72},"action":"remove","lines":["L"]}],[{"start":{"row":26,"column":71},"end":{"row":26,"column":72},"action":"insert","lines":["S"],"id":64},{"start":{"row":26,"column":72},"end":{"row":26,"column":73},"action":"insert","lines":["i"]},{"start":{"row":26,"column":73},"end":{"row":26,"column":74},"action":"insert","lines":["g"]},{"start":{"row":26,"column":74},"end":{"row":26,"column":75},"action":"insert","lines":["n"]}],[{"start":{"row":26,"column":75},"end":{"row":26,"column":76},"action":"insert","lines":[" "],"id":65},{"start":{"row":26,"column":76},"end":{"row":26,"column":77},"action":"insert","lines":["u"]},{"start":{"row":26,"column":77},"end":{"row":26,"column":78},"action":"insert","lines":["p"]}],[{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"remove","lines":["x"],"id":66},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["e"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["d"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["n"]},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["i"]}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["l"],"id":67},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["o"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["g"]},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["i"]},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"remove","lines":["n"],"id":68},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["i"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["g"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["o"]},{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["l"]}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["i"],"id":69},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["n"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["d"]},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["e"]},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["x"]}],[{"start":{"row":54,"column":0},"end":{"row":73,"column":40},"action":"remove","lines":["@app.route('/signup', methods=['post'])","def signup():","    if request.method == 'POST':","        name = request.form['name']","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        ","        table.put_item(","                Item={","        'name': name,","        'email': email,","        'password': password","            }","        )","        msg = \"Registration Complete. Please Login to your account !\"","    ","        return render_template('login.html',msg = msg)","    return render_template('index.html')"],"id":70}],[{"start":{"row":29,"column":0},"end":{"row":48,"column":40},"action":"insert","lines":["@app.route('/signup', methods=['post'])","def signup():","    if request.method == 'POST':","        name = request.form['name']","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        ","        table.put_item(","                Item={","        'name': name,","        'email': email,","        'password': password","            }","        )","        msg = \"Registration Complete. Please Login to your account !\"","    ","        return render_template('login.html',msg = msg)","    return render_template('index.html')"],"id":71}],[{"start":{"row":48,"column":40},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":74,"column":0},"end":{"row":102,"column":0},"action":"remove","lines":["","","@app.route('/login')","def login():    ","    return render_template('login.html')","","","@app.route('/check',methods = ['post'])","def check():","    if request.method=='POST':","        ","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        response = table.query(","                KeyConditionExpression=Key('email').eq(email)","        )","        items = response['Items']","        name = items[0]['name']","        print(items[0]['password'])","        if password == items[0]['password']:","            ","            return render_template(\"home.html\",name = name)","    return render_template(\"login.html\")","@app.route('/home')","def home():","    return render_template('home.html')",""],"id":73}],[{"start":{"row":73,"column":0},"end":{"row":74,"column":0},"action":"remove","lines":["",""],"id":74}],[{"start":{"row":48,"column":40},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":75},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":4},"end":{"row":50,"column":0},"action":"insert","lines":["",""]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":50,"column":4},"end":{"row":78,"column":0},"action":"insert","lines":["","","@app.route('/login')","def login():    ","    return render_template('login.html')","","","@app.route('/check',methods = ['post'])","def check():","    if request.method=='POST':","        ","        email = request.form['email']","        password = request.form['password']","        ","        table = dynamodb.Table('users')","        response = table.query(","                KeyConditionExpression=Key('email').eq(email)","        )","        items = response['Items']","        name = items[0]['name']","        print(items[0]['password'])","        if password == items[0]['password']:","            ","            return render_template(\"home.html\",name = name)","    return render_template(\"login.html\")","@app.route('/home')","def home():","    return render_template('home.html')",""],"id":76}],[{"start":{"row":73,"column":39},"end":{"row":73,"column":40},"action":"remove","lines":["e"],"id":77},{"start":{"row":73,"column":38},"end":{"row":73,"column":39},"action":"remove","lines":["m"]},{"start":{"row":73,"column":37},"end":{"row":73,"column":38},"action":"remove","lines":["o"]},{"start":{"row":73,"column":36},"end":{"row":73,"column":37},"action":"remove","lines":["h"]}],[{"start":{"row":73,"column":36},"end":{"row":73,"column":37},"action":"insert","lines":["m"],"id":78},{"start":{"row":73,"column":37},"end":{"row":73,"column":38},"action":"insert","lines":["a"]},{"start":{"row":73,"column":38},"end":{"row":73,"column":39},"action":"insert","lines":["i"]},{"start":{"row":73,"column":39},"end":{"row":73,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":75,"column":0},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":79}],[{"start":{"row":57,"column":17},"end":{"row":57,"column":18},"action":"remove","lines":["k"],"id":80},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"remove","lines":["c"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"remove","lines":["e"]},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"remove","lines":["h"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["m"],"id":81},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"insert","lines":["a"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"insert","lines":["i"]},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":58,"column":8},"end":{"row":58,"column":9},"action":"remove","lines":["k"],"id":82},{"start":{"row":58,"column":7},"end":{"row":58,"column":8},"action":"remove","lines":["c"]},{"start":{"row":58,"column":6},"end":{"row":58,"column":7},"action":"remove","lines":["e"]},{"start":{"row":58,"column":5},"end":{"row":58,"column":6},"action":"remove","lines":["h"]},{"start":{"row":58,"column":4},"end":{"row":58,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":58,"column":4},"end":{"row":58,"column":5},"action":"insert","lines":["m"],"id":83},{"start":{"row":58,"column":5},"end":{"row":58,"column":6},"action":"insert","lines":["a"]},{"start":{"row":58,"column":6},"end":{"row":58,"column":7},"action":"insert","lines":["i"]},{"start":{"row":58,"column":7},"end":{"row":58,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"remove","lines":["n"],"id":84},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"remove","lines":["i"]},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"remove","lines":["a"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"remove","lines":["m"]}],[{"start":{"row":57,"column":13},"end":{"row":57,"column":14},"action":"insert","lines":["c"],"id":85},{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"insert","lines":["h"]},{"start":{"row":57,"column":15},"end":{"row":57,"column":16},"action":"insert","lines":["e"]},{"start":{"row":57,"column":16},"end":{"row":57,"column":17},"action":"insert","lines":["c"]},{"start":{"row":57,"column":17},"end":{"row":57,"column":18},"action":"insert","lines":["k"]}],[{"start":{"row":57,"column":39},"end":{"row":57,"column":40},"action":"insert","lines":[" "],"id":86},{"start":{"row":57,"column":40},"end":{"row":57,"column":41},"action":"insert","lines":["#"]},{"start":{"row":57,"column":41},"end":{"row":57,"column":42},"action":"insert","lines":["T"]},{"start":{"row":57,"column":42},"end":{"row":57,"column":43},"action":"insert","lines":["h"]},{"start":{"row":57,"column":43},"end":{"row":57,"column":44},"action":"insert","lines":["i"]},{"start":{"row":57,"column":44},"end":{"row":57,"column":45},"action":"insert","lines":["s"]}],[{"start":{"row":57,"column":45},"end":{"row":57,"column":46},"action":"insert","lines":[" "],"id":87},{"start":{"row":57,"column":46},"end":{"row":57,"column":47},"action":"insert","lines":["i"]},{"start":{"row":57,"column":47},"end":{"row":57,"column":48},"action":"insert","lines":["s"]}],[{"start":{"row":57,"column":48},"end":{"row":57,"column":49},"action":"insert","lines":[" "],"id":88},{"start":{"row":57,"column":49},"end":{"row":57,"column":50},"action":"insert","lines":["m"]},{"start":{"row":57,"column":50},"end":{"row":57,"column":51},"action":"insert","lines":["y"]}],[{"start":{"row":57,"column":51},"end":{"row":57,"column":52},"action":"insert","lines":[" "],"id":89},{"start":{"row":57,"column":52},"end":{"row":57,"column":53},"action":"insert","lines":["m"]},{"start":{"row":57,"column":53},"end":{"row":57,"column":54},"action":"insert","lines":["a"]},{"start":{"row":57,"column":54},"end":{"row":57,"column":55},"action":"insert","lines":["i"]},{"start":{"row":57,"column":55},"end":{"row":57,"column":56},"action":"insert","lines":["n"]}],[{"start":{"row":57,"column":56},"end":{"row":57,"column":57},"action":"insert","lines":[" "],"id":90},{"start":{"row":57,"column":57},"end":{"row":57,"column":58},"action":"insert","lines":["p"]},{"start":{"row":57,"column":58},"end":{"row":57,"column":59},"action":"insert","lines":["a"]},{"start":{"row":57,"column":59},"end":{"row":57,"column":60},"action":"insert","lines":["g"]},{"start":{"row":57,"column":60},"end":{"row":57,"column":61},"action":"insert","lines":["e"]}],[{"start":{"row":57,"column":61},"end":{"row":57,"column":62},"action":"insert","lines":[" "],"id":91},{"start":{"row":57,"column":62},"end":{"row":57,"column":63},"action":"insert","lines":["b"]},{"start":{"row":57,"column":63},"end":{"row":57,"column":64},"action":"insert","lines":["u"]},{"start":{"row":57,"column":64},"end":{"row":57,"column":65},"action":"insert","lines":["t"]}],[{"start":{"row":57,"column":65},"end":{"row":57,"column":66},"action":"insert","lines":[" "],"id":92},{"start":{"row":57,"column":66},"end":{"row":57,"column":67},"action":"insert","lines":["w"]},{"start":{"row":57,"column":67},"end":{"row":57,"column":68},"action":"insert","lines":["h"]},{"start":{"row":57,"column":68},"end":{"row":57,"column":69},"action":"insert","lines":["e"]},{"start":{"row":57,"column":69},"end":{"row":57,"column":70},"action":"insert","lines":["n"]}],[{"start":{"row":57,"column":70},"end":{"row":57,"column":71},"action":"insert","lines":[" "],"id":93},{"start":{"row":57,"column":71},"end":{"row":57,"column":72},"action":"insert","lines":["I"]}],[{"start":{"row":57,"column":72},"end":{"row":57,"column":73},"action":"insert","lines":[" "],"id":94},{"start":{"row":57,"column":73},"end":{"row":57,"column":74},"action":"insert","lines":["c"]},{"start":{"row":57,"column":74},"end":{"row":57,"column":75},"action":"insert","lines":["h"]},{"start":{"row":57,"column":75},"end":{"row":57,"column":76},"action":"insert","lines":["e"]},{"start":{"row":57,"column":76},"end":{"row":57,"column":77},"action":"insert","lines":["c"]},{"start":{"row":57,"column":77},"end":{"row":57,"column":78},"action":"insert","lines":["k"]}],[{"start":{"row":57,"column":78},"end":{"row":57,"column":79},"action":"insert","lines":[" "],"id":95},{"start":{"row":57,"column":79},"end":{"row":57,"column":80},"action":"insert","lines":["t"]},{"start":{"row":57,"column":80},"end":{"row":57,"column":81},"action":"insert","lines":["o"]}],[{"start":{"row":57,"column":81},"end":{"row":57,"column":82},"action":"insert","lines":[" "],"id":96},{"start":{"row":57,"column":82},"end":{"row":57,"column":83},"action":"insert","lines":["t"]},{"start":{"row":57,"column":83},"end":{"row":57,"column":84},"action":"insert","lines":["o"]}],[{"start":{"row":57,"column":84},"end":{"row":57,"column":85},"action":"insert","lines":[" "],"id":97},{"start":{"row":57,"column":85},"end":{"row":57,"column":86},"action":"insert","lines":["/"]},{"start":{"row":57,"column":86},"end":{"row":57,"column":87},"action":"insert","lines":["m"]},{"start":{"row":57,"column":87},"end":{"row":57,"column":88},"action":"insert","lines":["a"]},{"start":{"row":57,"column":88},"end":{"row":57,"column":89},"action":"insert","lines":["i"]},{"start":{"row":57,"column":89},"end":{"row":57,"column":90},"action":"insert","lines":["n"]}],[{"start":{"row":57,"column":90},"end":{"row":57,"column":91},"action":"insert","lines":[" "],"id":98}],[{"start":{"row":57,"column":90},"end":{"row":57,"column":91},"action":"remove","lines":[" "],"id":99}],[{"start":{"row":57,"column":90},"end":{"row":57,"column":91},"action":"insert","lines":[","],"id":100}],[{"start":{"row":57,"column":91},"end":{"row":57,"column":92},"action":"insert","lines":[" "],"id":101},{"start":{"row":57,"column":92},"end":{"row":57,"column":93},"action":"insert","lines":["I"]}],[{"start":{"row":57,"column":93},"end":{"row":57,"column":94},"action":"insert","lines":[" "],"id":102},{"start":{"row":57,"column":94},"end":{"row":57,"column":95},"action":"insert","lines":["g"]},{"start":{"row":57,"column":95},"end":{"row":57,"column":96},"action":"insert","lines":["e"]},{"start":{"row":57,"column":96},"end":{"row":57,"column":97},"action":"insert","lines":["t"]}],[{"start":{"row":57,"column":97},"end":{"row":57,"column":98},"action":"insert","lines":[" "],"id":103},{"start":{"row":57,"column":98},"end":{"row":57,"column":99},"action":"insert","lines":["a"]},{"start":{"row":57,"column":99},"end":{"row":57,"column":100},"action":"insert","lines":["n"]}],[{"start":{"row":57,"column":100},"end":{"row":57,"column":101},"action":"insert","lines":[" "],"id":104},{"start":{"row":57,"column":101},"end":{"row":57,"column":102},"action":"insert","lines":["e"]},{"start":{"row":57,"column":102},"end":{"row":57,"column":103},"action":"insert","lines":["r"]},{"start":{"row":57,"column":103},"end":{"row":57,"column":104},"action":"insert","lines":["r"]},{"start":{"row":57,"column":104},"end":{"row":57,"column":105},"action":"insert","lines":["o"]},{"start":{"row":57,"column":105},"end":{"row":57,"column":106},"action":"insert","lines":["r"]}],[{"start":{"row":57,"column":106},"end":{"row":57,"column":107},"action":"insert","lines":[" "],"id":105},{"start":{"row":57,"column":107},"end":{"row":57,"column":108},"action":"insert","lines":["n"]},{"start":{"row":57,"column":108},"end":{"row":57,"column":109},"action":"insert","lines":["m"]},{"start":{"row":57,"column":109},"end":{"row":57,"column":110},"action":"insert","lines":["o"]},{"start":{"row":57,"column":110},"end":{"row":57,"column":111},"action":"insert","lines":["t"]}],[{"start":{"row":57,"column":110},"end":{"row":57,"column":111},"action":"remove","lines":["t"],"id":106},{"start":{"row":57,"column":109},"end":{"row":57,"column":110},"action":"remove","lines":["o"]},{"start":{"row":57,"column":108},"end":{"row":57,"column":109},"action":"remove","lines":["m"]}],[{"start":{"row":57,"column":108},"end":{"row":57,"column":109},"action":"insert","lines":["o"],"id":107},{"start":{"row":57,"column":109},"end":{"row":57,"column":110},"action":"insert","lines":["t"]}],[{"start":{"row":76,"column":0},"end":{"row":76,"column":1},"action":"insert","lines":["#"],"id":113}],[{"start":{"row":77,"column":0},"end":{"row":77,"column":1},"action":"insert","lines":["#"],"id":114}],[{"start":{"row":78,"column":1},"end":{"row":78,"column":2},"action":"insert","lines":["#"],"id":115}]]},"ace":{"folds":[],"scrolltop":152.5,"scrollleft":0,"selection":{"start":{"row":26,"column":28},"end":{"row":26,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1607635484150,"hash":"bc4120cbdf02bc3eecdc0ff7e27ecfe30e0aaab7"}