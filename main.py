from flask.json import jsonify



def check(result):
    if result.isalpha():   #isalpha() returns True if all characters in the string are alphabets
        return jsonify({'result':'sanitized'})
    else:
        return jsonify({'result':'unsanitized'})

