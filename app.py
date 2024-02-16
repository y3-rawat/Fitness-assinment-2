from flask import Flask, render_template, request, jsonify
import main1

import pickle
import numpy as np
current_body_weight = ""
goal_of_body_weight = ""
fitness_goal = ""
recommendation = ""

b = {'Cottage cheese with berries and nuts for breakfast, Chicken and quinoa salad for lunch, Baked cod with roasted vegetables for dinner, Protein bar for snacks':1,
    'Whole grain toast with peanut butter and banana for breakfast, Lentil soup with whole wheat bread for lunch, Grilled shrimp with zucchini noodles for dinner, Greek yogurt with honey for snacks':2,
     'Scrambled eggs with spinach and tomatoes for breakfast, Turkey and avocado salad for lunch, Baked chicken with quinoa for dinner, Mixed nuts for snacks':3,
      'Protein pancakes with berries for breakfast, Tuna salad with whole wheat pita for lunch, Grilled steak with sweet potato fries for dinner, Cottage cheese with pineapple for snacks':4,
       'Smoothie with kale, banana, and protein powder for breakfast, Quinoa salad with black beans for lunch, Grilled chicken with steamed broccoli for dinner, Greek yogurt with berries for snacks':5,
        'Oatmeal with fruits and nuts for breakfast, Grilled chicken salad for lunch, Steamed vegetables with quinoa for dinner, Greek yogurt with berries for snacks' :6,
        'Eggs with whole wheat toast and avocado for breakfast, Brown rice with lean beef for lunch, Baked salmon with sweet potatoes for dinner, Protein shake with banana for snacks':7 ,
        'Greek yogurt with granola and honey for breakfast, Turkey and avocado wrap for lunch, Stir-fried tofu with vegetables for dinner, Apple slices with almond butter for snacks':8,
               'Smoothie with spinach, banana, and protein powder for breakfast, Quinoa salad with chickpeas for lunch, Grilled fish with asparagus for dinner, Cottage cheese with pineapple for snacks':9,
                      'Oatmeal with almond milk and berries for breakfast, Turkey and avocado wrap for lunch, Grilled salmon with asparagus for dinner, Apple slices with almond butter for snacks':0}
app = Flask(__name__)
pipe = pickle.load(open(r'model\pipe.pkl','rb'))
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/output', methods=['POST'])
def output():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    
    global current_body_weight
    current_body_weight = input1
    global goal_of_body_weight
    goal_of_body_weight = input2
    global fitness_goal
    fitness_goal = input3
    
    

    inp3 = {"Gain Muscle":1,"Tone Up":2,"Lose Weight":3}
    inp_3= inp3.get(input3)

    p = np.array([int(input1),int(input2),inp_3],dtype=object).reshape(1,3)

    
    p_no = pipe.predict(p)
    key = [key for key, value in b.items() if value == p_no]
    global recommendation

    recommendation = key 

    return render_template('output.html', output={'input1': input1, 'input2': input2, 'input3': input3,'pred':key[0]})

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    global a 
    chatbot = main1.create_chatbot()

    if userText in chatbot:
        response = chatbot[userText]
        return response
        
    else:
        response = main1.short_final(userText,current_body_weight,goal_of_body_weight,fitness_goal,recommendation)
        return response
        

if __name__ == '__main__':
    app.run(debug=True)
