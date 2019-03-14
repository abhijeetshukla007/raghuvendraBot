from flask import session,flash
#import numpy as np 
from flask import Response
import os 
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
import tempfile
import simplejson as j
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import json
import pandas
from rasa_core.agent import Agent
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

app = Flask(__name__)      

@app.route('/')
def index():
    return render_template('index.html')
    
interpreter = Interpreter.load('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = interpreter)
@app.route('/nlu_parsing', methods=['POST'])
def transform():
    if request.headers['Content-Type'] == 'application/json':     
        query = request.json.get("utterance")
        print(query)
        #agent.handle_message(query)
        results=agent.handle_message(query)
        for r in results:
            print(r.get("text"))
            js=r.get("text")

        #js = json.dumps(results)
        #js = results
        resp = Response(js, status=200, mimetype='application/text')
        return resp

def train_dialogue(domain_file = 'restaurant_domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):
					
	featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)
	agent = Agent(domain_file, policies = [MemoizationPolicy(max_history = 5), KerasPolicy(featurizer)])
	
	agent.train(
				training_data_file,
				#max_history = 3,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2,
				augmentation_factor = 50)
				
	agent.persist(model_path)
	return agent

if __name__ == '__main__':
    train_dialogue()
    app.run(host='127.0.0.1', port='80', debug=True)