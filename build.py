import json
L=[l.split('|') for l in open('carriers.txt').read().split('\n')]
li=''.join(f'<li><img src="logos/{f}.webp" alt="{n}" loading="lazy" decoding="async"></li>' for f,n in L)
mq=f'<ul class="mtrack">{li}</ul><ul class="mtrack" aria-hidden="true">{li}</ul>'
S=[("auto","🚗","Auto Insurance","We know that accidents happen, but with our comprehensive coverage, you can rest easy knowing that you and your vehicle are protected.","auto","Auto"),
("home","🏠","Home Insurance","With home insurance, you can have peace of mind knowing that your property and belongings are covered in case of unexpected occurrences.","home","Home"),
("life","❤️","Life Insurance","Don’t wait until it’s too late – invest in our life insurance service today and enjoy the security of knowing that your family’s protected.","family","Life"),
("business","🏢","Business Insurance","Our business insurance service offers comprehensive coverage for businesses of all sizes.","business","Business"),
("wc","🦺","Workers Comp","Protect your employees & business today in the event of an employee’s on-the-job injury or illness.","flood","Workers Comp"),
("bond","⚖️","Court Bond Insurance","All types of court bonds; Probate / Administrator, Guardian, Trustee, Committee. As well as Attachment, Injunction, Replevin and Receiver.","sign","Court Bond"),
("ltc","🤝","Long-Term Care","Start living comfortably in your own home today with the proper care that you need.","care","Long-Term Care")]
cov={k:(t,i,d,s) for k,i,t,d,_,s in S}
tabs=''.join(f'<button role="tab" data-k="{k}" aria-selected="{"true" if n==0 else "false"}"><span class="ic">{i}</span>{s}</button>' for n,(k,i,t,d,_,s) in enumerate(S))
svc=''
for n,(k,i,t,d,img,s) in enumerate(S):
    if k=='wc': svc+=f'<a class="svc rv dark" href="#quote" data-k="{k}"><div class="tx"><span style="font-size:34px">{i}</span><h3 style="margin-top:12px">{t}</h3><p>{d}</p><span class="more">Get a quote →</span></div></a>';continue
    if k=='bond': svc+=f'<a class="svc rv dark" href="#quote" data-k="{k}"><div class="tx"><span style="font-size:34px">{i}</span><h3 style="margin-top:12px">{t}</h3><p>{d}</p><span class="more">Get a quote →</span></div></a>';continue
    svc+=f'<a class="svc rv{" wide" if k=="ltc" else ""}" href="#quote" data-k="{k}"><div class="ph"><img src="img/{img}.webp" alt="" loading="lazy"></div><div class="tx"><h3>{t}</h3><p>{d}</p><span class="more">Get a quote →</span></div></a>'
T=[("jay","Jay"),("ron","Ron"),("frank","Frank"),("ann-marie","Ann Marie")]
team=''.join(f'<div class="tm rv"><div class="pi"><img src="img/{f}.webp" alt="{n}" loading="lazy"></div><h3>{n}</h3><span class="ph-t">Placeholder: title</span></div>' for f,n in T)
R=[("Virginia W.","The Benson Thomson agency is a joy to work with. They are knowledgeable, efficient and offer practical information."),
("John D.","Benson Thomson Agency is a business that operates with honesty and integrity. Jay gives you the pluses and minuses of your options without pressure tactics. This is the place to go for your insurance needs."),
("Greg G.","Go in speak with Jay. He is one of the good guys!!"),
("Edward R.","Great prices, great service and super helpful. Been doing business with for many years and staff is very helpful. Highly rated."),
("Steve W.","Benson Thomson Agency is knowledgeable and responsive to your needs."),
("Steve W.","Jay is knowledgeable and responsive to your needs")]
rev=''.join(f'<figure class="rc rv"><q>{q}</q><cite>— {n}</cite></figure>' for i,(n,q) in enumerate(R))
h=open('tpl.html').read()
for a,b in [('%MQ%',mq),('%TABS%',tabs),('%COV%',json.dumps(cov,ensure_ascii=False)),('%SVC%',svc),('%TEAM%',team),('%REV%',rev)]: h=h.replace(a,b)
open('index.html','w').write(h)
