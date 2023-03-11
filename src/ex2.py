def get_sallory_bsed_on_profit(profit):
    border=[0,100000,200000,400000,600000,1000000]
    rate=[0.1,0.075,0.05,0.03,0.015,0.01]
    sallary=0
    for i in range(1,len(border)-1):
        sallary += border[i] * rate[i-1]
        if profit>border[i] and profit<border[i+1]:
            sallary+=(profit-border[i])*rate[i+1]
        print("Sallary:",sallary)
    return sallary

get_sallory_bsed_on_profit(120000)


