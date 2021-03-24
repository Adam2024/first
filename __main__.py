
from classify_v2.models.lstm import LSTM
from classify_v2.training import eval, load
from resultCal_py3 import calculate
import proc_docx
import const_last
import const
import torch 
docx_dir=""

sen_all=docx2sen(docx_dir)

#文本分类方法
trigger1=const.trigger_classify
sen1=classify_sen(event_sen,trigger,True)
model1, dataset1, params1 = load(
    const.MODEL_DIR, LSTM,
    gpu='cuda'
)

ans1={"迟延交付违约责任":[],"迟延支付违约责任":[],"质保期":[],"合同签订日期":[],"合同生效条件":[],"合同有效期":[]}
for key,value in sen1:
    for sen in value:
        text_list=[]
        text_list+=sen
        label_list = eval.predict_single(
            model1, text_list,dataset1, 
            #threshold=0.5,
            output_transform=torch.sigmoid,
            gpu='cuda'
        )
        label_list=(sen)
        if label_list[0]==key:
            ans1[key]+sen

for key,value in ans1.items():
    print(key,":")
    for val in value:
        print(val)
    print("\n")



#事件抽取方式
trigger2=const_last.trigger_event
sen2=event_sen(event_sen,trigger2,True)
one={"支付主体":None,"支付时间":None,"支付款项类型":None,"支付金额":None,"支付途径":None}
two={"返还主体":None,"返还时间":None,"返还款项类型":None,"返还金额":None}
three={"开票主体":None,"开票时间":None,"开票类型":None,"开票税率":None,"开票科目":None}
four={"交付主体":None,"交付时间":None,"交付地点":None,"交付内容":None,"交付方式":None}
five={"验收主体":None,"验收时间":None,"验收标准":None}
ans2={"支付":one,"返还":two,"开票":three,"交付":four,"验收":five}
model2=torch.load('/home/libaokui2021/ner/pytorch/model/model4.pkl')


for key,value in sen2:
    entityres=[]
    for sen in value:
        sen=torch.tensor(sen, dtype=torch.long)
        score,predict = model2(sen)
        entityres = calculate(sen,predict,const_last.id2word,const_last.id2tag,entityres)
    
    

    for ent in entityres:
        role=""
        argu=""
        for word in ent:
            word=word.split('/')
            argu+=word[0]
            if role=="":
                role=word[1][2:]
        if ans2[key].has_key(role):
            if ans2[key][role]==None:
                ans2[key][role]=argu
                
for key,value in ans2.items():
    print("事件类型:",key)
    for role,val in value.items():
        print(role,":",val)
    print("\n")
                
