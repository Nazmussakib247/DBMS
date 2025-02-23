from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def is_safe_state(available, max_need, allocated):
    num_processes = len(max_need)
    num_resources = len(available)
    need = [[max_need[i][j] - allocated[i][j] for j in range(num_resources)] for i in range(num_processes)]
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        allocated_this_round = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocated[i][j] for j in range(num_resources)]
                safe_sequence.append(i)
                finish[i] = True
                allocated_this_round = True
                break
        if not allocated_this_round:
            return False, []

    return True, safe_sequence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_safety():
    data = request.json
    available = list(map(int, data['available']))
    max_need = [list(map(int, row)) for row in data['max_need']]
    allocated = [list(map(int, row)) for row in data['allocated']]
    
    safe, sequence = is_safe_state(available, max_need, allocated)
    return jsonify({"safe": safe, "sequence": sequence})

if __name__ == '__main__':
    app.run(debug=True)
