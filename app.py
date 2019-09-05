from flask import Flask, render_template, url_for, request
import random
import json
import time



app = Flask(__name__)

def readhum():
    i = 0
    arr4 = []
    while i < 10:
        hum = random.randint(50, 80)
        i += 1
        arr4.append(hum)
    return arr4
def readtmp():
    i = 0
    arr5 = []
    while i < 10:
        tmp = random.randint(20, 30)
        i += 1
        arr5.append(tmp)
    return arr5

@app.route("/")
def he():
    arr1 = readtmp()
    arr2 = readhum()
    setTime = 0
    times = 0
    temperature = arr1[-1]
    humidity = arr2[-1]
    templateData = {
        'temperature' : temperature,
        'humidity' : humidity,
        'Tarr' : arr1,
        'Harr' : arr2
    }
    filename = 'temperature.json'
    with open(filename, 'w') as file_obj:
        json.dump(arr1, file_obj)
    filename = 'humidity.json'
    with open(filename, 'w') as file_obj:
        json.dump(arr2, file_obj)
    return render_template("main.html", **templateData)

@app.route("/update")
def update():
    arr1 = readtmp()
    arr2 = readhum()
    setTime = 0
    times = 0
    temperature = arr1[-1]
    humidity = arr2[-1]
    templateData = {
        'temperature': temperature,
        'humidity': humidity,
        'Tarr': arr1,
        'Harr': arr2
    }
    print(arr1)
    print(arr2)
    return render_template("main.html", **templateData)


@app.route("/water", methods=["POST", "GET"])
def water():
    arr1 = readtmp()
    arr2 = readhum()
    temperature = arr1[-1]
    humidity = arr2[-1]
    templateData = {
        'temperature': temperature,
        'humidity': humidity,
        'Tarr': arr1,
        'Harr': arr2
    }
    setTime = int(request.form.get('stime'))
    times = int(request.form.get('times'))
    print(setTime)
    print(times)
    j = 0
    while j < times:
        print("浇水中。。")
        time.sleep(setTime)
        print("暂停浇水")
        time.sleep(1)
        j += 1
    print("浇水完成")
    return render_template("main.html", **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug= True)
