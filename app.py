from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class IdeaEvaluator:
    def __init__(self):
        self.parameters = [
            'market_size',
            'future_scope',
            'innovation_level',
            'feasibility',
            'user_need',
            'scalability'
        ]
    
    def evaluate_market_size(self, idea):
        keywords = ['global', 'large', 'expanding', 'billion', 'million']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate_future_scope(self, idea):
        keywords = ['future', 'next 5 years', 'long-term', 'sustainable', 'growth']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate_innovation_level(self, idea):
        keywords = ['innovative', 'unique', 'novel', 'groundbreaking', 'disruptive']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate_feasibility(self, idea):
        keywords = ['feasible', 'practical', 'realistic', 'doable', 'achievable']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate_user_need(self, idea):
        keywords = ['need', 'problem', 'demand', 'necessity', 'requirement']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate_scalability(self, idea):
        keywords = ['scalable', 'expandable', 'grows', 'extensible', 'adaptable']
        score = sum(1 for keyword in keywords if keyword in idea.lower())
        return min(score * 2, 10)
    
    def evaluate(self, idea):
        scores = {}
        for parameter in self.parameters:
            evaluation_method = getattr(self, f'evaluate_{parameter}')
            scores[parameter] = evaluation_method(idea)
        
        final_score = sum(scores.values()) / len(self.parameters)
        return scores, final_score

evaluator = IdeaEvaluator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    idea = request.form['idea']
    scores, final_score = evaluator.evaluate(idea)
    return jsonify(scores=scores, final_score=final_score)

if __name__ == '__main__':
    app.run(debug=True)
