import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Injections
css_injection = """
/* ══════════════════════════════════════════════
   ELITE EFFECTS
══════════════════════════════════════════════ */
/* Custom Cursor */
body { cursor: none; }
#cursor { position: fixed; top: 0; left: 0; width: 8px; height: 8px; background: var(--gold); border-radius: 50%; pointer-events: none; z-index: 9999; transform: translate(-50%, -50%); transition: width 0.2s ease, height 0.2s ease, background 0.2s ease; mix-blend-mode: difference; }
#cursor-follower { position: fixed; top: 0; left: 0; width: 40px; height: 40px; border: 1px solid var(--gold-bdr); border-radius: 50%; pointer-events: none; z-index: 9998; transform: translate(-50%, -50%); transition: opacity 0.2s ease; }
a, button { cursor: none; }

/* Loader */
#loader { position: fixed; inset: 0; background: var(--bg); z-index: 10000; display: flex; align-items: center; justify-content: center; transition: opacity 0.8s var(--ease2), visibility 0.8s; }
.loader-text { font-family: var(--mono); font-size: 0.8rem; font-weight: 600; letter-spacing: 0.3em; color: var(--gold-dk); text-transform: uppercase; position: relative; overflow: hidden; }
.loader-text::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: var(--bg); transform: translateX(-100%); animation: loadSweep 1s var(--ease2) forwards 0.2s; }
@keyframes loadSweep { 0% { transform: translateX(0); } 100% { transform: translateX(101%); } }
body.loaded #loader { opacity: 0; visibility: hidden; }

/* Canvas Particles */
#particles-js { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; opacity: 0.8; }

/* Marquee */
.marquee-wrap { width: 100%; overflow: hidden; background: var(--surf2); border-top: 1px solid var(--gold-bdr2); border-bottom: 1px solid var(--gold-bdr2); padding: 18px 0; display: flex; white-space: nowrap; position: relative; }
.marquee-inner { display: inline-flex; animation: marquee 30s linear infinite; }
.marquee-item { font-family: var(--mono); font-size: 0.8rem; font-weight: 600; letter-spacing: 0.25em; text-transform: uppercase; color: var(--gold-dk); margin: 0 40px; display: inline-flex; align-items: center; gap: 40px; }
.marquee-item::after { content: '✦'; color: var(--gold-bdr); }
@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* Fixes for 3D and Magnetics */
.card, .proj-card, .skill-card, .cert-card, .tl-body, .contact-card { transform-style: preserve-3d; will-change: transform; }
.btn-gold, .btn-ghost, .nav-btn, .pill { will-change: transform; }
"""
content = content.replace('</style>', css_injection + '\n</style>')

# 2. HTML Injections
html_injection_body = """
<!-- ── LOADER & CURSOR ── -->
<div id="loader"><div class="loader-text">INITIALIZING</div></div>
<div id="cursor"></div>
<div id="cursor-follower"></div>
"""
content = content.replace('<body>', '<body>\n' + html_injection_body)

html_injection_canvas = '<canvas id="particles-js"></canvas>'
content = content.replace('<div class="hero-grid"></div>', '<div class="hero-grid"></div>\n  ' + html_injection_canvas)

html_injection_marquee = """
<!-- ── INFINITE MARQUEE ── -->
<div class="marquee-wrap">
  <div class="marquee-inner">
    <!-- Duplicate content for seamless loop -->
    <div class="marquee-item">IIT BHU Varanasi</div>
    <div class="marquee-item">Techradiance IIT Delhi</div>
    <div class="marquee-item">PRAGYAN'26</div>
    <div class="marquee-item">NASA AIASC</div>
    <div class="marquee-item">IIT Guwahati</div>
    <div class="marquee-item">University of Melbourne</div>
    <div class="marquee-item">IIT Madras CODE</div>
    <!-- Duplicates -->
    <div class="marquee-item">IIT BHU Varanasi</div>
    <div class="marquee-item">Techradiance IIT Delhi</div>
    <div class="marquee-item">PRAGYAN'26</div>
    <div class="marquee-item">NASA AIASC</div>
    <div class="marquee-item">IIT Guwahati</div>
    <div class="marquee-item">University of Melbourne</div>
    <div class="marquee-item">IIT Madras CODE</div>
  </div>
</div>
"""
content = content.replace('</section>\n<div class="section-divider"></div>\n<!-- ══════════════════════════════════════════\n     ABOUT', '</section>\n' + html_injection_marquee + '\n<!-- ══════════════════════════════════════════\n     ABOUT')

# Make the hero name scrambled initially
content = content.replace('<h1 class="hero-name">Manan Mishra</h1>', '<h1 class="hero-name" data-text="Manan Mishra">Manan Mishra</h1>')

