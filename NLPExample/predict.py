from pureml import BasePredictor,Input,Output
import pureml
from sklearn.metrics import accuracy_score
# # score = accuracy_score(y_pred,y_test)
# # print(f"{score}")
import pickle
import numpy as np

# with open('./utils/cleaned_token_list_data.p','rb') as file:
#     cleaned_token_list_data = pickle.load(file)
#
# # score = accuracy_score(y_pred,y_test)
# # print(f"{score}")sudo chmod a+r /home/lenovo/Downloads/code.deb

# # score = accuracy_score(y_pred,y_test)
# # print(f"{score}")
# # score = accuracy_score(y_pred,y_test)
# # print(f"{score}")
# # score = accuracy_score(y_pred,y_test)
# # print(f"{score}")
# with open('./utils/max_len.p','rb') as file:
#     max_len = pickle.load(file)
#
# with open('./utils/sentence_to_indices.p','rb') as file:
#     sentence_to_indices = pickle.load(file)
#
# with open('./utils/words_to_index.p','rb') as file:
# #     words_to_index = pickle.load(file)
# data = pureml.dataset.fetch(label='nlpexample_docs:development:v1')
# y_test = data['y_test']

class Predictor(BasePredictor):
    label = 'nlpexample_docs:model:v1'
    input = Input(type = 'numpy ndarray')
    output = Output(type = 'numpy ndarray')

    def load_models(self):
        self.model = pureml.model.fetch(self.label)

    def predict(self, data):
        prediction = self.model.predict(data)
        # for i, tk_lb in enumerate(cleaned_token_list_data):
        #     tokens, label = tk_lb
        #     sentence_to_indices(tokens, words_to_index, max_len, i, data)
        #     prediction[i] = label
        #prediction = np.argmax(prediction, axis=1)
        threshold = 0.4
        prediction = np.where(prediction > threshold,1,0)
        prediction = np.squeeze(prediction)
        return prediction

# p = Predictor()
# p.load_models()
# y_pred = p.predict(data['x_test'])
# # # above_threshold = np.sum(y_pred> 0.45)
# # # below_threshold = np.sum(y_pred < 0.45)
# # print(f"Above Threshold: {above_threshold}")
# # print(f"Below Threshold: {below_threshold}")
# print(f"Type of y-Pred: {type(y_pred)}")
# print(f"y-pred Shape: {y_pred.shape}")
# print(f"Type of y-test: {type(y_test)} ")
# print(f"y-test Shape: {y_test.shape}")


# print(f"y_pred: {y_pred}")
# print(f"y_test: {y_test}")

# union_data = set(y_pred).union(y_test)
# print(union_data)


# score = accuracy_score(y_pred,y_test)
# print(f"{score}")