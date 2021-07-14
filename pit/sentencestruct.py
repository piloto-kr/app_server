from konlpy.tag import Kkma

class SentenceStruct():
    #for sentence struct
    def makeResultString(self, corpus):
        retstr = ''
        clist = self.checkSSList(corpus)
        for cond in clist:
            if cond:
                retstr = retstr + '1'
            else:
                retstr = retstr + '0'
        return retstr

    def findPattern(self, p, sp, index1=0, index2=0):
        if index2 >= len(sp):
            return True
        elif index1 >= len(p):
            return False

        if p[index1] == sp[index2]:
            return self.findPattern(p, sp, index1+1, index2+1)
        else:
            return self.findPattern(p, sp, index1+1)

    def getPosPattern(self, pos, opt=0):
        pospat = []
        for morphs in pos:
            if opt:
                pospat.append(morphs[1][0]) #upper category
            else:
                pospat.append(morphs[1])
        return pospat

    def getWords(self, pos):
        words = []
        for morphs in pos:
            if morphs[1][0] in {'M','N','O','V'}:
                words.append(morphs)
        return words

    def checkSSList(self, corpus):
        kkma = Kkma()
        pos = kkma.pos(corpus)
        posn = kkma.nouns(corpus)
        words = self.getWords(pos)
        pospat = self.getPosPattern(pos)
        pospatu = self.getPosPattern(pos, 1)

        #a two words
        checkA = len(words) >= 2
        
        #b two words + not exist
        checkB = checkA #not implemented
        
        #c certain thing
        cnn = self.findPattern(pospatu, ['N','N'])
        cmn = self.findPattern(pospatu, ['M','N'])
        cven = self.findPattern(pospat, ['VA','ETD','NNG'])
        cven = cven or self.findPattern(pospat, ['VA', 'ETD', 'NN'])
        cven = cven or self.findPattern(pospat, ['VA', 'ETD', 'NNP'])
        checkC = cnn or cmn or cven

        #d plural
        checkD = ('들', 'XSN') in pos

        #e present continuous
        cgoit = self.findPattern(pos, [('고', 'ECE'), ('있', 'VV')])
        cjoongi = self.findPattern(pos, [('중', 'NNB'), ('이', 'VCP')])
        checkE = cgoit or cjoongi

        #f negative
        canha = ('안하', 'VV') in pos
        cani = ('아니', 'VCN') in pos
        canh = ('않', 'VXV') in pos
        csilh = ('싫', 'VV') in pos
        pos_r = [m for m in pos if m[1] == 'MAG' and m[0] != '안']
        pos_an = pos.copy()
        for m in pos_r:
            pos_an.remove(m)
        pos_an = self.getPosPattern(pos_an)
        can = self.findPattern(pos_an, ['MAG', 'VV'])
        can = can or self.findPattern(pos_an, ['MAG', 'VA'])
        checkF = canha or cani or canh or csilh or can
            
        #g personal pronouns
        pnp = [('나', 'NP'), ('너', 'NP'), ('우리', 'NP'),
            ('내', 'NP'), ('내', 'NNB'), ('네', 'NP'), ('너희', 'NP')]
        checkG = any(m in pos for m in pnp)
            
        #h three words phrase
        ctwp = len(words) >= 3
        cdesc = self.findPattern(self.getPosPattern(words, 1), ['M', 'V', 'N'])
        checkH = ctwp or cdesc
        
        #i three-year-old total
        checkI = len(words) >= 3 and (checkF or checkH)
            
        #j type3 sentence
        csubj = any(w in pos for w in [('은', 'JX'), ('는', 'JX'), ('이', 'JX'), ('가', 'JX')])
        ckkmaexc = self.findPattern(pos, [('나', 'VV'), ('는', 'ETD')])
        cobj = any(w in pos for w in [('을', 'JKO'), ('를', 'JKO')])
        cverb = 'VV' in pospat
        checkJ = (csubj or ckkmaexc) and cobj and cverb
        
        #k question words(who, when, where, what, how, why)
        wlist = [('누', 'NNG'), ('누구', 'NP'), ('언제','MAG'), ('언제', 'NP'),
                ('어디', 'NP'), ('뭐', 'NP'), ('무슨', 'MDT'),
                ('어떤', 'MDT'), ('무엇', 'NNG'), ('어떻', 'VA'),
                ('왜', 'MAG')]
        checkK = any(w in pos for w in wlist)
            
        #l using I
        checkL = ('나', 'NP') in pos
        
        #m possessive pronoun
        cmpp = self.findPattern(pos, [('그', 'VV'), ('어야', 'ECD')])
        cmpp = cmpp or self.findPattern(pos, [('의', 'JKG'), ('것', 'NNB')])
        cmpp = cmpp or ('거', 'NNB') in pos
        checkM = cmpp
        
        #o past tense
        checkO = ('었', 'EPT') in pos
            
        #p amount words
        alist = [('조금', 'MAG'), ('약간', 'MAG'), ('많이', 'MAG'),
                ('거의', 'MAG'), ('모두', 'MAG')]
        checkP = any(a in pos for a in alist)

        #n prepositional phrase in sentence
        checkN = checkO or checkP #not implemented
        
        #q connector
        candor = ('그리고','MAG') in pos
        candor = candor or ('또는', 'MAG') in pos
        cgruna = self.findPattern(pos, [('그러', 'VV'), ('나', 'ECE')])
        cddaemoon = self.findPattern(pos, [('때문', 'NNB'), ('에', 'JKM')])
        checkQ = candor or cgruna or cddaemoon
            
        #r verbal noun (gerund)
        checkhagi = self.findPattern(pos, [('하', 'XSV'), ('기', 'ETN')])
        pos_vr = [m for m in pos if m[1] == 'NNB' and m[0] != '것']
        pos_vn = pos.copy()
        for m in pos_vr:
            pos_vn.remove(m)
        pos_vn = self.getPosPattern(pos_vn)
        checkgut = self.findPattern(pos_vn, ['VV','ETD','NNB'])
        checkhgut = self.findPattern(pos_vn, ['XSV','ETD','NNB'])
        checkR = checkhagi or checkgut or checkhgut
            
        #s q words + right order
        cvsib = 'V' in pospatu
        checkS = checkK and cvsib
        
        #t sa nouns
        checkT = False
        for m in posn:
            if m[-1] == '사':
                checkT = True
            elif m == '사가':
                checkT = True
                
        #u compare expression
        checkU = any(c in pos for c in [('더', 'MAG'), ('가장', 'MAG'), ('제일', 'MAG')])

        return [
            checkA,
            checkB,
            checkC,
            checkD,
            checkE,
            checkF,
            checkG,
            checkH,
            checkI,
            checkJ,
            checkK,
            checkL,
            checkM,
            checkN,
            checkO,
            checkP,
            checkQ,
            checkR,
            checkS,
            checkT,
            checkU
        ]
