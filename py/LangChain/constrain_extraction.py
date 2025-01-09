import os
import json
from chain_detector import get_obligatory_constraint, get_forbidden_constraint

with open("../Dynamic/data/api_summary_groundtruth.json", "r") as file:
    data = json.load(file)


def get_constraints(sdk, api, content, forbidden, extra=""):
    if forbidden:
        res = get_forbidden_constraint(content, f"{sdk}_{api}")
        with open("res/forbidden2.log", "a") as file:
            file.write(f"------------------------------------\nSDK:{sdk}\nAPI:{api}\nContent:{content}\nresult:{res}\nextra:{extra}\n\n\n")
    # else:
    #     res = get_obligatory_constraint(content, f"{sdk}_{api}")
    #     with open("res/obligatory.log", "a") as file:
    #         file.write(f"------------------------------------\nSDK:{sdk}\nAPI:{api}\nContent:{content}\nresult:{res}\nextra:{extra}\n\n\n")

for sdk in data["LIBS"]:
    for api in sdk['privacy_APIs']:
        if 'conditions' in api.keys():
            con = api['conditions']
            get_constraints(sdk['SDK'], api['API_name'], con, False)
        if 'effects' in api.keys():
            con = api['effects']
            get_constraints(sdk['SDK'], api['API_name'], con, True)
        if 'parameter_configurations' in api.keys():
            for param in api['parameter_configurations']:
                if 'conditions' in param.keys():
                    con = param['conditions']
                    get_constraints(sdk['SDK'], api['API_name'], con, False, f"parameter = {param['parameter_values']}")
                if 'effects' in param.keys():
                    con = param['effects']
                    get_constraints(sdk['SDK'], api['API_name'], con, True, f"parameter = {param['parameter_values']}")


