(()=>{
  const doc=document.documentElement;
  let stored=null;try{stored=localStorage.getItem('muneerah-theme')}catch(e){}
  if(stored==='light'||stored==='dark')doc.dataset.theme=stored;
  const theme=document.querySelector('[data-theme-toggle]');
  function updateTheme(){if(theme){theme.setAttribute('aria-label',`Switch to ${doc.dataset.theme==='light'?'dark':'light'} mode`);theme.textContent=doc.dataset.theme==='light'?'☾':'☀';}}
  updateTheme();
  theme?.addEventListener('click',()=>{doc.dataset.theme=doc.dataset.theme==='light'?'dark':'light';try{localStorage.setItem('muneerah-theme',doc.dataset.theme)}catch(e){}updateTheme()});
  // Sticky liquid-glass surface deepens gently as content scrolls behind it.
  const header=document.querySelector('.site-header');
  let scrollPending=false;
  const updateHeader=()=>{scrollPending=false;header?.classList.toggle('is-scrolled',window.scrollY>28)};
  updateHeader();
  window.addEventListener('scroll',()=>{if(!scrollPending){scrollPending=true;requestAnimationFrame(updateHeader)}},{passive:true});
  const menu=document.querySelector('[data-menu-toggle]');
  const nav=document.querySelector('[data-nav-links]');
  const closeMenu=()=>{nav?.classList.remove('is-open');menu?.setAttribute('aria-expanded','false');menu?.setAttribute('aria-label','Open navigation');if(menu)menu.textContent='☰';};
  menu?.addEventListener('click',()=>{const open=nav?.classList.toggle('is-open');menu.setAttribute('aria-expanded',String(Boolean(open)));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');menu.textContent=open?'✕':'☰';});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('is-open')){closeMenu();menu?.focus();}});
  document.addEventListener('pointerdown',e=>{if(nav?.classList.contains('is-open')&&!header?.contains(e.target))closeMenu();});
  nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
  window.addEventListener('resize',()=>{if(window.innerWidth>840&&nav?.classList.contains('is-open'))closeMenu();},{passive:true});
  if('IntersectionObserver' in window){const ob=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');ob.unobserve(e.target)}})},{rootMargin:'0px 0px -35px 0px'});document.querySelectorAll('.reveal').forEach(x=>ob.observe(x));} else document.querySelectorAll('.reveal').forEach(x=>x.classList.add('visible'));
  const filters=document.querySelectorAll('[data-filter]');
  filters.forEach(btn=>btn.addEventListener('click',()=>{filters.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));const val=btn.dataset.filter;document.querySelectorAll('[data-evidence-category]').forEach(card=>card.hidden=!(val==='all'||card.dataset.evidenceCategory.split(' ').includes(val)));const shown=[...document.querySelectorAll('[data-evidence-category]')].filter(c=>!c.hidden).length;const note=document.querySelector('[data-filter-status]');if(note)note.textContent=`Showing ${shown} ${shown===1?'piece':'pieces'} of evidence`;}));
  const modal=document.querySelector('#proof-lightbox');
  document.querySelectorAll('[data-lightbox-image]').forEach(link=>link.addEventListener('click',e=>{if(!modal?.showModal)return;e.preventDefault();const img=modal.querySelector('img');img.src=link.href;img.alt=link.dataset.label||'Portfolio evidence';modal.showModal()}));
  modal?.querySelector('[data-close]')?.addEventListener('click',()=>modal.close());
  modal?.addEventListener('click',e=>{if(e.target===modal)modal.close()});

  // Additional approved evidence is loaded from a reviewed JSON file, not from public uploads.
  const gallery=document.querySelector('#evidence-gallery');
  if(gallery){fetch('../data/evidence.json',{cache:'no-cache'}).then(r=>r.ok?r.json():[]).then(entries=>{if(!Array.isArray(entries))return;for(const item of entries){if(!item||typeof item!=='object'||!/^[-a-z0-9]{1,72}$/.test(item.slug||''))continue;const cat=['community','recognition','campaign','coaching'].includes(item.category)?item.category:'community';const article=document.createElement('article');article.className='evidence-card reveal visible';article.dataset.evidenceCategory=cat;const art=document.createElement('div');art.className='evidence-art contain';const photo=document.createElement('img');photo.src='../assets/media/'+item.slug+'.webp';photo.loading='lazy';photo.alt=String(item.title||'Evidence').slice(0,90);art.append(photo);const content=document.createElement('div');content.className='evidence-description';const label=document.createElement('div');label.className='project-type';label.textContent=String(item.date||'Portfolio evidence').slice(0,90);const heading=document.createElement('h3');heading.textContent=String(item.title||'Evidence').slice(0,90);const para=document.createElement('p');para.textContent=String(item.description||'').slice(0,300);const link=document.createElement('a');link.href=photo.src;link.dataset.lightboxImage='';link.dataset.label=heading.textContent;link.textContent='View image ↗';link.addEventListener('click',e=>{const modal=document.querySelector('#proof-lightbox');if(!modal?.showModal)return;e.preventDefault();const img=modal.querySelector('img');img.src=link.href;img.alt=link.dataset.label;modal.showModal()});content.append(label,heading,para,link);article.append(art,content);gallery.append(article)}}).catch(()=>{});}
  // Local-only image preparation studio. No credentials, uploads, backend or hidden tracking.
  const upload=document.querySelector('#new-evidence-file');const zone=document.querySelector('#evidence-upload-zone');let chosen=null;let previewUrl=null;
  if(upload){
    for(const event of ['dragenter','dragover'])zone?.addEventListener(event,e=>{e.preventDefault();zone.classList.add('dragging')});
    for(const event of ['dragleave','drop'])zone?.addEventListener(event,e=>{e.preventDefault();zone.classList.remove('dragging')});
    zone?.addEventListener('drop',e=>{const f=e.dataTransfer?.files?.[0];if(f)chooseFile(f)});
    upload.addEventListener('change',()=>{if(upload.files?.[0])chooseFile(upload.files[0])});
    function chooseFile(f){const status=document.querySelector('#studio-status');if(!/^image\/(png|jpeg|webp)$/.test(f.type)||f.size>12*1024*1024){status.textContent='Choose a PNG, JPEG or WebP under 12 MB.';return}chosen=f;if(previewUrl)URL.revokeObjectURL(previewUrl);previewUrl=URL.createObjectURL(f);const img=document.querySelector('#studio-image');img.src=previewUrl;document.querySelector('#studio-preview').hidden=false;status.textContent='Preview loaded locally. Check for identifying information before publishing.';}
    const exportBtn=document.querySelector('#studio-export');exportBtn?.addEventListener('click',async()=>{const status=document.querySelector('#studio-status');const title=document.querySelector('#studio-title').value.trim();const description=document.querySelector('#studio-description').value.trim();if(!chosen||!title||!description){status.textContent='Select a screenshot, title and description before continuing.';return;}const slug=title.toLowerCase().normalize('NFKD').replace(/[^a-z0-9 ]/g,'').trim().replace(/\s+/g,'-').slice(0,65);if(!slug){status.textContent='Please provide a valid title.';return;}try{const image=await createImageBitmap(chosen);const scale=Math.min(1,1300/Math.max(image.width,image.height));const can=document.createElement('canvas');can.width=Math.round(image.width*scale);can.height=Math.round(image.height*scale);can.getContext('2d').drawImage(image,0,0,can.width,can.height);const blob=await new Promise((resolve,reject)=>can.toBlob(b=>b?resolve(b):reject(Error('Image conversion failed')),'image/webp',.85));const record={slug,category:document.querySelector('#studio-category').value,title,description,date:document.querySelector('#studio-date').value||new Date().toISOString().slice(0,10)};const dl=document.querySelector('#studio-image-download');const data=document.querySelector('#studio-json-download');if(dl.href.startsWith('blob:'))URL.revokeObjectURL(dl.href);if(data.href.startsWith('blob:'))URL.revokeObjectURL(data.href);dl.href=URL.createObjectURL(blob);dl.download=slug+'.webp';data.href=URL.createObjectURL(new Blob([JSON.stringify(record,null,2)],{type:'application/json'}));data.download=slug+'.json';document.querySelector('#studio-results').hidden=false;status.textContent='Files are ready. Download both, review them, then commit the image and append this JSON object to data/evidence.json in GitHub.';}catch(e){status.textContent='Could not prepare image: '+e.message;}});
  }

  document.querySelector('[data-print]')?.addEventListener('click',()=>window.print());
  const form=document.querySelector('[data-application-form]');
  form?.addEventListener('submit',async e=>{e.preventDefault();const name=form.querySelector('[name=name]').value.trim(),role=form.querySelector('[name=role]').value.trim(),message=form.querySelector('[name=message]').value.trim();const composed=`Hello Muneerah,\n\nMy name is ${name||'[Name]'} and I would like to discuss ${role||'an opportunity'}.\n\n${message}\n\nThank you.`;const output=document.querySelector('[data-form-status]');try{await navigator.clipboard.writeText(composed);output.textContent='Message copied. You can email contact@muneerah.page or send it on WhatsApp.';}catch{output.textContent='Select and copy the message below.';const box=document.querySelector('[data-copy-fallback]');box.hidden=false;box.value=composed;box.select();}});
})();
