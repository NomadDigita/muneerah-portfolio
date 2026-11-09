"""Build four ATS-readable, single-column PDFs from documented source material.
No portrait is embedded, since many international applicant-tracking systems prefer a clean text résumé.
To set the published portfolio URL, use PORTFOLIO_URL env var after verifying deployment.
"""
from pathlib import Path
from os import getenv
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

P=Path(__file__).resolve().parent; out=P/'assets'; out.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('Lato','/usr/share/fonts/truetype/lato/Lato-Regular.ttf'))
pdfmetrics.registerFont(TTFont('LatoBold','/usr/share/fonts/truetype/lato/Lato-Bold.ttf'))
W,H=595.276,841.89; L=49; R=49; WIDTH=W-L-R
ink=HexColor('#172820'); subdued=HexColor('#506258'); accent=HexColor('#2e6d53'); light=HexColor('#dce5df')
PORTFOLIO_URL=getenv('PORTFOLIO_URL','https://muneerah-cv.vercel.app').strip().rstrip('/')

ROLES=[
 ('General','Muneerah-Muhammad-Thalith-Resume.pdf','Digital Marketing | Community Operations | Customer Experience',
  'Digital marketer and independent community builder with practical experience promoting learning products, engaging prospects and guiding online audiences. Recognized by LearnerFlex as its top affiliate for March 2026, with 600+ sales reported during that month. Interested in remote community, marketing, and customer-facing roles.',
  ['Community engagement and onboarding','Customer enquiries and written support','Telegram and WhatsApp group coordination','Digital marketing and affiliate campaigns','Audience acquisition and follow-up','Clear product explanations and education'],
  ['Promoted digital education products using community engagement, product explanations and prospect follow-up.','Earned No. 1 LearnerFlex affiliate recognition for March 2026; its announcement reported 600+ sales that month.','Account dashboard screenshot displays 1,799 cumulative affiliate sales as of capture; period is distinct from March figures.'],
  ['Supported independent online learning communities by communicating updates, answering questions and assisting new members.','Supplied screenshots show a Telegram group with 1,261 members and a separate channel with 2,251 subscribers.','Provided beginner-friendly digital marketing guidance and encouraged participation in group discussions.']),
 ('Community','Muneerah-Community-Moderator-Resume.pdf','Community Management | Telegram & WhatsApp | User Engagement',
  'Community-focused professional experienced in supporting Telegram and WhatsApp groups, welcoming newcomers and keeping members informed. Combines practical audience growth experience with clear communication and customer-facing campaign work. Seeking community associate, moderator, or engagement coordinator opportunities.',
  ['Telegram and WhatsApp group operations','Community announcements and engagement','New-member onboarding and guidance','Responding to member enquiries','Community-oriented campaign promotion','Audience feedback and communication'],
  ['Used audience conversations and practical explanations to promote education products and nurture interest.','Ranked No. 1 LearnerFlex affiliate for March 2026, when over 600 sales were publicly reported.','Supported follow-up conversations with prospective customers and learners.'],
  ['Helped manage member communications, posts and guidance in independent Telegram/WhatsApp communities.','Documented community snapshots: 1,261 Telegram group members and 2,251 subscribers in a separate channel.','Helped new members understand learning resources and encouraged constructive questions.']),
 ('Customer Support','Muneerah-Customer-Support-Resume.pdf','Customer Communication | Learner Support | Onboarding',
  'Customer-facing digital marketer and community organizer experienced in explaining products, responding to questions and guiding people through online learning communities. Brings patient written communication, attention to user needs and practical follow-up experience. Seeking remote customer support and community support positions.',
  ['Written support and customer enquiries','Product explanation and onboarding','Telegram and WhatsApp communication','Member guidance and issue triage','Clear written messages and follow-up','Audience feedback and relationship-building'],
  ['Explained digital learning offers, answered questions and helped interested buyers understand next steps.','Contributed to a campaign recognized by LearnerFlex as No. 1 for March 2026, with 600+ reported sales.','Maintained audience communication throughout promotion and purchasing decisions.'],
  ['Helped newcomers navigate digital learning materials and online group information.','Coordinated community announcements and answered everyday member questions in Telegram/WhatsApp groups.','Worked with communities whose captured audiences included a 1,261-member group and a separate 2,251-subscriber channel.']),
 ('Marketing','Muneerah-Marketing-Resume.pdf','Digital Marketing | Affiliate Campaigns | Audience Growth',
  'Results-oriented independent digital marketer with practical experience in affiliate campaign execution, online prospect engagement and community-driven product promotion. Recognized as LearnerFlex No. 1 affiliate in March 2026, with more than 600 sales reported that month; a separate account snapshot shows 1,799 cumulative sales. Seeking growth and marketing opportunities.',
  ['Affiliate and digital marketing campaigns','Community-led prospect acquisition','Marketing copy and product positioning','Customer conversations and conversions','Telegram/WhatsApp channel engagement','Campaign communication and follow-up'],
  ['Promoted digital education offers through targeted audience engagement, consistent messaging and prospect follow-up.','Received LearnerFlex No. 1 affiliate award for March 2026; LearnerFlex recognition reported 600+ sales that month.','Separate affiliate dashboard snapshot recorded 1,799 cumulative sales at the time captured.'],
  ['Developed and engaged audiences through Telegram/WhatsApp learning and digital-marketing communities.','Community screenshots document a 1,261-member Telegram group and separate channel of 2,251 subscribers.','Helped community members learn digital marketing concepts and make informed product decisions.'])
]

