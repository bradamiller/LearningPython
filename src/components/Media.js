import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

/**
 * Site-root paths like /img/x.jpg must go through useBaseUrl, or they break the
 * moment the site is served from a subpath (GitHub Pages project sites are
 * served from /<repo>/). External URLs and data: URIs are passed through
 * untouched.
 */
function useMediaUrl(src) {
  const resolved = useBaseUrl(src || '');
  if (!src) return src;
  if (/^(https?:)?\/\//.test(src) || src.startsWith('data:')) return src;
  return resolved;
}

/**
 * Video block. If you pass `src` (a YouTube/Vimeo embed URL or a local
 * /videos/foo.mp4), it renders the real player. With no src it shows a
 * labeled placeholder so you can see exactly where your video will go and
 * drop it in later.
 *
 * Usage:
 *   <Video caption="XRP driving forward and back" placeholderLabel="Intro hook clip (1–2 min)" />
 *   <Video src="https://www.youtube.com/embed/XXXX" caption="Hardware tour" />
 *   <Video src="/videos/first-drive.mp4" mp4 caption="First upload" />
 */
export function Video({src, mp4 = false, caption, placeholderLabel = 'Video goes here'}) {
  const url = useMediaUrl(src);
  return (
    <figure className="videoBlock">
      {src ? (
        <div className="videoBlock__frame">
          {mp4 ? (
            <video controls src={url} />
          ) : (
            <iframe src={url} title={caption || 'video'} allowFullScreen />
          )}
        </div>
      ) : (
        <div className="videoPlaceholder">
          <div className="videoPlaceholder__play">▶</div>
          <div><strong>{placeholderLabel}</strong></div>
          <div className="videoPlaceholder__hint">Add a src to embed your video here</div>
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

/**
 * Image figure. Pass `src` for a real image, or leave it out to show a
 * placeholder frame with a description of the graphic you'll create.
 *
 * Usage:
 *   <Figure src="/img/lesson-01/xrp-parts.png" alt="Labeled XRP" caption="The parts of the XRP" />
 *   <Figure placeholderLabel="Labeled diagram of the XRP robot" caption="Robot hardware" />
 */
export function Figure({src, alt = '', caption, placeholderLabel = 'Graphic goes here'}) {
  const url = useMediaUrl(src);
  return (
    <figure className="videoBlock">
      {src ? (
        <img
          src={url}
          alt={alt}
          style={{borderRadius: 12, display: 'block', maxWidth: '100%', maxHeight: 520, width: 'auto', margin: '0 auto'}}
        />
      ) : (
        <div className="figurePlaceholder">
          <div className="figurePlaceholder__icon">🖼️</div>
          <div><strong>{placeholderLabel}</strong></div>
          <div className="videoPlaceholder__hint">Add a src to drop in your image</div>
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

/**
 * PlayFigure — an animated SVG that waits on its first frame until the reader
 * presses a button. Used where the first frame is a question (L1-6's motor
 * cases: arrows on the wheels, "which way will it drive?") and the motion is
 * the answer, so one picture does both jobs.
 *
 * The SVG is embedded with <object>, not <img>: an <img> SVG cannot be paused
 * or scripted. On load it is paused at time 0.
 *
 * One button (default): pressing it, or the picture, plays from 0. If the SVG
 * root carries data-hold="<seconds>" it pauses there, on the final pose,
 * instead of looping back to the start.
 *
 * Several buttons: if the SVG root carries
 *   data-modes='[{"label":"Effort control","start":0.4,"stop":12.1}, ...]'
 * one button is shown per mode, and each plays its own stretch of the timeline
 * and pauses at its stop. (L1-6's effort-vs-speed hill.)
 *
 * Usage:
 *   <PlayFigure src="/img/lesson-06/motors-curve-drive.svg" alt="..." caption="..." />
 */
export function PlayFigure({src, alt = '', caption, playLabel = 'Drive it', againLabel = 'Again'}) {
  const url = useMediaUrl(src);
  const ref = React.useRef(null);
  const timer = React.useRef(null);
  const [state, setState] = React.useState('ready'); // ready | playing | done
  const [modes, setModes] = React.useState(null);
  const [active, setActive] = React.useState(-1);

  const svgRoot = () => {
    const o = ref.current;
    try { return o && o.contentDocument && o.contentDocument.documentElement; } catch (e) { return null; }
  };
  const park = () => {
    const svg = svgRoot();
    if (!svg || !svg.pauseAnimations) return;
    svg.pauseAnimations(); svg.setCurrentTime(0);
    const m = svg.getAttribute('data-modes');
    if (m) { try { setModes(JSON.parse(m)); } catch (e) { /* ignore */ } }
  };
  const run = (from, to, which) => {
    const svg = svgRoot();
    if (!svg || !svg.pauseAnimations) return;
    clearTimeout(timer.current);
    svg.setCurrentTime(from);
    svg.unpauseAnimations();
    setState('playing'); setActive(which);
    if (to > from) {
      timer.current = setTimeout(() => { svg.pauseAnimations(); setState('done'); }, (to - from) * 1000);
    }
  };
  const play = () => {
    const svg = svgRoot();
    if (!svg) return;
    run(0, parseFloat(svg.getAttribute('data-hold')) || 0, 0);
  };
  React.useEffect(() => {
    const o = ref.current;
    if (!o) return undefined;
    o.addEventListener('load', park);
    park();   // in case it loaded before the effect ran
    return () => { o.removeEventListener('load', park); clearTimeout(timer.current); };
  }, [url]);

  const single = !modes;
  return (
    <figure className="videoBlock playFigure">
      <div className="playFigure__frame" onClick={single && state !== 'playing' ? play : undefined}
           style={single ? undefined : {cursor: 'default'}}>
        <object ref={ref} data={url} type="image/svg+xml" aria-label={alt} role="img" tabIndex={-1}>
          {alt}
        </object>
        {single && state !== 'playing' && (
          <button type="button" className="playFigure__button" onClick={(e) => { e.stopPropagation(); play(); }}>
            {state === 'ready' ? `▶ ${playLabel}` : `↺ ${againLabel}`}
          </button>
        )}
      </div>
      {!single && (
        <div className="playFigure__modes">
          {modes.map((m, i) => (
            <button key={i} type="button"
                    className={'playFigure__button playFigure__button--inline' + (active === i ? ' is-active' : '')}
                    disabled={state === 'playing'}
                    onClick={() => run(m.start, m.stop, i)}>
              ▶ {m.label}
            </button>
          ))}
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

/**
 * TreeFigure — a tree diagram that opens one level per click (L4-5's problem
 * decomposition). It starts with only the top box; clicking a box that breaks
 * down (it shows a +) reveals its parts, and clicking it again folds them away.
 *
 * The SVG is embedded with <object> so its boxes can be clicked. It is drawn
 * with everything showing (so it reads in full anywhere scripts don't run),
 * and marks its structure with attributes (scripts/figures/fdecomp.py):
 *   data-parent="<id>"  this element belongs under box <id>
 *   data-node="<id>" data-expand  a box that breaks down further
 * The picture's height follows the levels showing, so no empty space is left
 * under a closed box.
 *
 * Usage:
 *   <TreeFigure src="/img/lesson-m4-05/decomposition.svg" alt="..." caption="..." />
 */
export function TreeFigure({src, alt = '', caption, hint = 'Click a box with a + to break it down.'}) {
  const url = useMediaUrl(src);
  const ref = React.useRef(null);
  const api = React.useRef(null);
  const [ratio, setRatio] = React.useState('680 / 76');

  React.useEffect(() => {
    const o = ref.current;
    if (!o) return undefined;
    const setup = () => {
      let svg;
      try { svg = o.contentDocument && o.contentDocument.documentElement; } catch (e) { return; }
      if (!svg || svg.tagName.toLowerCase() !== 'svg' || svg.__tree) return;
      svg.__tree = true;
      const fullH = svg.viewBox.baseVal.height;
      const W = svg.viewBox.baseVal.width;
      const nodes = {};
      svg.querySelectorAll('[data-node]').forEach((g) => { nodes[g.getAttribute('data-node')] = g; });
      const parentOf = (id) => nodes[id] && nodes[id].getAttribute('data-parent');
      const open = new Set();
      const shown = (id) => { const p = parentOf(id); return !p || (open.has(p) && shown(p)); };
      const under = (id, anc) => { const p = parentOf(id); return !!p && (p === anc || under(p, anc)); };
      const render = () => {
        svg.querySelectorAll('[data-parent]').forEach((el) => {
          const p = el.getAttribute('data-parent');
          el.classList.toggle('hid', !(open.has(p) && shown(p)));
        });
        Object.entries(nodes).forEach(([id, g]) => {
          g.classList.toggle('open', open.has(id));
          g.setAttribute('tabindex', shown(id) ? '0' : '-1');
          g.setAttribute('aria-expanded', open.has(id) ? 'true' : 'false');
        });
        let bottom = 0;
        Array.from(svg.children).forEach((el) => {
          if (el.tagName.toLowerCase() !== 'g' || el.classList.contains('hid')) return;
          const b = el.getBBox();
          bottom = Math.max(bottom, b.y + b.height);
        });
        const h = Math.min(fullH, Math.ceil(bottom + 12));
        svg.setAttribute('viewBox', `0 0 ${W} ${h}`);
        svg.removeAttribute('height');
        svg.removeAttribute('width');
        setRatio(`${W} / ${h}`);
      };
      const toggle = (id) => {
        if (open.has(id)) {
          open.delete(id);
          Object.keys(nodes).forEach((k) => { if (under(k, id)) open.delete(k); });
        } else {
          open.add(id);
        }
        render();
      };
      Object.entries(nodes).forEach(([id, g]) => {
        g.setAttribute('role', 'button');
        g.addEventListener('click', () => toggle(id));
        g.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(id); }
        });
      });
      api.current = {
        all: () => { Object.keys(nodes).forEach((k) => open.add(k)); render(); },
        reset: () => { open.clear(); render(); },
      };
      render();
    };
    o.addEventListener('load', setup);
    setup();   // in case it loaded before the effect ran
    return () => o.removeEventListener('load', setup);
  }, [url]);

  return (
    <figure className="videoBlock treeFigure">
      <object ref={ref} data={url} type="image/svg+xml" aria-label={alt} role="img"
              style={{aspectRatio: ratio}}>
        {alt}
      </object>
      <div className="treeFigure__bar">
        <span className="treeFigure__hint">{hint}</span>
        <button type="button" className="treeFigure__button" onClick={() => api.current && api.current.all()}>
          Show all
        </button>
        <button type="button" className="treeFigure__button" onClick={() => api.current && api.current.reset()}>
          Start over
        </button>
      </div>
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

/**
 * StepFigure — an animated SVG that plays like a video and can also be walked
 * through one step at a time, so a teacher can stop on each step and explain it
 * (L4-2's "Building a path in a loop").
 *
 * The SVG is embedded with <object> so it can be paused and moved. Its root
 * carries data-steps="t1,t2,...": the time, in seconds, of each step's finished
 * frame, and data-dur="<seconds>" its length (scripts/figures/pathanim.py
 * writes both). Step goes to the next one
 * and pauses there, Back to the one before, Play carries on from where it is.
 *
 * Usage:
 *   <StepFigure src="/img/lesson-m4-02/build-path.svg" alt="..." caption="..." />
 */
export function StepFigure({src, alt = '', caption}) {
  const url = useMediaUrl(src);
  const ref = React.useRef(null);
  const [steps, setSteps] = React.useState([]);
  const [loop, setLoop] = React.useState(0);       // the animation's length, to read where a loop is
  const [at, setAt] = React.useState(-1);          // step showing while paused; -1 when playing
  const [paused, setPaused] = React.useState(false);
  const [ratio, setRatio] = React.useState('680 / 440');

  const svgRoot = () => {
    const o = ref.current;
    try { return o && o.contentDocument && o.contentDocument.documentElement; } catch (e) { return null; }
  };
  React.useEffect(() => {
    const o = ref.current;
    if (!o) return undefined;
    const setup = () => {
      const svg = svgRoot();
      if (!svg || !svg.getAttribute) return;
      const s = (svg.getAttribute('data-steps') || '').split(',').map(parseFloat).filter((x) => !isNaN(x));
      setSteps(s);
      setLoop(parseFloat(svg.getAttribute('data-dur')) || 0);
      const vb = svg.viewBox && svg.viewBox.baseVal;
      if (vb && vb.width) setRatio(`${vb.width} / ${vb.height}`);
    };
    o.addEventListener('load', setup);
    setup();   // in case it loaded before the effect ran
    return () => o.removeEventListener('load', setup);
  }, [url]);

  const show = (i) => {
    const svg = svgRoot();
    if (!svg || !svg.pauseAnimations || !steps.length) return;
    const k = Math.max(0, Math.min(steps.length - 1, i));
    svg.pauseAnimations();
    svg.setCurrentTime(steps[k]);
    setAt(k); setPaused(true);
  };
  // the step at or after the current time, when stepping out of playback
  const nextFromNow = () => {
    const svg = svgRoot();
    const now = svg && svg.getCurrentTime ? (loop ? svg.getCurrentTime() % loop : svg.getCurrentTime()) : 0;
    const k = steps.findIndex((t) => t > now + 0.05);
    return k < 0 ? 0 : k;
  };
  const step = () => show(paused ? (at >= steps.length - 1 ? 0 : at + 1) : nextFromNow());
  const back = () => show(paused ? at - 1 : nextFromNow() - 1);
  const play = () => {
    const svg = svgRoot();
    if (!svg || !svg.unpauseAnimations) return;
    if (paused && at >= steps.length - 1) svg.setCurrentTime(0);
    svg.unpauseAnimations();
    setPaused(false); setAt(-1);
  };
  // pause on the last step already shown, so the picture is a clean frame
  const pause = () => {
    const svg = svgRoot();
    const now = svg && svg.getCurrentTime ? (loop ? svg.getCurrentTime() % loop : svg.getCurrentTime()) : 0;
    let k = 0;
    steps.forEach((t, i) => { if (t <= now) k = i; });
    show(k);
  };

  return (
    <figure className="videoBlock stepFigure">
      <object ref={ref} data={url} type="image/svg+xml" aria-label={alt} role="img"
              style={{aspectRatio: ratio}}>
        {alt}
      </object>
      {steps.length > 0 && (
        <div className="treeFigure__bar">
          <button type="button" className="treeFigure__button" onClick={back}
                  disabled={paused && at <= 0}>◀ Back</button>
          <button type="button" className="treeFigure__button" onClick={step}>Step ▶</button>
          {paused
            ? <button type="button" className="treeFigure__button" onClick={play}>▶ Play</button>
            : <button type="button" className="treeFigure__button" onClick={pause}>⏸ Pause</button>}
          <span className="treeFigure__hint" aria-live="polite">
            {paused ? `Step ${at + 1} of ${steps.length}` : 'Playing'}
          </span>
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}
