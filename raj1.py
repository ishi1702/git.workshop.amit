import webbrowser
print("Hi!")
print("How can I help you") 
while(True):
	b=[]
	a=input()
	if(a=="restaurants"):
		webbrowser.open('https://www.google.com/maps/search/restaurants+in+amritapuri/@9.0932873,76.4878334,16.25z')
	elif(a=="busstops"):
		webbrowser.open('https://www.google.com/maps/search/bus+stops+in+amritapuri/@9.0853214,76.4852264,15z/data=!3m1!4b1')
	elif(a=="facebook"):
		webbrowser.open('https://www.facebook.com/')
	elif(a=="gmail"):
		webbrowser.open('https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
	if(a=="thankyou"):
		break

