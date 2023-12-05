import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
  
# loading in the model to predict on the data 
pickle_in = open('nbclassifier.pkl', 'rb') 
classifier = pickle.load(pickle_in) 
  
def welcome(): 
    return 'welcome all'
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(Jumlah_Tanggungan, Pendidikan_Ayah, Usia_Ayah, Pendidikan_Ibu, Usia_Ibu, Penghasilan):   
   
    prediction = classifier.predict( 
        [[Jumlah_Tanggungan, Pendidikan_Ayah, Usia_Ayah, Pendidikan_Ibu, Usia_Ibu, Penghasilan]]) 
    print(prediction) 
    return prediction 
      
  
# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    st.title("Prediksi Keterlambatan Pembayaran Uang Sekolah") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Masukkan data-data yang diperlukan  </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    Jumlah_Tanggungan = st.number_input("Jumlah Tanggungan", 1, 4) 
    Pendidikan_Ayah = st.number_input("Pendidikan Ayah", 1, 3) 
    Usia_Ayah = st.number_input("Usia Ayah", 1, 100) 
    Pendidikan_Ibu = st.number_input("Pendidikan Ibu", 1, 3)
    Usia_Ibu = st.number_input("Usia Ibu", 1, 100)
    Penghasilan = st.number_input("Penghasilan", 1, 5) 
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if st.button("Predict"): 
        result = prediction(Jumlah_Tanggungan, Pendidikan_Ayah, Usia_Ayah, Pendidikan_Ibu, Usia_Ibu, Penghasilan) 
    st.success('The output is {} (1=terlambat, 0=tepat waktu)'.format(result)) 
     
if __name__=='__main__': 
    main()