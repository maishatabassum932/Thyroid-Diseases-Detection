physical_exam_mapping = {
    'Single nodular goiter-left': 0,
    'Multinodular goiter': 1,
    'Palpable lymph nodes': 2,
}

pathology_mapping = {
    'Micropapillary': 0,
    'Papillary': 1,
    'Follicular': 2,
}

T_mapping = {
    'T1a': 0,
    'T1b': 1,
    'T2': 2,
    'T3': 3,
}

N_mapping = {
    'N0': 0,
    'N1': 1,
}

M_mapping = {
    'M0': 0,
    'M1': 1,
}

stage_mapping = {
    'I': 0,
    'II': 1,
    'III': 2,
    'IV': 3,
}

response_mapping = {
    'Excellent': 0,
    'Indeterminate': 1,
    'Biochemical incomplete': 2,
    'Structural incomplete': 3,
}
import streamlit as st
import pickle
import numpy as np

# Load your model and scaler
model = pickle.load(open('xgb_model.pkl', 'rb'))

st.title("Thyroid Cancer Recurrence Prediction")

# Inputs
age = st.number_input('Age', min_value=10, max_value=100, value=30)
gender = st.selectbox('Gender', ['F', 'M'])
smoking = st.selectbox('Smoking', ['No', 'Yes'])
hx_smoking = st.selectbox('History of Smoking', ['No', 'Yes'])
hx_radiotherapy = st.selectbox('History of Radiotherapy', ['No', 'Yes'])
thyroid_func = st.selectbox('Thyroid Function', ['Euthyroid', 'Hypothyroid', 'Hyperthyroid'])
physical_exam = st.selectbox('Physical Examination', list(physical_exam_mapping.keys()))
adenopathy = st.selectbox('Adenopathy', ['No', 'Yes'])
pathology = st.selectbox('Pathology', list(pathology_mapping.keys()))
focality = st.selectbox('Focality', ['Uni-Focal', 'Multi-Focal'])
risk = st.selectbox('Risk', ['Low', 'Medium', 'High'])
T = st.selectbox('Tumor Classification (T)', list(T_mapping.keys()))
N = st.selectbox('Nodal Classification (N)', list(N_mapping.keys()))
M = st.selectbox('Metastasis Classification (M)', list(M_mapping.keys()))
stage = st.selectbox('Stage', list(stage_mapping.keys()))
response = st.selectbox('Response to Treatment', list(response_mapping.keys()))

# Encode inputs
gender_encoded = 0 if gender == 'F' else 1
smoking_encoded = 0 if smoking == 'No' else 1
hx_smoking_encoded = 0 if hx_smoking == 'No' else 1
hx_radiotherapy_encoded = 0 if hx_radiotherapy == 'No' else 1
thyroid_func_encoded = {'Euthyroid': 0, 'Hypothyroid': 1, 'Hyperthyroid': 2}[thyroid_func]
physical_exam_encoded = physical_exam_mapping[physical_exam]
adenopathy_encoded = 0 if adenopathy == 'No' else 1
pathology_encoded = pathology_mapping[pathology]
focality_encoded = 0 if focality == 'Uni-Focal' else 1
risk_encoded = {'Low': 0, 'Medium': 1, 'High': 2}[risk]
T_encoded = T_mapping[T]
N_encoded = N_mapping[N]
M_encoded = M_mapping[M]
stage_encoded = stage_mapping[stage]
response_encoded = response_mapping[response]

# Prepare feature array (order must match your training data!)
input_features = np.array([[age, gender_encoded, smoking_encoded, hx_smoking_encoded,
                            hx_radiotherapy_encoded, thyroid_func_encoded,
                            physical_exam_encoded, adenopathy_encoded,
                            pathology_encoded, focality_encoded, risk_encoded,
                            T_encoded, N_encoded, M_encoded, stage_encoded,
                            response_encoded]])


if st.button('Predict Recurrence'):
    prediction = model.predict(input_features)

    if prediction[0] == 1:
        st.error("⚠️ The model predicts a recurrence of thyroid cancer.")
    else:
        st.success("✅ The model predicts no recurrence.")
