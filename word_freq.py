# create list of lower case words
import sys
import re
class convert:
	def __init__(self):
		self.stopwords=[w.strip() for w in open('english','r')]
		self.words=[w.strip() for w in open('vocab.txt','r')]
		self.add_count=0
		self.add_word=[]
	def stem(self,word):
		regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
		stems, suffix = re.findall(regexp, word)[0]
		return stems
	def file_input(self,filename):
		word_list = re.split(r'\s+|/', file(filename).read().lower())
		word_list2 = [w.strip() for w in word_list if not w in self.stopwords]

	# create dictionary of word:frequency pairs
		freq_dic = {}
	# punctuation and numbers to be removed
		punctuation = re.compile(r'[-.?!,":;()%~\[\]|0-9|\xe2\x80\x9c]') 
		for word in word_list2:
			word = punctuation.sub("", word)
		# form dictionary
			if word !='' and word not in self.stopwords:
				try: 
					freq_dic[word] += 1
				except: 
					freq_dic[word] = 1
		freq_list2 = [(val, stem(key)) for key, val in freq_dic.items()]
		freq_list2.sort(reverse=True)
		#print 'Words in text:', len(freq_list2)
		f = open("wordfreq.txt", "w")
		for i,j in freq_list2:
			f.write(str(i)+' '+j+'\n')
		f.close()
		length=len(freq_list2)
		f=open("test.dat",'w')
		f.write(str(length)+' ')
		for i,j in freq_list2:
			if j in self.words:
				index=self.words.index(j)
			else:
				index=len(self.words)+1
				self.words.append(j)
				self.add_count+=1
				self.add_word.append(j)
			f.write(str(index)+":"+str(i)+" ")
		f.close()
	def list_input(self,word_list):
		word_list2 = [w.strip() for w in word_list if not w in self.stopwords]
		freq_dic = {}
	# punctuation and numbers to be removed
		punctuation = re.compile(r'[-.?!,":;()%~\[\]#|0-9|\xe2\x80\x9c]')  
		for word in word_list2:
		# remove punctuation marks
			word = punctuation.sub("", word)
		# form dictionary
			if word !='' and word not in self.stopwords:
				try:
					word=self.stem(word)
				except:
					print word
					exit()
				try: 
					
					freq_dic[word] += 1
				except: 
					freq_dic[word] = 1
		freq_list2 = [(val, key) for key, val in freq_dic.items()]
	# sort by val or frequency
		freq_list2.sort(reverse=True)
		#print 'Words in text:', len(freq_list2)
		length=len(freq_list2)
		f=''
		f+=(str(length)+' ')
		for i,j in freq_list2:
			if j in self.words:
				index=self.words.index(j)
			else:
				index=len(self.words)+1
				self.words.append(j)
				self.add_count+=1
				self.add_word.append(j)
			f+=(str(index)+":"+str(i)+" ")
		return f
	def create_wordlist(self,filename):
		f=open(filename,'w')
		for i in self.words:
			f.write(i+'\n')
	def addwords(self,filename):
		f=open(filename,'w')
		for i in self.add_word:
			f.write(i+'\n')
if __name__ == '__main__':
	#print sys.argv[1]
	c=convert()
	# c.file_input(sys.argv[1])
	f=open(sys.argv[1],'r')
	ff=open('testt.dat','w')
	# corpus=[]

	for i in f:
		if i[:9]=='<content>':
			# print i[9:-11]
			tmp=re.split(r'\s+|/',i[9:-11])
			ff.write(c.list_input(tmp)+'\n')
	print "words add "+str(c.add_count)
	c.addwords('addword.txt')