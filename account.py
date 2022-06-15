account={"accno":1000,
         "opening_date":"20/5/2022",
         "type_acc":"savings",
         "acc_holder":"ram"}
print(account.get("accno"))
print(account.get("opening_date"))
print(account.get("acc_holder"))

# if "balance" in account:
#     account["balance"]=25000
# else:
#     account["balance"]=30000

account["balance"]=25000 if "balance" in account else 30000
print(account)

if account["balance"]>20000:
    account["balance"]-=2000
else:
    account["balance"]-=500
print(account)