def make(config):
 _, filename, headline, summary, skills, campaign, community=config
 C=canvas.Canvas(str(out/filename),pagesize=(W,H));C.setTitle(f'Muneerah Muhammad Thalith - {headline} Resume');C.setAuthor('Muneerah Muhammad Thalith')
 def write(text,x,y,size=10,bold=False,color=ink):
  C.setFillColor(color);C.setFont('LatoBold' if bold else 'Lato',size);C.drawString(x,y,text)
 def flow(s,x,y,width,sz=9.9,leading=14.4,color=subdued,bold=False):
  font='LatoBold' if bold else 'Lato'
  for line in simpleSplit(s,font,sz,width):write(line,x,y,sz,bold,color);y-=leading
  return y
 def rule(y):C.setLineWidth(.65);C.setStrokeColor(light);C.line(L,y,W-R,y)
 def section(label,y):
  write(label.upper(),L,y,9.2,True,accent);rule(y-10);return y-32
 def bullets(lines,y,sz=9.5):
  for item in lines:
   C.setFillColor(accent);C.circle(L+3,y+3,2,fill=1,stroke=0)
   y=flow(item,L+13,y,WIDTH-15,sz,13.8)-4
  return y
 def line_text(lines,y):
  for s in lines:y=flow(s,L,y,WIDTH,9.4,13.4)-4
  return y
 # clean and machine-readable: no text converted to outlines, no photos/columns
 C.setFillColor(HexColor('#f0f5f1'));C.rect(0,H-147,W,147,stroke=0,fill=1)
 C.setFillColor(accent);C.rect(L,H-118,4,70,fill=1,stroke=0)
 write('MUNEERAH MUHAMMAD THALITH',L+18,H-64,19.6,True)
 y=flow(headline,L+18,H-84,WIDTH-18,10.2,14,accent,True)
 contact='Nigeria | +234 704 900 1254 | contact@muneerah.page'
 write(contact,L+18,H-112,9.1,False,subdued)
 write('Telegram @DNeerah | X @Dneerah_ | muneerah-cv.vercel.app',L+18,H-128,8.5,False,subdued)
 C.linkURL('mailto:contact@muneerah.page', (L+230,H-120,W-R,H-98), relative=0)
 y=H-170
 y=section('Professional profile',y)
 y=flow(summary,L,y,WIDTH,10.1,14.5)-13
 y=section('Experience',y)
 write('Independent Digital Marketer & Affiliate Campaign Operator',L,y,10.8,True)
 y-=16
 write('Independent project-based work / LearnerFlex affiliate activity | 2025-2026*',L,y,9.1,False,accent);y-=24
 y=bullets(campaign,y);y-=12
 write('Community Organizer & Learner Support',L,y,10.8,True);y-=16
 write('Independent Telegram and WhatsApp communities | 2025-2026*',L,y,9.1,False,accent);y-=24
 y=bullets(community,y);y-=8
 y=section('Relevant capabilities',y)
 y=line_text([skills[i]+'   |   '+skills[i+1] for i in range(0,len(skills),2)],y)
 y-=5
 y=section('Recognition and portfolio',y)
 y=flow('LearnerFlex Top Affiliate - March 2026. Award and supporting screenshots available on request.',L,y,WIDTH,9.5,13.5,ink)
 if PORTFOLIO_URL:
  y-=3
  write('Portfolio: '+PORTFOLIO_URL,L,y,9.6,False,accent)
  C.linkURL(PORTFOLIO_URL,(L,y-4,W-R,y+10),relative=0);y-=16
 y-=4
 rule(66)
 yfoot=52
 yfoot=flow('* Years reflect approximate project activity. Performance figures are based on supplied awards, social posts and account screenshots; figures refer to distinct periods.',L,yfoot,WIDTH,7.7,10,subdued)
 if y<86: print('WARNING possible footer overflow',filename,y)
 C.showPage();C.save()
 print('Created',out/filename,'end y',round(y,1))
for role in ROLES:make(role)
