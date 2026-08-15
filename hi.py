#passw strength checker using flask
#feel free to modify
from flask import Flask, request, jsonify, send_from_directory
hi = Flask(__name__)
common_passwords = [
    "password",
    "12345",
    "123456789",
    "qwerty",
    "letmein",
    "iloveyou",
    "admin",
    "welcome",
    "abc123",
    "11111",
    "123123",
    "00000",
    "passw0rd",
]
def check_password(password):
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_characters:
            has_special = True
    is_long = len(password) >= 8
    is_common = password.lower() in common_passwords
    print("")
    print("length 8+: " + ("yes" if is_long else "no"))
    print("uppercase letter: " + ("yes" if has_upper else "no"))
    print("lowercase letter: " + ("yes" if has_lower else "no"))
    print("number: " + ("yes" if has_number else "no"))
    print("special character: " + ("yes" if has_special else "no"))
    print("common password: " + ("yes (bad)" if is_common else "no"))
    print("")
    score = 0
    if is_long:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_special:
        score += 1
    if is_common:
        result = "weak (commonly used password)"
    elif score <= 2:
        result = "weak"
    elif score <= 3:
        result = "fair"
    elif score <= 4:
        result = "strong"
    else:
        result = "excellent"
    print("result: " + result)
    return {
        "result": result,
        "long_enough": is_long,
        "upper": has_upper,
        "lower": has_lower,
        "number": has_number,
        "special": has_special,
        "common": is_common,
    }
@hi.route("/")
def home():
    return send_from_directory(".", "index.html")
@hi.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    return jsonify(check_password(password))
if __name__ == "__main__":
    hi.run(debug=True)
