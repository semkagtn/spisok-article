import os
from collections import Counter
from pylab import pie, savefig, figure, setp
from matplotlib import font_manager as fm


dataset_dir = 'dataset'
gender_train_file = os.path.join(dataset_dir, 'train-gender.csv')
gender_test_file = os.path.join(dataset_dir, 'test-gender.csv')

with open(gender_train_file) as f:
    gender_train_counter = Counter(f.read().splitlines()[1:])
with open(gender_test_file) as f:
    gender_test_counter = Counter(f.read().splitlines()[1:])
counter = gender_train_counter + gender_test_counter

labels = 'Мужчины', 'Женщины'
fracs = [counter['0'], counter['1']]
colors = ['white', 'grey']
figure(1, figsize=(6, 6))
_, texts, autotexts = pie(fracs, labels=labels, colors=colors,
        shadow=False, startangle=150, autopct='%1.1f%%')

text_props = fm.FontProperties()
text_props.set_size(18)
text_props.set_family('serif')
autotext_props = fm.FontProperties()
autotext_props.set_size(18)
text_props.set_family('serif')

setp(texts, fontproperties=text_props)
setp(autotexts, fontproperties=autotext_props)
savefig('gender-pie.pdf', bbox_inches='tight')

