import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_option('deprecation.showPyplotGlobalUse', False)

def linear_regression(x, y):
    model = LinearRegression()
    model.fit(x, y)
    return model.coef_[0], model.intercept_

def plot_regression(x, y, slope, intercept):
    plt.scatter(x, y)
    plt.plot(x, slope * x + intercept, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regresi Linear Sederhana')
    st.pyplot()

def main():
    st.title('Analisis Regresi Linear Sederhana')
    st.write('Masukkan data di bawah ini:')
    
    # Memasukkan data X
    x_input = st.text_input('Variabel X (pisahkan dengan koma)', '1,2,3,4,5')
    x = [float(x.strip()) for x in x_input.split(',')]

    # Memasukkan data Y
    y_input = st.text_input('Variabel Y (pisahkan dengan koma)', '2,4,5,4,5')
    y = [float(y.strip()) for y in y_input.split(',')]
    
    # Menampilkan data sebagai tabel
    df = pd.DataFrame({'X': x, 'Y': y})
    st.write(df)

    # Memanggil fungsi regresi linear
    slope, intercept = linear_regression(pd.DataFrame(x), pd.DataFrame(y))

    # Menampilkan hasil regresi linear
    st.write('Estimasi Parameter:')
    st.write(f'Y = {slope} * X + {intercept}')

    # Menampilkan korelasi
    correlation = 'Positif' if slope > 0 else 'Negatif'
    st.write('Korelasi:', correlation)

    # Menampilkan grafik
    plot_regression(x, y, slope, intercept)

if __name__ == '__main__':
    main()

