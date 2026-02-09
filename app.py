from flask import Flask, render_template, request, jsonify
from functions.binary_to_decimal import binary_to_decimal
from functions.binary_to_hexadecimal import binary_to_hexadecimal
from functions.hexadecimal_to_decimal import hexadecimal_to_decimal
from functions.hexadecimal_to_binary import hexadecimal_to_binary
from functions.decimal_to_binary import decimal_to_binary
from functions.decimal_to_hexadecimal import decimal_to_hexadecimal
from functions.ip_binary_to_decimal import ip_binary_to_decimal
from functions.ip_binary_to_hexadecimal import ip_binary_to_hexadecimal
from functions.ip_hexadecimal_to_decimal import ip_hexadecimal_to_decimal
from functions.ip_hexadecimal_to_binary import ip_hexadecimal_to_binary
from functions.ip_decimal_to_binary import ip_decimal_to_binary
from functions.ip_decimal_to_hexadecimal import ip_decimal_to_hexadecimal
from functions.rgb_binary_to_decimal import rgb_binary_to_decimal
from functions.rgb_binary_to_hexadecimal import rgb_binary_to_hexadecimal
from functions.rgb_hexadecimal_to_decimal import rgb_hexadecimal_to_decimal
from functions.rgb_hexadecimal_to_binary import rgb_hexadecimal_to_binary
from functions.rgb_decimal_to_binary import rgb_decimal_to_binary
from functions.rgb_decimal_to_hexadecimal import rgb_decimal_to_hexadecimal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    conv_type = data['type']
    from_base = data['from']
    to_base = data['to']
    input_val = data['input']
    
    if conv_type == 'number':
        if from_base == 'binary' and to_base == 'decimal':
            result = binary_to_decimal(input_val)
        elif from_base == 'binary' and to_base == 'hexadecimal':
            result = binary_to_hexadecimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'decimal':
            result = hexadecimal_to_decimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'binary':
            result = hexadecimal_to_binary(input_val)
        elif from_base == 'decimal' and to_base == 'binary':
            result = decimal_to_binary(int(input_val))
        elif from_base == 'decimal' and to_base == 'hexadecimal':
            result = decimal_to_hexadecimal(int(input_val))
        else:
            result = 'Invalid conversion'
    elif conv_type == 'ip':
        if from_base == 'binary' and to_base == 'decimal':
            result = ip_binary_to_decimal(input_val)
        elif from_base == 'binary' and to_base == 'hexadecimal':
            result = ip_binary_to_hexadecimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'decimal':
            result = ip_hexadecimal_to_decimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'binary':
            result = ip_hexadecimal_to_binary(input_val)
        elif from_base == 'decimal' and to_base == 'binary':
            result = ip_decimal_to_binary(input_val)
        elif from_base == 'decimal' and to_base == 'hexadecimal':
            result = ip_decimal_to_hexadecimal(input_val)
        else:
            result = 'Invalid conversion'
    elif conv_type == 'rgb':
        if from_base == 'binary' and to_base == 'decimal':
            result = rgb_binary_to_decimal(input_val)
        elif from_base == 'binary' and to_base == 'hexadecimal':
            result = rgb_binary_to_hexadecimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'decimal':
            result = rgb_hexadecimal_to_decimal(input_val)
        elif from_base == 'hexadecimal' and to_base == 'binary':
            result = rgb_hexadecimal_to_binary(input_val)
        elif from_base == 'decimal' and to_base == 'binary':
            result = rgb_decimal_to_binary(input_val)
        elif from_base == 'decimal' and to_base == 'hexadecimal':
            result = rgb_decimal_to_hexadecimal(input_val)
        else:
            result = 'Invalid conversion'
    else:
        result = 'Invalid type'
    
    return jsonify({'result': str(result)})

if __name__ == '__main__':
    app.run(debug=True)