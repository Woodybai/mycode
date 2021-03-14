import matplotlib.pyplot as plt
 

reciepe= ["480g Flour", "50g Eggs", "90g Sugar"]
amt=[int(x.split('g ')[0]) for x in reciepe]
ing=[x.split()[-1] for x in reciepe]
fig, ax=plt.subplots(figsize=(5,5), subplot_kw=dict(aspect='equal'))
wadges, text, autotext=ax.pie(amt, labels=ing, startangle=90,
                              autopct=lambda p:"{:.0f}g\n({:.1f})%".format(p*sum(amt)/100, p),
                              textprops=dict(color='k', weight='bold', fontsize=8))
ax.legend(wadges, ing,title='Ingredents', loc='best', bbox_to_anchor=(0.35,0.85,0,0))
