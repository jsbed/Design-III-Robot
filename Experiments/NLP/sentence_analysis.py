from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql1.fcfg')
#query = 'What cities are located in China'
query = 'What cities have populations above 1,000,000'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)