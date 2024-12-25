
#Dataframe
#pip install pandas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Makine Öğrenmesi
#denetimli Öğrenme
#Regresyon -Bağımsız ve Bağımlı Değişkenlerimiz var-
#Sınıflandırma
#denetimsiz öğrenme
#Kümeleme

#Reinforcement Learning

#m2 büyüklüğü, konum, oda sayısı, yapım yılı,Konut fiyatı
#100,Göztepe, 4+1,2015,4500000

#mail içerik,gönderen,alıcı,durum


#Regresyon Algoritmaları
#Lineer Regresyon, Polinom Regresyon, Lasso,Ridge,Elastik Net, SVN

# data=pd.read_csv("business_revenue_data.csv",sep=",")
# X=data.drop(columns=["Monthly_Revenue"]) #bağımsız Değişkenleri
# y=data["Monthly_Revenue"] #bağımlı değişkeni
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# linear_model=LinearRegression()
# linear_model.fit(X_train,y_train)
# y_pred_linear=linear_model.predict(X_test)

# mse_linear=mean_squared_error(y_test, y_pred_linear)
# r2_linear=r2_score(y_test, y_pred_linear)
# print("MSE Lineer:",mse_linear)
# print("r2 lineer:",r2_linear)

# poly=PolynomialFeatures(degree=2)
# X_poly_train=poly.fit_transform(X_train)
# X_poly_test=poly.transform(X_test)

# poly_model=LinearRegression()
# poly_model.fit(X_poly_train,y_train)
# y_pred_poly=poly_model.predict(X_poly_test)

# mse_poly=mean_squared_error(y_test, y_pred_poly)
# r2_poly=r2_score(y_test, y_pred_poly)
# print("MSE Poly:",mse_poly)
# print("r2 Poly:",r2_poly)

# rf_model=RandomForestRegressor(n_estimators=100,random_state=42)
# rf_model.fit(X_train,y_train)
# y_pred_rf=rf_model.predict(X_test)

# mse_rf=mean_squared_error(y_test, y_pred_rf)
# r2_rf=r2_score(y_test, y_pred_rf)

# print("MSE RF:",mse_rf)
# print("r2 RF:",r2_rf)


#Bir işletmenin yeni şubelerinin gelirini tahmin etmek
#Bağımsız Değişkenler
#Nüfus:Şubenin bulunduğu bölgedeki nüfus
#Rakip Sayısı: Bölgedeki rakip şube sayısı
#Ortalama Harcama: Bölgede kişi başına düşün ortalama harcama
#Reklam Harcaması: Şubenin tanımı için yapılan harcama

#Tahmin edilen hedef değişkeni aylık gelir-bağımlı değişken



np.random.seed(42)
n_samples=200
#generate data
data={"Nufus":np.random.uniform(5000,50000,n_samples),
"Rakip_Sayisi":np.random.randint(1,10,n_samples),
"Ortalama_Harcama":np.random.uniform(20,100,n_samples),
"Reklam_Harcama":np.random.uniform(1000,10000,n_samples),
"Aylık_Gelir":None}
#add noise
data["Aylık_Gelir"]=(0.5*data["Nufus"]-300*data["Rakip_Sayisi"]+50*data["Ortalama_Harcama"]+2*data["Reklam_Harcama"]+ np.random.normal(0,5000,n_samples))


data=pd.DataFrame(data)

#bağımsız değişkenler
X=data.drop(columns=["Aylık_Gelir"])
y=data["Aylık_Gelir"]

X_train,X_test,y_train,y_test=train_test_split(X, y,test_size=0.2,random_state=42)

print("Linear Regresyon")
linear_model=LinearRegression()

linear_model.fit(X_train,y_train)
y_pred_linear=linear_model.predict(X_test)
mse_linear=mean_squared_error(y_test,y_pred_linear)
r2_linear=r2_score(y_test,y_pred_linear)
print("Linear Regresyon MSE:",mse_linear)
print("Linear Regresyon R2:",r2_linear)

print("Polynomial Regresyon")

poly=PolynomialFeatures(degree=2)
X_poly_train=poly.fit_transform(X_train)
X_poly_test=poly.transform(X_test)

poly_model=LinearRegression()
poly_model.fit(X_poly_train,y_train)
y_pred_poly=poly_model.predict(X_poly_test)

mse_poly=mean_squared_error(y_test,y_pred_poly)
r2_poly=r2_score(y_test,y_pred_poly)
print("Poly Regresyon MSE:",mse_poly)
print("Poly Regresyon R2:",r2_poly)



print("Random Forest Regressor")

rf_model=RandomForestRegressor(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)
y_pred_rf=rf_model.predict(X_test)

mse_rf=mean_squared_error(y_test,y_pred_rf)
r2_rf=r2_score(y_test,y_pred_rf)
print("RF Regresyon MSE:",mse_rf)
print("RF Regresyon R2:",r2_rf)



print("Gradient Boosting Regressor")

gb_model=GradientBoostingRegressor(n_estimators=100,random_state=42)
gb_model.fit(X_train,y_train)
y_pred_gb=gb_model.predict(X_test)


mse_gb=mean_squared_error(y_test,y_pred_gb)
r2_gb=r2_score(y_test,y_pred_gb)
print("GB Regresyon MSE:",mse_gb)
print("GB Regresyon R2:",r2_gb)




scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Support Vector Machine")
svr_model=SVR(kernel="rbf",C=100,gamma=0.1,epsilon=0.01)
svr_model.fit(X_train_scaled,y_train)
y_pred_svr=svr_model.predict(X_test_scaled)


mse_svr=mean_squared_error(y_test,y_pred_svr)
r2_svr=r2_score(y_test,y_pred_svr)
print("SVR Regresyon MSE:",mse_svr)
print("SVR Regresyon R2:",r2_svr)
