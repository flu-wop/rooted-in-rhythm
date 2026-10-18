#!/usr/bin/env python3
"""Generates the static site: python3 tools/build.py  ->  index.html, about.html, sponsor-us.html
Copy and links are from the live Squarespace site (rootedinrhythm.co); only layout/CSS is new."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONATE = 'https://www.paypal.com/donate/?hosted_button_id=C93SNBPCQ8GFW'
METER_DONATE = 'https://www.paypal.com/donate/?hosted_button_id=B4NMF6TV4ZBCL'
IG = 'https://www.instagram.com/rootedinrhythm.co/'
FB = 'https://www.facebook.com/rootedinrhythm.co'
SUBSTACK = 'https://substack.com/@rootedinrhythmco'
EMAIL = 'connect@rootedinrhythm.co'
BITS = 'https://bits-nola.vercel.app'

ICONS = {
 'ig': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-8h2.7l.4-3.200h-3.100V7.800c0-.9.3-1.500 1.600-1.500h1.700V3.400C16.500 3.300 15.500 3.200 14.400 3.200c-2.400 0-4 1.400-4 4.100v2.500H7.700V13h2.700v8z"/></svg>',
 'link': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M10 14a4 4 0 0 0 5.700 0l3-3a4 4 0 0 0-5.700-5.700l-1 1M14 10a4 4 0 0 0-5.700 0l-3 3a4 4 0 0 0 5.700 5.700l1-1"/></svg>',
}
def social(cls=''):
    return (f'<div class="social {cls}">'
            f'<a href="{IG}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{ICONS["ig"]}</a>'
            f'<a href="{FB}" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{ICONS["fb"]}</a>'
            f'<a href="{SUBSTACK}" target="_blank" rel="noopener noreferrer" aria-label="Newsletter">{ICONS["link"]}</a></div>')

WAVE_DOWN = lambda fill, bg: (f'<div class="wave" style="--wave-bg:{bg}" aria-hidden="true"><svg viewBox="0 0 1440 120" preserveAspectRatio="none">'
    f'<path fill="{fill}" d="M0,0 L1440,0 L1440,50 C1200,130 1000,0 720,55 C440,110 240,10 0,70 Z"/></svg></div>')

def head(title, page, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:site_name" content="Rooted In Rhythm">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="/img/logo.webp">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/img/logo.webp" type="image/webp">
<link rel="preload" href="/fonts/Bellefair-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">
</head>
<body data-page="{page}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="site-header__bar">
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" data-menu><span class="menu-btn__bars" aria-hidden="true"></span><span class="sr-only">Menu</span></button>
<nav class="site-nav" id="site-nav" aria-label="Main"><a href="/"{' aria-current="page"' if page=='home' else ''}>Home</a><a href="/about"{' aria-current="page"' if page=='about' else ''}>About</a><a href="/sponsor-us"{' aria-current="page"' if page=='sponsor' else ''}>Sponsor Us</a></nav>
<a class="brand" href="/"><img src="/img/logo.webp" width="84" height="75" alt="Rooted In Rhythm"></a>
<div class="site-header__right">{social('social--head')}<a class="btn btn--sm" href="{DONATE}" target="_blank" rel="noopener noreferrer">Donate</a></div>
</div>
</header>
<main id="main">
'''

def foot():
    return f'''</main>
<footer class="site-footer">
<div class="site-footer__inner">
{social('social--foot')}
<p class="site-footer__mail"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="site-footer__bits">A <a href="{BITS}" target="_blank" rel="noopener noreferrer">Breaks In The Simulation</a> initiative</p>
</div>
</footer>
<script src="/js/site.js" defer></script>
</body>
</html>
'''

def img(name, alt, w, h, cls='', lazy=True):
    return f'<img{" class=%s" % chr(34)+cls+chr(34) if cls else ""} src="/img/{name}.webp" width="{w}" height="{h}" alt="{alt}"{" loading=%slazy%s" % (chr(34),chr(34)) if lazy else ""}>'

def marquee(text, n=6):
    items = ''.join(f'<span>{text}</span><span class="dot" aria-hidden="true">&bull;</span>' for _ in range(n))
    return f'<div class="marquee" role="presentation"><div class="marquee__track" aria-hidden="true">{items}{items}</div><p class="sr-only">{text}</p></div>'

# ---------------------------------------------------------------- home
def home():
    # (file, alt, url, w, h, chip): chip = card colour that keeps the logo legible on teal
    sponsors = [('trunorth','TruNorth','https://www.trunorth.institute/',446,100,'dark'),
                ('virgin-abis','Virgin ABIS','https://www.virginabis.com/',600,600,'light'),
                ('viable','Viable Productions','https://www.viableproductions.co/',600,600,'light'),
                ('copalli','Copalli Rum','https://www.copallirum.com/',600,750,'light')]
    partners = [('ashe','The Ashe Company','https://theashecompany.org/',600,255,'dark'),
                ('elevatewi','ElevateWI','https://www.wielevate.org/',600,400,'dark')]
    lg = lambda items: ''.join(f'<li><a class="chip chip--{c}" href="{u}" target="_blank" rel="noopener noreferrer">{img(n,a,w,h)}</a></li>' for n,a,u,w,h,c in items)
    return head('Rooted In Rhythm','home','Rooted in Rhythm is a cultural exchange model connecting New Orleans and the Caribbean through artist collaboration, wellness and community.') + f'''
<section class="hero hero--home">
<img class="hero__img" src="/img/hero-home.webp" width="2000" height="1125" alt="" fetchpriority="high">
<div class="hero__shade"></div>
<div class="wrap"><h1 class="hero__mission">Rooted in Rhythm is a cultural exchange model that honors and strengthens the shared cultural heritage of New Orleans and the Caribbean by cultivating cross-regional artistic collaboration, embedding wellness-centered practices in creative development, and positioning cultural exchange as an activator for community healing and economic growth.</h1></div>
</section>
{WAVE_DOWN('#000','#000')}
<section class="band band--black event">
<div class="wrap event__grid">
<a class="event__flyer" href="https://www.eventbrite.com/e/wine-pon-mi-90s-lime-tickets-2000869875660?aff=ebdsoporgprofile" target="_blank" rel="noopener noreferrer">{img('wine-pon-mi','Wine Pon Mi 90’s Lime flyer: Saturday October 24, 2026, Waterfront, St. Thomas, U.S. Virgin Islands',1200,1200)}</a>
<div class="event__text">
<h2 class="display">Wine Pon Mi: 90’s Lime Coming Soon...</h2>
<p>St. Thomas, it’s been too long since we last had a good “Lime” like back in the day. Rooted In Rhythm is bringing that nostalgia back. This is more than just another event, this is a function for 80’s &amp; 90’s babies to indulge in the sounds, tastes, sights, textures, foods, libations, energy, and CULTURE that raised us.</p>
<p><a class="btn" href="https://www.eventbrite.com/e/wine-pon-mi-90s-lime-tickets-2000869875660?aff=ebdsoporgprofile" target="_blank" rel="noopener noreferrer">Get your tickets here</a></p>
</div>
</div>
</section>
<section class="band band--black launch">
<div class="wrap">
<div class="launch__head">
<p class="script">Thank you for joining us at our</p>
<h2 class="display">From Congo Square to the Caribbean</h2>
<p class="script script--accent">Launch Party <span class="tag">In New Orleans</span></p>
<p class="launch__copy">Rooted in Rhythm and our partners presented a collaborative initiative: From Congo Square to the Caribbean. This cultural exchange artist residency connects artists of the African diaspora from New Orleans, the U.S. Virgin Islands, and Jamaica through creativity, wellness, and participation in community-led climate initiatives.</p>
</div>
<div class="gallery">
<figure class="g g--a">{img('dominoes','Hands playing dominoes at the launch party',1200,1800)}</figure>
<figure class="g g--b">{img('congo-flyer','From Congo Square to the Caribbean launch party flyer',700,906)}</figure>
<figure class="g g--c">{img('dancing','Guests dancing at the launch party, seen from above',1200,1800)}</figure>
<figure class="g g--d">{img('stilts','A stilt walker and guests at the launch party',853,1280)}</figure>
<figure class="g g--e">{img('band','A brass band performing at the launch party',1400,934)}</figure>
</div>
</div>
</section>
<section class="band band--black news">
<div class="wrap wrap--narrow center">
<h2 class="display">Subscribe To Our Newsletter!</h2>
<p><a class="btn btn--lg" href="{SUBSTACK}" target="_blank" rel="noopener noreferrer">Subscribe</a></p>
</div>
</section>
<div class="wave wave--up" style="--wave-bg:#000" aria-hidden="true"><svg viewBox="0 0 1440 120" preserveAspectRatio="none"><path fill="#34dad2" d="M0,120 L1440,120 L1440,70 C1200,-10 1000,120 720,65 C440,10 240,110 0,50 Z"/></svg></div>
<section class="band band--teal partners">
<div class="wrap">
<h2 class="display display--accent center">In Partnership With</h2>
<ul class="logos logos--partners">{lg(partners)}</ul>
<div class="meter">
{img('support-meter','Support meter: fundraising goal of $25,000',700,875)}
<div class="meter__cta"><p>Help us reach our goal.</p><a class="btn btn--dark" href="{METER_DONATE}" target="_blank" rel="noopener noreferrer">Donate</a></div>
</div>
</div>
</section>
<section class="band band--teal sponsors">
{marquee('Huge Thanks to our Seed Sponsors')}
<div class="wrap">
<ul class="logos logos--sponsors">{lg(sponsors)}</ul>
<p class="center"><a class="btn btn--dark" href="{DONATE}" target="_blank" rel="noopener noreferrer">Donate</a></p>
</div>
</section>
''' + foot()

# ---------------------------------------------------------------- about
def about():
    return head('About - Rooted In Rhythm','about','Rooted in Rhythm began with a conversation between two Caribbean-rooted women building lives and creative communities in New Orleans.') + f'''
<section class="hero hero--page hero--about">
<img class="hero__img" src="/img/hero-about.webp" width="1200" height="1600" alt="" fetchpriority="high">
<div class="hero__shade hero__shade--bottom"></div>
<div class="wrap"><h1 class="hero__title">Rooted In Culture, Rising In Rhythm.</h1></div>
</section>
<section class="band band--teal about">
<div class="wrap">
<p class="lead lead--accent center">Rooted in Rhythm began with a conversation between two Caribbean-rooted women building lives and creative communities in New Orleans. What started as a shared vision grew into a platform for cultural exchange, artistic development, and collective healing across the African diaspora.</p>
<article class="bio">
<figure>{img('nikki','Nikki Fernandes',900,1180)}</figure>
<div>
<h2 class="display">Nikki Fernandes</h2>
<p>Co-founder <strong>Nikki Fernandes</strong> was raised on the island of St. Thomas, where the rhythms of community, resilience, and cultural heritage shaped her understanding of healing. Growing up in a small island territory facing environmental and economic challenges sparked her lifelong commitment to systems that support community resilience and equity. Nikki earned her B.A. in Medical Anthropology from the University of North Carolina at Chapel Hill and her Master of Public Health in International Health and Development from the Tulane University School of Public Health and Tropical Medicine. Her work bridges public health, culture, and systems change, grounded in a belief that grassroots communities should lead the solutions that shape their futures.</p>
<p>For Nikki, culture is more than expression—it is infrastructure. Music, storytelling, and artistic practice are powerful tools for healing, economic opportunity, and community resilience. Rooted in Rhythm reflects her passion for building spaces where artists of the African diaspora can create, connect, and thrive while prioritizing holistic wellness and joy.</p>
</div>
</article>
<article class="bio bio--flip">
<figure>{img('raquel','Raquel Haupt, also known as Rocky Raine',900,1090)}</figure>
<div>
<h2 class="display">Raquel Haupt</h2>
<p>Co-founder, <strong>Raquel Haupt</strong>, creatively known as Rocky Raine, is a Jamaican-American artist and Founder of a New Orleans-based creative agency, Breaks In The Simulation, dedicated to the sustainable development of emerging creatives and the ecosystems around them. With a B.S. in Psychology, an upbringing in performance arts, and a deep commitment to mental health and holistic wellness, Raquel brings years of experience as an international cultural curator and producer. She has aided in creating cultural exchange festivals and platforms for artists around the world—from South Africa to London, Paris, Atlanta, and New Orleans—through global initiatives including Milk + Cookies Music Week and Black Everywhere. With a multidisciplinary approach to creativity, connection, and education, Raquel has dedicated her career to breaking the pattern and building the artist.</p>
</div>
</article>
<div class="closing center">
<p class="lead lead--accent">The two connected through their shared Caribbean heritage, their love for New Orleans, and a shared understanding that artists need more than stage: they need support systems.</p>
<p class="lead lead--accent">Rooted in Rhythm was created to build that infrastructure.</p>
<p class="lead lead--accent">We envision a thriving creative economy where the cultural legacy of the African diaspora fuels social impact, equitable tourism, and climate resilience. By connecting New Orleans with the Caribbean and beyond, we support artists in preserving heritage, prioritizing wellness, and leading culture-driven transformation.</p>
<p class="lead lead--accent">Because when artists are supported, culture thrives.<br>And when culture thrives, communities heal.</p>
</div>
</div>
</section>
''' + foot()

# ---------------------------------------------------------------- sponsor
TIERS = [
 ('tier-1','FOR DEH CULTURE','$25,000','list',['Prominent logo placement on event materials with Presenting Sponsor recognition','Full page event program feature','Private cultural immersion activities and dinner with the Caribbean delegation','Inclusion in post event storytelling contents credits as Presenting Sponsor','Branded visual content from the event','Recognition in newsletters, website, and social media campaigns pre and post event on ElevateWi and Rooted in Rhythm platforms','Verbal acknowledgement during the event']),
 ('tier-2','THREE QUEENS','$10,000','list',['Recognition attached to the ElevateWi delegation travel from USVI','Featured in post event storytelling content','Half page program feature','Inclusion in documentary credits as Three Queens Sponsor','Artist and partner meet and greet','Verbal acknowledgement during the event']),
 ('tier-3','FIREBURN','$5,000','list',['Logo on event materials and website','Social media recognition','Opportunity to display promotional materials at events','Name listed in event program as Fireburn Sponsor','Name listed in documentary credits','Verbal acknowledgement during event']),
 ('tier-4','GONE TO COME BACK','$2,500','list',['Logo listed on website and event program as sponsor','Social media shout-out','Opportunity to display promotional materials at event','Name listed in documentary credits']),
 ('tier-5','MELEE','$1,000','list',['Name listed on website and event program as sponsor','Social media thank you','Opportunity to display promotional materials at events']),
]
def sponsor():
    rows = ''.join(
        f'<article class="tier"><figure>{img(i,t.title()+" sponsorship tier",700,700)}</figure>'
        f'<div><h3 class="display tier__name">{t}</h3><p class="tier__price">{p}</p><ul class="ticks">{"".join(f"<li>{x}</li>" for x in b)}</ul></div></article>'
        for i,t,p,_,b in TIERS)
    return head('Sponsor Us - Rooted In Rhythm','sponsor','Explore our range of Sponsorship Packages designed to help you support our cause with ease, no matter your budget.') + f'''
<section class="hero hero--page hero--sponsor">
<img class="hero__img" src="/img/hero-sponsor.webp" width="2000" height="1125" alt="" fetchpriority="high">
<div class="hero__shade hero__shade--left"></div>
<div class="wrap hero__copy"><h1 class="hero__title">Explore Our Sponsorship Packages</h1><p class="hero__sub">Explore our range of Sponsorship Packages designed to help you support our cause with ease, no matter your budget.</p></div>
</section>
<section class="band band--teal sponsor">
{marquee('Become a Sponsor')}
<div class="wrap">
<h2 class="display center">Our Sponsorship Packages</h2>
<div class="tiers">
{rows}
<article class="tier tier--last"><figure>{img('tier-6','In kind sponsorship',700,700)}</figure>
<div><h3 class="display tier__name">BUILD YOUR OWN &amp; IN KIND</h3><p class="tier__price">Contribution: Varies based on Value</p><p class="tier__note">*Benefits will align with the value of the In Kind Donations / Custom Created Sponsorship Package.</p></div></article>
</div>
<p class="center"><a class="btn btn--lg btn--dark" href="{DONATE}" target="_blank" rel="noopener noreferrer">Sponsor Us</a></p>
</div>
</section>
''' + foot()

def main():
    for name, fn in (('index', home), ('about', about), ('sponsor-us', sponsor)):
        open(f'{ROOT}/{name}.html', 'w').write(fn())
    print('built 3 pages')
main()
