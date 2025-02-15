# task1.py
def kwargsAcceptFun(**kwargs):
    print("Received named arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
