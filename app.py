from flask import Flask, jsonify
import importlib.util
 
app = Flask(__name__)
 
@app.route('/run-script')
def run_script():
    # Load the local python file (assume downloaded already)
    spec = importlib.util.spec_from_file_location("script", "./script.py")
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
 
    if hasattr(script, 'main'):
        result = script.main()
        return jsonify(result)
    return jsonify([]), 500
 
if __name__ == '__main__':
    app.run(port=5000)
