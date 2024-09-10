import json

test_str = ['[{\n    "SDK_name": "AppLovin MAX SDK",\n    "API_name": "setHasUserConsent",\n    "conditions": [\n      "The developer is responsible for complying with applicable privacy regulations.",\n      "The developer is responsible for correctly collecting consent values and passing those to AppLovin.", \n      "The developer must set the value of this flag before initializing the AppLovin SDK.",\n      "Consent values and flags indicate whether users from certain locations provided opt-in consent to collect and use their personal data for interest-based advertising."\n    ],\n    "effects": [\n      "The API records the values of this flag during the SDK initialization.", \n      "Once the consent value for a particular user is set, AppLovin will continue to respect that value for the lifetime of your application or until the user revokes consent to interest-based advertising.", \n      "Consent values are sharable with some mediation partners using adapters."\n    ],\n    "parameter_configuations": [\n      {\n\t      "parameter_values":["true", "context"],\n\t      "conditions":["If a user consents to interest-based advertising, this parameter combination can be used."],\n\t      "effects":["On setting this parameter, the user consent flag is set as true, indicates the user has given the consent"]\n      },\n      {\n\t      "parameter_values":["false", "context"],\n\t      "conditions":["If a user does not consent to interest-based advertising, this parameter combination can be used."],\n\t      "effects":["On setting this parameter, the user consent flag is set as false, indicates the user has not given the consent"]\n      }\n    ]\n  }]']

actual_json_str = json.loads(test_str[0])
print(actual_json_str)

# Load the JSON data from the decoded string

beautified_json = json.dumps(actual_json_str, indent=4)
print(beautified_json)