#超参数以及触发词

#文本分类触发词
give=["逾期交付","逾期违约金","延迟交付","延期交付","逾期","延期"]
pay=["逾期支付","逾期付款","延迟支付","延迟付款","支付违约金","逾期","延期"]
quality=["质量保证期","质保期"]
date=["签约日期","签署日期","签订日期","日期"]
effective=["生效"]
indate=["协议有效期","合同期限","终止"]

trigger_classify={"迟延交付违约责任":give,"迟延支付违约责任":pay,"质保期":quality,"合同签订日期":date,"合同生效条件":effective,"合同有效期":indate}



#事件抽取触发词





#事件抽取上下句扩展
updown=4
#【支付】":one,"【返还】":two,"【开票】":three,"【交付】":four，【验收】":five
one=["预付","结算","合同款","支付","合同付款"]
two=["退给","退还","返还"]
three=["发票"]
four=["交货","送达","送到"]
five=["验收"]
trigger_event={"支付":one,"返还":two,"开票":three,"交付":four,"验收":five}


with open('../data/Bosondata.pkl', 'rb') as inp:
    ord2id = pickle.load(inp)
    id2word = pickle.load(inp)
    tag2id = pickle.load(inp)
    id2tag = pickle.load(inp)
    x_train = pickle.load(inp)
    y_train = pickle.load(inp)
    x_test = pickle.load(inp)
    y_test = pickle.load(inp)
    x_valid = pickle.load(inp)
    y_valid = pickle.load(inp)