# 3. JS Injections
js_injection = """
/* --- Loader --- */
window.addEventListener('load', () => {
  setTimeout(() => {
    document.body.classList.add('loaded');
    // Trigger Scramble on Load
    const heroName = document.querySelector('.hero-name');
    if (heroName) {
      const fx = new TextScramble(heroName);
      fx.setText(heroName.getAttribute('data-text'));
    }
  }, 1000);
});

/* --- Custom Cursor --- */
const cursor = document.getElementById('cursor');
const follower = document.getElementById('cursor-follower');
let mouseX = 0, mouseY = 0, followerX = 0, followerY = 0;
document.addEventListener('mousemove', (e) => {
  mouseX = e.clientX; mouseY = e.clientY;
  cursor.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
});
function animateFollower() {
  followerX += (mouseX - followerX) * 0.15;
  followerY += (mouseY - followerY) * 0.15;
  follower.style.transform = `translate(${followerX}px, ${followerY}px) translate(-50%, -50%)`;
  requestAnimationFrame(animateFollower);
}
animateFollower();
const hoverTargets = document.querySelectorAll('a, button, .gal-item, .card, .proj-card, .skill-card, .cert-card, .contact-card');
hoverTargets.forEach(el => {
  el.addEventListener('mouseenter', () => {
    cursor.style.width = '40px'; cursor.style.height = '40px';
    cursor.style.background = 'rgba(24, 43, 73, 0.1)'; cursor.style.border = '1px solid #182B49';
    follower.style.opacity = '0';
  });
  el.addEventListener('mouseleave', () => {
    cursor.style.width = '8px'; cursor.style.height = '8px';
    cursor.style.background = '#182B49'; cursor.style.border = 'none';
    follower.style.opacity = '1';
  });
});

/* --- Text Scramble --- */
class TextScramble {
  constructor(el) {
    this.el = el;
    this.chars = '!<>-_\\\\/[]{}—=+*^?#________';
    this.update = this.update.bind(this);
  }
  setText(newText) {
    const oldText = this.el.innerText;
    const length = Math.max(oldText.length, newText.length);
    const promise = new Promise((resolve) => this.resolve = resolve);
    this.queue = [];
    for (let i = 0; i < length; i++) {
      const from = oldText[i] || '';
      const to = newText[i] || '';
      const start = Math.floor(Math.random() * 40);
      const end = start + Math.floor(Math.random() * 40);
      this.queue.push({ from, to, start, end });
    }
    cancelAnimationFrame(this.frameRequest);
    this.frame = 0;
    this.update();
    return promise;
  }
  update() {
    let output = '';
    let complete = 0;
    for (let i = 0, n = this.queue.length; i < n; i++) {
      let { from, to, start, end, char } = this.queue[i];
      if (this.frame >= end) {
        complete++;
        output += to;
      } else if (this.frame >= start) {
        if (!char || Math.random() < 0.28) {
          char = this.randomChar();
          this.queue[i].char = char;
        }
        output += `<span style="color:var(--gold-bdr);font-family:var(--mono);">${char}</span>`;
      } else {
        output += from;
      }
    }
    this.el.innerHTML = output;
    if (complete === this.queue.length) {
      this.resolve();
    } else {
      this.frameRequest = requestAnimationFrame(this.update);
      this.frame++;
    }
  }
  randomChar() {
    return this.chars[Math.floor(Math.random() * this.chars.length)];
  }
}

/* --- Animated Counters --- */
const counters = document.querySelectorAll('.stat-num');
const counterObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const targetText = el.innerText;
      const targetNum = parseInt(targetText.replace(/[^0-9]/g, ''));
      if(isNaN(targetNum)) return;
      const suffix = targetText.replace(/[0-9]/g, '');
      let count = 0;
      const duration = 1500;
      const stepTime = Math.max(20, Math.floor(duration / targetNum));
      const inc = Math.max(1, Math.floor(targetNum / (duration / 20)));
      const timer = setInterval(() => {
        count += inc;
        if (count >= targetNum) {
          el.innerText = targetText;
          clearInterval(timer);
        } else {
          el.innerText = count + suffix;
        }
      }, stepTime);
      observer.unobserve(el);
    }
  });
}, { threshold: 0.5 });
counters.forEach(c => counterObserver.observe(c));

/* --- 3D Tilt Effect --- */
const tiltCards = document.querySelectorAll('.card, .proj-card, .skill-card, .cert-card, .tl-body, .contact-card');
tiltCards.forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = ((y - centerY) / centerY) * -4;
    const rotateY = ((x - centerX) / centerX) * 4;
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
    card.style.transition = 'none';
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
    card.style.transition = 'transform 0.5s var(--ease)';
  });
});

/* --- Magnetic Buttons --- */
const magnetics = document.querySelectorAll('.btn-gold, .btn-ghost, .nav-btn, .pill, .cert-placeholder');
magnetics.forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'translate(0px, 0px)';
  });
});

/* --- Simple Canvas Particles --- */
const canvas = document.getElementById('particles-js');
if (canvas) {
  const ctx = canvas.getContext('2d');
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;
  let particles = [];
  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });
  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.size = Math.random() * 1.5 + 0.5;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(24, 43, 73, 0.4)';
      ctx.fill();
    }
  }
  for (let i = 0; i < 60; i++) particles.push(new Particle());
  function animateParticles() {
    ctx.clearRect(0, 0, width, height);
    particles.forEach(p => { p.update(); p.draw(); });
    particles.forEach((p1, i) => {
      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(24, 43, 73, ${0.12 - dist/120 * 0.12})`;
          ctx.stroke();
        }
      }
    });
    requestAnimationFrame(animateParticles);
  }
  animateParticles();
}
"""
content = content.replace('</script>', js_injection + '\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Features added successfully.")
