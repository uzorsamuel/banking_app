
import streamlit as st
from savings_account import SavingsAccount
st.set_page_config(page_title='Savings Account', layout='centered')

savings = SavingsAccount(200000)

with st.form('savings_form'):
    amount = st.number_input('Enter Amount')
    operation = st.selectbox('Deposit','withdraw')
    submit = st.form_submit_button('Submit')
    if submit and operation == 'withdraw':
        with st.spinner('processing..'):
            savings.withdraw(amount)
            print(savings.balance)


