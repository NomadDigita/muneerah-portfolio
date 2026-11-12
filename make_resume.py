"""Produce four professional, ATS-friendly one-page PDF resumes.
All work is described accurately as independent activity; numbers match the awards and dashboards.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

P=Path(__file__).resolve().parent
OUT=P/'assets';OUT.mkdir(exist_ok=True)
FONT='/usr/share/fonts/truetype/lato/'
pdfmetrics.registerFont(TTFont('Lato',FONT+'Lato-Regular.ttf'))
pdfmetrics.registerFont(TTFont('LatoBold',FONT+'Lato-Bold.ttf'))
pdfmetrics.registerFont(TTFont('LatoBlack',FONT+'Lato-Heavy.ttf'))
W,H=595.28,841.89
L,R=47,48
CW=W-L-R
INK=HexColor('#172722')
GREEN=HexColor('#266a51')
MUTED=HexColor('#465850')
PALE=HexColor('#d5e2da')

DATA=[
 dict(file='Muneerah-Muhammad-Thalith-Resume.pdf',role='Digital Marketer | Community Manager | Customer Experience',
 summary='Digital marketer with experience since December 2023 driving affiliate sales, growing Telegram communities and supporting online learners. I combine practical audience engagement, clear communication and campaign execution to turn interest into lasting relationships.',
 campaign=['Achieved LearnerFlex No. 1 affiliate ranking in March 2026 with more than 600 sales that month.','Placed second in the January–April 2026 sales challenge, achieving 1,458 sales.','Promoted digital learning products through audience education, prospect engagement and consistent follow-up.'],
 community=['Built and managed Telegram learning communities, including a 2,175-member group and a channel with 2,251 subscribers.','Organized updates, welcomed members, answered questions and supported learner onboarding.'],
 skills=['Digital marketing  •  Affiliate campaigns  •  Audience engagement  •  Community moderation','Telegram & WhatsApp  •  Customer communication  •  Member onboarding  •  Social media']),
 dict(file='Muneerah-Community-Moderator-Resume.pdf',role='Community Manager | Telegram Moderator | Member Engagement',
 summary='Community builder with digital marketing experience since December 2023, growing and managing Telegram and WhatsApp learning spaces. Skilled in welcoming new members, moderating conversations, communicating updates and building consistent participation across online communities.',
 campaign=['Used community-led marketing, product education and direct conversations to support high-performing affiliate campaigns.','Earned LearnerFlex No. 1 affiliate ranking in March 2026 with 600+ sales.','Placed second in a January–April 2026 sales challenge with 1,458 sales.'],
 community=['Built and supported a 2,175-member REAMB learning group and 2,251-subscriber Telegram channel.','Organized member guidance and announcements, answered everyday questions and encouraged healthy engagement.','Helped newcomers understand digital marketing tools, learning resources and next steps.'],
 skills=['Telegram & WhatsApp  •  Community moderation  •  Member onboarding  •  Engagement','Announcements  •  Customer enquiries  •  Online events & learning  •  Communication']),
 dict(file='Muneerah-Customer-Support-Resume.pdf',role='Customer Support | Community Support | Onboarding',
 summary='Customer-focused digital marketing and community professional, active since December 2023, experienced in responding to questions, explaining digital products and helping online learners take their next steps. I bring patient written communication, attentive follow-up and a clear, practical approach to member support.',
 campaign=['Explained educational product offers, guided interested customers and followed up on questions.','Supported affiliate campaigns that earned LearnerFlex No. 1 ranking in March 2026 with 600+ sales.','Used clear, accessible product guidance to help prospective customers make informed decisions.'],
 community=['Supported Telegram and WhatsApp audiences, including a 2,175-member group and 2,251-subscriber channel.','Welcomed learners, communicated announcements and addressed everyday member enquiries.','Provided beginner-friendly help with digital learning materials and online community resources.'],
 skills=['Customer communication  •  Written support  •  Onboarding  •  Troubleshooting guidance','Telegram & WhatsApp  •  Member assistance  •  Follow-up  •  Product education']),
 dict(file='Muneerah-Marketing-Resume.pdf',role='Digital Marketing | Affiliate Sales | Community Growth',
 summary='Performance-driven digital marketer with experience since December 2023 promoting digital education products, engaging prospects and converting audience interest into sales. Recognized for strong LearnerFlex affiliate results and the ability to grow engaged online communities.',
 campaign=['Ranked No. 1 on LearnerFlex for March 2026, generating 600+ affiliate sales during the month.','Won second place in the January–April 2026 sales challenge with 1,458 sales.','Reached 1,799 recorded affiliate sales on a LearnerFlex account dashboard; promoted offers through consistent audience engagement and follow-up.'],
 community=['Built and engaged Telegram learning groups and channels, including a 2,175-member group and 2,251-subscriber channel.','Created product education conversations and encouraged ongoing participation around learning resources.'],
 skills=['Affiliate marketing  •  Lead generation  •  Audience growth  •  Campaign execution','Community-led acquisition  •  Content promotion  •  Customer follow-up  •  Social media'])
]

def render(d):
 path=OUT/d['file'];c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
 c.setTitle('Muneerah Muhammad Thalith | '+d['role'])
 c.setAuthor('Muneerah Muhammad Thalith')
 y=H-42
 def t(x,y,text,size=10,font='Lato',color=INK):
  c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,text)
 def wrap(text,x,y,size=10,leading=14,color=MUTED,font='Lato',width=CW):
  lines=simpleSplit(text,font,size,width)
  for line in lines:
   t(x,y,line,size,font,color);y-=leading
  return y
 def line(y):
  c.setStrokeColor(PALE);c.setLineWidth(.65);c.line(L,y,W-R,y)
 def heading(title,y):
  y-=18
  t(L,y,title.upper(),9.25,'LatoBlack',GREEN)
  y-=10;line(y)
  return y-21
 def bullet_list(items,y):
  for item in items:
   c.setFillColor(GREEN);c.circle(L+4,y+3,2.2,stroke=0,fill=1)
   y=wrap(item,L+16,y,size=9.75,leading=14.4,width=CW-16)-4.4
  return y
 # Brand rule and name, but no large banner or bottom fine print.
 c.setStrokeColor(GREEN);c.setLineWidth(3);c.line(L,H-24,W-R,H-24)
 t(L,y,'MUNEERAH MUHAMMAD THALITH',21.5,'LatoBlack',INK)
 y-=23
 t(L,y,d['role'],10.9,'LatoBold',GREEN)
 y-=22
 t(L,y,'Nigeria  |  +234 704 900 1254  |  contact@muneerah.top',9.4,'Lato',MUTED)
 y-=16
 t(L,y,'muneerah-portfolio-git.vercel.app  |  X: @Dneerah_  |  Telegram: @DNeerah',9.05,'Lato',MUTED)
 c.linkURL('https://muneerah-portfolio-git.vercel.app',(L,y-3,L+235,y+11),relative=0)
 c.linkURL('mailto:contact@muneerah.top',(L+194,y+16,L+335,y+31),relative=0)
 y=heading('Professional summary',y)
 y=wrap(d['summary'],L,y,size=10.15,leading=15.2,color=INK)-6
 y=heading('Platform experience',y)
 t(L,y,'Digital marketing & affiliate projects  |  Started 3 Dec 2023',10.7,'LatoBold',INK)
 y-=20
 platforms=[
  ('LearnerFlex','Jun 2025 - May 2026','Affiliate campaigns & customer engagement'),
  ('Selar','Jan 2025 - Jun 2025','Digital-product marketing'),
  ('ZenithStake','Dec 2024 - May 2025','Affiliate & audience marketing'),
  ('Digitstem','Jan 2024 - Nov 2024','Digital marketing & outreach'),
 ]
 for company,period,activity in platforms:
  t(L+1,y,company,9.85,'LatoBold',INK)
  c.setFont('LatoBold',8.8);c.setFillColor(GREEN)
  c.drawRightString(W-R,y,period)
  y-=13.3
  t(L+1,y,activity,9.05,'Lato',MUTED)
  y-=20
 y=heading('Campaign achievements',y)
 y=bullet_list(d['campaign'][:2],y)
 y=heading('Community & customer support',y)
 y=bullet_list(d['community'][:2],y)
 y=heading('Awards & recognition',y)
 y=wrap('LearnerFlex Top Affiliate — March 2026 (#1; 600+ sales).  Sales Challenge Runner-up — January–April 2026 (#2; 1,458 sales).',L,y,size=9.75,leading=14.8,color=INK)-5
 y=heading('Core skills',y)
 for skillline in d['skills']:
  y=wrap(skillline,L,y,size=9.5,leading=14.4,color=MUTED)-5
 # Single-page body ends well above bottom; no misleading audit disclaimer or footnote.
 if y<47: raise RuntimeError(f'Resume overflow ({d["file"]}, y={y})')
 c.showPage();c.save()
 print('Created',path.name,'remaining blank',round(y,1))
for data in DATA:render(data)
