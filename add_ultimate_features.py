import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Injections for Ultimate Polish
css_ultimate = """
/* ══════════════════════════════════════════════
   ULTIMATE POLISH (Awwwards Level)
══════════════════════════════════════════════ */
/* Hero Text Shimmer */
.hero-name {
  background: linear-gradient(to right, #0F1D33 20%, #253F68 40%, #253F68 60%, #0F1D33 80%);
  background-size: 200% auto;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  animation: shine 4s linear infinite;
}
@keyframes shine {
  to { background-position: 200% center; }
}

/* Floating Ornaments */
.ornament { position: absolute; color: var(--gold-bdr2); pointer-events: none; z-index: 0; animation: floatObj 8s ease-in-out infinite; }
.orn-1 { top: 15%; left: 10%; font-size: 2.5rem; }
.orn-2 { top: 75%; left: 85%; font-size: 1.2rem; animation-delay: -2s; animation-duration: 10s; }
.orn-3 { top: 80%; left: 15%; font-size: 1.8rem; animation-delay: -4s; animation-duration: 7s; }
.orn-4 { top: 25%; left: 80%; font-size: 2rem; animation-delay: -6s; animation-duration: 9s; opacity: 0.5; }
@keyframes floatObj { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-30px) rotate(15deg); } }

/* Glow Cards */
.glow-element::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(24, 43, 73, 0.05), transparent 40%);
  opacity: 0; transition: opacity 0.5s; pointer-events: none; z-index: 0;
}
.glow-element:hover::after { opacity: 1; }
.card > *, .proj-card > *, .skill-card > *, .cert-card > *, .tl-body > *, .contact-card > * { position: relative; z-index: 1; }

/* Enhanced Nav Glassmorphism */
#nav {
  background: rgba(250, 246, 238, 0.5) !important;
  backdrop-filter: blur(24px) saturate(2) !important;
  -webkit-backdrop-filter: blur(24px) saturate(2) !important;
  border-bottom: none !important;
}
#nav::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(24, 43, 73, 0.15), transparent);
}

/* Better Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: rgba(24, 43, 73, 0.2); border-radius: 10px; border: 2px solid var(--bg); }
::-webkit-scrollbar-thumb:hover { background: rgba(24, 43, 73, 0.4); }

/* Selection */
::selection { background: rgba(24, 43, 73, 0.2); color: var(--gold-dk); }
"""
content = content.replace('</style>', css_ultimate + '\n</style>')

# 2. HTML Injections
html_ornaments = """
<div class="ornament orn-1">✦</div>
<div class="ornament orn-2">●</div>
<div class="ornament orn-3">▲</div>
<div class="ornament orn-4">✦</div>
"""
content = content.replace('<div class="hero-grid"></div>', '<div class="hero-grid"></div>\n  ' + html_ornaments)


# 3. JS Injections
js_ultimate = """
/* --- Glow Cards Effect --- */
const glowCards = document.querySelectorAll('.card, .proj-card, .skill-card, .cert-card, .tl-body, .contact-card, .stat-box');
glowCards.forEach(card => {
  card.classList.add('glow-element');
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty('--mouse-x', `${x}px`);
    card.style.setProperty('--mouse-y', `${y}px`);
  });
});

/* --- Hero Parallax & Reveal --- */
const heroInner = document.querySelector('.hero-inner');
const photoRing = document.querySelector('.photo-ring');
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  if(scrollY < window.innerHeight) {
    if(heroInner) heroInner.style.transform = `translateY(${scrollY * 0.2}px)`;
    if(photoRing) photoRing.style.transform = `translateY(${scrollY * 0.1}px)`;
  }
});

/* --- Image Reveal Parallax (Gallery) --- */
const galItems = document.querySelectorAll('.gal-item img');
const galObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      entry.target.style.transition = 'transform 1.5s cubic-bezier(0.16, 1, 0.3, 1)';
      entry.target.style.transform = 'scale(1)';
    } else {
      entry.target.style.transform = 'scale(1.15)';
    }
  });
}, { threshold: 0.1 });
galItems.forEach(img => {
  img.style.transform = 'scale(1.15)';
  img.style.transformOrigin = 'center';
  galObserver.observe(img);
});
"""
content = content.replace('</script>', js_ultimate + '\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ultimate features added successfully.")
