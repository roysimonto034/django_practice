import pickle
jsn={}
jsn['sdsfv']=('sam','hrh','efgfb','lkaf')
jsn['fhjhj']={'dgfhhj','rthjjy','ryhtj','ghhj','345fggf'}
jsn['num']=[2,3,5,6,7,8]
jsn['link']='https://google.com'

with open('jsn.pickle','wb') as f:
    pickle.dump(jsn,f)

print(jsn) 
