import subprocess
import pickle

def uso_peligroso_subprocess(cmd):
    subprocess.call(cmd, shell=True)  # B602

def uso_peligroso_pickle(data):
    return pickle.loads(data)  # B301

def hardcoded_password():
    password = "supersecreto123"  # B105

def uso_input_dinamico():
    user_input = input("Ingresa algo: ")  # B322
    eval(user_input)  # B307
