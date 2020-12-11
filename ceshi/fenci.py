#encoding=utf-8
import jieba
seq_list=jieba.cut("我来到北京大学",cut_all=True)
#print("Full mode"+ "/ ".join(seq_list))

seq_list=jieba.cut("我来到北京大学",cut_all=False)
print("Full mode : "+ "/  ".join(seq_list))