import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu
import openpyxl
import datetime
import time
from sklearn.preprocessing import OneHotEncoder
from prophet import Prophet

st.set_page_config(page_title = 'Application')
st.title("Supplier Analysis")

file= st.file_uploader(label = 'Upload your dataset:',type=['xlsx','csv'])

if file is not None:
     po_receiving_data=pd.read_excel(file,na_values='Missing',usecols="D,G,J,N,P:Q,S",engine='openpyxl')
     df_main=po_receiving_data.copy()
     df_main['ITEM_ID'].fillna(-1,inplace=True)
     df_main=df_main.loc[(df_main['ITEM_ID']!=-1)].copy()
     st.write(df_main.sample(7).reset_index(drop=True))
     if df_main['ITEM_ID'].dtype != 'O':
          df_main['ITEM_ID']=pd.to_numeric(df_main['ITEM_ID'], downcast='integer', errors='coerce') 
        # st.write(df_main.dtypes)
     df_main['TRANSACTION_DATE']=pd.to_datetime(df_main['TRANSACTION_DATE'])
     df=df_main.loc[(df_main['VENDOR_ID']==4820827) & (df_main['ITEM_ID']==21646515)].sort_values(by=['PO_LINE_ID','TRANSACTION_DATE']).copy()
     qn=dict(df.loc[df['TRANSACTION_TYPE']=='RECEIVE'].groupby(['VENDOR_ID','ITEM_ID','PO_LINE_ID'])['ACTUAL_QUANTITY'].sum())
     rej_rate=[]
     tot_qn={}
     rej_rate=[]
     tot_qn={}
     for i,j in qn.items():
         act=df.loc[(df['VENDOR_ID']==i[0])&(df['ITEM_ID']==i[1])&(df['PO_LINE_ID']==i[2])&(df['TRANSACTION_TYPE']=='ACCEPT')].sort_values(by=['TRANSACTION_DATE'])['ACTUAL_QUANTITY'].sum()
         rec=df.loc[(df['VENDOR_ID']==i[0])&(df['ITEM_ID']==i[1])&(df['PO_LINE_ID']==i[2])&(df['TRANSACTION_TYPE']=='RECEIVE')].sort_values(by=['TRANSACTION_DATE'])['ACTUAL_QUANTITY'].sum()
         if act==0:
             tot_qn[i]=rec
         else:
             tot_qn[i]=act
     for index, row in df.iterrows():
         if row['TRANSACTION_TYPE']!='RECEIVE':
             if row['TRANSACTION_TYPE']=='ACCEPT':
                 tol=tot_qn[(row['VENDOR_ID'],row['ITEM_ID'],row['PO_LINE_ID'])]
                 total=df.loc[(df['VENDOR_ID']==row['VENDOR_ID'])&(df['ITEM_ID']==row['ITEM_ID'])&(df['PO_LINE_ID']==row['PO_LINE_ID'])&(df['TRANSACTION_TYPE']=='ACCEPT')]['ACTUAL_QUANTITY'].sum()
                 if total==tol:
                     act=tol-total
                 else:
                     print("true")
                     act=tol-row['ACTUAL_QUANTITY']
                 rej_rate.append((act/tol)*100)
             else:
                 tol=tot_qn[(row['VENDOR_ID'],row['ITEM_ID'],row['PO_LINE_ID'])]
                 rej_rate.append((row['ACTUAL_QUANTITY']/tol)*100)
            
                
     df.insert(5,'REJECTION_RATE',0.0)
     df.loc[df['TRANSACTION_TYPE']!='RECEIVE','REJECTION_RATE']=rej_rate
     DF=df.loc[df['TRANSACTION_TYPE']!='RECEIVE'].sort_values(by=['PO_LINE_ID','TRANSACTION_DATE']).copy()
     DF.reset_index(inplace=True)
     DF.drop(columns=['index'],inplace=True)
     st.write(DF)
     DF['ds']=DF['TRANSACTION_DATE'].copy()
     DF['y']=DF['REJECTION_RATE'].copy()
     DF.drop(columns=['PO_LINE_ID','ACTUAL_QUANTITY','TRANSACTION_TYPE','TRANSACTION_DATE','REJECTION_RATE','PROMISED_DATE'],inplace=True)
     encoder=OneHotEncoder(sparse_output=False)
     encoded = encoder.fit_transform(DF[['VENDOR_ID', 'ITEM_ID']])
     columns = [f"{col}_{int(val)}" for col, vals in zip(['VENDOR', 'ITEM'], encoder.categories_) for val in vals]
     DF[columns] = encoded
     DF.drop(columns=['VENDOR_ID', 'ITEM_ID'], inplace=True)
     model=Prophet()
     for col in columns:
          model.add_regressor(col)
     model.fit(DF)
     future = model.make_future_dataframe(periods=2, freq='M')
     inp3=4820827
     inp4=21646515
     selected_vendor = "VENDOR_"+str(inp3)
     selected_item = "ITEM_"+str(inp4)
     for col in columns:
          future[col] = 1 if col in [selected_vendor, selected_item] else 0
     forecast=model.predict(future)
     st.write(forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(15))
     st.write(pd.__version__)
     st.write(Prophet.__version__)
