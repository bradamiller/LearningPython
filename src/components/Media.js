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
 * clicks "Drive it". Used where the first frame is a question (L1-6's motor
 * cases: arrows on the wheels, "which way will it drive?") and the motion is
 * the answer, so one picture does both jobs.
 *
 * The SVG is embedded with <object>, not <img>: an <img> SVG cannot be paused
 * or scripted. On load it is paused at time 0. Pressing the button (or the
 * picture) restarts it from 0; if the SVG root carries data-hold="<seconds>"
 * it pauses there, on the final pose, instead of looping back to the start.
 *
 * Usage:
 *   <PlayFigure src="/img/lesson-06/motors-curve-drive.svg" alt="..." caption="..." />
 */
export function PlayFigure({src, alt = '', caption, playLabel = 'Drive it', againLabel = 'Again'}) {
  const url = useMediaUrl(src);
  const ref = React.useRef(null);
  const timer = React.useRef(null);
  const [state, setState] = React.useState('ready'); // ready | playing | done

  const svgRoot = () => {
    const o = ref.current;
    try { return o && o.contentDocument && o.contentDocument.documentElement; } catch (e) { return null; }
  };
  const park = () => {
    const svg = svgRoot();
    if (svg && svg.pauseAnimations) { svg.pauseAnimations(); svg.setCurrentTime(0); }
  };
  const play = () => {
    const svg = svgRoot();
    if (!svg || !svg.pauseAnimations) return;
    clearTimeout(timer.current);
    svg.setCurrentTime(0);
    svg.unpauseAnimations();
    setState('playing');
    const hold = parseFloat(svg.getAttribute('data-hold'));
    if (hold > 0) {
      timer.current = setTimeout(() => { svg.pauseAnimations(); setState('done'); }, hold * 1000);
    }
  };
  React.useEffect(() => {
    const o = ref.current;
    if (!o) return undefined;
    o.addEventListener('load', park);
    park();   // in case it loaded before the effect ran
    return () => { o.removeEventListener('load', park); clearTimeout(timer.current); };
  }, [url]);

  return (
    <figure className="videoBlock playFigure">
      <div className="playFigure__frame" onClick={state === 'playing' ? undefined : play}>
        <object ref={ref} data={url} type="image/svg+xml" aria-label={alt} role="img" tabIndex={-1}>
          {alt}
        </object>
        {state !== 'playing' && (
          <button type="button" className="playFigure__button" onClick={(e) => { e.stopPropagation(); play(); }}>
            {state === 'ready' ? `▶ ${playLabel}` : `↺ ${againLabel}`}
          </button>
        )}
      </div>
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}
