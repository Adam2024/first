
import re
import docx
import os

#给定文件目录,docx转换为句子
def docx2sen(path_dir):
    sentence_all=[]
    sentence_from_par=[]
    path_list=os.listdir(path_dir)
    print(path_list)
    for path in path_list:
        #path="F:\\work\\履约事件抽取\\抽取列表和维度\\1 (84).docx"
        path=f'{path_dir}\\{path}'
        print(path)
        file=docx.Document(path)
        par=file.paragraphs
        
        for i in range(len(par)):
            a = re.split(u'(.*?[!。?;])',par[i].text)
            sentence_from_par.append(a)
            for j in range(len(a)):
                sentence_all.append(a[j].strip())
    return sentence_all


#将句子更细粒度，按标点符号划分，以便序列标注
def sen2less(sen_list):
    sentence=[]
    for sen in sen_list:
        tmp=re.split('[，。！？、‘’“”（）]/[O]', sen)
        sentence+=tmp
    return sentence
    
    
#文本分类,依据is_trigger的值，不对全文判别，仅仅对存在触发词的句子判别
def classify_sen(sen_list,trigger,is_trigger:bool =False):
    ans_sen={"迟延交付违约责任":[],"迟延支付违约责任":[],"质保期":[],"合同签订日期":[],"合同生效条件":[],"合同有效期":[]}
    trig_list=[]
    if is_trigger:
        for role,tri in trigger.items():
            trig_list+=tri
        for sen in sen_list:
            for key,value in trigger.items():
                for tri in value:
                    if sen.count(tri)!=0:
                    ans_sen[key]+=sen
                    break
    else:
        ans_sen=sen_list
        
    return ans_sen
   

def event_sen(sen_list,trigger,is_trigger:bool=False):
  
    ans_event={"支付":[],"返还":[],"开票":[],"交付":[],"验收":[]}
    num=const.updown
    if is_trigger:
        for i in range(len(sen_list)):
            flag=False
            for key,value in trigger.items():
                
                for tri in value：
                    if sen[i].count(tri)!=0:
                    
                        ans_event[key]+=sen_list[i-num:i+num]
                        flag=True
                        break
            if flag:
                i=i+num-1
    else:
        ans_event=sen_list
    return ans_event
            
    
    
    
    