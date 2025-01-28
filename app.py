from flask import Flask, request, jsonify

app = Flask(__name__)

students = [{"name":"BCPr6N","marks":13},{"name":"0bLSbx8s","marks":59},{"name":"A","marks":92},{"name":"6Xl8oQ2B","marks":12},{"name":"CfPYY6","marks":16},{"name":"dDts2tJ","marks":75},{"name":"oQf","marks":23},{"name":"jEqh0A","marks":11},{"name":"9","marks":63},{"name":"W","marks":27},{"name":"CHJ5U66zu","marks":54},{"name":"KZCqa10G","marks":97},{"name":"60eDaJCB","marks":89},{"name":"f2vWfVOpW","marks":97},{"name":"pd1","marks":32},{"name":"ojywJwE1","marks":16},{"name":"a","marks":37},{"name":"WbFp","marks":9},{"name":"1b","marks":89},{"name":"oy","marks":50},{"name":"rf","marks":45},{"name":"1FtKDHkZ","marks":92},{"name":"Kd","marks":66},{"name":"Au2zl","marks":48},{"name":"tlx","marks":98},{"name":"YUusM","marks":86},{"name":"2eNAh","marks":57},{"name":"EQMEGuY9s","marks":20},{"name":"AbQ6","marks":68},{"name":"hgxY","marks":96},{"name":"6I","marks":82},{"name":"sLe","marks":97},{"name":"NMegq7rM","marks":23},{"name":"YXA17x","marks":26},{"name":"JkZdWlw","marks":62},{"name":"x","marks":88},{"name":"HU2JNJxr","marks":25},{"name":"rrIs","marks":46},{"name":"27xstxMY","marks":10},{"name":"XhrcS9tkR","marks":36},{"name":"7v","marks":72},{"name":"xIePQR7s","marks":60},{"name":"DeaJZp5u8g","marks":19},{"name":"AdYOS4","marks":62},{"name":"R0","marks":30},{"name":"WOcs","marks":22},{"name":"w84Th","marks":20},{"name":"Dp","marks":19},{"name":"Do","marks":18},{"name":"Qx","marks":65},{"name":"aSkl","marks":97},{"name":"ekwWIloP","marks":30},{"name":"fZHbvxudQ","marks":33},{"name":"yEc","marks":87},{"name":"ZvKUU5Ds","marks":73},{"name":"o7dluAV","marks":3},{"name":"zTlmcHV","marks":96},{"name":"Rn1stul","marks":77},{"name":"IMBgJ5","marks":94},{"name":"k9uj6G3Wmv","marks":22},{"name":"gqLl","marks":38},{"name":"TWi9fDb","marks":72},{"name":"2Hl1U3Z","marks":42},{"name":"8I7bO","marks":73},{"name":"jSeucmA","marks":6},{"name":"V6E","marks":3},{"name":"enxV36ZX","marks":48},{"name":"kv","marks":73},{"name":"LSevwudyiH","marks":30},{"name":"fVxqebpe6","marks":69},{"name":"eVQ0aEFDuf","marks":3},{"name":"CO","marks":79},{"name":"P","marks":23},{"name":"46qOCaU","marks":81},{"name":"IiSVZHZeCo","marks":84},{"name":"RG","marks":62},{"name":"209VbQxGdv","marks":64},{"name":"eEJv0ZUnu","marks":62},{"name":"tAfY","marks":6},{"name":"HyFe4r","marks":56},{"name":"yALPUaag","marks":7},{"name":"CuX","marks":34},{"name":"gvS7H1c","marks":91},{"name":"1jJsHSxf","marks":22},{"name":"Pbzqvq","marks":55},{"name":"88z","marks":39},{"name":"8n3RCJA","marks":70},{"name":"BntU","marks":77},{"name":"JQn8PCNO","marks":45},{"name":"6Z54s","marks":77},{"name":"LBdpsxi0YH","marks":49},{"name":"NYhaLmF","marks":73},{"name":"ZT3RNe6kI","marks":76},{"name":"OysJaB66k4","marks":20},{"name":"X2DEOXYD","marks":36},{"name":"xZrdQLIZUO","marks":40},{"name":"QvGq49Egu","marks":40},{"name":"8ya","marks":27},{"name":"drEVL","marks":74},{"name":"pzxfEx","marks":5}]

def find_marks_by_names(names):
    result = {}
    for name in names:
        for student in students:
            if student["name"] == name:
                result['marks'] = student["marks"]
                break
        else:
            result[name] = None
    return result

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "No names provided"}), 400

    marks_result = find_marks_by_names(names)
    
    return jsonify(marks_result)

if __name__ == '__main__':
    app.run(debug=True)
