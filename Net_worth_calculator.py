import streamlit as st

def get_valid_percentage(value):
    try:
        percent = float(value)
        if percent < 0 or percent > 100:
            raise ValueError
        return percent / 100
    except ValueError:
        return None

def suggest_allocation(risk_level):
    if risk_level == 'High':
        return {'Bank': 0.1, 'FD': 0.1, 'Gold': 0.3, 'Stocks': 0.5}
    elif risk_level == 'Medium':
        return {'Bank': 0.3, 'FD': 0.3, 'Gold': 0.2, 'Stocks': 0.2}
    elif risk_level == 'Low':
        return {'Bank': 0.5, 'FD': 0.3, 'Gold': 0.1, 'Stocks': 0.1}
    else:
        return {'Bank': 0.3, 'FD': 0.3, 'Gold': 0.2, 'Stocks': 0.2}

def calculate_growth(net_worth, allocations):
    counter = 0
    while net_worth < 85000000:
        counter += 1
        bank = net_worth * allocations['Bank'] * 1.06
        fd = net_worth * allocations['FD'] * 1.08
        gold = net_worth * allocations['Gold'] * 1.11
        stocks = net_worth * allocations['Stocks'] * 1.15
        net_worth = bank + fd + gold + stocks
    return counter

st.title("Net Worth Growth Calculator 📈")

st.header("Step 1: Risk Profile")
risk_level = st.radio("Select your risk preference:", ('Low', 'Medium', 'High'))

if st.button("Suggest Allocation Based on Risk"):
    suggestion = suggest_allocation(risk_level)
    st.session_state['bank'] = suggestion['Bank'] * 100
    st.session_state['fd'] = suggestion['FD'] * 100
    st.session_state['gold'] = suggestion['Gold'] * 100
    st.session_state['stocks'] = suggestion['Stocks'] * 100

st.header("Step 2: Enter Your Current Details")

net_worth = st.number_input("Enter your current net worth (in ₹)", min_value=0.0, format="%f")

bank = st.number_input("Bank Savings (%)", min_value=0.0, max_value=100.0, key='bank')
fd = st.number_input("Fixed Deposit (FD) (%)", min_value=0.0, max_value=100.0, key='fd')
gold = st.number_input("Gold Investment (%)", min_value=0.0, max_value=100.0, key='gold')
stocks = st.number_input("Stocks Investment (%)", min_value=0.0, max_value=100.0, key='stocks')

if st.button("Calculate Years to Become Millionaire"):
    allocations = {
        'Bank': get_valid_percentage(bank),
        'FD': get_valid_percentage(fd),
        'Gold': get_valid_percentage(gold),
        'Stocks': get_valid_percentage(stocks)
    }

    if None in allocations.values():
        st.error("Please ensure all percentage values are between 0 and 100.")
    elif sum(allocations.values()) != 1:
        st.error("Total allocation must be exactly 100%.")
    else:
        years = calculate_growth(net_worth, allocations)
        st.success(f"It will take approximately {years} years to become a millionaire!")
        st.balloons()
