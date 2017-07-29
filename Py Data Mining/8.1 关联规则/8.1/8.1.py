# -*- coding: utf-8 -*-

import pandas
from apyori import apriori

data = pandas.read_csv('D:\\PDM\\8.1\\data.csv')

transactions = data.groupby(by='交易ID').apply(
    lambda x: list(x.购买商品)
).values

#min_support -- The minimum support of relations (float).
#min_confidence -- The minimum confidence of relations (float).
#min_lift -- The minimum lift of relations (float).
#max_length
results = list(
    apriori(
        transactions
    )
)

#支持度（support）
supports = [];
#自信度（confidence）
confidences = []
#提升度（lift）
lifts = []
#基于项items_base
bases = []
#推导项items_add
adds = []
for r in results:
    supports.append(r.support)
    confidences.append(r.ordered_statistics[0].confidence)
    lifts.append(r.ordered_statistics[0].lift)
    bases.append(list(r.ordered_statistics[0].items_base))
    adds.append(list(r.ordered_statistics[0].items_add))

result = pandas.DataFrame({
    'support': supports,
    'confidence': confidences,
    'lift': lifts,
    'base': bases,
    'add': adds
})


r = result[(result.lift>1) & (result.support>0.5) & (result.confidence>0.5)]
