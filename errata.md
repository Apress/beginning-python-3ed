# Errata for *Beginning Python, 3rd Edition*

On **page 369**:
 

The error is in the definition of function parse. 

The original source code:
def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
                for rule in self.rules:
                    if rule.condition(block):
                        last = rule.action(block,
                               self.handler)
                        if last: break
        self.handler.end('document')
'rule' has been looped 3 times in the 'for filter in self.filters:' statement, this is incorrect. 
I think it should be: 
def parse(self, file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last: break
		self.handler.end('document')
]
