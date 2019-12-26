import datetime
import time

import OpenOPC
ctpList=[u'1_ЦТП_4-1',u'ЦТП_25-1',u'ИТП_Ям67',u'ЦТП_51_б2',u'ЦТП_60-1',u'ЦТП_53_4',u'ЦТП_9-1']
tagsList=[]
for i in range(0,31):
    tagsList.append(u'CTPClient:ЦТП_60-1.Аналог.Аналог'+str(i))
def ReadOPC(tagList=tagsList,infinity=True):
    opc=OpenOPC.client()
    servers=opc.servers()
    #print (servers)
    server=servers[4]    
    try:
        opc.connect(server)
        data=opc.read(tags=tagList,update='1',include_error='true')
        #time.sleep(1)
    finally:
        opc.close()
        listValue=[]
        if data:
            for item in data:
                 listValue.append('{0}.{2} : {3}'.format(*str(item[0]).split(':')[-1].split('.'),item[1]))
            return listValue 
        else:
            return 'Данные не прочитаны!'
start=datetime.datetime.now()
params=[]
for ctp in ctpList:
    tagsList=[]
    for i in range(0,32):
        tagsList.append(u'CTPClient:'+ctp+u'.Аналог.Аналог'+str(i))
    params.append(ReadOPC(tagList=tagsList))
    end=datetime.datetime.now()
    #print (str(end-start))

for ctpParam in params:
    for line in ctpParam:
        print(line)
print (str(datetime.datetime.now()-start))
#return [(val,quality) for a[1],a[2] in data
